from sqlalchemy import (
    create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Float
)

#executing the intrustions from our localhost "chinook" db,
#/// means that the db is local on the machine
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

#create a variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

#making the connections
with db.connect() as connection: