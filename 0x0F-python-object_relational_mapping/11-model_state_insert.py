#!/usr/bin/python3
'''
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
                    database_name
                    )

    engine = create_engine(database_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name='Louisiana'))
    session.commit()

    results = (
            session.query(State)
            .filter(State.name == 'Louisiana')
            .all()
            )

    if (results):
        for result in results:
            print('{}'.format(result.id))

    session.close()
