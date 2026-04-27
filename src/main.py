# This is the main file.
# This will connect the PostgreSQL database and run the application.

import psycopg2
import database.config as config

# creating the function to connect to the PostgreSQL database
def connect():
    connection = None
    params = config()
    print("Connecting to the PostgreSQL database...")

    # The **params unpacks the dictionary returned by the config function and passes it as keyword arguments to the connect function of psycopg2.
    connection = psycopg2.connect(**params)

    # Creating a cursor object to interact with the database
    cursor = connection.cursor()
    print("PostgreSQL Version:")
    cursor.execute("SELECT version()")
