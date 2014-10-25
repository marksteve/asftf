from flask import Flask

# Create an app instance
app = Flask(__name__)

# Decorate a function that returns
# your response with the `route` method
@app.route('/')
def index():
  return "Hello, world"

# Run the development server in debug mode
if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
