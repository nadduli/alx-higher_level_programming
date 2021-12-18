#!/usr/bin/python3
""" list all states from states table
    where name is an argument
    order by state id from hbtn_0e_0_usa """
if __name__ == '__main__':
    
    import MySQLdb
    import sys
    
    db = MySQLdb.connect(host="localhost", port=3306,
                          user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
