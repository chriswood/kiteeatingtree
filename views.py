from flask import Flask, url_for
from flask import render_template

app = Flask(__name__.split('.')[0])

@app.route("/")
def index():
    header_url = url_for('static', filename='images/header.png')
    logged_in = True
    return render_template("main.html", header=header_url, logged_in=logged_in)
