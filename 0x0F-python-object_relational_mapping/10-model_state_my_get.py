#!/usr/bin/python3
"""
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    import sys

    if len(sys.argv) != 5:
        sys.exit(
            "Usage: 10-model_state_my_get.py <mysql_username> " +
            "<mysql_password> <database_name> <state name>")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_recycle=3600)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = session.query(State).filter(
        State.name == sys.argv[4]).order_by(State.id).first()
    if state is not None:
        print("{}".format(state.id, state.name))
    else:
        print("Not found")

    session.close()
