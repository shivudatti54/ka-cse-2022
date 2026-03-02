# **Language (HQL) Revision Notes**

## **Introduction**

- HQL (Hive Query Language) is a SQL-like language used for querying and managing data in Hive.
- It is used to write queries that can be executed on Hive's data storage.

## **Syntax and Basics**

- HQL is case-insensitive.
- Queries are written in a SQL-like syntax.
- Use `SELECT`, `FROM`, `WHERE`, `GROUP BY`, and `ORDER BY` clauses.
- Use `LIMIT` and `OFFSET` clauses for pagination.
- Use `JOIN` and `UNION` operators for combining data.

## **Data Types and Operators**

- **Data Types**:
  - Integer: `INT`, `TINYINT`, `BIGINT`
  - String: `STRING`, `CHAR`, `VARCHAR`
  - Date/Time: `DATE`, `TIME`, `TIMESTAMP`
  - Boolean: `BOOLEAN`
- **Operators**:
  - Arithmetic operators: `+`, `-`, `*`, `/`, `%`
  - Comparison operators: `=`, `!=`, `>`, `<`, `>=` , `<=`
  - Logical operators: `AND`, `OR`, `NOT`

## **Functions and Aggregate Functions**

- **String Functions**:
  - `LOWER()`, `UPPER()`, `INITCAP()`
  - `LENGTH()`, `SUBSTRING()`, `CONCAT()`
- **Numeric Functions**:
  - `SUM()`, `AVG()`, `MAX()`, `MIN()`
  - `COUNT()`, `GROUP_CONCAT()`
- **Date/Time Functions**:
  - `DATE_FORMAT()`, `TIMESTAMP_FORMAT()`

## **Important Formulas and Theorems**

- **Hive Data Model**:
  - Hive uses a column-oriented storage model.
  - Each row is stored as a vector of values.
- **Data Compression**:
  - Hive uses various compression algorithms (e.g., Snappy, Gzip).
  - Compression is enabled by default.

## **Best Practices**

- Use meaningful table and column names.
- Optimize queries using `EXPLAIN` and `ANALYZE`.
- Use `LIMIT` and `OFFSET` for pagination.
- Avoid using `SELECT *`; specify only required columns.
