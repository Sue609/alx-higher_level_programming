OBJECT RELATIONAL MAPPERS(ORM)
- This is a code libraray that automates transfer of data stored in relational database used in application code. It provides a high level abstraction upon relational database that allow a developer to write python code instead of SQL to create, update, and delete data and schemas in their database. It allows high speed for not having to switch back and forth between languages, its typically easier to do using a single programming language. It is easy to switch between application between various relational database. In this project we shall be dealing with MySQLdb AND MySQLalchemy.

- In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.
