import sqlalchemy
from sqlalchemy import create_engine

#db_connstring = 'postgresql+psycopg2://user:password@localhost:port/dbname'
db_connstring = 'postgresql+psycopg2://postgres@localhost:5432/siyamak'

engine = create_engine(db_connstring, echo = True)

engine.execute("select 1").scalar()