# importing pandas to work with dataframes and perform data manipulation tasks (extracting basically).
import pandas as pd

# extract data function
def extract(file_name):
    # This function will extract data from the data file and return it as a pandas dataframe.
    # adding a try-except block for error handingling and seeing if the dataframe is empty after reading the data file.
    try:
        df = pd.read_csv(f"../data/{file_name}")
        if df.empty:
            raise ValueError(f'Dataframe is empty after reading {file_name}')
        print("Data extracted successfully:")
        return df
    except Exception as error:
        print(f"Error extracting data: {error}")
        return pd.DataFrame()