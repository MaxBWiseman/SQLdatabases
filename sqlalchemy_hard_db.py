from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#To use this method use this -
# Install the "SQLAlchemy" Python package
# `pip3 install SQLAlchemy`
# Create a new file called "sql-expression.py"
# `touch sql-expression.py`

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData()

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True), #Primary keys are unique identifiers
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))#Foreign keys are references to primary keys in other tables
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),#Foreign keys are references to primary keys in other tables
    Column("MediaTypeId", Integer, primary_key=False),#Not defined as primary key for this lesson
    Column("GenreId", Integer, primary_key=False),#Not defined as primary key for this lesson
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# create all tables
meta.create_all(bind=db)

# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)