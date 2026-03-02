# **7 Use Hive to create, alter, and drop databases, tables, views, functions, and indexes**

## **Introduction**

Hive is a data warehousing and SQL-like query language for Hadoop, a popular big data processing framework. Hive allows users to create, manage, and analyze large datasets stored in Hadoop Distributed File System (HDFS). In this module, we will explore the various ways to use Hive to create, alter, and drop databases, tables, views, functions, and indexes.

## **Historical Context**

Hive was first introduced in 2006 by Doug Cutting and Ben Mason, the co-founders of Metamarkets. Initially, Hive was designed to provide a SQL-like interface for Hadoop, making it easier for users to analyze large datasets. Since then, Hive has evolved to become a widely-used data warehousing and analytics tool.

## **Modern Developments**

In recent years, Hive has undergone significant improvements, including the introduction of:

1. **Hive 0.14**: Introduced a new query optimizer, which improved query performance and reduced memory usage.
2. **Hive 1.0**: Introduced support for Hadoop 2.0, which enabled faster data processing and improved scalability.
3. **Hive Metastore**: Introduced a new metastore architecture, which improved data cataloging and reduced data duplication.

## **Creating Databases and Tables**

In Hive, a database is essentially a container for tables. To create a database, use the `CREATE DATABASE` statement.

**Example 1: Creating a Database**

```sql
CREATE DATABASE mydatabase;
```

To create a table within a database, use the `CREATE TABLE` statement.

**Example 2: Creating a Table**

```sql
CREATE TABLE mydatabase.mytable (
  id INT,
  name STRING,
  age INT
);
```

## **Alter Table**

To alter a table, use the `ALTER TABLE` statement.

**Example 3: Altering a Table**

```sql
ALTER TABLE mydatabase.mytable
ADD COLUMN email STRING;
```

## **Drop Database**

To drop a database, use the `DROP DATABASE` statement.

**Example 4: Dropping a Database**

```sql
DROP DATABASE mydatabase;
```

## **Drop Table**

To drop a table, use the `DROP TABLE` statement.

**Example 5: Dropping a Table**

```sql
DROP TABLE mydatabase.mytable;
```

## **Creating Views**

A view is a virtual table that is based on the result of a query. To create a view, use the `CREATE VIEW` statement.

**Example 6: Creating a View**

```sql
CREATE VIEW mydatabase.myview AS
SELECT * FROM mydatabase.mytable WHERE age > 18;
```

## **Alter View**

To alter a view, use the `ALTER VIEW` statement.

**Example 7: Altering a View**

```sql
ALTER VIEW mydatabase.myview
ADD COLUMN country STRING;
```

## **Drop View**

To drop a view, use the `DROP VIEW` statement.

**Example 8: Dropping a View**

```sql
DROP VIEW mydatabase.myview;
```

## **Creating Functions**

A function is a reusable block of code that can be called from a query. To create a function, use the `CREATE FUNCTION` statement.

**Example 9: Creating a Function**

```sql
CREATE FUNCTION mydatabase.myfunc(
  id INT,
  name STRING
) RETURNS INT AS
BEGIN
  RETURN id * 2;
END;
```

## **Alter Function**

To alter a function, use the `ALTER FUNCTION` statement.

**Example 10: Altering a Function**

```sql
ALTER FUNCTION mydatabase.myfunc
ADD COLUMN email STRING;
```

## **Drop Function**

To drop a function, use the `DROP FUNCTION` statement.

**Example 11: Dropping a Function**

```sql
DROP FUNCTION mydatabase.myfunc;
```

## **Creating Indexes**

An index is a data structure that improves query performance by allowing Hive to quickly locate data. To create an index, use the `CREATE INDEX` statement.

**Example 12: Creating an Index**

```sql
CREATE INDEX mydatabase.myindex ON mydatabase.mytable (name);
```

## **Alter Index**

To alter an index, use the `ALTER INDEX` statement.

**Example 13: Altering an Index**

```sql
ALTER INDEX mydatabase.myindex ON mydatabase.mytable REBUILD;
```

## **Drop Index**

To drop an index, use the `DROP INDEX` statement.

**Example 14: Dropping an Index**

```sql
DROP INDEX mydatabase.myindex ON mydatabase.mytable;
```

## **Diagrams**

Here is a diagram showing the relationships between Hive tables and indexes:

```
+---------------+
|  Hive Database  |
+---------------+
|  +-----------+
|  |  Table   |
|  +-----------+
|  +-----+
|  | Index  |
|  +-----+
|  +-----+
|  | Function|
|  +-----+
|  +-----+
|  | View   |
|  +-----+
```

## **Case Studies**

Here are a few case studies demonstrating the use of Hive to create, alter, and drop databases, tables, views, functions, and indexes:

1. **Analyzing Customer Data**

Create a Hive database and table to store customer data.

```sql
CREATE DATABASE customerdb;
CREATE TABLE customerdb.customers (
  id INT,
  name STRING,
  age INT
);
```

Create a view to filter customers by age.

```sql
CREATE VIEW customerdb.customerview AS
SELECT * FROM customerdb.customers WHERE age > 18;
```

Create a function to calculate the total revenue of customers.

```sql
CREATE FUNCTION customerdb.totalrevenue(
  id INT,
  name STRING
) RETURNS INT AS
BEGIN
  RETURN id * 2;
END;
```

2. **Optimizing Query Performance**

Create an index on the `name` column of the `customers` table.

```sql
CREATE INDEX customerdb.customers_name ON customerdb.customers (name);
```

Rebuild the index to improve query performance.

```sql
ALTER INDEX customerdb.customers_name ON customerdb.customers REBUILD;
```

3. **Implementing Data Warehousing**

Create a Hive database and table to store sales data.

```sql
CREATE DATABASE salesdb;
CREATE TABLE salesdb.sales (
  id INT,
  product STRING,
  quantity INT
);
```

Create a view to filter sales data by product.

```sql
CREATE VIEW salesdb.salesview AS
SELECT * FROM salesdb.sales WHERE product = 'Product A';
```

Create a function to calculate the total sales revenue.

```sql
CREATE FUNCTION salesdb.totalsales(
  id INT,
  product STRING
) RETURNS INT AS
BEGIN
  RETURN id * 2;
END;
```

## **Conclusion**

In this module, we have explored the various ways to use Hive to create, alter, and drop databases, tables, views, functions, and indexes. We have also provided case studies demonstrating the use of Hive in real-world scenarios. With this knowledge, you can now effectively use Hive to manage and analyze large datasets.

## **Further Reading**

- [Hive Documentation](https://hive.apache.org/docs/)
- [Hive Tutorial](https://www.tutorialspoint.com/hive/index.htm)
- [Big Data Analytics with Hive and Spark](https://www.packtpub.com/product/big-data-analytics-with-hive-and-spark/9781787287347)

I hope this detailed content helps! Let me know if you need any further assistance.
