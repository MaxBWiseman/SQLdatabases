from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String, select
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connect to the local database
db = create_engine("postgresql:///chinook")
base = declarative_base() #this is the base class for all our models

# create a class-based model for the Artist table
class Artist(base):
    __tablename__ = "Artist"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)
    
# create a class-based model for the Album table
class Album(base):
    __tablename__ = "Album"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))
    
# create a class-based model for the Track table
class Track(base):
    __tablename__ = "Track"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Float)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the database)
Session = sessionmaker(db)
# opens an actual session by calling the Session() class defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# query 1 - select all records from the Artist table
#artists = session.query(Artist)
#for artist in artists:
    #print(artist.ArtistId, artist.Name, sep=" | ")
    
# query 2 - select only the Name column from the Artist table
#artists = session.query(Artist)
#for artist in artists:
    #print(artist.Name)
    
# query 3 - select only Queen, the artist with ArtistId = 275
#artist = session.query(Artist).filter_by(ArtistId=51).first()# deprecated but easier to read
#print(artist.ArtistId, artist.Name, sep=" | ")

# query 4 - select only Queen
#artist = session.query(Artist).filter_by(Name="Queen").first()
#print(artist.ArtistId, artist.Name, sep=" | ")

# query 5 - query Album with ArtistId
artist = session.query(Album).filter_by(ArtistId=51).first()
print(artist.AlbumId, artist.Title, artist.ArtistId, sep=" | ")
