-- This SQL statement creates a table named unique_id with a default value of 1 for the id column and ensures that the id column values are unique in your MySQL server, if the table doesn't already exist.
CREATE TABLE IF NOT EXISTS unique_id (
  id INT DEFAULT 1 UNIQUE,
  name VARCHAR(256)
);
