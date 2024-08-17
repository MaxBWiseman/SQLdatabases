from sqlalchemy import (
    create_engine, Column, Integer, String, or_
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# connect to the local database
db = create_engine("postgresql:///chinook")
base = declarative_base()  # this is the base class for all our models

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
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

# add each instance of our programmers to our sessions
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)

# commit our session to the database
session.commit()

# if there is a duplicate record, use this code to delete the extras
# Define the conditions for the people you want to delete duplicates for
#conditions = [
    #(Programmer.first_name == "Alan", Programmer.last_name == "Turing"),
    # Add more conditions as needed
#]

#for condition in conditions:
    #persons = session.query(Programmer).filter(or_(*condition)).all()
    #if len(persons) > 1:
        #for person in persons[1:]:
            #session.delete(person)
        #session.commit()

# query the database to find all programmers
programmers = session.query(Programmer).all()
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )