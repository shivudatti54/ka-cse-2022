# **Inserting Records into a Table**

**Definition:** Inserting records into a table is a database management system operation that adds new data to an existing table.

**Key Points:**

- **Insert Statement:** Used to insert new records into a table. Syntax: `INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);`
- **Column Order:** The order of columns in the `INSERT INTO` clause must match the order of columns in the table.
- **Value Order:** The order of values in the `VALUES` clause must match the order of columns in the table.
- **Auto-Increment:** Some databases (e.g. MySQL) support auto-incrementing primary keys, which can be used to automatically assign a unique value to a new record.
- **Constraints:** Insert statements can include constraints, such as `UNIQUE` or `PRIMARY KEY`, to ensure data integrity.

**Important Formulas/Definitions/Theorems:**

- **Primary Key:** A unique identifier for each record in a table.
- **Foreign Key:** A field in a table that references the primary key of another table.
- **Data Integrity:** The accuracy and consistency of data in a database.

**Revision Tips:**

- Make sure to match column and value orders in the `INSERT INTO` and `VALUES` clauses.
- Understand the role of auto-incrementing primary keys and constraints in ensuring data integrity.
