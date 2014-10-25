from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name='world'):
  # Flask uses Jinja as its templating engine
  # By default, templates are read from
  # the `templates` folder in the same level
  # of your app module

  # You give context to your templates
  # by passing them as keyword arguments
  # to the `render_template` function
  return render_template('templates.html', name=name)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
