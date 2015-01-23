import sys
import sqlite3
import datetime
from settings import db_path

class db_wrapper:
    def __init__(self):
        self.conn_obj = sqlite3.connect(db_path)
        self.c = self.conn_obj.cursor()

    def add_user(self, user): # hashlib crap
        user.passhash = md5(user.passhash.data)

        params = tuple([f.data for f in user if f.name is not 'confirm'])

        sql = """INSERT INTO users (firstname, lastname, email,
                                    username, passhash) VALUES (?,?,?,?,?)"""
        self.c.execute(sql, params)
        self.conn_obj.commit()
