from flask import Flask
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
  return "Welcome to Home page..."

@app.route('/user/admin/')
def admin_fun():
  return "Welcome to Administrator..."

@app.route('/guest_user/<user_name>')
def guest_fun(user_name):
  return 'Welcome %s' % user_name

@app.route('/user/<name>')
def user(name):
  if name == 'admin':
    return redirect(url_for('admin_fun'))
  else:
    return redirect(url_for('guest_fun', user_name = name))
    return redirect(url_for('hello_guest',guest = name))
  
if __name__ == '__main__':
  app.run(debug=True)