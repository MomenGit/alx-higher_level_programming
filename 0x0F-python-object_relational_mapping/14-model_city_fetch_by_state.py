#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(
            "Usage: 14-model_city_fetch_by_state.py <mysql_username> " +
            "<mysql_password> <database_name>")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]
                                   ))

    Base.metadata.create_all(engine)
    session = Session(engine)
    states_cities = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()
    for state_city in states_cities:
        print('{}: ({}) {}'.format(
            state_city[0].name, state_city[1].id, state_city[1].name))
    session.close()
