-- This SQL script creates a MySQL server user named user_0d_1 with a password 'user_0d_1_pwd' and grants all privileges to that user.
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
