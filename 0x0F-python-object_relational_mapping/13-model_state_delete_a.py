#!/usr/bin/python3
"""Delete states via SQLAlchemy"""
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
    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()
    for state in states:
        if "a" in state.name:
            session.delete(state)
    session.commit()
