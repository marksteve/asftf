import docker
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
dc = docker.Client()


SLIDES = [
  ('hello-world', "Hello, world"),
  ('routing', "Routing"),
  ('templates', "Templates"),
  ('http-methods', "HTTP Methods"),
]


@app.route('/')
def index():
  return render_template('index.html', slides=SLIDES)


@app.route('/<int:n>/<id>', methods=['GET', 'POST'])
def slides(n=1, id=None):
  prev_url = url_for(
    'slides', n=n - 1, id=SLIDES[n - 2][0],
  ) if n > 1 else None
  next_url = url_for(
    'slides', n=n + 1, id=SLIDES[n][0],
  ) if n < len(SLIDES) else None

  code_file = '{}.py'.format(id)
  with open(code_file) as f:
    code = f.read()

  template_file = 'templates/{}.html'.format(id)
  try:
    with open(template_file) as f:
      template = f.read()
  except IOError:
    template = None

  container_name = 'asftf_slide_{}'.format(n)

  if request.args.get('recreate'):
    dc.remove_container(container_name, force=True)

  try:
    container = dc.inspect_container(container_name)
  except docker.errors.APIError:
    container = None

  if not container:
    container = dc.create_container(
      'asftf_app',
      command=['python', code_file],
      ports={
        '5000/tcp': {},
      },
      name=container_name,
    )
    dc.start(container, port_bindings={
      '5000/tcp': None,
    })

  port = dc.port(container, '5000')[0]['HostPort']
  container_url = "http://{}:{}".format(
    request.headers["Host"].split(':')[0],
    port,
  )

  return render_template(
    'slide.html',
    n=n,
    title=SLIDES[n - 1][1],
    code_file=code_file,
    code=code,
    template_file=template_file,
    template=template,
    container=container,
    container_url=container_url,
    prev_url=prev_url,
    next_url=next_url,
  )


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True)
