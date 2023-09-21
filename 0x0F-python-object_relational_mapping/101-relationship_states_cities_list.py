#!/usr/bin/python3
"""
lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(
            "Usage: 100-relationship_states_cities.py <mysql_username> " +
            "<mysql_password> <database_name>")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]
                                   ))

    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
