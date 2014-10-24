from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    logged_in = True
  else:
    logged_in = False
  return render_template('http-methods.html', logged_in=logged_in)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
