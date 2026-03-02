# Language (HQL)

### Overview

- Hive Query Language (HQL) is a SQL-like language used for interacting with Hive databases.
- HQL is designed to be easy to learn and use, with a syntax similar to SQL.

### Key Features

- **SELECT**: Retrieves data from a table.
- **INSERT**: Inserts new data into a table.
- **UPDATE**: Updates existing data in a table.
- **DELETE**: Deletes data from a table.
- **CREATE**: Creates a new table or views.
- **DROP**: Deletes a table or view.
- **JOIN**: Combines data from multiple tables.
- **GROUP BY**: Groups data by one or more columns.
- **HAVING**: Filters grouped data.
- **ORDER BY**: Sorts data in ascending or descending order.

### Important Formulas and Definitions

- **Filter**: `SELECT * FROM table WHERE condition;`
- **Aggregation**: `SELECT column, COUNT(*) FROM table GROUP BY column;`
- **Join**: `SELECT * FROM table1, table2 WHERE table1.id = table2.id;`
- **Subquery**: `SELECT * FROM (SELECT * FROM table WHERE condition) AS subquery;`

### Theorems

- **Data Type Conversion**: `CAST(column AS data_type)`
- **Function**: `FUNCTION(column, data_type)`

### Important HQL Functions

- **SUM**: `SUM(column)`
- **AVG**: `AVG(column)`
- **MAX**: `MAX(column)`
- **MIN**: `MIN(column)`
- **GROUP_CONCAT**: `GROUP_CONCAT(column)`

### HQL Best Practices

- Use meaningful table and column names.
- Use indexes to improve query performance.
- Optimize queries for large datasets.
