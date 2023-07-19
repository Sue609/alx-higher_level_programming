-- script that lists all the tables of a database in your MySQL server.

USE information_schema;

SELECT table_name
FROM tables
WHERE table_schema = 'hbtn_0c_0';
