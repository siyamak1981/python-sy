import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import or_, and_

from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound





#db_connstring = 'postgresql+psycopg2://user:password@localhost:port/dbname'

#Configuration
db_connstring = 'postgresql+psycopg2://postgres@localhost:5432/siyamak'
engine = create_engine(db_connstring, echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()


# Check connection is true or not
# engine.execute("select 1").scalar()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    #CRUD => Create, Read, Update, Delete
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    
    def __repr__(self):
        return "<User('{name}', '{fullname}', '{pw}')> ".format(name = self.name, 
                                                  fullname = self.fullname, 
                                                  pw = self.password)



Base.metadata.create_all(engine)