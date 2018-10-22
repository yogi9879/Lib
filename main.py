from flask import Flask, render_template
#import pandas as pd

app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return "Hi"
if __name__ == '__main__':
   app.run()
