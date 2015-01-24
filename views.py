from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from db_functions import db_wrapper
from appforms import User
from sqlite3 import IntegrityError

app = Flask(__name__.split('.')[0])

@app.route('/')
def index():
    logged_in = True
    return render_template("main.html", logged_in=logged_in)

@app.route('/user/new', methods=['GET', 'POST'])
def register():
    logged_in=True
    error = ''
    title = 'create user'
    form = User(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User(request.values)
            db = db_wrapper()
            try:
                db.add_user(user)
            except IntegrityError:
                error = "email already in use"
                return render_template('user.html', form=form,
                       logged_in=logged_in, title=title,
                       posturl=url_for('register'), error=error)
            flash('Thanks for registering')
            return redirect(url_for('index'))

    return render_template('user.html', form=form,
           logged_in=logged_in, title=title,
           posturl=url_for('register'))

@app.route('/edit/<username>')
def user(username):
    db = db_wrapper()
    user = db.get_user(username)
    logged_in = True

    #return 'User %s' % username
    return render_template('user.html', user=username, logged_in=logged_in)



