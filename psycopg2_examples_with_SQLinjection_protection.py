import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(
    dbname="chinook",
    user="max",  # replace with your actual database user
    password="coco100",  # replace with your actual database password
    host="localhost",  # assuming the database is running locally
    port="5432"  # default PostgreSQL port
)

# build a cursor object of the database
cursor = connection.cursor()

# NOTE: Using %s is better for SQL injection security
# https://realpython.com/prevent-python-sql-injection/#using-psycopg2

# Query 1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)
