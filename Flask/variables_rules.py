from flask import Flask

app = Flask(__name__)

@app.route('/')# goto to url 127.0.0.1:5000/hello/wasit
def index():
  return 'Welcome to home page'

# This is route to non-canonical url, for canonical url use @app.route('/helloworld/')
@app.route('/helloworld')# goto to url 127.0.0.1:5000/hello
def hello_world():
  return 'Hello World'

# This is route to canonical url 
@app.route('/hello/<name>') # goto to url 127.0.0.1:5000/hello/wasit, default datatype for variable is string for others we have to mention data type
def hello_person(name):
  return 'hello %s!' % name

if(__name__ == '__main__'):
  app.run()