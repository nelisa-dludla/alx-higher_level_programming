#!/usr/bin/python3
'''
This script prints all City objects from the database hbtn_0e_14_usa
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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
            session.query(City, State)
            .filter(City.state_id == State.id)
            .order_by(City.id)
            .limit(15)
            .all()
            )

    unique_results = set(results)

    if (unique_results):
        for city, state in results:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
