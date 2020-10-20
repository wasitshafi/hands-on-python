from flask import Flask
from flask import request
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome to home Page'

@app.route('/login/', methods=['GET', 'POST'])
def login_fun():
  if request.method == 'GET':  # method return the current method name
    username = request.args.get('txtb_username') # args is used to get data from url string incase of get method
    password = request.args.get('txtb_password')
  else:
    username = request.form['txtb_username'] # from is a dictionary consisting key,value pair
    password = request.form['txtb_password']

  output = 'You are using <b>%s</b> Method' %request.method # CTM : not request.method()
  output += '<br>Username : <b>' + username + '</b>'
  output += '<br>Password : <b>' + password + '</b>'
  return output

if __name__ == '__main__':
  app.run(debug=True)