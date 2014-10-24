from flask import (abort, Flask, redirect, render_template, request, session,
                   url_for)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['password'] != 'password':
      abort(401)
    session['logged_in'] = request.form['username']
  logged_in = session.get('logged_in')
  return render_template(
    'sessions.html',
    logged_in=logged_in,
  )

@app.route('/logout')
def logout():
  session.clear()
  return redirect(url_for('login'))


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
