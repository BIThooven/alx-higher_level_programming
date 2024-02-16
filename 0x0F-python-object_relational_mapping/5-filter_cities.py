#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities from the database hbtn_0e_4_usa"""


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
    part1 = "SELECT cities.name FROM cities JOIN states"
    part2 = " ON cities.state_id = states.id WHERE states.name = %s"
    part3 = " ORDER BY cities.id"
    curr.execute("{}{}{}".format(part1, part2, part3), (search,))
    rows = curr.fetchall()
    [print(row[0], end=", " if row != rows[-1] else "\n") for row in rows]
    curr.close()
    db.close()
