-- This SQL script creates a database named hbtn_0d_2 and a MySQL server user named user_0d_2 with a password 'user_0d_2_pwd'.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- This SQL script grants SELECT privileges on the hbtn_0d_2 database to the user user_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
