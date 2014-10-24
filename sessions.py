from flask import (abort, flash, Flask, redirect, render_template, request,
                   session, url_for)

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    if request.form['password'] == 'password':
      session['logged_in'] = request.form['username']
      flash("You are now logged in as {}".format(
        session['logged_in'],
      ))
    else:
      flash("Incorrect password")
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
