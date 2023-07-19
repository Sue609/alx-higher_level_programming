SQL is a programming language used for managing and manipulating relational databases. It provides standerdized way to interact with databases, alloweing users to perform various operations, such as creating, modifying and querying data stored in databse.
The key features of SQL include:
1. Data Defination Language.
2. Data Manipulation Language.
3. Data Query Language.
4. Data Control Language.

SQL is used by various database management systems (DBMS) like MySQL, PostgreSQL, Oracle, SQL Server, and many others. Each DBMS may have slight variations in SQL syntax and additional features, but the core SQL commands are standardized by ANSI (American National Standards Institute).

- In this project we shall be looking at how to:
1. Create a new user.
2. Granting a user permissions.
3. Types of SQL joins:
	- INNER JOIN
	- FULL [OUTER] JOIN
	- FULL [OUTER] JOIN without the intersection
	- LEFT [OUTER] JOIN
	- LEFT [OUTER] JOIN without the intersection
	- RIGHT [OUTER] JOIN
	- RIGHT [OUTER] JOIN without the intersection
	- NATURAL JOIN
	- OUTER JOIN
	- CROSS JOIN

In this project we shall be looking and trying to answer the following questions:
0. Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

1. Write a script that creates the MySQL server user user_0d_1.
- user_0d_1 should have all privileges on your MySQL server
- The user_0d_1 password should be set to user_0d_1_pwd
- If the user user_0d_1 already exists, your script should not fail

2. Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
- The user_0d_2 password should be set to user_0d_2_pwd
- If the database hbtn_0d_2 already exists, your script should not fail
- If the user user_0d_2 already exists, your script should not fail

3. Write a script that creates the table force_name on your MySQL server.
- force_name description:
	- id INT
	- name VARCHAR(256) can’t be null
- The database name will be passed as an argument of the mysql command
- If the table force_name already exists, your script should not fail

4. Write a script that creates the table id_not_null on your MySQL server.
- id_not_null description:
	- id INT with the default value 1
	- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table id_not_null already exists, your script should not fail

5. Write a script that creates the table unique_id on your MySQL server.
- unique_id description:
	- id INT with the default value 1 and must be unique
	- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table unique_id already exists, your script should not fail
