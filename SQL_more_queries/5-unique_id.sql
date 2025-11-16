-- create table unique_id with id default 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,   -- id number, uses 1 when missing and must be unique
    name VARCHAR(256)          -- name text
);
