from sqlalchemy import Sequence
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///database.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String, unique = True)
    password = Column(String)
    accesstype = Column(String)
 

    #----------------------------------------------------------------------
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.accesstype = accesstype
        


# create tables
Base.metadata.create_all(engine)
