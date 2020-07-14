-- creates a table called first_table in the current database of a MySQL server
-- script does not fail if the database already exists
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));

