# JDBC: Statement Objects and ResultSet

## 1. Introduction to Statement Objects

In JDBC (Java Database Connectivity), a `Statement` object is used to execute SQL queries and updates against a relational database. Once a connection to the database is established using a `Connection` object, you use a `Statement` object to send SQL commands and receive results.

Think of the `Connection` as the bridge between your Java application and the database, and the `Statement` as the vehicle that carries your SQL commands across that bridge.

## 2. Types of Statement Objects

JDBC provides three types of Statement interfaces, each serving a different purpose.

### 2.1. Statement

The basic interface for executing static SQL statements. The SQL query is fixed and provided at the time of creation.

**Use Case:** Ideal for ad-hoc queries that are executed only once and where the SQL string is complete and doesn't require parameterization.

**Example:**

```java
Statement stmt = connection.createStatement();
String sql = "SELECT * FROM Employees WHERE department = 'Sales'";
ResultSet rs = stmt.executeQuery(sql);
```

### 2.2. PreparedStatement

Extends the `Statement` interface. It represents a precompiled SQL statement that can contain input parameters (denoted by `?`). The SQL is sent to the DBMS precompiled, which allows for efficient execution, especially when the same statement is executed multiple times with different parameters. It also provides built-in protection against SQL injection attacks.

**Use Case:** The best choice for parameterized queries that are executed multiple times with high efficiency and security.

**Example:**

```java
String sql = "UPDATE Products SET price = ? WHERE product_id = ?";
PreparedStatement pstmt = connection.prepareStatement(sql);
pstmt.setDouble(1, 29.99); // Sets the first parameter (price)
pstmt.setInt(2, 101);      // Sets the second parameter (product_id)
int rowsAffected = pstmt.executeUpdate();
```

### 2.3. CallableStatement

Extends the `PreparedStatement` interface. It is used to execute stored procedures residing in the database. Like `PreparedStatement`, it can also use input parameters (`IN`), but it additionally supports output parameters (`OUT`) and input/output parameters (`INOUT`).

**Use Case:** Exclusively for calling database stored procedures.

**Example:**

```java
String sql = "{call calculate_employee_bonus(?, ?)}";
CallableStatement cstmt = connection.prepareCall(sql);
cstmt.setInt(1, employeeId); // Set IN parameter
cstmt.registerOutParameter(2, Types.DOUBLE); // Register OUT parameter
cstmt.execute();
double bonus = cstmt.getDouble(2); // Retrieve the value of the OUT parameter
```

## 3. Comparison of Statement Types

| Feature             | Statement                   | PreparedStatement               | CallableStatement                                    |
| :------------------ | :-------------------------- | :------------------------------ | :--------------------------------------------------- |
| **SQL Nature**      | Static                      | Precompiled, Parameterized      | For stored procedures                                |
| **Performance**     | Good for single use         | Excellent for repeated use      | Varies                                               |
| **Security**        | Vulnerable to SQL Injection | Secure (prevents SQL Injection) | Secure                                               |
| **Use Case**        | Simple, one-time queries    | Parameterized, repeated queries | Executing stored procedures                          |
| **Parameter Types** | N/A                         | Input (`IN`) only               | Input (`IN`), Output (`OUT`), Input/Output (`INOUT`) |

## 4. Executing Queries and Updates

The type of SQL command you execute determines which method you call on the Statement object.

| Method                      | Return Type | Use For                                                                                                                                                 |
| :-------------------------- | :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `executeQuery(String sql)`  | `ResultSet` | `SELECT` statements (queries that return data).                                                                                                         |
| `executeUpdate(String sql)` | `int`       | `INSERT`, `UPDATE`, `DELETE`, `DDL` (e.g., `CREATE TABLE`) statements. Returns the number of rows affected.                                             |
| `execute(String sql)`       | `boolean`   | General-purpose execution, often for statements that return multiple result sets or update counts. Returns `true` if the first result is a `ResultSet`. |

**Example Usage:**

```java
// Execute a SELECT query
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT id, name FROM users");

// Execute an INSERT update
PreparedStatement pstmt = conn.prepareStatement("INSERT INTO users (name, email) VALUES (?, ?)");
pstmt.setString(1, "Alice");
pstmt.setString(2, "alice@example.com");
int count = pstmt.executeUpdate(); // 'count' will be 1
```

## 5. Understanding the ResultSet Object

A `ResultSet` object is a table of data representing the result set of a database query. It maintains a cursor pointing to its current row of data. Initially, the cursor is positioned **before the first row**. You must call the `next()` method to move the cursor to the first row.

### 5.1. Navigating Through a ResultSet

The `ResultSet` interface provides methods to move the cursor.

- `next()`: Moves the cursor to the next row. Returns `false` when there are no more rows.
- `previous()`: Moves the cursor to the previous row (requires a scroll-sensitive ResultSet).
- `first()` / `last()`: Move to the first or last row (requires a scroll-sensitive ResultSet).
- `absolute(int row)`: Moves to a specific row number (requires a scroll-sensitive ResultSet).
- `relative(int rows)`: Moves the cursor a relative number of rows (requires a scroll-sensitive ResultSet).

