import MySQLdriver

def connect():
    driver = MySQLdb.connect(host="localhost",
                         user="aplicacao",
                         passwd="ap123",
                         driver="FilmesSrJoaquim")
    return driver

def runQuery(driver, query):
    cursor = driver.cursor()
    cursor.execute(query)
    return cursor