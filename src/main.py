# This is the main file.
from scripts.extract import extract
from scripts.transform import transform
# from scripts.load import load
from database.connect import connect

from database.config import config
# use the below 'file_name' variable insert the file name and path to this variable to extract the data from.
file_name = 'data.csv'

# creating the main function to run the ETL pipeline
def run_pipeline():
    # NEED TO ADD ERROR HANDLING TO THIS FUNCTION TO HANDLE ANY EXCEPTIONS THAT MAY OCCUR DURING THE ETL PROCESS.
    # connect to the database using the connect function and passing the config function as an argument to it to get the connection parameters from the database.ini file.
    connect(config)
    # extracting the data from the data file using the extract function and passing the file name as an argument to it to get the data as a pandas dataframe.
    extracted_df = extract(file_name)
    # transforming the data using the transform function and passing the extracted dataframe as an argument to it to get the transformed dataframe.
    transformed_df = transform(extracted_df)
    print(transformed_df)
    # function not implemented yet. Just a placeholder for now. 
    # loaded_df = load(transformed_df)
    

# This is the entry point of the script. When the script is run, it will execute the run_pipeline function.
if __name__ == "__main__":
    run_pipeline()
