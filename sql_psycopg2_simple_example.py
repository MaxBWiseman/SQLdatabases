import psycopg2

# Connect to "chinook" database
connection = psycopg2.connect(
    dbname="chinook",
    user="max",  # replace with your actual database user
    password="coco100",  # replace with your actual database password
    host="localhost",  # assuming the database is running locally
    port="5432"  # default PostgreSQL port
)


# Open a cursor to perform database operations
cursor = connection.cursor()

# Query 1: Select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')
# Notice the use of quotations, this is important when using psycopg2
# compared to native SQL

# Fetch all results
results = cursor.fetchall()

# Fetch result (single)
# results = cursor.fetchone()

# Close connection
connection.close()

# Print results
for result in results:
    print(result)