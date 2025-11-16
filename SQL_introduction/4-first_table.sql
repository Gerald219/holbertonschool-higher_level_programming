-- task 4: create first_table with id and name columns
CREATE TABLE IF NOT EXISTS first_table (  -- create the table only if it does not already exist
    id INT,                               -- id column stores whole number ids
    name VARCHAR(256)                     -- name column stores text up to 256 characters
);
