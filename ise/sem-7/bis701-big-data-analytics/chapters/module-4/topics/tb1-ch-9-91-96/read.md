# **TB1: Ch 9: 9.1-9.6 - Introduction to Hive**

## **9.1: What is Hive?**

Hive is a data warehousing and SQL-like query language for Hadoop, a popular Big Data processing framework. It provides a way to store and manage large datasets in a structured format, allowing users to perform complex queries and data analysis.

**Key Features of Hive:**

- Supports SQL-like syntax for querying data
- Provides support for multiple data formats, including CSV, JSON, and Avro
- Enables data warehousing and business intelligence capabilities
- Scalable and fault-tolerant architecture

## **9.2: Hive Architecture**

Hive's architecture consists of the following components:

- **Hive metastore**: A central repository that stores metadata about the data in a Hive table
- **Hive runtime engine**: The engine that executes Hive queries and manages data storage
- **Hive client**: The user interface that submits Hive queries and interacts with the Hive runtime engine

## **9.3: Hive Data Types**

Hive supports the following data types:

- **Int**: A 32-bit integer type
- **Int64**: A 64-bit integer type
- **Double**: A 64-bit floating-point type
- **String**: A string type
- **Boolean**: A boolean type
- **Date**: A date type
- **Timestamp**: A timestamp type

## **9.4: Hive File Formats**

Hive supports the following file formats:

- **CSV**: Comma Separated Values
- **JSON**: JavaScript Object Notation
- **Avro**: Apache Arrow
- **Parquet**: Columnar storage format
- **Text**: Plain text files

## **9.5: Hive Query Language**

Hive's query language is similar to SQL and consists of the following components:

- **SELECT**: Selects data from one or more tables
- **FROM**: Specifies the tables to select from
- **WHERE**: Filters data based on conditions
- **GROUP BY**: Groups data by one or more columns
- **HAVING**: Filters grouped data based on conditions
- **ORDER BY**: Sorts data in ascending or descending order

## **9.6: Hive Query Syntax**

Here is an example of a Hive query that selects data from a table called `orders`:

```sql
SELECT order_id, customer_name, order_date
FROM orders
WHERE order_date > '2020-01-01'
GROUP BY order_id, customer_name
HAVING SUM(order_total) > 1000;
```

This query selects the `order_id`, `customer_name`, and `order_date` columns from the `orders` table, filters data where the `order_date` is greater than '2020-01-01', groups data by `order_id` and `customer_name`, and filters grouped data where the sum of `order_total` is greater than 1000.
