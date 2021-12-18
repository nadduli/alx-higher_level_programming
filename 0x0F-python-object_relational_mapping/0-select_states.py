#!/usr/bin/python3
""" list all files in hbtn_0e_0_usa order by states.id """

if __name__ == '__main__':

    import MySQLdb
    import sys
    db = MySQLdb.connect (host = "localhost", port = 3306, user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    info = mycursor.fetchall()
    for items in info:
        print(items)
