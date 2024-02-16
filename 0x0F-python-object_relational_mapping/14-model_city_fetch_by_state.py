#!/usr/bin/python3
"""Print all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]),
                       pool_pre_ping=True)

    Base.metadata.create_all(db)
    session = sessionmaker(bind=db)
    session = session()
    query = session.query(City, State)
    q = query.filter(City.state_id == State.id).order_by(City.id)

    for city, state in q:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
