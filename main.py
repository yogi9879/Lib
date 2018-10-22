from flask import Flask, render_template
form pandas import *

app = Flask(__name__)

@app.route('/')
def upload_file():
   return "Hi"
if __name__ == '__main__':
   app.run()
