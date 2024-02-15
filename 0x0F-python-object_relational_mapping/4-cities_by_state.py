#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    curr = db.cursor()
    query_part1 = "SELECT cities.id, cities.name, states.name FROM cities "
    query_part2 = "JOIN states ON cities.state_id = states.id "
    query_part3 = "ORDER BY cities.id"
    curr.execute(query_part1 + query_part2 + query_part3)
    rows = curr.fetchall()
    for row in rows:
        print(row)

    curr.close()
    db.close()
