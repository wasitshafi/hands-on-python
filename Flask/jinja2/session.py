from flask import Flask
from flask import request
from flask import make_response
from flask import session
from flask import render_template
from flask import redirect
from flask import session
from flask import url_for


app = Flask(__name__)
app.secret_key = 'ThisIsMySecreteKeyString'

@app.route('/')
def index():
  name = 'wasit'
  if name in session: # check if session contains name as key
    return redirect(url_for('homepage', username = name))
  return render_template('login.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
  name = ''
  password = ''
  
  if request.method == 'GET':
    name = request.args.get('txtb_username')
    password = request.args.get('txtb_password')
  else:
    name = request.form['txtb_username'] # from is a dictionary consisting key,value pair
    password = request.form['txtb_password']
  session[name] = password
  return redirect(url_for('homepage', username = name))

@app.route('/homepage/<username>')
def homepage(username):
  return 'Welcome ' + username + '<br> Your password was : ' + session[username];

if __name__ == '__main__':
  app.run()