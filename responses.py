from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

# It's easy to composes responses in Flask
@app.route('/')
def login():
  type = request.args.get('type', 'html')
  if type == 'html':
    # Return a string and it'll automatically
    # get the `text/html` content type
    return "<html>Hello, world</html>"
  elif type == 'json':
    # There's a `jsonify` function that allows
    # easy creation of JSON responses
    return jsonify(hello="world")
  else:
    # You can also return a tuple w/c contains
    # the response body, status code and a headers
    # dictionary
    return "Hello, world", 200, {'Content-Type': 'text/plain'}

# Default error pages can be changed using the
# `errorhandler` method
@app.errorhandler(404)
def not_found(error):
  # You can also return a Werkzeug response
  # object if that's your thing
  resp = make_response("FUUUUUUUUUU!!!", 404)
  resp.headers['Content-Type'] = 'text/plain'
  return resp

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
