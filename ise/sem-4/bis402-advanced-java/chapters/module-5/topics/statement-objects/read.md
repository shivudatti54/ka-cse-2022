# Statement Objects

=====================================

## Overview

---

In Java Database Connectivity (JDBC), a Statement object is a class that provides methods for executing SQL statements and retrieving data from a database. Statements are used to interact with the database, and they are an essential part of the JDBC API.

## Definition

---

A Statement object is a proxy that delegates method calls to a Statement implementation, which performs the actual database operations.

## Key Characteristics

---

### 1. SQL Statement Execution

- Statements are used to execute SQL statements, which can be SELECT, INSERT, UPDATE, or DELETE statements.
- Statements can be used to execute stored procedures and functions.

### 2. Query Execution

- Statements can execute queries, which can retrieve data from the database.
- Statements can also be used to update data in the database.

### 3. Parameterized Statements

- Statements can be parameterized, which allows for more efficient execution and reduces the risk of SQL injection attacks.
- Parameterized statements use placeholders in the SQL statement, which are replaced with actual values before execution.

### 4. Auto-Commit

- Statements are associated with a connection, and they are automatically committed when they are closed.
- Statements can also be set to auto-commit, which allows for automatic commit of changes.

## Types of Statements

---

### 1. Prepared Statements

- Prepared statements are precompiled SQL statements that can be executed multiple times with different parameters.
- Prepared statements are more efficient than regular statements and reduce the risk of SQL injection attacks.

### 2. CallableStatements

- Callable statements are used to execute stored procedures and functions.
- Callable statements return a result set, which can be retrieved using the `getResultSet()` method.

## Statement Methods

---

### 1. executeQuery()

- Executes a query and returns a result set.
- The result set is populated with the data returned by the query.

### 2. executeUpdate()

- Executes an update statement and returns the number of rows affected.
- The update statement is executed and the changes are committed to the database.

### 3. setAutoCommit(boolean)

- Sets the auto-commit mode for the statement.
- If set to true, the statement will be automatically committed when it is closed.

### 4. setMaxRows(int)

- Sets the maximum number of rows that can be retrieved from the result set.
- If set to -1, there is no limit on the number of rows.

## Example

---

```java
// Create a connection to the database
Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "username", "password");

// Create a statement object
Statement stmt = conn.createStatement();

// Create a prepared statement
String query = "SELECT * FROM mytable WHERE name = ?";
PreparedStatement pstmt = conn.prepareStatement(query);

// Set the parameter
pstmt.setString(1, "John");

// Execute the prepared statement
ResultSet rs = pstmt.executeQuery();

// Print the results
while (rs.next()) {
    System.out.println(rs.getString(1) + " " + rs.getString(2));
}
```

In this example, we create a connection to the database and a statement object. We then create a prepared statement with a parameterized query. We set the parameter and execute the prepared statement, which returns a result set. We then print the results to the console.
