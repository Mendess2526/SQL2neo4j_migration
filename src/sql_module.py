import MySQLdb

def connect():
    db = MySQLdb.connect(host="localhost",
                         user="aplicacao",
                         passwd="ap123",
                         db="FilmesSrJoaquim")
    return db

def runQuery(db, query):
    cursor = db.cursor()
    cursor.execute(query)
    return cursor