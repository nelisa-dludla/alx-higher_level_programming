#!/usr/bin/python3
'''
This script lists all State objects from the database hbtn_0e_6_usa
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

    states = session.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))

    session.close()
