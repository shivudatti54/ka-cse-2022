# Views in SQL

## Revision Notes

### Key Concepts

- **Definition**: A view is a virtual table based on the result of a SQL query.
- **Purpose**: To simplify complex queries, improve data security, and enhance data abstraction.
- **Type**: Physical table or materialized view.

### Important Formulas/Definitions

- **View Creation**: `CREATE VIEW view_name AS SELECT column1, column2 FROM table_name;`
- **View Updates**: `ALTER VIEW view_name AS SELECT column1, column2 FROM table_name;`
- **View Drop**: `DROP VIEW view_name;`

### Key Theorems

- **View Independence Theorem**: A view is independent of the physical storage of the underlying tables.
- **View Materialization Theorem**: A view can be materialized as a physical table.

### Important SQL Statements

- **CREATE VIEW**: Used to create a view.
- **ALTER VIEW**: Used to modify a view.
- **DROP VIEW**: Used to drop a view.

### SQL Syntax

- `SELECT * FROM view_name;` to query a view
- `INSERT INTO view_name VALUES (...);` to insert data into a view
- `UPDATE view_name SET ...;` to update data in a view
- `DELETE FROM view_name;` to delete data from a view

### Best Practices

- Use views to simplify complex queries and improve data security.
- Use materialized views for queries that require frequent data retrieval.
- Avoid using views with large amounts of data to improve performance.
