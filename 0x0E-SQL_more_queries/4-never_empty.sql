-- creates the table id_not_null on your MySQL server
-- script should not fail if table already exists
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1,
name VARCHAR(256));
