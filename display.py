#!/bin/python3

from collect import collectsmn, collectaccu, collectwc
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    smn_temp = collectsmn()
    accu_temp = collectaccu()
    wc_temp = collectwc()
    return render_template('index.html', smn_temp=smn_temp, accu_temp=accu_temp, wc_temp=wc_temp)

if __name__ == "__main__":
    app.run(0.0.0.0)
