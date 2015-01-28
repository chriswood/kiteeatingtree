kiteeatingtree.org is a website I'm getting going to share
things with family and friends and allow them to do the same.

TODO: (not prioritized, X = done)
    Add growl type notifications
    add information section to front page
    make user form error display not jump to top on error
    implement posts
    add posts to db
    display all posts
    display posts per user
    let user edit his posts
    implement picture sharing
    add password edit feature
    add send someone a private message
    add send a request to admin
    add email user/users feature
    write bash script to rsync with server and touch wsgi file
    X - Handle login/session
    X - add validated user to session
    X - check for validated user
    X - Add login decorator
    X - Fix when to show logged in as
    X - create user
    X - Add feedback on form submittal success for user/edit
    X - add sqlite db
    X - get schema going
    X - split home page into posts and info
    X - figure out envars
    X - fix where edit screwed up create
    X - edit user info
    X - Fix OBNOXIOUS db permission error (www-data must own
        db file AND directory)

Future ideas for app:
    -Maybe use OpenId and Flask-Login for user session and authentication
    -Generalize everything, so that someone with little to no programming
        experience can create their family/group an instance of this
    -maybe have design/stationery templates for emails/pages
    -Give everyone a way to make todo lists

-----The following code will run an instance of ket in a python interpreter
     for easier debugging on the server

import os, sys
PROJECT_DIR = '/var/www/kiteeatingtree.org/ket'
sys.path.append(PROJECT_DIR)
from ket import app as application
from flask import Flask, request, url_for, redirect, flash, session
from flask import render_template
from db_functions import db_wrapper
from appforms import UserBase, UserNew
from sqlite3 import IntegrityError
from utils import login_required, is_active

app = Flask(__name__.split('.')[0])
import sys
import sqlite3
import datetime
from settings import db_path
from utils import gen_hash
conn_obj = sqlite3.connect(db_path)
conn_obj.row_factory = sqlite3.Row

-----APACHE CONF
# domain: kiteeatingtree.org
# public: /var/www/kiteeatingtree.org/public_html/

<VirtualHost *:80>
  # Admin email, Server Name (domain name), and any aliases
  ServerAdmin chris@kiteeatingtree.org
  ServerName  www.kiteeatingtree.org
  ServerAlias kiteeatingtree.org

  # Index file and Document Root (where the public files are located)
  DirectoryIndex index.html
  DocumentRoot /var/www/kiteeatingtree.org/ket
  # Log file locations
  LogLevel warn
  CustomLog /var/www/kiteeatingtree.org/ket/log/access.log combined

  # All files below document root should be handled by application.wsgi
  # Reload processes on wsgi file edit
  WSGIDaemonProcess ket user=www-data group=www-data threads=5
  WSGIScriptAlias / /var/www/kiteeatingtree.org/ket/application.wsgi
  WSGIScriptReloading On

  <Directory /var/www/kiteeatingtree.org/ket>
    WSGIProcessGroup ket
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
  </Directory>

  Alias /static /var/www/kiteeatingtree.org/ket/static
  <Directory /var/www/kiteeatingtree.org/ket/static/>
    Order allow,deny
    Allow from all
  </Directory>
  Alias /images /var/www/kiteeatingtree.org/ket/static/images
  <Directory /var/www/kiteeatingtree.org/ket/images/>
  Order allow,deny
  Allow from all
  </Directory>

</VirtualHost>



