from flask import Flask, url_for
from flask import render_template

app = Flask(__name__.split('.')[0])

@app.route("/")
def index():
    image = url_for('static', filename='images/elephants.jpg')
    return render_template("main.html", image=image)
