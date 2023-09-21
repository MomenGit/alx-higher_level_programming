#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(
            "Usage: 13-model_state_delete_a.py <mysql_username> " +
            "<mysql_password> <database_name>")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]
                                   ))

    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()
