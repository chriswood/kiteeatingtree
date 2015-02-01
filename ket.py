from flask import Flask
from flask import render_template

app = Flask(__name__.split('.')[0])
app.secret_key = '\xf3Rr/I\x17\xdf?\x86\xf1\xa6\x1e*\xae\xc0\x04\xb4\x16[*uc\x05\xc9'
app.debug = True #TODO turn off in 'production'

import ket
import views
from views import *

if __name__ == "__main__":
    app.debug = True
    app.secret_key = '\xf3Rr/I\x17\xdf?\x86\xf1\xa6\x1e*\xae\xc0\x04\xb4\x16[*uc\x05\xc9'
    app.run()
