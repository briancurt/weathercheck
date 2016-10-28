#!/bin/python3

from collect import collectsmn
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    smn_temp = collectsmn()
    return render_template('index.html', smn_temp=smn_temp)

if __name__ == "__main__":
    app.run()
