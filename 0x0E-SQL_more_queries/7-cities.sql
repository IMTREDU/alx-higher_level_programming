-- This SQL script creates a database named hbtn_0d_usa and a table named cities within that database on your MySQL server, if they don't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- This SQL script switches to the hbtn_0d_usa database for subsequent operations.
USE hbtn_0d_usa;

-- This SQL script creates a table named cities with columns id (integer, unique, auto-increment, not null), state_id (integer, not null), and name (varchar, not null) in the hbtn_0d_usa database.
CREATE TABLE IF NOT EXISTS cities (
  id INT UNIQUE AUTO_INCREMENT NOT NULL,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  PRIMARY KEY(id),
  FOREIGN KEY(state_id) REFERENCES states(id)
);
