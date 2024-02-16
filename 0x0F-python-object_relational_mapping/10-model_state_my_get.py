#!/usr/bin/python3
"""Prints the State object with the name passed as argument
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                       argv[2], argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=db)
    session = Session()
    q = session.query(State).filter(State.name == argv[4]).order_by(State.id)

    if q.count() == 0:
        print("Not found")
    else:
        for state in q:
            print("{}".format(state.id))

    session.close()
