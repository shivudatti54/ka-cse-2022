# **BIG DATA ANALYTICS: INTRODUCTION TO HIVE**

## **Introduction to Hive (10.1)**

### Overview

Apache Hive is an open-source data warehousing and SQL-like query language for Hadoop, a popular big data processing framework. Hive provides a way to analyze and process large datasets stored in Hadoop Distributed File System (HDFS).

### Key Concepts

- **Hive**: A data warehousing and SQL-like query language for Hadoop.
-     **Hive Query Language (HQL)**: A SQL-like language used for querying and manipulating data in Hive.
- **Hive Schema**: A schema that defines the structure of a Hive table or view.
- **Partitioning**: A technique used to store data in separate files based on a key or attribute.

### Hive Architecture

---

### Components

- **Metastore**: A central repository that stores metadata about the Hive schema.
-     **Hive Query Engine**: A component that executes HQL queries on the data stored in HDFS.
- **Hive UI**: A web-based interface for managing Hive schema, creating views, and executing queries.

### Data Flow

- **Data Ingestion**: Data is ingested into HDFS using tools like Sqoop or Flume.
- **Hive Schema Creation**: A Hive schema is created based on the ingested data.
- **Data Storage**: Data is stored in HDFS based on the Hive schema.
- **Query Execution**: HQL queries are executed on the stored data.

## **Hive Data Types**

### Overview

Hive supports various data types, including primitive types, string types, and numeric types.

### Primitive Types

- **INT**: A 32-bit signed integer type.
- **BIGINT**: A 64-bit signed integer type.
- **FLOAT**: A 32-bit floating point type.
- **DOUBLE**: A 64-bit floating point type.
- **BOOLEAN**: A boolean type that can take values TRUE or FALSE.

### String Types

- **CHAR**: A character string type.
- **VARCHAR**: A variable-length character string type.
- **STRING**: A string type that can store any type of data.

### Numeric Types

- **INT**: A 32-bit signed integer type.
- **BIGINT**: A 64-bit signed integer type.
- **FLOAT**: A 32-bit floating point type.
- **DOUBLE**: A 64-bit floating point type.

### Date and Time Types

- **DATE**: A date type that represents a date without time.
- **TIMESTAMP**: A timestamp type that represents a date and time.

## **Hive File Formats**

### Overview

Hive supports various file formats, including text files, CSV files, JSON files, and Parquet files.

### File Formats

- **TEXT**: A text file format that stores data as plain text.
- **CSV**: A comma-separated values file format that stores data in a tabular format.
- **JSON**: A JavaScript object notation file format that stores data in a JSON format.
- **PARQUET**: A columnar storage file format that stores data in a compressed format.

### Key Concepts

- **Partitioning**: A technique used to store data in separate files based on a key or attribute.
- **Bucketing**: A technique used to store data in separate files based on a key or attribute.

## **Hive Query**

### Overview

Hive Query Language (HQL) is a SQL-like language used for querying and manipulating data in Hive.

### HQL Syntax

- **SELECT**: Used to select data from a Hive table or view.
- **FROM**: Used to specify the table or view from which to select data.
- **WHERE**: Used to filter data based on a condition.
- **GROUP BY**: Used to group data based on one or more columns.
- **HAVING**: Used to filter grouped data based on a condition.

### HQL Example

```sql
SELECT *
FROM table_name
WHERE column_name = 'value'
GROUP BY column_name
HAVING SUM(column_name) > 100;
```

This query selects all columns from the `table_name` table where the value in the `column_name` column is 'value', groups the data by the `column_name` column, and filters the grouped data to include only those groups where the sum of the `column_name` column is greater than 100.
