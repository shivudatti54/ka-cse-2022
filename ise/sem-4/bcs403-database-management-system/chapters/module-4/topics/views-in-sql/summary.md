# **Views in SQL**

**Definition:** A view in SQL is a virtual table based on the result-set of a query. It does not store data itself but rather provides a way to access data from one or more tables.

**Key Points:**

- **Creation of a View:**
  - Uses the `CREATE VIEW` statement
  - Specifies the query that defines the view
  - Can be created from a single table or multiple tables
- **View Characteristics:**
  - Does not store data itself
  - Does not support data modification
  - Does not support data deletion
  - Supports data retrieval
- **Types of Views:**
  - **Materialized View:** Stores the result-set in a physical table
  - **Virtual View:** Does not store the result-set and only stores the query definition
- **Benefits:**
  - Simplifies complex queries
  - Provides a layer of abstraction
  - Supports data security and access control
- **Formulas:**
  - None specific to views
- **Theorems:**
  - **Data Independence Theorem:** Views provide a layer of abstraction and do not depend on the physical implementation of the data
- **Important SQL Statements:**
  - `CREATE VIEW`: Creates a view
  - `DROP VIEW`: Drops a view
  - `ALTER VIEW`: Modifies a view
  - `SELECT * FROM`: Retrieves data from a view
