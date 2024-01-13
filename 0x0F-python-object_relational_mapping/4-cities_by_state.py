#!/usr/bin/python3
'''
This script that lists all cities from the database hbtn_0e_4_usa
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
            SELECT cities.id, cities.name, states.name
            FROM states
            JOIN cities
            ON states.id=cities.state_id
            ORDER BY cities.id ASC
            LIMIT 15
            '''

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
