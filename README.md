### PostgreSQL database setup

If the database you wish to connect to is already active, then skip to the point in the intructions that states so.

- Use the command `wget` in the terminal with an argument of a URL or GitHub URL that links to a database you wish to play with. In this case, the Chinook database.
- To download the postgresSQL server locally for practice use 
    ```bash
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    sudo service postgresql start
    sudo service postgresql status
    ```
- Next you need to create a user with a password and set the user privileges, use the following
    ```bash
    sudo su - postgres
    psql
    CREATE USER max WITH PASSWORD 'coco100';
    ALTER USER max WITH SUPERUSER;
    ```
- To leave a postgres user session, use `exit` in the terminal
  - To return to the CLI use (leave the -d part out if have not yet created the chinook database with the instructions below, or just dont want to opne the chinook database on startup)
  ```bash
  psql -U max -d chinook
  ```
  - NOTE: sometimes when using postgeSQL locally, the authentication method will be peer, this will need changing to md5 else you will only be able to access the database as the "postgres" user with 
  ```bash
  sudo su - postgres
  psql
  ```
  - To change this use `sudo nano /etc/postgresql/12/main/pg_hba.conf` In the terminal and modify this line from 
  ```bash
  local   all             all                                     peer
  ```
  to
  ```bash
  local   all             all                                     md5
  ```
  - And then save and exit with `Ctrl+X`, then `Y` and `Enter`.
  - Be sure to retart the postgres service to apply the changes with `sudo service postgresql restart`
  This will make the local practice experience feel like a more real scenairo. Logging in as the "postgres" user is fine for local practice, although is less common in the workplace.

- Next we need to populate the postgresSQL server with the .sql files data that was downloaded earlier.
  - Inside the postgres CLI type `\l` to list the current databases installed in the servers enviroment. By default the postgres CLI comes with 3 databases out of the box "postgres", "template0" and "template". Instead of using these lets create a new database with the data from the downloaded .sql file.
  - Use `CREATE DATABASE chinook;` in the CLI and then use `\l` again to view the new database.
  - To connect to a listed database we use `\c` followed by the database you wish to connect to, for example `\c chinook`
  - Now to install the databases data from the downloaded .sql file with `\i`, which stands for install, initialize or include. For example `\i Chinook_PostgreSQL.sql`
  - Finally use `\q` , which stands for quit, to leave the postgres CLI

- START HERE IF DATABASE IS ALREADY ACTIVE

- The next steps are different depending on whether you are carrying on using PostgreSQL through the terminal or using the psycopg2 adapter that allows queries and such written in Python instead. In a professional work enviroment a user and password should be given to you, if not then create one and be sure to delete the user after for data protection Here are both options:


### For normal PostgreSQL
  - Start the PostgreSQL CLI with `psql` in the terminal and use `-d` to connect directly to a databases that is already included within the postgres server:

    ```bash
    psql -d chinook
    ```
    - Here I will include some basic postgres CLI commands
      - `\dt` will display all the tables in the database
      - Looking at the table choices I have decided to select all the data from the "Artist" table, with `SELECT * FROM "Artist";`
      - To quickly return from a long query use `q`
      - Lets add to the last query and pull a specific artist name with `SELECT * FROM "Artist" WHERE "Name" = 'Queen';`
      - As you may have noticed, I've used double-quotes again, except when it comes to the specific value I'd like to search for, which must be in single-quotes. This is to distinguish between the various table and column names, versus the specific context or value I need to find.
      - Notice this result provides us with the ArtistId primary key, this is the main identifier for this data entry, we could use this ArtistId to provide us with the same output at the last query with `SELECT * FROM "Artist" WHERE "ArtistId" = 51;`
      - We can further use this primary key to find more results relating to this specific key (51) in different tables with `SELECT * FROM "Album" WHERE "ArtistId" = 51;`. This obviously provides a list of the artist Queen's albums.
      - Notice how the Primary Key for Queen is referenced in this table as a Foreign Key, demonstrating that these tables are related. The albums here have their own Primary Key of AlbumId aswell.
      - Lets now try looking in the Track table, from prior knowledge I know that I must use the column header of "Composer" to search for all the tracks by Queen, usually you would have had to gain this understanding from going through the database. `SELECT * FROM "Track" WHERE "Composer" = 'Queen';`
      - You can see that only 9 tracks are listed, all of which belong to the "Greatest Hits 2" album, as specified by the foreign key of 36 under AlbumId, that we saw from the last query. The other columns here contain additional data about those tracks, some of which have foreign keys related to different tables on our database. In a real-world scenario, you should probably consider making the Composer column actually be the ArtistId foreign key, to keep with the relational database schema.




    ### For the psycopg2 adapter version
    Run the below code to setup a basic postgreSQL query using the psycopg2 adapter for python. Look through the other included .py files in this repo for more examples of this method of querying SQL with python.

    ```python
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
    ```

### SQLAlchemy

Some of the best reasons to use SQLAlchemy include having cleaner code, the logic is
simple, and your code is more secure than using raw SQL commands.
In fact, the SQLAlchemy library comes with three different layers of abstraction, meaning
you can choose the level of support necessary for your applications.
The lowest layer of abstraction is to simply use SQLAlchemy's engine component in order
to execute raw SQL, nothing too complex or fancy.
The middle layer of abstraction uses SQLAlchemy's Expression Language to build SQL statements
in a more Pythonic way, instead of relying purely on those raw strings.
The highest layer of abstraction uses SQLAlchemy's full ORM capabilities, allowing us to make
use of Python classes and objects, instead of using database tables and connections.
With each level of abstraction, you, as a user, are moved further away from writing
raw SQL, and using more Python.