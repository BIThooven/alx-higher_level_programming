#!/usr/bin/python3
""" script that makes my states.id safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id",
                 (search,))
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    db.close()
