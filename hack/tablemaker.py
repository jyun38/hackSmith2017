import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
import csv
 
engine = create_engine('sqlite:///tutorial.db', echo=True)
 

Session = sessionmaker(bind=engine)
session = Session()
ifile  = open("test.csv", "r")
read = csv.reader(ifile)
for row in read:
    user = User(row[0], row[1])
    session.add(user)
    session.commit()    

    print(user)

print("done....")
print(session)