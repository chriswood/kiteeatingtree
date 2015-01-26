from flask import Flask, request, url_for, redirect, flash, session
from flask import render_template
from db_functions import db_wrapper
from appforms import UserBase, UserNew
from sqlite3 import IntegrityError
from utils import login_required

app = Flask(__name__.split('.')[0])

@app.route('/')
@login_required
def index():
#        if 'username' in session:
#        return 'Logged in as %s' % escape(session['username'])
#    return 'You are not logged in'
    logged_in = False
    return render_template("main.html", logged_in=logged_in)

@app.route('/login', methods=['POST'])
def login():
    un = request.form['username']
    pw = request.form['password']
    db = db_wrapper()
    if db.check_user(un, pw):
        session['username'] = un
        flash("Login succesful.")
        return redirect(url_for('index'))
    else:
        return render_template("main.html", logged_in=False)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/user/new', methods=['GET', 'POST'])
def register():
    logged_in=True
    error = ''
    title = 'create user'
    form = UserNew(request.form)

    if request.method == 'POST':
        if form.validate():
            user = UserNew(request.values)
            db = db_wrapper()
            try:
                db.add_user(user)
            except IntegrityError, e:
                error = 'That ' + e.message.rsplit('.')[-1] + \
                        ' already exists.'
                return render_template('user.html', form=form,
                       logged_in=logged_in, title=title,
                       posturl=url_for('register'), error=error,
                       showpass=True)
            flash("You're ready to go.")
            return redirect(url_for('index'))

    return render_template('user.html', form=form,
           logged_in=logged_in, title=title,
           posturl=url_for('register'), form_action='/user/new')

@app.route('/edit/<username>', methods=['GET', 'POST'])
def user(username):
    logged_in = True
    title = 'edit user'

    if request.method == 'POST':
        form = UserBase(request.values)
        if form.validate():
            db = db_wrapper()
            newname = db.edit_user(form, username)
            flash('Changes saved.')
            return redirect(url_for('user', username=newname))
    else:
        db = db_wrapper()
        user = db.get_user(username)
        form = UserBase()
        form.munge(user)

    return render_template('user.html', form=form,
                            user=username, logged_in=logged_in,
                            title=title, form_action='/edit/' + username)




