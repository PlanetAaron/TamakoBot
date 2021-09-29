import sqlite3

lbzn = sqlite3.connect("lbznames.sqlite")
cursor = lbzn.cursor()
mktable = """
CREATE TABLE lbz
(
    uid TEXT,
    username INT
);
"""
cursor.execute(mktable)
lbzn.commit()
lbzn.close()