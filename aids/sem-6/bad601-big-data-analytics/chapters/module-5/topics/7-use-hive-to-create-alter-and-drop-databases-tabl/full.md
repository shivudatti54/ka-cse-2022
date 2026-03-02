# **7 Use Hive to create, alter, and drop databases, tables, views, functions, and indexes**

## **Introduction**

Hive is a data warehousing and SQL-like query language for Hadoop, a popular big data processing framework. It provides a way to create, manage, and query large datasets stored in Hadoop Distributed File System (HDFS). In this section, we will delve into the world of Hive and explore how to create, alter, and drop databases, tables, views, functions, and indexes.

## **Historical Context**

Hive was first released in 2007 by the Apache Software Foundation. Since then, it has become a widely adopted tool for big data analytics. Hive is designed to work with existing data storage and management systems, making it an ideal choice for organizations looking to migrate their existing data into Hadoop.

## **Modern Developments**

In recent years, Hive has undergone significant improvements, including the introduction of Hive 2.0, which focuses on improving performance, scalability, and usability. Additionally, Hive has been integrated with other big data tools, such as Spark and Impala, to provide a more comprehensive big data analytics platform.

## **Creating Databases**

In Hive, a database is a container that holds one or more tables. To create a database, you use the `CREATE DATABASE` statement.

```sql
CREATE DATABASE mydatabase;
```

Once a database is created, you can create tables within it using the `CREATE TABLE` statement.

```sql
CREATE TABLE customers (
  id INT,
  name STRING,
  email STRING
);
```

## **Creating Tables**

A table in Hive is a collection of rows and columns. Each column has a specific data type, such as INT, STRING, or DATE.

```sql
CREATE TABLE customers (
  id INT,
  name STRING,
  email STRING
);
```

## **Alter Table Statements**

Hive provides several `ALTER TABLE` statements to modify existing tables. These include:

- `ALTER TABLE`: adds or changes a column in an existing table.
- `DROP COLUMN`: removes a column from an existing table.
- `ADD COLUMN`: adds a new column to an existing table.
- `RENAME COLUMN`: renames a column in an existing table.

```sql
-- add a new column
ALTER TABLE customers ADD column phone STRING;

-- remove a column
ALTER TABLE customers DROP COLUMN email;

-- rename a column
ALTER TABLE customers RENAME COLUMN phone TO mobile;
```

## **Creating Views**

A view in Hive is a virtual table that is based on the result of a query. Views are useful for simplifying complex queries and providing a layer of abstraction between the data and the end user.

```sql
CREATE VIEW customer_info AS
SELECT id, name, email
FROM customers;
```

## **Creating Functions**

A function in Hive is a reusable block of code that performs a specific task. Functions can be used to simplify complex queries and improve performance.

```sql
CREATE FUNCTION get_last_name(name STRING) RETURNS STRING
RETURNS
  CASE
    WHEN name LIKE '% %' THEN SPLIT(name, ' ')[-1]
    ELSE name
  END;
```

## **Creating Indexes**

An index in Hive is a data structure that improves the speed of data retrieval by providing a quick way to locate specific data.

```sql
CREATE INDEX idx_id ON customers (id);
```

## **Dropping Databases**

To drop a database, you use the `DROP DATABASE` statement.

```sql
DROP DATABASE mydatabase;
```

## **Dropping Tables**

To drop a table, you use the `DROP TABLE` statement.

```sql
DROP TABLE customers;
```

## **Dropping Views**

To drop a view, you use the `DROP VIEW` statement.

```sql
DROP VIEW customer_info;
```

## **Dropping Functions**

To drop a function, you use the `DROP FUNCTION` statement.

```sql
DROP FUNCTION get_last_name(name STRING) RETURNS STRING;
```

## **Dropping Indexes**

To drop an index, you use the `DROP INDEX` statement.

```sql
DROP INDEX idx_id ON customers;
```

## **Case Study:**

Suppose we have a customer database with the following structure:

```sql
CREATE TABLE customers (
  id INT,
  name STRING,
  email STRING,
  phone STRING
);

CREATE TABLE orders (
  id INT,
  customer_id INT,
  order_date DATE
);
```

We want to create a view that shows the customer name and email for each order.

```sql
CREATE VIEW customer_info AS
SELECT c.name, c.email, o.order_date
FROM customers c
JOIN orders o ON c.id = o.customer_id;
```

We can then query the view to get the desired information.

```sql
SELECT * FROM customer_info;
```

## **Applications:**

Hive provides a wide range of applications, including:

- **Data Warehousing:** Hive can be used to create a data warehouse that stores data from various sources.
- **Business Intelligence:** Hive can be used to create reports and dashboards to analyze business data.
- **Data Mining:** Hive can be used to perform data mining tasks, such as clustering and regression analysis.

## **Further Reading:**

- [Hive documentation](https://hive.apache.org/docs/)
- [Hive tutorials](https://hive.apache.org/learn/)
- [Hive recipes](https://cwiki.apache.org/hive/hive-cookbook/)
- [Data Warehousing with Hive](https://www.tutorialspoint.com/data_warehousing/data_warehousing_with_hive.htm)

I hope this comprehensive guide has provided you with a deep understanding of Hive and its capabilities. Whether you are a beginner or an experienced data analyst, Hive is a powerful tool that can help you unlock the full potential of your big data.
