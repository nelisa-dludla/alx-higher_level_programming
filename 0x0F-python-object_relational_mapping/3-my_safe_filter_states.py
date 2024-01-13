#!/usr/bin/python3
'''
script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, it is safe from MySQL injections!
'''

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name_searched = sys.argv[4]
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
            SELECT *
            FROM states
            WHERE name = %s
            ORDER BY states.id ASC
            '''
    cursor.execute(query, (state_name_searched,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
