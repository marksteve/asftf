from flask import Flask, render_template

app = Flask(__name__)

# Flask, by default, exposes files from the `static` folder
# to the /static path
@app.route('/')
def index():
  return render_template('static.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
