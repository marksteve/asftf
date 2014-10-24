from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/hello/<name>')
def hello(name="world"):
  return "Hello, {}".format(name)

@app.route('/url/<name>')
def hello_url(name):
  return url_for('hello', name=name)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
