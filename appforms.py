#from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms import Form, TextField, PasswordField, validators

class UserBase(Form):
    firstname = TextField('first name')
    lastname = TextField('last name')
    email = TextField('email address', [
        validators.Email(message='wtf is this. invalid email.'),
        validators.Length(min=4, max=75)
    ])
    username = TextField('Username', [
        validators.InputRequired(message='userbase.'),
        validators.Length(min=2, max=75)
    ])

    def munge(self, obj):
        self.firstname.data = obj['firstname']
        self.lastname.data = obj['lastname']
        self.email.data = obj['email']
        self.username.data = obj['username']

class UserNew(UserBase):
    passhash = PasswordField('password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match, jerk')
    ])
    confirm = PasswordField('Repeat Password (just like a REAL website!)')


    
