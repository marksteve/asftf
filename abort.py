from flask import Flask, abort, request

app = Flask(__name__)

@app.route('/')
def login():
  # Abort raises an exception which stops the
  # processing of the request and returns with
  # the appropriate error status code
  if (
    request.args.get('username') != 'admin' or
    request.args.get('password') != 'admin'
  ):
    abort(401)
  return "Logged in"

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
