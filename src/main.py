# This is the main file.
from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load


# use the below 'file_name' variable insert the file name and path to this variable to extract the data from.
file_name = 'customers_data.csv'
# enter the table/schema.table name that you want to load the data into in the 'table_name' variable below.
table_name = 'testbank.customers'
# Did trial and error to see which schema table the data will load into by default. The intended schema is the testbank schema.

# creating the main function to run the ETL pipeline
def run_pipeline():
    # NEED TO ADD ERROR HANDLING TO THIS FUNCTION TO HANDLE ANY EXCEPTIONS THAT MAY OCCUR DURING THE ETL PROCESS.
   
    # extracting the data from the data file using the extract function and passing the file name as an argument to it to get the data as a pandas dataframe.
    extracted_df = extract(file_name)
    # transforming the data using the transform function and passing the extracted dataframe as an argument to it to get the transformed dataframe.
    transformed_df = transform(extracted_df)
    print(transformed_df)
    # loading the transformed data into the database using the load function and passing the transformed dataframe as an argument to it to get the loaded dataframe.
    loaded_df = load(transformed_df, table_name)
    
    
    return loaded_df

# This is the entry point of the script. When the script is run, it will execute the run_pipeline function.
if __name__ == "__main__":
    run_pipeline()
