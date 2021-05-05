from sqlite import sqlite_db
from bin import parser

def view():
   res = sqlite_db.read_db()
   return res

def get(param):
    sqlite_db.write_db(param, param, parser.parse(param))
