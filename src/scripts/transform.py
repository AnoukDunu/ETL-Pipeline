import pandas as pd

#transform data function
def transform(df):
    # This function will transform the data and return the transformed dataframe.
    # adding a try-except block for error handling and seeing if the dataframe is empty after transforming the data.
    try:
        # removing any leading or trailing whitespace from the column names to ensure that the column names are clean and consistent.
        df.columns = [col.strip() for col in df.columns]
        # Example transformation: converting all column names to lowercase
        df.columns = [col.lower() for col in df.columns]
        # removing the spaces between words in the column names to standardize the column names and make them easier to work with.
        df.columns = [col.replace(' ', '_') for col in df.columns]
        
        # combining city and country columns into a new column called location to create a new column that combines the city and country information for easier analysis.
        if 'city' in df.columns and 'country' in df.columns:
            df['location'] = df['city'] + ', ' + df['country']
            # tells panda to look at columns (axis=1) and drop the city and country columns after creating the location column to clean up the dataframe and remove redundant information.
            df = df.drop(['city', 'country'], axis=1)

        df = df.drop(['subscription_date', 'website'], axis=1)

        df = df.drop (['phone_2'], axis=1)
        # checking if the dataframe is empty after transforming the data and raising an error if it is to ensure that we have valid data to work with after the transformation process.
        if df.empty:
            raise ValueError('Dataframe is empty after transformation')
        print("Data transformed successfully:")
        return df
    except Exception as error:
        print(f"Error transforming data: {error}")
        return pd.DataFrame()
    
    
    

# LOOK UP HOW TO DO DATA CLEANING, FILTERING AND FORMATTING PROPERLY. ADD RELEVANT CODE AND IMPLEMENT IN THE FUTURE