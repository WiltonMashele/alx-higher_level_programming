-- a script that removes all records with a score <= 5 in the table second_table
UPDATE `second_table`
SET `score` = 10
WHERE `name` = "Bob";
