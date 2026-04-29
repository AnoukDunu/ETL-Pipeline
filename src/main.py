# This is the main file.
# This will connect the PostgreSQL database and run the application.
from fileinput import filename

import psycopg2
from config import config
# importing pandas to work with dataframes and perform data manipulation tasks (extracting basically).
import pandas as pd

# use the below 'file_path' variable insert the file name and path to this variable to extract the data from.
file_path = '../data/test.csv'

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


def extract_data(file_path):
    # This function will extract data from the data file and return it as a pandas dataframe.
    # adding a try-except block for error handingling and seeing if the dataframe is empty after reading the data file.
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            raise ValueError(f'Dataframe is empty after reading {file_path}')
        print("Data extracted successfully:")
        return df
    except Exception as error:
        print(f"Error extracting data: {error}")
        return pd.DataFrame()



if __name__ == "__main__":
    connect()

    extract_data(file_path)

