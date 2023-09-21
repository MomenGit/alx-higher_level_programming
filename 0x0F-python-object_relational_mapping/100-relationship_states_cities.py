#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
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
    state = State(name='California')
    session.add(state)
    session.commit()
    city = City(name='San Francisco', state_id=state.id)
    session.add(city)
    session.commit()
    session.close()
