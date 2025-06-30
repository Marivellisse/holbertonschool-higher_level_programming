#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa with their state names
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parámetros
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Conexión
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cur = db.cursor()

    # Consulta con JOIN entre ciudades y estados
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

