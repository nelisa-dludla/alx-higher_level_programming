#!/usr/bin/python3
'''
This script lists all states with a name starting with N
from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys


if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(
            host=host,
            port=port,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name)

    cursor = db.cursor()
    query = '''
            SELECT *
            FROM states
            WHERE name
            LIKE "N%"
            ORDER BY states.id ASC
            '''

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
