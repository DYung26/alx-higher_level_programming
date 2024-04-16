#!/usr/bin/python3
"""First state via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ), pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()
    states = session.query(State).order_by(State.id).all()
    state = states[0]
    print(f"{state.id}: {state.name}")
