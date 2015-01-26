from flask import Flask, session, redirect, url_for, request
import hashlib
from functools import wraps


def gen_hash(pw):
    salt = 'M8s2'
    return hashlib.md5(salt + pw).hexdigest()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['username'] is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function
