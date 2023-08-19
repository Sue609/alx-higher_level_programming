#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""


import MySQLdb
import sys


def list_states(username, password, database):
    """
    Function that lists all states with name
    starting with 'N'.
    """

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name "
                "LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
