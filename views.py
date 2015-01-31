""" All functions returning an http response for ket site """

from flask import Flask, request, url_for, redirect, session
from flask import render_template
from db_functions import DBwrapper
from appforms import UserBase, UserNew
from sqlite3 import IntegrityError
from utils import login_required, is_active

app = Flask(__name__.split('.')[0])

@app.route('/')
def index():
    """ home page """
    if is_active():
        username = session['username']
        logged_in = True
    else:
        logged_in = False
        username = None
    return render_template("main.html", logged_in=logged_in,
                           username=username)

@app.route('/login', methods=['POST'])
def login():
    """ login form """
    username = request.form['username']
    dbase = DBwrapper()
    if dbase.check_user(username, request.form['password']):
        session['username'] = username
        #flash("Login succesful.")
        return redirect(url_for('index'))
    else:
        return render_template("main.html", logged_in=False)

@app.route('/logout')
def logout():
    """ log user out """
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/user/new', methods=['GET', 'POST'])
def register():
    """ add user to database """
    error = ''
    title = 'create user'
    form = UserNew(request.form)

    if request.method == 'POST':
        if form.validate():
            user = UserNew(request.values)
            dbase = DBwrapper()
            try:
                dbase.add_user(user)
            except IntegrityError, e:
                error = 'That ' + e.message.rsplit('.')[-1] + \
                        ' already exists.'
                return render_template('user.html', form=form,
                                       title=title,
                                       posturl=url_for('register'),
                                       error=error)
            #flash("You're ready to go.")
            return redirect(url_for('index'))

    return render_template('user.html', form=form,
                           title=title, posturl=url_for('register'),
                           form_action='/user/new')

@app.route('/edit/<username>', methods=['GET', 'POST'])
@login_required
def useredit(username):
    """ update userinfo """
    title = 'edit user'
    if request.method == 'POST':
        form = UserBase(request.values)
        if form.validate():
            dbase = DBwrapper()
            newname = dbase.edit_user(form, username)
            #flash('Changes saved.')
            return redirect(url_for('user', username=newname))
    else:
        dbase = DBwrapper()
        user = dbase.get_user(username)
        form = UserBase()
        form.munge(user)

    return render_template('user.html', form=form,
                           user=username, logged_in=is_active(),
                           title=title, form_action='/edit/' + username,
                           username=session['username'])

@app.route('/post/create')
def post_create():
    return render_template('post.html')



