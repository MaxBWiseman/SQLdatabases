from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connect to the local database
db = create_engine("postgresql:///chinook")
base = declarative_base() #this is the base class for all our models


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the database)
Session = sessionmaker(db)
# opens an actual session by calling the Session() class defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)