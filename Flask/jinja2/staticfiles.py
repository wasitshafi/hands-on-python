from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)

# Method 2, passing arguments
@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run()