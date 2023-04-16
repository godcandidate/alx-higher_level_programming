#!/usr/bin/python3

"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve state
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Sessions = sessionmaker(bind=engine)

    sessions = Sessions()
    instances = sessions.query(State).order_by(State.id).first()

    if instances is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(instances.id, instances.name))
