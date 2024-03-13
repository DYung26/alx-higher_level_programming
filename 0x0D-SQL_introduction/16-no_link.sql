-- Lists all records of the table `second_table` without listing rows with a NULL value in `name`.
SELECT score, name FROM second_table WHERE name IS
NOT NULL ORDER BY score DESC;
