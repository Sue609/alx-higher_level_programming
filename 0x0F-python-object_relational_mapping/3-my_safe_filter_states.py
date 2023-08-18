#!/usr/bin/python3
"""This module introduces a function."""


import sys
import MySQLdb


def injection(username, password, database, state_name):
    """
    Injection to delete all records of a table.
    """

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    injection(username, password, database, state_name)
