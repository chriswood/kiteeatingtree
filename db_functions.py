import sys
import sqlite3
import datetime
from settings import db_path
from utils import gen_hash


class db_wrapper:
    ''' This is a wrapper for app specific database calls.
        The calling function should handle exceptions'''
    def __init__(self):
        self.conn_obj = sqlite3.connect(db_path)
        self.conn_obj.row_factory = sqlite3.Row
        self.c = self.conn_obj.cursor()

    def add_user(self, user): # hashlib crap
        user.passhash = gen_hash(user.passhash.data)
        params = tuple([f.data for f in user if f.name is not 'confirm'])
        sql = """ INSERT INTO users (firstname, lastname, email,
                  username, passhash) VALUES (?,?,?,?,?) """
        self.c.execute(sql, params)
        self.conn_obj.commit()

    def get_user(self, username):
        params = (username,)
        sql = """ SELECT * FROM users WHERE username = ? """
        self.c.execute(sql, params)
        return(self.c.fetchone())

    def edit_user(self, user, oldname):
        ignore = ['passhash', 'confirm']
        fields = [f.data for f in user if f.name not in ignore]
        fields.append(oldname)
        params = tuple(fields,)
        sql = """ UPDATE users SET firstname = ?, lastname = ?,
                  email = ?, username = ?
                  WHERE username = ?"""
        self.c.execute(sql, params)
        self.conn_obj.commit()
        return(params[3])

    def check_user(self, user, pw):
        params = (user, pw,)
        sql = """ SELECT 1 FROM users
                  WHERE username = ? AND passhash = ? """
        self.c.execute(sql, params)
        return(self.c.fetchone())

