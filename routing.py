from flask import Flask, url_for

app = Flask(__name__)

# Add url parameters by surrounding
# variables with angle brackets
@app.route('/')
@app.route('/hello/<name>')
def hello(name="world"):
  # Url parameters are passed as
  # keyword arguments to your
  # view function
  return "Hello, {}".format(name)

@app.route('/url/<name>')
def hello_url(name):
  # You can use `url_for` to keep DRY
  # when building dynamic urls
  return url_for('hello', name=name)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
