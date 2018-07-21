#!/usr/bin/python3
"""list first states"""

import MySQLdb
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    table = session.query(State).first()

    if table is not None:
        print("{}: {}".format(table.id, table.name))
    else:
        print("Nothing")

    session.close()
