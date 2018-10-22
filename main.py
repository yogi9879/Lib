from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def upload_file():
   return "Hi"
@app.route('/upload')
def upload_file1():
   return "yoyo"                    #render_template('upload.html')
if __name__ == '__main__':
   app.run()
