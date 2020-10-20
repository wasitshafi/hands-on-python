from flask import Flask

app = Flask(__name__) # creating object of Flask()

@app.route('/')
def index():
  return "<h1>This is home page</h1>"

@app.route('/hello')
def hello_world():
  return "<h2>Hello World</h2>"

if __name__ == '__main__':
  app.run(debug=True)   # default port no is 5000 => 127.0.0.1:5000 