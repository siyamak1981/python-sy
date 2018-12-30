import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

db_connstring = 'sqlite:///:memory:'
engine = create_engine(db_connstring, echo = True)

engine.execute("Select 1").scalar()