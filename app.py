from flask import Flask, render_template, url_for

app = Flask(__name__)


SLIDE_TITLES = [
  "Hello, world"
]


@app.route('/')
def index():
  return render_template('index.html', slide_titles=SLIDE_TITLES)


@app.route('/<int:n>')
def slides(n=1):
  prev_url = url_for('slides', n=n - 1) if n > 1 else None
  next_url = url_for('slides', n=n + 1) if n < len(SLIDE_TITLES) else None
  return render_template(
    'slide_{}.html'.format(n),
    n=n,
    title=SLIDE_TITLES[n - 1],
    demo_url=url_for('demos', n=n, _external=True),
    prev_url=prev_url,
    next_url=next_url,
  )


@app.route('/demos/<int:n>')
def demos(n):
  if n == 1:
    return "Hello, world"


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True, threaded=True)

