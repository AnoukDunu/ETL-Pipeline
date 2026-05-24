-- # This file will contain the table creation code for the database. Here you can customize the table structure and the data types of the columns as per your requirements. You can also add any constraints or indexes to the table if needed.

-- # Apparently this database/table creation code needs to be included and can run in the load.py file/function itself.
-- # Not to future self to maybe implement this if it makes sense

-- # Maybe refer to this article for more information (https://medium.com/@anandparayan/building-a-production-ready-etl-pipeline-my-complete-data-engineering-journey-with-python-41fb849471a9)
-- # and maybe this youtube video (https://www.youtube.com/watch?v=G0crKzK9Ayk)


CREATE TABLE testbank.customers (
    c_index SERIAL,
    customer_id VARCHAR(100) PRIMARY KEY,
    firstname VARCHAR(100) NOT NULL,
    lastname VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    location VARCHAR(100),
    company VARCHAR(100),
    joined_date DATE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- testbank is the name of the database schema
-- the table is not visible with the regular \dt command because its inside the testbank schema and it normally shows the public scehmas only.
-- Therefore, to see the table, you can use the command \dt testbank.* in the psql terminal to list all tables within the testbank schema. This will allow you to verify that the customers table has been created successfully and is available for use in your ETL pipeline.


-- entered the table creation SQL in here as reference. This table will be used to store the transformed data after it has been loaded into the database. The table includes columns for customer information such as their name, contact details, location, company, and the date they joined. The created_at column will automatically store the timestamp of when each record is inserted into the table.
-- the database table will be created using the psql terminal seperately.
-- later on, I will look into creating the table using SQLAlchemy in the load.py script to automate the process of creating the table if it does not already exist. After getting the basics of course.

-- Below constraint is added to ensure that there are no duplicate entries
ALTER TABLE testbank.customers
ADD CONSTRAINT unique_customer UNIQUE (customer_id);