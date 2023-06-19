#!/usr/bin/python3
"""
    A script that lists all states from the database hbtn_0e_0_usa
    matching a name
"""
import sys
import MySQLdb


def list_states_by_names():
    """List all states by name"""

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cursor = db.cursor()

    sql = """ SELECT * FROM states
          WHERE name LIKE BINARY '{}'
          ORDER BY id ASC """.format(sys.argv[4])

    cursor.execute(sql)

    data = cursor.fetchall()

    for row in data:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    list_states_by_names()
