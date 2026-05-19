CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(100) UNIQUE,
    location VARCHAR(100),
    company VARCHAR(100),
    joined_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- entered the table creation SQL in here as reference. This table will be used to store the transformed data after it has been loaded into the database. The table includes columns for customer information such as their name, contact details, location, company, and the date they joined. The created_at column will automatically store the timestamp of when each record is inserted into the table.
-- the database table will be created using the psql terminal seperately.
-- later on, I will look into creating the table using SQLAlchemy in the load.py script to automate the process of creating the table if it does not already exist. After getting the basics of course.