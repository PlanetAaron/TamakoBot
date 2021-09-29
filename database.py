import sqlite3

lbzn = sqlite3.connect("lbznames.sqlite")
cursor = lbzn.cursor()
table = "lbz"

def dbsetup():
    cursor.execute('''CREATE TABLE lbz(uid text, username text)''')

def dbcount():
    cursor.execute("select * from " + table)
    results = cursor.fetchall()
    return len(results)

def addentry(uid, uname):

    cursor.execute('INSERT INTO lbz VALUES("' + str(uid) + '", "' + str(uname) + '")')
    lbzn.commit()
    print("Database Updated");
