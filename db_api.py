import mysql.connector
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError


def dbconfig() -> dict:
    tmpdbconfig = { 'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB'}
    return tmpdbconfig


def logStructure():
    dbconfig = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB'}

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("""describe log""")
    res = cursor.fetchall()
    for row in res:
        print(row)


def insertLog():
    conn = mysql.connector.connect(**dbconfig())
    cursor = conn.cursor()
    _SQL = """insert into log
              (phrase, letters, ip, browser_string, results)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, ('hitch-hikder', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}"))
    conn.commit()


def listLog():
    dbconfig = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB'}

    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """Select * from log"""
    cursor.execute(_SQL)
    res = cursor.fetchall()
    for row in res:
        print(row)


def listLogWithVersion():
    dbconfig = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB'}

    try:
        with UseDatabase(dbconfig) as cursor:
            _SQL = """Select * from logError"""
            cursor.execute(_SQL)
            res = cursor.fetchall()
            for row in res:
                print(row)
    except ConnectionError as err:
        print('Connection Error: ', err)
    except CredentialsError as err:
        print('Credential Error:', err)


listLogWithVersion()
# insertLog()