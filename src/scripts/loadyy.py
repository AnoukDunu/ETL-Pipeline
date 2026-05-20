from database.config import config
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd

# This whole function was added by copilot to load the transformed data into the database and return the loaded dataframe.

def load(df, table='customers'):
    # """Load a transformed DataFrame into Postgres.

    # - Maps common dataframe columns to the target table columns.
    # - Uses `execute_values` for efficient bulk insert.
    # - Skips rows with no `email` (email is unique in the schema).
    # """
    if df is None or df.empty:
        print("No data to load.")
        return df

    params = config()
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cols = ['firstname', 'lastname', 'phone_number', 'email', 'location', 'company', 'joined_date']

        rows = []
        for _, r in df.iterrows():
            firstname = r.get('first_name') or r.get('firstname')
            lastname = r.get('last_name') or r.get('lastname')
            phone = r.get('phone_1') or r.get('phone_number')
            email = r.get('email')
            location = r.get('location')
            company = r.get('company')
            joined = r.get('subscription_date') or r.get('joined_date')

            # convert pandas NaN to None for psycopg2
            def clean(x):
                return None if (pd.isna(x) or x == '') else x

            row = (clean(firstname), clean(lastname), clean(phone), clean(email), clean(location), clean(company), clean(joined))
            # require at least an email or firstname/lastname to insert
            if row[3] is None and (row[0] is None and row[1] is None):
                continue
            rows.append(row)

        if not rows:
            print("No valid rows to insert.")
            return df

        insert_sql = f"INSERT INTO {table} ({', '.join(cols)}) VALUES %s ON CONFLICT (email) DO NOTHING"
        execute_values(cur, insert_sql, rows)
        conn.commit()
        cur.close()
        print(f"Inserted {len(rows)} rows into {table}.")
    except Exception as e:
        print(f"Error loading data: {e}")
        if conn is not None:
            conn.rollback()
        raise
    finally:
        if conn is not None:
            conn.close()

    return df

# This function will load the transformed data into the database and return the loaded dataframe.
