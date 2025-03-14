from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql://max:coco100@localhost/chinook")
# Notice the use of the username and password, aswell as the localhost and the database name
# The format is "postgresql://username:password@localhost/databasename"

# After our engine is created, and connected to our database, we need to use the MetaData
# class, which we can save to a variable name of 'meta'.
# The MetaData class will contain a collection of our table objects, and the associated data
# within those objects.
# Essentially, it's recursive data about data, meaning the data about our tables, and the
# data about the data in those tables
meta = MetaData()

# Before we start to query the database, we need to construct our tables, so that Python
# knows the schema that we're working with.
# Sometimes you'll hear this referred to as data models.

# To help find what the column names are for the tables, we can query in the postgres CLI this "SELECT * FROM "Artist" WHERE false",
# simply returning false, which intentionally gives us zero results, showing only the column names.

# Our first table class, or model, will be for the Artist table, which I'll assign to the variable of 'artist_table'.
# Using the Table import, we need to specify the name of our table, and provide the meta schema.
# As you can see, from the Artist table by querying false in the CLI described above,
# we have two columns; "ArtistId", which you might recall as being our primary key, and "Name".

# Back within our file, the format when defining columns, is the column name, followed by the
# type of data presented, and then any other optional fields after that.
# In our case, we have a column for "ArtistId", which is an Integer, and for this one, we
# can specify that primary_key is set to True.
# The next column is for "Name", and this is simply just a String, with no other values necessary.
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# In order to perform all six original queries that we've been using so far, we also need
# to create variables for the Album and Track tables.
# album_table = Table, and the name of the actual table from our database is "Album".
# Using quickly the false CLI method explained above for that table, in order to view the column headers, which
# are AlbumId, Title, and ArtistId.

# AlbumId is an Integer, and is, of course, our primary key.
# Title is just a String.
# Then, we have ArtistId as an Integer, but this time, since this is the Album table,
# it will not act as our primary key, but instead, as a Foreign Key.
# With the ForeignKey, we need to tell it which table and key to point to, so in this case,
# it's artist_table.ArtistId, using the table defined above.
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("Artist.ArtistId"))
)

# Our final table is the Track table,
# so lets quickly return false with a CLI query to the "Track" table to view those column headers in the terminal.
# ( SELECT * FROM "Track" WHERE false; )
# As you can see, we have multiple columns.
# This table will be track_table as our variable, using "Track" for the table name.
# TrackId, an Integer, which is our primary key.
# Name, which is a String.
# AlbumId, an Integer, which is our ForeignKey pointing to the album_table.AlbumId from above.
# MediaTypeId, an Integer, which is technically a foreign key as well, but for these lessons,
# we aren't defining all tables, just those that we need, so we can simply set primary_key to False.
# GenreId, an Integer, and again, technically it's a foreign key, but we'll just set it
# to False as the primary key.
# Composer, which is a String.
# Milliseconds, an Integer.
# Bytes, another Integer.
# And finally, UnitPrice, which is a Float, since it uses decimal values for the price.
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("Album.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# create all tables
meta.create_all(bind=db)

# Now, we need to actually connect to the database, using the .connect() method, and the Python with-statement.
# This saves our connection to the database into a variable called 'connection'.

# making the connection
with db.connect() as connection:
    
    # NOTE: How the variables artist_table, album_table, and track_table are used to perform the queries.
    # This is because we have already above defined the tables, and their columns, and we can use them to
    # perform the queries by just referencing the variable name associated with the created table.

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

# Although the initial setup might've taken a bit longer, by defining each table, you
# can see that the execution of the query is actually quite simple.