#!/usr/bin/python3
'''
This script prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    database_url = 'mysql://{}:{}@{}:{}/{}'.format(
                    mysql_username,
                    mysql_password,
                    host,
                    port,
                    database_name
                    )

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
            session.query(State)
            .filter(State.name == state_name)
            .all()
            )

    if (results):
        for result in results:
            print('{}'.format(result.id))
    else:
        print('Not found')

    session.close()
