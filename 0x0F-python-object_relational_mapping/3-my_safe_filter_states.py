#!/usr/bin/python3
"""
a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""
import MySQLdb
from sys import argv


def filter_states_by_name():
    """Filter states by name and prevent sql injection"""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3], port=3306)
    cur = db.cursor()
    match = argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    filter_states_by_name()
