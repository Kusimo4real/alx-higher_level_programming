-- a script that lists the number o records with the same score in the table seconf_table of the database hbtn_0c_0
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
