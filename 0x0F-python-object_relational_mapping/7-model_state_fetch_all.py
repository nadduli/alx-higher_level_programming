#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = '3306'
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(username, password, database_name, host, port, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_info = session.query(State).order_by(State.id).all()
    session.close()
    engine.dispose()
    
    for state in state_info:
        print('{}: {}'.format(State.id, State.name))
    
