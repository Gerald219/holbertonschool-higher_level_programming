-- create database hbtn_0d_2 if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user user_0d_2 with password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- give user_0d_2 permission to only read (select) from this database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- apply changes
FLUSH PRIVILEGES;
