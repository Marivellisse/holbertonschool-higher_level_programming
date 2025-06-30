#!/usr/bin/python3
"""
Safely filters states by name to avoid SQL injection
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parámetros de entrada
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Conexión
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cur = db.cursor()

    # Consulta protegida
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

