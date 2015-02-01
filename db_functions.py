""" abstract out direct db calls and get rid of boiler plate
    connection code
"""

import sqlite3
from settings import db_path
from utils import gen_hash


class DBwrapper(object):
    ''' This is a wrapper for app specific database calls.
        The calling function should handle exceptions'''
    def __init__(self):
        """ get cursor ready """
        self.conn_obj = sqlite3.connect(db_path)
        self.conn_obj.row_factory = sqlite3.Row
        self.c = self.conn_obj.cursor()

    def add_user(self, user): # TODO fix hashlib crap
        """ add user to db """
        user.passhash = gen_hash(user.passhash.data)
        params = tuple([f.data for f in user if f.name is not 'confirm'])
        sql = """ INSERT INTO users (firstname, lastname, email,
                  username, passhash) VALUES (?,?,?,?,?) """
        self.c.execute(sql, params)
        self.conn_obj.commit()

    def get_user(self, username):
        """ return user """
        params = (username,)
        sql = """ SELECT * FROM users WHERE username = ? """
        self.c.execute(sql, params)
        return self.c.fetchone()

    def edit_user(self, user, oldname):
        """ update user """
        ignore = ['passhash', 'confirm']
        fields = [f.data for f in user if f.name not in ignore]
        fields.append(oldname)
        params = tuple(fields,)
        sql = """ UPDATE users SET firstname = ?, lastname = ?,
                  email = ?, username = ?
                  WHERE username = ?"""
        self.c.execute(sql, params)
        self.conn_obj.commit()
        return params[3]

    def check_user(self, user, password):
        """ return true if user exists """
        params = (user, password,)
        sql = """ SELECT 1 FROM users
                  WHERE username = ? AND passhash = ? """
        self.c.execute(sql, params)
        return self.c.fetchone()

    def get_user_id(self, username):
        """ return userid based on username """
        sql = """ SELECT id FROM users WHERE username = ? """
        params = (username,)
        self.c.execute(sql, params)
        res = self.c.fetchone()
        return(res['id'])

    def add_post(self, post, username):
        """ insert post into db """
        title = post.title.data
        userid = self.get_user_id(username)
        message = post.message.data
        print("**************")
        print(userid)
        params = (userid, title, message)
        sql = """ INSERT INTO posts (userid, title, message)
                  VALUES (?,?,?) """
        self.c.execute(sql, params)
        self.conn_obj.commit()

    def delete_post(self):
        """ remove post form a user """
        pass

    def update_post(self):
        """ update user post """
        pass



