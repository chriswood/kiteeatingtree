import sys
import sqlite3
import datetime
from settings import db_path
from utils import gen_hash
import atexit


class db_wrapper:
    ''' This is a wrapper for app specific database calls.
        The calling function should handle exceptions'''
    def __init__(self):
        self.conn_obj = sqlite3.connect(db_path)
        self.c = self.conn_obj.cursor()
        atexit.register(self.conn_obj.close)

    def add_user(self, user): # hashlib crap
        user.passhash = gen_hash(user.passhash.data)
        params = tuple([f.data for f in user if f.name is not 'confirm'])
        sql = """INSERT INTO users (firstname, lastname, email,
                                    username, passhash) VALUES (?,?,?,?,?)"""
        self.c.execute(sql, params)
        self.conn_obj.commit()

    def get_user(self, username):
        params = (username,)
        sql = """SELECT * FROM users WHERE username = ?"""
        self.c.execute(sql, params)

        return self.c.fetchone()
