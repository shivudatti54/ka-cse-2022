### Revision Notes: Hive DDL Operations

#### BIG DATA ANALYTICS: Spark and Big Data Analytics: Spark, Introduction to Data Analysis with Spark.

# **Hive DDL Operations**

- **Create Database**
  - `CREATE DATABASE database_name;`
- **Alter Database**
  - `ALTER DATABASE database_name;`
- **Drop Database**
  - `DROP DATABASE database_name;`

## **Create Table**

- **Create Table**
  - `CREATE TABLE table_name (column1 data_type, column2 data_type, ...);`
- **Use Hive Query Language (HQL)**
  - `CREATE TABLE table_name LIKE original_table_name;`

## **Alter Table**

- **Alter Table**
  - `ALTER TABLE table_name ADD COLUMN column_name data_type;`
  - `ALTER TABLE table_name DROP COLUMN column_name;`
- **Modify Data Type**
  - `ALTER TABLE table_name MODIFY COLUMN column_name data_type;`

## **Drop Table**

- **Drop Table**
  - `DROP TABLE table_name;`
- **Delete Table**
  - `DROP TABLE table_name CASCADE;`

## **Create View**

- **Create View**
  - `CREATE VIEW view_name AS SELECT column1, column2 FROM table_name;`
- **View Definition**
  - `CREATE VIEW view_name AS SELECT * FROM table_name;`

## **Create Function**

- **Create Function**
  - `CREATE FUNCTION function_name return_type (argument1 argument_type, argument2 argument_type, ...) AS language;`
- **Function Definition**
  - `CREATE FUNCTION function_name (argument1 argument_type, argument2 argument_type, ...) RETURNS return_type AS language;`

## **Create Index**

- **Create Index**
  - `CREATE INDEX index_name ON table_name (column1, column2, ...);`
- **Index Definition**
  - `CREATE INDEX index_name ON table_name (column1, column2, ...);`

### Important Formulas and Definitions

- No specific formulas to note.
- Definitions:
  - Hive Query Language (HQL): A SQL-like language used for querying and managing data in Hive.
  - Data Type: A category of data types such as INT, STRING, DATE, etc.
  - Table: A collection of related data.
  - View: A virtual table based on the result of a query.
  - Function: A reusable block of code that performs a specific task.
  - Index: A data structure that improves the speed of data retrieval.

### Important Theorems

- No specific theorems to note.
