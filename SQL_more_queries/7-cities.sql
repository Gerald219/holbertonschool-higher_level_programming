-- create database hbtn_0d_usa and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- work inside this database
USE hbtn_0d_usa;

-- create cities table linked to states table
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- city id number that grows 1 by 1
    state_id INT NOT NULL,                       -- link to a state id
    name VARCHAR(256) NOT NULL,                  -- city name, cannot be empty
    FOREIGN KEY (state_id) REFERENCES states(id) -- state_id must match an id in states
);
