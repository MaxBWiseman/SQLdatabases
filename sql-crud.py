from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connect to the local database
db = create_engine("postgresql:///chinook")
base = declarative_base() #this is the base class for all our models

# create a class-based model for the best programmers in the world table
class Programmer(base):
    __tablename__ = "programmers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the database)
Session = sessionmaker(db)
# opens an actual session by calling the Session() class defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our programmer table

class Programmer(base):
    __tablename__ = "programmers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# for creating records on the programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)



# add each instance of our programmers to our sessions
session.add(ada_lovelace)

# commit our session to the database
session.commit()


# if there is a duplicate record, use this code to delete the extras

#ada_lovelaces = session.query(Programmer).filter_by(first_name="Ada", last_name="Lovelace").all()
#if len(ada_lovelaces) > 1: #change this to the name of duplicate record
    #for ada in ada_lovelaces[1:]: #this too
        #session.delete(ada)
    #session.commit()


# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
        )