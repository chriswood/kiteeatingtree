from flask import Flask
from flask import render_template

app = Flask(__name__.split('.')[0])

import ket
import views
from views import *

if __name__ == "__main__":
    app.debug = True
    app.run()


