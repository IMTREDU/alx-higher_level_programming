-- This SQL query lists all records from the table named `second_table` where the name value is not empty in my MySQL server.
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
