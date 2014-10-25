from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  # The `request` global contains
  # information about the incoming request
  # such as its headers and body
  return render_template(
    'request-data.html',
    args=request.args,
    form=request.form,
  )

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
