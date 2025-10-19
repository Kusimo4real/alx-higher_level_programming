-- a script that prints the full description of the table first_table
-- from the database hbtn_0c_0 in your mysql server
SELECT COLUMN_NAME, DATA_TYPE
FROM information_schema.columns
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
