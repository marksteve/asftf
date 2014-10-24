import os

import docker
from flask import Flask, jsonify, render_template, request, url_for

app = Flask(__name__)
dc = docker.Client()


SLIDE_TITLES = [
  "Hello, world"
]


@app.route('/')
def index():
  return render_template('index.html', slide_titles=SLIDE_TITLES)


@app.route('/<int:n>', methods=['GET', 'POST'])
def slides(n=1):
  prev_url = url_for('slides', n=n - 1) if n > 1 else None
  next_url = url_for('slides', n=n + 1) if n < len(SLIDE_TITLES) else None

  slide_file = 'slide_{}.py'.format(n)

  with open(slide_file) as f:
    code = f.read()

  container_name = 'asftf_{}'.format(n)

  try:
    container = dc.inspect_container(container_name)
  except docker.errors.APIError:
    container = None

  if request.method == 'POST':
    if container:
      dc.remove_container(container_name, force=True)
    container = dc.create_container(
      'asftf_app',
      command=['python', slide_file],
      ports={
        '5000/tcp': {},
      },
      name=container_name,
    )
    dc.start(container, port_bindings={
      '5000/tcp': None,
    })


  if container:
    port = dc.port(container, '5000')[0]['HostPort']
    container_url = "http://{}:{}".format(
      request.headers["Host"].split(':')[0],
      port,
    )
  else:
    container_url = None

  return render_template(
    'slide.html',
    n=n,
    title=SLIDE_TITLES[n - 1],
    code=code,
    container=container,
    container_url=container_url,
    prev_url=prev_url,
    next_url=next_url,
  )


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True)
