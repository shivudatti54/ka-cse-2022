# **Statement Objects**

**Definition:** A Statement object is a JDBC object that represents a SQL statement that can be executed to retrieve or modify data.

**Key Features:**

- **Creating a Statement Object:** `Statement obj = conn.createStatement();`
- **Executing a Statement:** `obj.execute(query);`
- **Updating a Statement:** `obj.update(values);`
- **Querying a Statement:** `obj.getResultSet();`
- **Closing a Statement:** `obj.close();`

**Types of Statement Objects:**

- **CallableStatement:** Used for stored procedures and functions
- **ResultSet:** Used to retrieve data from a query
- **PreparedStatement:** Used for parameterized queries

**Important Formulas:**

- No specific formulas are required for Statement Objects.

**Important Definitions:**

- **Statement:** A JDBC object that represents a SQL statement.
- **CallableStatement:** A Statement object that can execute stored procedures and functions.
- **ResultSet:** A Statement object that can retrieve data from a query.

**Important Theorems:**

- The JDBC Statement object is used to execute SQL statements.
- The ResultSet object is used to retrieve data from a query.

**Revision Tips:**

- Understand the different types of Statement objects.
- Know how to create, execute, and close a Statement object.
- Understand the difference between a Statement object and a ResultSet object.
