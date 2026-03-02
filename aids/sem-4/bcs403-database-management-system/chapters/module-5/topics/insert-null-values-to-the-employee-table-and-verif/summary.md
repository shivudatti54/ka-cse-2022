# **Insert Null Values to the Employee Table and Verify the Result**

**Key Points:**

- **Null Values:**
  - A null value represents an unknown or missing value in a database table.
  - Null values are represented by a symbol `NULL` or an empty string (`''`).
- **Inserting Null Values:**
  - To insert a null value into a table, use the `NULL` keyword or an empty string.
  - Example: `INSERT INTO employee (name, age, salary) VALUES ('John Doe', NULL, 5000.00);`
- **Verifying Null Values:**
  - To verify null values, use the `IS NULL` or `IS NOT NULL` operators.
  - Example: `SELECT * FROM employee WHERE age IS NULL;`
- **Best Practices:**
  - Use null values to represent missing or unknown data.
  - Avoid using null values to represent invalid or inconsistent data.
- **Theorem:**
  - **The Null Value Principle:** A table can contain null values, but a column can have only one null value.

**Important Formulas and Definitions:**

- **Null Value Formula:** `NULL` (symbol or empty string `''`)
- **IS NULL Operator:** `SELECT * FROM table WHERE column IS NULL`
- **IS NOT NULL Operator:** `SELECT * FROM table WHERE column IS NOT NULL`
