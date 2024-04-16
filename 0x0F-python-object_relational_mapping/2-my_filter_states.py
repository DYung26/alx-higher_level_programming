#!/usr/bin/python3
'''Filter states by user input'''
import MySQLdb
import sys

if __name__ == '__main__':
    '''Establish a connection to the MySQL database.
    Parameters:
        host: The host name where the MySQL server is running.
        port: The port number on which the MySQL server
            is listening (default is 3306 for MySQL).
        user: The username for authenticating with the MySQL server.
        passwd: The password for authenticating with the MySQL server.
        db: The name of the MySQL database to connect to.
        charset: The character set to use for communication
            with the MySQL database (default is "utf8").'''
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{0}'"
        " ORDER BY id ASC".format(sys.argv[4])
    )
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    conn.close()
