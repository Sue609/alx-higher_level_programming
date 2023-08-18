#!/usr/bin/python3
"""
Script that takes three arguements.
"""


import sys
import MySQLdb


def list_cities(username, password, database):
    """
    This function lists all the cities form the database.
    """

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()

    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")

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

    list_cities(username, password, database)
