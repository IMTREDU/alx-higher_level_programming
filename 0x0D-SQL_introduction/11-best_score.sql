-- This SQL query lists all records from the table named `second_table` where the score is greater than or equal to 10, and it orders them by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
