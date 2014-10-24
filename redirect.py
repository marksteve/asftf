from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return redirect(url_for('maintenance'))

@app.route('/maintenance')
def maintenance():
  return "Under maintenance"

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
