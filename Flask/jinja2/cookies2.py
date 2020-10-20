from flask import Flask
from flask import request
from flask import make_response
from flask import render_template

# To check presence of cookie in chrome : inspect => Application
app = Flask(__name__)
@app.route('/')
def index():
  return render_template('cookie_details.html')

@app.route('/create_cookie/', methods = ['GET', 'POST'])
def create_cookie():
  cok = make_response("<b1>Setting a Cookie...</b>")
  name = ''
  value = ''
  max_age = 0
    
  if request.method == 'GET': # then we have to take data from url string
    name = request.args.get('txtb_id')
    value = request.args.get('txtb_content')
    max_age = int(request.args.get('txtb_age'))
  else:
    name = request.form['txtb_id']
    value = request.form['txtb_content']
    max_age = int(request.form['txtb_age'])
        
  cok.set_cookie(name, value, max_age)
  return cok # returning response

@app.route('/read_cookie/', methods=['GET', 'POST'])
def readcookie():
  name = '102' # assumed
  value = request.cookies.get(name)
  output = 'Reading Cookie Content <br/><br/>' + 'Content of <b>' + str(name) + '</b> is : <b>' + str(value) + '</b>'
  return output

if __name__ == '__main__':
  app.run()