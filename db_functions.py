import sys
import sqlite3
import datetime
from settings import db_path

class db_wrapper:
    def __init__(self):
        self.conn_obj = sqlite3.connect(db_path)
        self.cursor = self.conn_obj.cursor()
