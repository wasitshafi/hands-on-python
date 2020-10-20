from flask import Flask
from flask import request
from flask import make_response

# To check presence of cookie in chrome : inspect => Application
app = Flask(__name__)
@app.route('/')
def index():
  return 'Welcome to homepage...!!!' + '<br/> /create_cookie<br> /read_cookie <br> /delete_cookie'

@app.route('/create_cookie')
def createcookie():
  cok = make_response("<b1>Setting a cookie...</b>")
  name = 'cok1'
  value = '18MCA054'
  max_age = 60 * 60 * 24 # 24-Hours
  #max_age = None # if cookie is not set, then it will expire one the browser is closed
  cok.set_cookie(name, value, max_age)  # setCookie(<title>, <content>, <expiry time>)
  return cok

@app.route('/delete_cookie')
def deletecookie():
  cok = make_response("<b1>Deleteing a cookie...</b>")
  name = 'cok1'
  value = '18MCA054'
  max_age = 0 # it will delete the cookie
  cok.set_cookie(name, value, max_age)  # setCookie(<title>, <content>, <expiry time>)
  return cok

@app.route('/read_cookie')
def readcookie():
  name = 'cok1'
  value = request.cookies.get(name)
  output = 'Reading Cookie Content <br/><br/>' + 'Content of <b>' + str(name) + '</b> is : <b>' + str(value) + '</b>' 
  return output

if __name__ == '__main__':
  app.run()