**Basic Navigation Loop:**

```java
ResultSet rs = stmt.executeQuery("SELECT * FROM Employees");
while (rs.next()) { // Move to the next row until none are left
    // Retrieve data from the current row
    int id = rs.getInt("id");
    String name = rs.getString("name");
    System.out.println(id + ": " + name);
}
```

### 5.2. Retrieving Data from a ResultSet

You retrieve data using getter methods named `getXxx()`, where `Xxx` is the data type (e.g., `Int`, `String`, `Double`). These methods can take either a **column name** (String) or a **column index** (int, starting from 1) as an argument.

**Example:**

```java
// Using column name (more readable, less fragile if schema changes)
String email = rs.getString("email");

// Using column index (slightly faster, but fragile)
double salary = rs.getDouble(5); // Gets the 5th column in the SELECT list
```

### 5.3. Types and Concurrency of ResultSet

When creating a Statement, you can specify the **type** and **concurrency** of the ResultSet it will produce.

- **ResultSet Type:**
  - `TYPE_FORWARD_ONLY`: The default. The cursor can only move forward.
  - `TYPE_SCROLL_INSENSITIVE`: The cursor can scroll forwards and backwards, but is not sensitive to changes made by others to the database while it is open.
  - `TYPE_SCROLL_SENSITIVE`: The cursor can scroll and is sensitive to changes made by others.

- **ResultSet Concurrency:**
  - `CONCUR_READ_ONLY`: The default. The ResultSet cannot be updated.
  - `CONCUR_UPDATABLE`: The ResultSet can be updated, and changes can be persisted back to the database.

**Creating a Scrollable, Updatable ResultSet:**

```java
Statement stmt = connection.createStatement(
    ResultSet.TYPE_SCROLL_INSENSITIVE,
    ResultSet.CONCUR_UPDATABLE
);
ResultSet rs = stmt.executeQuery("SELECT * FROM Products");
rs.absolute(3); // Move to the 3rd row
rs.updateDouble("price", 39.99); // Update the 'price' column in memory
rs.updateRow(); // Persist the update to the database
```

## 6. ASCII Diagram: JDBC Data Retrieval Flow

```
+----------------+      +-------------+      +-----------------+      +-----------+
| Java Application|      | Statement   |      |   Database      |      | ResultSet |
|                |      |   Object    |      |    Server       |      |   Object  |
+----------------+      +-------------+      +-----------------+      +-----------+
        |                     |                     |                     |
        | 1. createStatement()|                     |                     |
        |-------------------->|                     |                     |
        |                     |                     |                     |
        | 2. executeQuery(...)|                     |                     |
        |-------------------->| 3. Send SQL Query   |                     |
        |                     |-------------------->|                     |
        |                     |                     | 4. Execute Query &  |
        |                     |                     |    Build Result Set|
        |                     |                     |---------------------|
        |                     | 5. Return ResultSet |                     |
        |                     |<--------------------|                     |
        | 6. Return ResultSet |                     |                     |
        |<--------------------|                     |                     |
        |                     |                     |                     |
        | 7. rs.next()        |                     |                     |
        |---> (moves cursor)  |                     |                     |
        | 8. rs.getInt("id")  |                     |                     |
        |---> (fetches data)  |                     |                     |
        |                     |                     |                     |
```

## 7. Key Exceptions

- `SQLException`: The base exception for almost all JDBC-related errors. It provides database-specific error codes (`getErrorCode()`) and SQLState strings (`getSQLState()`).
- `SQLSyntaxErrorException`: A subclass of `SQLException` thrown when there is a syntax error in your SQL statement.
- `DataTruncation`: Exception thrown when a data value is truncated during a read or write operation.

**Best Practice:** Always use try-with-resources to ensure `Connection`, `Statement`, and `ResultSet` objects are closed automatically, preventing resource leaks.

```java
try (Connection conn = DriverManager.getConnection(url, user, pass);
     PreparedStatement pstmt = conn.prepareStatement(sql)) {
    pstmt.setString(1, "value");
    try (ResultSet rs = pstmt.executeQuery()) {
        while (rs.next()) {
            // Process results
        }
    } // ResultSet auto-closed here
} // Connection and PreparedStatement auto-closed here
```

## 8. Exam Tips

1.  **PreparedStatement vs. Statement:** Always prefer `PreparedStatement` over a simple `Statement` for any user-input-driven query. Remember it's for performance (precompilation) and security (prevents SQL injection).
2.  **Cursor Initial Position:** The `ResultSet` cursor starts **before the first row**. You **must** call `next()` at least once to access data.
3.  **Column Index Starts at 1:** The column index in methods like `getString(1)` is 1-based, not 0-based.
4.  **Resource Management:** Be able to identify code that correctly uses try-with-resources to close JDBC objects. This is a very common exam topic.
5.  **Method Return Types:** Know which `execute` method to use:
    - `executeQuery()` for `SELECT` -> returns `ResultSet`.
    - `executeUpdate()` for `INSERT/UPDATE/DELETE` -> returns `int` (row count).
    - `execute()` for anything -> returns `boolean` (`true` if a `ResultSet` is available).
