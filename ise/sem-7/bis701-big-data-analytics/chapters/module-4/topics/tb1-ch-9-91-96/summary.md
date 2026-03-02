**TB1: Ch 9: 9.1-9.6 - Big Data Analytics**

### Introduction to Hive

- **What is Hive?**: Hive is a data warehousing and SQL-like query language for Hadoop.
- **Hive Architecture**:
  - **Server**: Hive Server (hs2)
  - **Client**: Hive Client (beeswax, hive-impala)
  - **Storage**: HDFS (Hive stores metadata in HDFS)

### Hive Data Types

- **Numeric Types**:
  - `INT`: 32-bit integer
  - `BIGINT`: 64-bit integer
  - `FLOAT`: 32-bit floating-point number
  - `DOUBLE`: 64-bit floating-point number
- **String Types**:
  - `CHAR`: fixed-length string
  - `VARCHAR`: variable-length string
- **Date/Time Types**:
  - `DATE`: date value
  - `TIME`: time value
  - `TIMESTAMP`: date and time value
- **Boolean Type**: `BOOLEAN`

### Hive File Formats

- **Internal Table Format**: tables stored in HDFS (Hive stores metadata in HDFS)
- **External Table Format**: tables stored in external storage systems (e.g. CSV, Parquet)
- **Storage**: HDFS (Hive stores metadata in HDFS)

### Hive Query

- **SELECT Statement**:
  - `SELECT * FROM table_name;`
  - `SELECT column1, column2 FROM table_name;`
- **WHERE Clause**:
  - `SELECT * FROM table_name WHERE condition;`
- **JOIN Clause**:
  - `SELECT * FROM table1 JOIN table2 ON table1.column = table2.column;`
- **GROUP BY Clause**:
  - `SELECT * FROM table_name GROUP BY column1, column2;`
- **HAVING Clause**:
  - `SELECT * FROM table_name GROUP BY column1, column2 HAVING condition;`

### Important Formulas/Definitions/Theorems

- **Join**: inner join, left join, right join
- **Subquery**: complex query within a query
- **Aggregate Function**: `SUM`, `AVG`, `MAX`, `MIN`, etc.

This summary provides a concise overview of the key concepts in Ch 9: 9.1-9.6 of the BIG DATA ANALYTICS topic.
