-- lists the number of records with the same score in the table second_table
-- displays score and number of records (sorted by number of records)
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
