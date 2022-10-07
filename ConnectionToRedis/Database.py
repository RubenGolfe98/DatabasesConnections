import sqlite3
import redis

DB_NAME = "contacts.db"

def existsDB():
    existsDB=True
    con,cur = openConnectionAndCursor()
    try:
        cur.execute(f"SELECT * FROM users")
    except sqlite3.OperationalError:
        existsDB=False
    return existsDB

def openConnection():
    con = redis.Redis(host="localhost")
    return con

def closeConnectionAndCursor(con):
    con.close()

