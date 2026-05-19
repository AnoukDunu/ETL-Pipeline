import sys

import psycopg2
# from config import config
# creating the function to connect to the PostgreSQL database
def connect(config):
    connection = None
    # using a try-except block to handle any exceptions that may occur during the connection process
    try:
            params = config
            print("Connecting to the PostgreSQL database...")

            # The **params unpacks the dictionary returned by the config function and passes it as keyword arguments to the connect function of psycopg2.
            connection = psycopg2.connect(**params)

            # Creating a cursor object to interact with the database
            cursor = connection.cursor()
            print("PostgreSQL Version:")
            cursor.execute("SELECT version()") 
            # fetchone() retrieves the next row of a query result set, returning a single sequence, or None when no more data is available.
            db_version = cursor.fetchone()
            print(db_version)
            # need to close the cursor after use (very important to avoid memory leaks)
            cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        # if error occurs during the connection process, we print the error message and exit the program with a non-zero status code to indicate that an error occurred.
        sys.exit(1)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")