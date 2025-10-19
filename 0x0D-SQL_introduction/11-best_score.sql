-- a sript that lists all records with a score >= 10 in the table econd_table o the database hbtn+0c_0

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
