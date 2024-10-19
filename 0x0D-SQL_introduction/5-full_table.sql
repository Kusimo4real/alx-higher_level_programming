-- a script that prints the full description of the table first_table from the database hbtn_0c_0
SELECT table_name, table_schema
FROM information_schema.tables
WHERE table_name = 'first_table'
AND table_schema = DATABASE();
