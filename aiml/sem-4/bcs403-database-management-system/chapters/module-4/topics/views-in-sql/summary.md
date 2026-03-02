# Views in SQL

**Definition:** A view is a virtual table based on the result of a SQL query. It appears as a regular table but is actually a query that selects data from one or more tables.

**Key Points:**

- A view can be thought of as a stored query that can be used to manipulate data.
- Views do not store data themselves, but instead reference the underlying tables.
- Views can be used to:
  - Simplify complex queries
  - Hide underlying table structures
  - Provide a layer of abstraction
- Views can be created using the `CREATE VIEW` statement.
- Views can be used to restrict access to data by defining which tables can be accessed.

**Important Formulas/Definitions:**

- **View Creation Syntax:**

```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table1
WHERE condition;
```

- **View Update:** Not possible, as views are virtual tables.
- **View Delete:** Not possible, as views are virtual tables.

**Theorems:**

- **Separation of Concerns:** Views can help separate concerns by hiding underlying table structures and providing a layer of abstraction.
- **Data Integrity:** Views can help maintain data integrity by restricting access to data and ensuring that data is consistent.

**Revision Tips:**

- Remember that views are virtual tables and do not store data themselves.
- Understand the syntax for creating views and how to use them to simplify complex queries.
- Be aware of the limitations of views, such as not being able to update or delete them.
