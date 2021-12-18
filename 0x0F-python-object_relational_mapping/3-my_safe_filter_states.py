#!/usr/bin/python3
""" list all states from state table
    from hbtn_0e_4_usa where name 
    is passed as an argument and
    free from sql injection """
if __name__ == '__main__':

    import sys
    import MySQLdb

    db = MySQLdb.connect( host='localhost', port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s 
                 ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
