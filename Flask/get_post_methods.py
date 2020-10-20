from flask import Flask
from flask import request

app = Flask(__name__) 

@app.route('/')
def index():
  return "Welcome to Home Page...!"

@app.route('/hello', methods = ['GET', 'POST'])
def hello_world():
  if request.method == 'GET': # by default method is GET
    return "Hello World...! We are using GET Method..."
  else:
    return "Hello World...! We are using POST Method..."

if __name__ == '__main__':
  app.run(debug=True)