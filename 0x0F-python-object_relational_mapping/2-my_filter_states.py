#!/usr/bin/python3
import MySQLdb
"""
This module introduces a new function.
"""


import sys
import MySQLdb


def display_value(username, password, database, nameSearch):
    """
    Script that displays all values in the state table.
    """

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database,
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s "
                "ORDER BY id ASC", (nameSearch,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    nameSearch = sys.argv[4]

    display_value(username, password, database, nameSearch)
