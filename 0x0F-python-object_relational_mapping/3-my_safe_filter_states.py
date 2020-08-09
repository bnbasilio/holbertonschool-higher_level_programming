#!/usr/bin/python3
"""lists all states where name matches argument from database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    arg = ("%{}%".format(argv[4]))
    cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY %s \
                ORDER BY states.id ASC", [arg])
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
