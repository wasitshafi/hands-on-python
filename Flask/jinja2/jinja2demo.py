from flask import Flask
from flask import url_for
from flask import redirect
from flask import render_template

app = Flask(__name__)

# hard code method, without jinja template
"""
@app.route('/')
def index():
  return '\
<!doctype html>\
<html>\
  <head>\
    <title>Welcome</title>\
  </head>\
  <body>\
    <div style="text-align: center;"><p>Welcome to Home Page <b>{{ name }}</b></div>\
  </body>\
</html>'
"""

# Method 1
@app.route('/')
def index():
  return render_template('home.html')

# Method 2, passing arguments
@app.route('/hello/<username>')
def hello(username):
  return render_template('home.html', name = username)


@app.route('/result/')
def result():
  nm = 'wasit'
  dict1 = {"C" : 50, "CPP" : 40, "Java" : 65, "OS" : 27, "Networking" : 80}
  return render_template('showmarks.html',subject_marks = dict1, name=nm)
if __name__ == '__main__':
  app.run()