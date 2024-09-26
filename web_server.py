import flask
from flask import render_template
import os
from utils import const


def start_ngrok():
    # os.system(const.ngrok_host)
    os.system(const.ngrok_server)



start_ngrok()
app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


app.run(port=1515)
