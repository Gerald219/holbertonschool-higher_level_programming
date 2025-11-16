-- create table force_name with id and a name that cannot be empty
CREATE TABLE IF NOT EXISTS force_name (
    id INT,                       -- simple id number
    name VARCHAR(256) NOT NULL    -- name text, cannot be null
);
