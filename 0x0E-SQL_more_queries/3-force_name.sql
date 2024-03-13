-- This SQL statement creates a table named force_name with columns id (integer) and name (varchar) that cannot be NULL in your MySQL server .
CREATE TABLE IF NOT EXISTS force_name (
  id INT,
  name VARCHAR(256) NOT NULL
);
