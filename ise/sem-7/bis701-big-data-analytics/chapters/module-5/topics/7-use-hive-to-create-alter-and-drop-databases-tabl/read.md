# **7 Use Hive to Create, Alter, and Drop Databases, Tables, Views, Functions, and Indexes**

## **Introduction**

Hive is a data warehousing and SQL-like query language for Hadoop, a popular big data processing engine. In this topic, we will explore the different use cases of Hive to create, alter, and drop databases, tables, views, functions, and indexes.

## **Creating Databases**

In Hive, a database is a container that holds one or more tables. To create a database, you can use the `CREATE DATABASE` statement.

### Example

```sql
CREATE DATABASE mydatabase;
```

This will create a new database named `mydatabase`.

## **Creating Tables**

A table is a collection of data that is stored in a Hive database. To create a table, you can use the `CREATE TABLE` statement.

### Example

```sql
CREATE TABLE mytable (
  id INT,
  name STRING,
  age INT
);
```

This will create a new table named `mytable` with three columns: `id`, `name`, and `age`.

## **Altering Tables**

You can alter a table by adding, modifying, or removing columns. To alter a table, you can use the `ALTER TABLE` statement.

### Example

```sql
ALTER TABLE mytable
ADD COLUMN city STRING;

ALTER TABLE mytable
MODIFY name STRING(255);
```

This will add a new column named `city` to the `mytable` table and modify the `name` column to have a maximum length of 255 characters.

## **Dropping Tables**

You can drop a table by using the `DROP TABLE` statement.

### Example

```sql
DROP TABLE mytable;
```

This will drop the `mytable` table.

## **Creating Views**

A view is a virtual table that is based on the result of a SQL query. To create a view, you can use the `CREATE VIEW` statement.

### Example

```sql
CREATE VIEW myview AS
SELECT id, name, age
FROM mytable;
```

This will create a new view named `myview` that displays the `id`, `name`, and `age` columns of the `mytable` table.

## **Creating Functions**

A function is a reusable block of code that performs a specific task. To create a function, you can use the `CREATE FUNCTION` statement.

### Example

```sql
CREATE FUNCTION myfunction(id INT) RETURNS INT
AS
BEGIN
  RETURN id * 2;
END;
```

This will create a new function named `myfunction` that takes an `id` parameter and returns the result of multiplying the `id` by 2.

## **Altering Functions**

You can alter a function by modifying its parameters, return type, or body. To alter a function, you can use the `ALTER FUNCTION` statement.

### Example

```sql
ALTER FUNCTION myfunction(id INT) RETURNS INT
AS
BEGIN
  RETURN id * 3;
END;
```

This will modify the `myfunction` function to multiply the `id` by 3 instead of 2.

## **Dropping Functions**

You can drop a function by using the `DROP FUNCTION` statement.

### Example

```sql
DROP FUNCTION myfunction(id INT);
```

This will drop the `myfunction` function.

## **Creating Indexes**

An index is a data structure that improves the speed of data retrieval. To create an index, you can use the `CREATE INDEX` statement.

### Example

```sql
CREATE INDEX myindex ON mytable (id);
```

This will create a new index named `myindex` on the `id` column of the `mytable` table.

## **Altering Indexes**

You can alter an index by modifying its columns or table. To alter an index, you can use the `ALTER INDEX` statement.

### Example

```sql
ALTER INDEX myindex ON mytable REBUILD;
```

This will rebuild the `myindex` index on the `mytable` table.

## **Dropping Indexes**

You can drop an index by using the `DROP INDEX` statement.

### Example

```sql
DROP INDEX myindex ON mytable;
```

This will drop the `myindex` index on the `mytable` table.

## **Key Concepts**

- **Database**: A container that holds one or more tables.
- **Table**: A collection of data that is stored in a Hive database.
- **View**: A virtual table that is based on the result of a SQL query.
- **Function**: A reusable block of code that performs a specific task.
- **Index**: A data structure that improves the speed of data retrieval.
- **CREATE DATABASE**: Statement used to create a new database.
- **CREATE TABLE**: Statement used to create a new table.
- **ALTER TABLE**: Statement used to modify a table.
- **DROP TABLE**: Statement used to drop a table.
- **CREATE VIEW**: Statement used to create a new view.
- **CREATE FUNCTION**: Statement used to create a new function.
- **ALTER FUNCTION**: Statement used to modify a function.
- **DROP FUNCTION**: Statement used to drop a function.
- **CREATE INDEX**: Statement used to create a new index.
- **ALTER INDEX**: Statement used to modify an index.
- **DROP INDEX**: Statement used to drop an index.
