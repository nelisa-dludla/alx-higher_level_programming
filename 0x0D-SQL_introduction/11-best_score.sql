-- Lists all the records with a score >= 10 in the table second_table, from highest to lowest.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
