#from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms import Form, TextField, PasswordField, validators


class User(Form):
    firstname = TextField('first name')
    lastname = TextField('last name')
    username = TextField('Username', [
        validators.InputRequired(),
        validators.Length(min=2, max=75)
    ])
    email = TextField('email address', [
        validators.Email(message='wtf is this. invalid email.'),
        validators.Length(min=4, max=75)
    ])
    passhash = PasswordField('password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match, jerk')
    ])
    confirm = PasswordField('Repeat Password (just like a REAL website!)')
    
