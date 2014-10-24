from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route('/')
def login():
  type = request.args.get('type', 'html')
  if type == 'html':
    return "<html>Hello, world</html>"
  elif type == 'json':
    return jsonify(hello="world")
  else:
    return "Hello, world", 200, {'Content-Type': 'text/plain'}

@app.errorhandler(404)
def not_found(error):
  resp = make_response("FUUUUUUUUUU!!!", 404)
  resp.headers['Content-Type'] = 'text/plain'
  return resp

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
