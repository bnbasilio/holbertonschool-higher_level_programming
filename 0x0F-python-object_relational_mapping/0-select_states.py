#!/usr/bin/python3
""" lists all states from database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user=argv[1],
                     passwd=argv[2], db=argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
