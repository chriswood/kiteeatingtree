#from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms import Form, TextField, PasswordField, validators


class User(Form):
    firstname = TextField('first name')
    lastname = TextField('last name')
    username = TextField('Username', [validators.Length(min=4, max=75)])
    email = TextField('email address', [validators.Length(min=4, max=75)])
    passhash = PasswordField('password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    
