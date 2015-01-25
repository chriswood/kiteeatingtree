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
        print(user)
        print("***************")
        user.passhash = gen_hash(user.passhash.data)
        params = tuple([f.data for f in user if f.name is not 'confirm'])
        sql = """INSERT INTO users (firstname, lastname, username,
                 email, passhash) VALUES (?,?,?,?,?)"""
        print("*****", sql,"***", params)
        self.c.execute(sql, params)
        self.conn_obj.commit()
        self.c.close()

    def get_user(self, username):
        params = (username,)
        sql = """SELECT * FROM users WHERE username = ?"""
        self.c.execute(sql, params)
        self.c.close()
        return self.c.fetchone()

    def edit_user(self, user):
        ignore = ['passhash', 'confirm']
        params = tuple([f.data for f in user if f.name not in ignore])
        sql = """ UPDATE users SET firstname = ?, lastname = ?, email = ?,
                  username = ? WHERE username"""
