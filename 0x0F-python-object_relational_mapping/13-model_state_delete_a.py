#!/usr/bin/python3
'''
This script deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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
            .all()
            )

    if (results):
        for result in results:
            session.delete(result)
        session.commit()

    session.close()
