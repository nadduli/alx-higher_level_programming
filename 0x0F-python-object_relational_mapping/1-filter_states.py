#!/usr/bin/python3
""" list all states from states table where name starts with N from hbtn_0e_0_usa """

if __name__ == '__main__':
    import sys
    import MYSQLdb
    db = MYSQLdb.connect(
        host = "localhost",
        port = 3306,
        user = sys.argv[1],
        passwd = sys.argv[2],
        db = sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
