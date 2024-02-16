#!/usr/bin/python3
""" 8-model_state_fetch_first.py """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                       sys.argv[2], sys.argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=db)
    session = Session()
    if session.query(State).first() is None:
        print("Nothing")
    else:
        print("{}: {}".format(session.query(State).first().id,
              session.query(State).first().name))

    session.close()
