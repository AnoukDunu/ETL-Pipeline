import pandas as pd

#transform data function
def transform(df):
    # This function will transform the data and return the transformed dataframe.
    # adding a try-except block for error handling and seeing if the dataframe is empty after transforming the data.
    try:
        # Example transformation: converting all column names to lowercase
        df.columns = [col.lower() for col in df.columns]
        if df.empty:
            raise ValueError('Dataframe is empty after transformation')
        print("Data transformed successfully:")
        return df
    except Exception as error:
        print(f"Error transforming data: {error}")
        return pd.DataFrame()
    

# LOOK UP HOW TO DO DATA CLEANING, FILTERING AND FORMATTING PROPERLY. ADD RELEVANT CODE AND IMPLEMENT IN THE FUTURE