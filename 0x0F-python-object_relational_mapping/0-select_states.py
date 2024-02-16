#!/usr/bin/python3
import MySQLdb
import sys
"""listing states from the database hbtn_0e_0_usa"""
def main():
    """
        Function containing code to select all the states
        from the database.
    """

    conn = MySQLdb.connect(
                host="localhost", port=3306, user=sys.argv[1],
                passwd=sys.argv[2], db=sys.argv[3], charset="utf8mb4"
            )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
