""" Define all forms here. """

from wtforms import Form, TextField, PasswordField, validators, IntegerField
from wtforms import TextAreaField

class UserBase(Form):
    """ Id field is primary key, and referenced from Post table. """
    firstname = TextField('first name')
    lastname = TextField('last name')
    email = TextField('email address', [
        validators.Email(message='wtf is this. invalid email.'),
        validators.Length(min=4, max=75)
    ])
    username = TextField('Username', [
        validators.InputRequired(),
        validators.Length(min=2, max=75)
    ])

    def munge(self, obj):
        """ Do the dictionary to model transfer. """
        self.firstname.data = obj['firstname']
        self.lastname.data = obj['lastname']
        self.email.data = obj['email']
        self.username.data = obj['username']

class UserNew(UserBase):
    """ On user create these fields are needed. """
    passhash = PasswordField('password', [
        validators.InputRequired(),
        validators.EqualTo('confirm', message='Passwords must match, jerk')
    ])
    confirm = PasswordField('Repeat Password (just like a REAL website!)')

class Post(Form):
    """ Store post data. Id field is primary key. """
    userid = IntegerField('userid')
    title = TextField('title (optional)')
    message = TextAreaField('message', [
        validators.Length(min=1, max=500)
    ])
    
    
