# This is the main file.
# This will connect the PostgreSQL database and run the application.

import psycopg2  # type: ignore[import]
import database.config as config

# creating the function to connect to the PostgreSQL database
def connect():
    connection = None
    # using a try-except block to handle any exceptions that may occur during the connection process
    try:
            params = config()
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
    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    connect()