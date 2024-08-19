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
"""
max_wiseman = Programmer(
    first_name="Max",
    last_name="Wiseman",
    gender="M",
    nationality="British",
    famous_for="Junior Software Developer"
)


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
"""

# add each instance of our programmers to our sessions
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_lee)
#session.add(max_wiseman)


# this is how you would update a single record
#programmer = session.query(Programmer).filter_by(id=7).first()
#programmer.famous_for = "Microsoft"
# first() acts as a iterator so we can loop through the results for the first record
"""
    important to be sure to add the .first() method at the end of our query.
If you don't add the .first() method, then you'll have to use a for-loop to iterate over
the query list, even though it'll only find a single record using that ID.
"""

# updating multiple records
"""
people = session.query(Programmer)
for person in people:
    if person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print("Gender not specified")
    session.commit()# commit must be part of the loop to update all records
"""

# delete a single record
"""
fname = input("Enter the first name of the programmer you want to delete: ")
lname = input("Enter the last name of the programmer you want to delete: ")
programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# defensive programming
if programmer is not None:
    print("Programmer found: ", programmer.first_name + " " + programmer.last_name)
    confirmation = input("Are you sure you want to delete this record? (y/n): ")
    if confirmation.lower() == "y":
        session.delete(programmer)
        session.commit()
        print("Programmer deleted")
    else:
        print("Programmer not deleted")
else:
    print("Programmer not found")
"""

# commit our session to the database
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