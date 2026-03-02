# 7 Use Hive to create, alter, and drop databases, tables, views, functions, and indexes

## Introduction

Hive is a data warehousing and SQL-like query language for Hadoop. It allows users to create, modify, and drop various database objects such as databases, tables, views, functions, and indexes.

### Key Points

- **Creating Databases and Tables**
  - Create database: `CREATE DATABASE db_name;`
  - Create table: `CREATE TABLE table_name (column1 data_type, column2 data_type);`
- **Altering Databases and Tables**
  - Alter database: `ALTER DATABASE db_name;`
  - Alter table: `ALTER TABLE table_name ADD COLUMN column_name data_type;`
  - Drop table: `DROP TABLE table_name;`
- **Creating Views**
  - Create view: `CREATE VIEW view_name AS SELECT column1, column2 FROM table_name;`
- **Creating Functions**
  - Create function: `CREATE FUNCTION func_name(data_type) RETURNS data_type AS 'function_body';`
- **Creating Indexes**
  - Create index: `CREATE INDEX index_name ON table_name (column1, column2);`
- **Dropping Databases and Tables**
  - Drop database: `DROP DATABASE db_name;`
  - Drop table: `DROP TABLE table_name;`

### Important Formulas and Definitions

- **Hive Query Language (HQL)**: a SQL-like language used to interact with Hive databases.
- **Hive Data Types**: used to define the data type of each column in a Hive table.
- **Partitioning**: a technique used to improve query performance by dividing large tables into smaller, more manageable pieces.

### Theorems and Concepts

- **Data Warehousing**: a process of collecting, storing, and analyzing data from various sources to support business intelligence and decision-making.
- **Big Data Analytics**: the process of analyzing large datasets to gain insights and make informed decisions.

### Quick Revision Tips

- Understand the basics of Hive and HQL.
- Practice creating and altering databases, tables, views, functions, and indexes.
- Familiarize yourself with Hive data types and partitioning concepts.
