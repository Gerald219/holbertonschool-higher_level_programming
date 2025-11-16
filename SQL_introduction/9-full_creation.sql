-- create second_table and fill it with sample rows

USE hbtn_0c_0;  -- work inside this database

CREATE TABLE IF NOT EXISTS second_table (
    id INT,             -- id number for the row
    name VARCHAR(256),  -- person name text
    score INT           -- score value
);

INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
