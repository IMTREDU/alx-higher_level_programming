-- This SQL statement creates a table named `first_table` with columns `id` (integer) and `name` (varchar) in my MySQL server, if it doesn't already exist.
CREATE TABLE IF NOT EXISTS `first_table` (
  `id` INT,
  `name` VARCHAR(256)
);
