#!/usr/bin/python3
"""filters states by states.id and starts with N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    [print(row) for row in curr.fetchall() if row[1][0] == 'N']
    curr.close()
    db.close()
