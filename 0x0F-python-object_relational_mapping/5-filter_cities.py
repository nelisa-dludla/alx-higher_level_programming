#!/usr/bin/python3
'''
This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
'''

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]
host = 'localhost'
port = 3306


def main():
    '''This is the main program'''

    db = MySQLdb.connect(
            host=host,
            port=port,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name)

    cursor = db.cursor()
    query = '''
            SELECT cities.name
            FROM cities
            JOIN states
            ON cities.state_id=states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            '''

    cursor.execute(query, (state_name,))
    results = cursor.fetchall()

    if (results):
        unique_results = set(results)
        cities = [city[0] for city in unique_results]

        print(', '.join(cities))

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
