import psycopg2

#To setup this method use this -
# Install the "psycopg2" Python package
# `pip3 install psycopg2`

# Create a new file: "sql-psycopg2.py"
# `touch sql-psycopg2.py`

#connect to chinook database
connection = psycopg2.connect(database="chinook")

#build a cursor object of the database
cursor = connection.cursor()

#execute a query that selects all records from the Artist table
cursor.execute('SELECT * FROM "Artist"')

#select only the "Name" column from the Artist table
cursor.execute('SELECT "Name" FROM "Artist"')

#select only "Queen" from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = \'Queen\'')

#select only "ArtistId" #51 from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 51')

#select only the albums with "ArtistId" #51 from the "Album" table
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 51')

#select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = \'Queen\'')
#two ways to do this, this way is better for SQL injection security
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ('Queen',))

#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = 88')

cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = 88')

#fetch the results (multiple)
results = cursor.fetchall()

#fetch the results (single)
#results = cursor.fetchone()

#close the connections
connection.close()

#print results
for result in results:
    print(result)
