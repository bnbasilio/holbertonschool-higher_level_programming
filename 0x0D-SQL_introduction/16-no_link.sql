-- lists all records of the table second_table of the database hbtn_0c_0
-- rows without names will not be displayed
-- displays the score and the name (ordered by score)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
