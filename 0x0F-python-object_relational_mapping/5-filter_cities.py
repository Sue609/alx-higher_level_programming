#!/usr/bin/python3
"""
This module introduces a script.
"""


import sys
import MySQLdb


def list_cities_by_state(username, password, database, state_name):
    """
    Function that takes state as an arguement and lists
    all cities of that state using the database hbtn_0e_4_usa.
    """

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cur = db.cursor()

    query = ("SELECT cities.name FROM cities "
             "INNER JOIN states ON states.id=cities.state_id "
             "WHERE states.name=%s")
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    city_names = list(row[0] for row in rows)
    print(", ".join(city_names))
    cur.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)
