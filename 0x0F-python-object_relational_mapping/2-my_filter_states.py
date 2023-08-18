#!/usr/bin/python3
"""
This module introduces a new function.
"""


import MySQLdb
import sys


def display_value(username, password, database, nameSearch):
    """
    Script that displays all values in the state table.
    """

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database,
                         port=3306)
    cur = db.cursor()

    query = ("SELECT * FROM states WHERE name = '{}' "
             "ORDER BY id ASC".format(nameSearch))
    cur.execute(query)

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
