from flask import Flask, request, url_for, redirect, flash
from flask import render_template
from db_functions import db_wrapper
from appforms import UserBase, UserNew
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

            return redirect(url_for('index'))

    return render_template('user.html', form=form,
           logged_in=logged_in, title=title,
           posturl=url_for('register'), showpass=True,
           form_action='/user/new')

@app.route('/edit/<username>', methods=['GET', 'POST'])
def user(username):
    logged_in = True
    title = 'edit user'

    if request.method == 'POST':
        form = UserBase(request.values)
        if form.validate():
            db = db_wrapper()
            newname = db.edit_user(form, username)

            flash('Thanks for editing')
            return redirect(url_for('user', username=newname))

    else:
        db = db_wrapper()
        user = db.get_user(username)
        form = UserBase()
        form.munge(user)

    #return 'User %s' % username
    return render_template('user.html', form=form,
                            user=username, logged_in=logged_in,
                            title=title, form_action='/edit/' + username)



