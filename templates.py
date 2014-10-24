from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='world'):
  return render_template('templates.html', name=name)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
