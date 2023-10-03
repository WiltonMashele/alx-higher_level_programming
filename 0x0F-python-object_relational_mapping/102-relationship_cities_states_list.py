#!/usr/bin/python3
"""
script that lists all City objects from the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}')
    session = sessionmaker(bind=engine)()
    results = session.query(City, State).join(State, City.state_id == State.id).order_by(asc(City.id)).all()
    for city, state in results:
        print(f"{city.id}: {city.name} -> {state.name}")
