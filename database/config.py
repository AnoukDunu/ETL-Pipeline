# This file will parse the data inside database.ini and return the connection parameters as a dictionary.
from configparser import ConfigParser

# Define a function to read from the database.ini file
def config(filename='database.ini', section='postgresql'):
    # creating the parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
    # creating a dictionary to store all the data read from the database.ini file
    db = {}
    # verification step to check if the section exists in the database.ini file
    if parser.has_section(section):
        params = parser.items(section)
        # creating a for loop to iterate through the items in the section and add them to the dictionary
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f"Section '{section}' not found in the '{filename}' file.")
    # return db

    # show what's in the db dictionary
    print(db)


config()