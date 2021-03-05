import os
import sys

from flask import Flask, session, render_template, request, flash, redirect, abort, jsonify
from flask_session import Session
from datetime import datetime
import requests
import geojson
import json

app = Flask(__name__)

# fix windows terminal issue on my computer
if sys.platform.lower() == "win64":
    os.system('color')

# default route, no data is passed to index
@app.route("/", methods=['POST', 'GET'])
def index():
    # get today's date
    today = datetime.today().strftime('%Y-%m-%d')
    # default dates for widget will be passed as today's date
    return render_template("index.html", fr=today, to=today)

# when dates are passed, feed data to index
@app.route("/dates", methods=['POST'])
def dates():
    # get today's date
    today = datetime.today().strftime('%Y-%m-%d')
    # get from and to dates from the date picker
    fr = request.form.get("from")
    to = request.form.get("to")
    # if from date is in the future, return an Error
    if today < fr:
        err2=1
    else:
        err2=0
    # if from is later than to, send error
    if fr > to:
        err=1
    else:
        err=0
    url = "https://data.calgary.ca/resource/c2es-76ed.geojson?$where=issueddate > '"+fr+"' and issueddate < '"+to+"'"
    # request with url
    data = requests.get(url).json()
    # get only features
    data2 = data['features']
    # if there are no results, send error
    if data2 == []:
        err1=1
    else:
        err1=0
    return render_template("index.html",data=data2, fr=fr, to=to, today=today, err=err, err1=err1, err2=err2)
