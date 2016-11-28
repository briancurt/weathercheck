#!/bin/python3

from collect import collectsmn, collectaccu, collectwc, collecttime, timeofday
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    smn_temp, accu_temp, wc_temp, lastupdate, checktime = collectsmn(), collectaccu(), collectwc(), collecttime(), timeofday()
    if 6 <= checktime <= 20:
     ampm = 1
    else:
     ampm = 0 
    return render_template('index.html', smn_temp=smn_temp, accu_temp=accu_temp, wc_temp=wc_temp, lastupdate=lastupdate, ampm=ampm)

if __name__ == "__main__":
    app.run('0.0.0.0')
