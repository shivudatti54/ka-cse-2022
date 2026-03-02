# **7 Use Hive to Create, Alter, and Drop Databases, Tables, Views, Functions, and Indexes**

## **Introduction**

Hive is a data warehousing and SQL-like query language for Hadoop, a popular big data processing framework. In this section, we will explore how to use Hive to create, alter, and drop databases, tables, views, functions, and indexes.

## **Creating Databases**

A database in Hive is a collection of tables that share a common metadata. To create a database, use the `CREATE DATABASE` statement.

### Example:

```sql
CREATE DATABASE mydatabase;
```

This will create a new database named `mydatabase`.

## **Creating Tables**

A table in Hive is a collection of rows and columns. To create a table, use the `CREATE TABLE` statement.

### Example:

```sql
CREATE TABLE orders (
  order_id INT,
  customer_id INT,
  order_date DATE,
  total DECIMAL(10,2)
);
```

This will create a new table named `orders` with the specified columns.

## **Altering Databases and Tables**

To alter a database or table, use the `ALTER DATABASE` or `ALTER TABLE` statement.

### Altering a Database:

```sql
ALTER DATABASE mydatabase ADD CLUSTERED PARTITION (year = '2020');
```

This will add a new partition to the `mydatabase` database based on the `year` column.

### Altering a Table:

```sql
ALTER TABLE orders DROP COLUMN order_date;
```

This will drop the `order_date` column from the `orders` table.

## **Creating Views**

A view in Hive is a virtual table that is based on the result of a query. To create a view, use the `CREATE VIEW` statement.

### Example:

```sql
CREATE VIEW sales AS SELECT customer_id, SUM(total) AS total_sales FROM orders GROUP BY customer_id;
```

This will create a new view named `sales` that shows the total sales for each customer.

## **Creating Functions**

A function in Hive is a reusable block of code that takes input parameters and returns output values. To create a function, use the `CREATE FUNCTION` statement.

### Example:

```sql
CREATE FUNCTION calculate_total_sales(customer_id INT) RETURNS DECIMAL(10,2)
RETURNS SUM(total) FROM orders WHERE customer_id = customer_id;
```

This will create a new function named `calculate_total_sales` that takes a `customer_id` parameter and returns the total sales for that customer.

## **Creating Indexes**

An index in Hive is a data structure that improves query performance by allowing the database to quickly locate specific data. To create an index, use the `CREATE INDEX` statement.

### Example:

```sql
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
```

This will create a new index named `idx_orders_customer_id` on the `customer_id` column of the `orders` table.

## **Dropping Databases, Tables, Views, Functions, and Indexes**

To drop a database, table, view, function, or index, use the `DROP DATABASE`, `DROP TABLE`, `DROP VIEW`, `DROP FUNCTION`, or `DROP INDEX` statement.

### Dropping a Database:

```sql
DROP DATABASE mydatabase;
```

This will drop the `mydatabase` database.

### Dropping a Table:

```sql
DROP TABLE orders;
```

This will drop the `orders` table.

Note: Be cautious when dropping databases, tables, views, functions, and indexes, as they cannot be recovered once dropped.

## **Key Concepts:**

- **Database**: A collection of tables that share a common metadata.
- **Table**: A collection of rows and columns.
- **View**: A virtual table that is based on the result of a query.
- **Function**: A reusable block of code that takes input parameters and returns output values.
- **Index**: A data structure that improves query performance by allowing the database to quickly locate specific data.
