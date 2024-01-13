#!/usr/bin/python3
'''
This script lists all State objects that contain the
letter a from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    database_url = 'mysql://{}:{}@{}:{}/{}'.format(
                    mysql_username,
                    mysql_password,
                    host,
                    port,
                    database_name)

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
            session.query(State)
            .filter(State.name.like('%a%'))
            .order_by(State.id.asc())
            .all()
            )

    if results:
        for result in results:
            print('{}: {}'.format(result.id, result.name))

    session.close()
