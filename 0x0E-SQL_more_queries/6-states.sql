-- This SQL script creates a database named hbtn_0d_usa and a table named states within that database on your MySQL server, if they don't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This SQL script switches to the hbtn_0d_usa database for subsequent operations.
USE hbtn_0d_usa;

-- This SQL script creates a table named states with columns id (integer, unique, auto-increment, not null) and name (varchar, not null), with id as the primary key in the hbtn_0d_usa database.
CREATE TABLE IF NOT EXISTS states (
  id INT UNIQUE NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY(id)
);
