#!/usr/bin/python3
"""First state via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ), pool_pre_ping=True
    )
    session = sessionmaker(bind=engine)()
    citi_states = session.query(City, State).join(State).filter(
        State.id == City.state_id).order_by(City.id).all()
    for city, state in citi_states:
        print(f'{state.name}: ({city.id}) {city.name}')
