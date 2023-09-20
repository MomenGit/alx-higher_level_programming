#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine, Column
    from sqlalchemy.orm import Session
    import sys

    if len(sys.argv) != 4:
        sys.exit(
            "Usage: 11-model_state_insert.py <mysql_username> " +
            "<mysql_password> <database_name>")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_recycle=3600)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print("{}".format(state.id))

    session.close()
