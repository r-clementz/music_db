import sqlite3

db_name = 'music.db'

def run(query, values = {}): 
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    result = cur.execute(query,values) # executemany()
    conn.commit()
    conn.close()
    return result.lastrowid 

def get(query,values = {}):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(query,values)
    results = cur.fetchall()
    conn.close()
    return results 