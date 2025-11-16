-- create table id_not_null with id default 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,           -- id number, uses 1 when no value is given
    name VARCHAR(256)           -- name text
);
