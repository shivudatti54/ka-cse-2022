# **TB1: Ch 9: 9.1-9.6 - Introduction to Hive**

## **9.1: What is Hive?**

### Definition

Hive is a data warehousing and SQL-like query language for Hadoop, a popular open-source big data processing framework. Hive provides a way to store and manage large datasets in a structured format, making it easier to analyze and extract insights.

### Features

- Supports SQL-like queries
- Manages large datasets
- Provides data warehousing capabilities
- Integrates with Hadoop ecosystem

### Example Use Case

Suppose we have a large log file containing user activity data. We can use Hive to create a table to store this data, define a schema to organize the data, and write SQL-like queries to analyze and extract insights from the data.

## **9.2: Hive Architecture**

### Overview

Hive's architecture consists of the following components:

- **Hive Metastore**: stores metadata about the data in Hive, such as table definitions and schema
- **Hive Query Compiler**: converts Hive queries into MapReduce jobs
- **Hive Query Optimizer**: optimizes the MapReduce jobs for performance
- **Hive Execution Engine**: executes the optimized MapReduce jobs

### Diagram

```
+---------------+
|  Hive Metastore  |
+---------------+
       |
       |  Metadata
       v
+---------------+
| Hive Query    |
|  Compiler     |
+---------------+
       |
       |  Query
       v
+---------------+
| Hive Query    |
|  Optimizer    |
+---------------+
       |
       |  Optimized
       |  Query
       v
+---------------+
| Hive Execution|
|  Engine      |
+---------------+
       |
       |  MapReduce
       |  Jobs
       v
+---------------+
|  Hadoop Cluster  |
+---------------+
```

## **9.3: Hive Data Types**

### Overview

Hive supports various data types, including:

- **Integer**: whole numbers, e.g., 1, 2, 3, etc.
- **String**: text data, e.g., "hello", "world", etc.
- **Date**: date and time data, e.g., "2022-01-01", "2022-01-02", etc.
- **Timestamp**: timestamp data, e.g., "2022-01-01 12:00:00", "2022-01-02 12:00:00", etc.

### Example

Suppose we have a table `orders` with the following schema:

```sql
CREATE TABLE orders (
  order_id INT,
  customer_name STRING,
  order_date DATE,
  order_time TIMESTAMP
);
```

We can insert data into the table using the following query:

```sql
INSERT INTO orders (order_id, customer_name, order_date, order_time)
VALUES (1, "John Doe", "2022-01-01", "2022-01-01 12:00:00");
```

## **9.4: Hive File Formats**

### Overview

Hive supports various file formats, including:

- **Text File**: plain text files, e.g., `.txt`
- **CSV File**: comma-separated value files, e.g., `.csv`
- **JSON File**: JavaScript object notation files, e.g., `.json`
- **AVRO File**: Apache Arrow files, e.g., `.avro`

### Example

Suppose we have a text file `orders.txt` containing the following data:

```text
1,John Doe,2022-01-01,12:00:00
2,Jane Doe,2022-01-02,13:00:00
```

We can import this file into Hive using the following query:

```sql
LOAD DATA INPATH '/path/to/orders.txt' INTO TABLE orders;
```

## **9.5: Hive Query**

### Overview

Hive queries are used to retrieve data from Hive tables. Hive queries can be written using SQL-like syntax.

### Example

Suppose we have a table `orders` with the following data:

```sql
+---------+---------------+------------+------------------+
| order_id| customer_name | order_date | order_time       |
+---------+---------------+------------+------------------+
|        1| John Doe      | 2022-01-01 | 2022-01-01 12:00:00|
|        2| Jane Doe      | 2022-01-02 | 2022-01-02 13:00:00|
+---------+---------------+------------+------------------+
```

We can retrieve all orders for John Doe using the following query:

```sql
SELECT * FROM orders WHERE customer_name = 'John Doe';
```

## **9.6: Hive Query Optimization**

### Overview

Hive query optimization is used to optimize Hive queries for performance. Hive query optimization involves the following steps:

1.  **Parse**: parse the Hive query
2.  **Analyze**: analyze the parsed query
3.  **Optimize**: optimize the analyzed query
4.  **Generate**: generate the optimized query

### Example

Suppose we have a Hive table `orders` with the following data:

```sql
+---------+---------------+------------+------------------+
| order_id| customer_name | order_date | order_time       |
+---------+---------------+------------+------------------+
|        1| John Doe      | 2022-01-01 | 2022-01-01 12:00:00|
|        2| Jane Doe      | 2022-01-02 | 2022-01-02 13:00:00|
|        3| John Doe      | 2022-01-03 | 2022-01-03 14:00:00|
+---------+---------------+------------+------------------+
```

We can optimize the query to retrieve all orders for John Doe using the following command:

```sql
SET hive.optimize.subquery = true;
SET hive.optimize.subquery.limit = 100;
```

This will optimize the query to retrieve all orders for John Doe in batches of 100.
