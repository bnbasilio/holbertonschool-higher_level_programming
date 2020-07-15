-- creates the table force_name on your MySQL server
-- script should not fail if table already exists
CREATE TABLE IF NOT EXISTS force_name(id INT,
name VARCHAR(256) NOT NULL);
