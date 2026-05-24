# This file will be written entirely by me.
import sys
import psycopg2

from database.config import config

def load (df, table_name):
    # condition to check if the dataframe is empty or not. If it is empty, we print a message and exit the program with a non-zero status code to indicate that an error occurred.
    if df is None or df.empty:
        print("No data to load.")
        sys.exit(1)

    # initialising the database connection to start the loading process.
    connection = None
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

        for _, row in df.iterrows():
            # adding error handling for duplicate rows so that everytime the ETL is run, only inserts the new rows that are not already in the database and skips the duplicate rows to avoid any errors or issues with the loading process.
            try:
                # creating an insert query to insert the data into the database. The %s placeholders will be replaced with the actual values from the dataframe.
                insert_query = f"INSERT INTO {table_name} (customer_id, firstname, lastname, phone_number, email, location, company, joined_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                # executing the insert query with the values from the dataframe. The row['column_name'] syntax is used to access the values from the dataframe for each column.
                cursor.execute(insert_query, (row['customer_id'], row['first_name'], row['last_name'], row['phone_1'], row['email'], row['location'], row['company'], row['subscription_date']))
            except psycopg2.errors.UniqueViolation:
                # Ignore duplicate rows
                connection.rollback()
            else:
                 # committing the transaction to save the changes to the database.
                connection.commit()
                print("Data committed to database successfully.")
       

        # temp success message to confirm the behaviours of variables passed.
        print(f"Successfully loaded {len(df)} rows of data into {table_name} table...")
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
