#!/usr/bin/python3
""" add state data to table """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = '3306'

    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
                           username, password, host, port, database_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state1 = State(name='Louisiana')
    session.add(state1)
    session.commit

    print(state1.id)
    session.close()
    engine.dispose()
