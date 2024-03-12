-- Creates a table `second_table`.
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
-- Inserting rows into `second_table`
-- Inserting rows for John
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
-- Inserting rows for Alex
INSERT INTO second_table (id, name, score) VALUES (2, "Alex", 3);
-- Inserting rows for Bob
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 14);
-- Inserting rows for George
INSERT INTO second_table (id, name, score) VALUES (4, "George", 8);
