from database.connect import connect
from database.config import config

def load(df):

    connect(config)
    print("Loading data into the database...")

    return df
    # This function will load the transformed data into the database and return the loaded dataframe.
