#!/usr/bin/python3
"""
Lists all states starting with 'N' from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parámetros: usuario, contraseña y base de datos
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Conexión a la base de datos
    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd, db=db_name)
    cur = db.cursor()

    # Consulta: estados que comienzan con 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Mostrar resultados
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

