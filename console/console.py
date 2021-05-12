from bin.parser import Parser
from sqlite import sqlite_db
from bin import parser
from sqlite.sqlite_db import Database


class Console:
    def __init__(self):
        self.db = Database()

    def view(self):
        res = self.db.read_db()
        return res

    def get(self, param):
        self.db.write_db(Parser(param))
