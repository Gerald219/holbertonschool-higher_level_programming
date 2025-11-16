-- create database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- work inside this database
USE hbtn_0d_usa;

-- create states table with auto id and non empty name
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,  -- auto id for each state
    name VARCHAR(256) NOT NULL                   -- name must always be given
);
