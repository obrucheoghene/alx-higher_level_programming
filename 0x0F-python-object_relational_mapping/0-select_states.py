#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


def list_all_states():
    """List all states"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        host='localhost',
        port=3306,
        charset="utf8"
        )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    if len(argv) < 4:
        print("3 arguments required")
    else:
        list_all_states()
