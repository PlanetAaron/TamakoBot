import sqlite3

lbzn = sqlite3.connect("lbznames.sqlite")
cursor = lbzn.cursor()
table = "lbz"

def dbcount():
    cursor.execute("select * from " + table)
    results = cursor.fetchall()
    return len(results)