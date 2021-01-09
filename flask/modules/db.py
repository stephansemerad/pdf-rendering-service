import sqlite3, os
db_path = os.path.join( os.path.dirname(os.path.realpath(__file__)), 'pdf-rendering-service.db' )

def select(sql):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    data = cursor.execute(sql).fetchall()
    cursor.close()
    conn.close()
    return data

def insert(sql):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    lastrowid = cursor.lastrowid
    cursor.close()
    conn.close()
    return lastrowid

def update(sql):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True

def delete(sql):
    update(sql)

# tables set up from tables.sql
sql_tables = open (os.path.join( os.path.dirname(os.path.realpath(__file__)), 'tables.sql' ), "r").read()
sql_tables = sql_tables.split(';')
for sql in sql_tables:
    print(sql)
    print(insert(sql))











