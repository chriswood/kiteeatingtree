from flask import Flask, session, redirect, url_for, request
import hashlib
from functools import wraps


def gen_hash(pw):
    salt = 'M8s2'
    return hashlib.md5(salt + pw).hexdigest()

def is_active():
    return(session.has_key('username') and
           session['username'] is not None)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not is_active():
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function
