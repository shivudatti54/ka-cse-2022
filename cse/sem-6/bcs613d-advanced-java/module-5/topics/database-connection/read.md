# JDBC Database Connection in Java

## Introduction to JDBC

**JDBC (Java Database Connectivity)** is an API that enables Java applications to interact with relational databases. It provides a standard set of interfaces and classes for connecting to databases, executing SQL queries, and processing results. JDBC acts as a bridge between Java applications and database management systems (DBMS) like MySQL, PostgreSQL, Oracle, SQL Server, and others.

JDBC is part of the Java Standard Edition (Java SE) platform and is included in the `java.sql` and `javax.sql` packages. It allows developers to write database-independent code that can work with different databases by simply changing the database driver.

## JDBC Architecture

### JDBC Components

1. **JDBC API**: Provides interfaces and classes for database connectivity
2. **JDBC Driver Manager**: Manages database drivers
3. **JDBC Driver**: Vendor-specific implementation for database connectivity
4. **Database**: The actual database system (MySQL, Oracle, PostgreSQL, etc.)

### JDBC Driver Types

**Type 1: JDBC-ODBC Bridge Driver**

- Translates JDBC calls to ODBC calls
- Requires ODBC driver installation
- Deprecated in Java 8

**Type 2: Native-API Driver**

- Converts JDBC calls to database-specific native calls
- Requires native library installation
- Platform-dependent

**Type 3: Network Protocol Driver**

- Uses middleware server to convert JDBC calls
- Platform-independent
- Requires middleware server setup

**Type 4: Thin Driver (Pure Java Driver)** ⭐ Most Common

- Pure Java implementation
- Directly converts JDBC calls to database-specific protocol
- Platform-independent, no additional installation required
- Best performance

## Steps to Connect to a Database

### Step 1: Import JDBC Packages

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;
```

### Step 2: Load and Register the Driver

Modern JDBC drivers (Type 4) are automatically registered. However, explicit loading can be done:

```java
// Automatic (JDBC 4.0+) - Preferred method
// Driver automatically loaded when DriverManager is used

// Explicit loading (older approach)
try {
 Class.forName("com.mysql.cj.jdbc.Driver"); // MySQL
 // Class.forName("org.postgresql.Driver"); // PostgreSQL
 // Class.forName("oracle.jdbc.driver.OracleDriver"); // Oracle
} catch (ClassNotFoundException e) {
 System.out.println("Driver not found: " + e.getMessage());
}
```

### Step 3: Establish Connection

Use `DriverManager.getConnection()` to establish a connection.

```java
String url = "jdbc:mysql://localhost:3306/mydatabase";
String username = "root";
String password = "password";

Connection connection = null;

try {
 connection = DriverManager.getConnection(url, username, password);
 System.out.println("Connected to database successfully!");
} catch (SQLException e) {
 System.out.println("Connection failed: " + e.getMessage());
}
```

### Step 4: Create Statement

```java
Statement statement = connection.createStatement();
```

### Step 5: Execute Query

```java
String sql = "SELECT * FROM students";
ResultSet resultSet = statement.executeQuery(sql);
```

### Step 6: Process Results

```java
while (resultSet.next()) {
 int id = resultSet.getInt("id");
 String name = resultSet.getString("name");
 int age = resultSet.getInt("age");
 System.out.println(id + " | " + name + " | " + age);
}
```

### Step 7: Close Resources

```java
resultSet.close();
statement.close();
connection.close();
```

## Complete JDBC Connection Example

```java
import java.sql.*;

public class JDBCExample {
 // Database connection parameters
 static final String DB_URL = "jdbc:mysql://localhost:3306/school";
 static final String USER = "root";
 static final String PASS = "password";

 public static void main(String[] args) {
 Connection conn = null;
 Statement stmt = null;
 ResultSet rs = null;

 try {
 // Step 1: Register JDBC driver (automatic in JDBC 4.0+)
 // Class.forName("com.mysql.cj.jdbc.Driver");

 // Step 2: Open a connection
 System.out.println("Connecting to database...");
 conn = DriverManager.getConnection(DB_URL, USER, PASS);
 System.out.println("Connected successfully!");

 // Step 3: Execute a query
 stmt = conn.createStatement();
 String sql = "SELECT id, name, age, grade FROM students";
 rs = stmt.executeQuery(sql);

 // Step 4: Extract data from result set
 while (rs.next()) {
 // Retrieve by column name
 int id = rs.getInt("id");
 String name = rs.getString("name");
 int age = rs.getInt("age");
 String grade = rs.getString("grade");

 // Display values
 System.out.print("ID: " + id);
 System.out.print(", Name: " + name);
 System.out.print(", Age: " + age);
 System.out.println(", Grade: " + grade);
 }

 } catch (SQLException e) {
 System.out.println("Database error: " + e.getMessage());
 e.printStackTrace();
 } finally {
 // Step 5: Clean up environment
 try {
 if (rs != null) rs.close();
 if (stmt != null) stmt.close();
 if (conn != null) conn.close();
 } catch (SQLException e) {
 e.printStackTrace();
 }
 }

 System.out.println("Connection closed.");
 }
}
```

## Connection URL Formats

### MySQL

```java
// Format: jdbc:mysql://hostname:port/database_name
String url = "jdbc:mysql://localhost:3306/school";

// With parameters
String url = "jdbc:mysql://localhost:3306/school?useSSL=false&serverTimezone=UTC";
```

### PostgreSQL

```java
// Format: jdbc:postgresql://hostname:port/database_name
String url = "jdbc:postgresql://localhost:5432/school";
```

### Oracle

```java
// Format: jdbc:oracle:thin:@hostname:port:SID
String url = "jdbc:oracle:thin:@localhost:1521:orcl";
```

### SQL Server

```java
// Format: jdbc:sqlserver://hostname:port;databaseName=database_name
String url = "jdbc:sqlserver://localhost:1433;databaseName=school";
```

### SQLite (File-based)

```java
// Format: jdbc:sqlite:path_to_database_file
String url = "jdbc:sqlite:C:/databases/school.db";
```

## DriverManager Class

The `DriverManager` class manages JDBC drivers and establishes database connections.

### Key Methods

```java
// Get connection with URL, username, password
Connection conn = DriverManager.getConnection(url, username, password);

// Get connection with Properties object
Properties props = new Properties();
props.setProperty("user", "root");
props.setProperty("password", "password");
Connection conn = DriverManager.getConnection(url, props);

// Register driver explicitly (usually not needed)
DriverManager.registerDriver(new com.mysql.cj.jdbc.Driver());

// Deregister driver
DriverManager.deregisterDriver(driver);

// Set login timeout (seconds)
DriverManager.setLoginTimeout(30);
```

## Connection Interface

The `Connection` interface represents a session with the database.

### Important Methods

```java
Connection conn = DriverManager.getConnection(url, user, pass);

// Create different types of statements
Statement stmt = conn.createStatement();
PreparedStatement pstmt = conn.prepareStatement(sql);
CallableStatement cstmt = conn.prepareCall("{call procedure_name(?)}");

// Transaction management
conn.setAutoCommit(false); // Disable auto-commit
conn.commit(); // Commit transaction
conn.rollback(); // Rollback transaction

// Get metadata
DatabaseMetaData meta = conn.getMetaData();

// Check if connection is closed
boolean isClosed = conn.isClosed();

// Close connection
conn.close();

// Set connection properties
conn.setTransactionIsolation(Connection.TRANSACTION_READ_COMMITTED);
conn.setReadOnly(false);
```

## Connection with Try-with-Resources

Modern approach that automatically closes resources:

```java
import java.sql.*;

public class ModernJDBCExample {
 public static void main(String[] args) {
 String url = "jdbc:mysql://localhost:3306/school";
 String user = "root";
 String password = "password";

 String sql = "SELECT id, name, age FROM students";

 // Try-with-resources automatically closes resources
 try (Connection conn = DriverManager.getConnection(url, user, password);
 Statement stmt = conn.createStatement();
 ResultSet rs = stmt.executeQuery(sql)) {

 System.out.println("Connected to database!");

 while (rs.next()) {
 int id = rs.getInt("id");
 String name = rs.getString("name");
 int age = rs.getInt("age");

 System.out.println(id + " | " + name + " | " + age);
 }

 } catch (SQLException e) {
 System.out.println("Error: " + e.getMessage());
 e.printStackTrace();
 }
 // Resources automatically closed here
 }
}
```

## Database Connection Utility Class

Reusable utility class for database operations:

```java
import java.sql.*;

public class DatabaseUtil {
 private static final String URL = "jdbc:mysql://localhost:3306/school";
 private static final String USER = "root";
 private static final String PASSWORD = "password";

 // Get database connection
 public static Connection getConnection() throws SQLException {
 return DriverManager.getConnection(URL, USER, PASSWORD);
 }

 // Close ResultSet
 public static void close(ResultSet rs) {
 if (rs != null) {
 try {
 rs.close();
 } catch (SQLException e) {
 e.printStackTrace();
 }
 }
 }

 // Close Statement
 public static void close(Statement stmt) {
 if (stmt != null) {
 try {
 stmt.close();
 } catch (SQLException e) {
 e.printStackTrace();
 }
 }
 }

 // Close Connection
 public static void close(Connection conn) {
 if (conn != null) {
 try {
 conn.close();
 } catch (SQLException e) {
 e.printStackTrace();
 }
 }
 }

 // Close all resources
 public static void closeAll(ResultSet rs, Statement stmt, Connection conn) {
 close(rs);
 close(stmt);
 close(conn);
 }
}

// Usage
public class Main {
 public static void main(String[] args) {
 Connection conn = null;
 Statement stmt = null;
 ResultSet rs = null;

 try {
 conn = DatabaseUtil.getConnection();
 stmt = conn.createStatement();
 rs = stmt.executeQuery("SELECT * FROM students");

 while (rs.next()) {
 System.out.println(rs.getString("name"));
 }
 } catch (SQLException e) {
 e.printStackTrace();
 } finally {
 DatabaseUtil.closeAll(rs, stmt, conn);
 }
 }
}
```

## Connection Pooling Basics

Connection pooling reuses database connections instead of creating new ones for each request, improving performance.

### Why Connection Pooling?

- Creating connections is expensive (time and resources)
- Connection pooling maintains a pool of reusable connections
- Reduces overhead of connection creation/destruction
- Improves application performance

### Simple Connection Pool Example

```java
import java.sql.*;
import java.util.*;

public class SimpleConnectionPool {
 private static final String URL = "jdbc:mysql://localhost:3306/school";
 private static final String USER = "root";
 private static final String PASSWORD = "password";
 private static final int POOL_SIZE = 10;

 private List<Connection> connectionPool;
 private List<Connection> usedConnections = new ArrayList<>();

 // Initialize connection pool
 public SimpleConnectionPool() throws SQLException {
 connectionPool = new ArrayList<>(POOL_SIZE);
 for (int i = 0; i < POOL_SIZE; i++) {
 connectionPool.add(createConnection());
 }
 }

 // Create new connection
 private Connection createConnection() throws SQLException {
 return DriverManager.getConnection(URL, USER, PASSWORD);
 }

 // Get connection from pool
 public Connection getConnection() {
 if (connectionPool.isEmpty()) {
 throw new RuntimeException("No available connections");
 }
 Connection connection = connectionPool.remove(connectionPool.size() - 1);
 usedConnections.add(connection);
 return connection;
 }

 // Return connection to pool
 public boolean releaseConnection(Connection connection) {
 connectionPool.add(connection);
 return usedConnections.remove(connection);
 }

 // Get pool size
 public int getSize() {
 return connectionPool.size() + usedConnections.size();
 }

 // Close all connections
 public void shutdown() throws SQLException {
 for (Connection conn : usedConnections) {
 conn.close();
 }
 for (Connection conn : connectionPool) {
 conn.close();
 }
 }
}

// Usage
public class Main {
 public static void main(String[] args) {
 try {
 SimpleConnectionPool pool = new SimpleConnectionPool();

 Connection conn1 = pool.getConnection();
 Connection conn2 = pool.getConnection();

 // Use connections
 Statement stmt = conn1.createStatement();
 ResultSet rs = stmt.executeQuery("SELECT * FROM students");

 // Return connections to pool
 pool.releaseConnection(conn1);
 pool.releaseConnection(conn2);

 // Shutdown pool
 pool.shutdown();

 } catch (SQLException e) {
 e.printStackTrace();
 }
 }
}
```

## Common JDBC Exceptions

### SQLException

The primary exception for JDBC operations:

```java
try {
 Connection conn = DriverManager.getConnection(url, user, pass);
} catch (SQLException e) {
 System.out.println("Error Code: " + e.getErrorCode());
 System.out.println("SQL State: " + e.getSQLState());
 System.out.println("Message: " + e.getMessage());
 e.printStackTrace();
}
```

### ClassNotFoundException

Thrown when JDBC driver class is not found:

```java
try {
 Class.forName("com.mysql.cj.jdbc.Driver");
} catch (ClassNotFoundException e) {
 System.out.println("Driver not found: " + e.getMessage());
}
```

## Best Practices for Database Connections

### 1. Always Close Resources

```java
// Use try-with-resources (preferred)
try (Connection conn = DriverManager.getConnection(url, user, pass)) {
 // Use connection
}

// Or close manually in finally block
Connection conn = null;
try {
 conn = DriverManager.getConnection(url, user, pass);
} finally {
 if (conn != null) conn.close();
}
```

### 2. Use Connection Pooling

```java
// For production applications, use connection pooling libraries
// - Apache Commons DBCP
// - HikariCP (fastest)
// - C3P0
```

### 3. Externalize Configuration

```java
// Store database credentials in properties file
Properties props = new Properties();
props.load(new FileInputStream("db.properties"));

String url = props.getProperty("db.url");
String user = props.getProperty("db.username");
String password = props.getProperty("db.password");
```

### 4. Handle Exceptions Properly

```java
try {
 // Database operations
} catch (SQLException e) {
 // Log error
 logger.error("Database error", e);
 // Notify user appropriately
 System.out.println("An error occurred while accessing the database");
}
```

### 5. Use PreparedStatement for Parameterized Queries

```java
// Avoid SQL injection
String sql = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = conn.prepareStatement(sql);
pstmt.setString(1, username);
pstmt.setString(2, password);
```

## Common Mistakes to Avoid

### 1. Not Closing Resources

```java
// Wrong: Resources not closed (memory leak)
Connection conn = DriverManager.getConnection(url, user, pass);
Statement stmt = conn.createStatement();
// Forgot to close!

// Correct: Always close resources
try (Connection conn = DriverManager.getConnection(url, user, pass);
 Statement stmt = conn.createStatement()) {
 // Use resources
} // Automatically closed
```

### 2. Creating New Connection for Each Operation

```java
// Wrong: Creates new connection every time
public void insertData() {
 Connection conn = DriverManager.getConnection(url, user, pass);
 // Insert data
 conn.close();
}

// Correct: Use connection pooling or reuse connection
```

### 3. Hardcoding Database Credentials

```java
// Wrong: Hardcoded credentials
String url = "jdbc:mysql://localhost:3306/school";
String user = "root";
String password = "mypassword123";

// Correct: Use configuration file or environment variables
```

### 4. Not Handling Exceptions

```java
// Wrong: No exception handling
Connection conn = DriverManager.getConnection(url, user, pass);

// Correct: Handle exceptions
try {
 Connection conn = DriverManager.getConnection(url, user, pass);
} catch (SQLException e) {
 e.printStackTrace();
}
```

## Exam Tips

1. **Know the steps**: Memorize the 7 steps to connect to a database
2. **DriverManager.getConnection()**: Know the syntax and parameters
3. **Connection URL format**: Remember the format for different databases (especially MySQL)
4. **Import statements**: Remember `java.sql.*` package
5. **Resource closing**: Always close ResultSet, Statement, and Connection (in that order)
6. **Try-with-resources**: Understand how it automatically closes resources
7. **SQLException**: Know how to catch and handle it
8. **Connection interface methods**: `createStatement()`, `setAutoCommit()`, `commit()`, `rollback()`
9. **JDBC driver types**: Type 4 (Thin driver) is most commonly used
10. **Connection pooling**: Understand the concept and benefits

**Sample Exam Questions:**

- Write code to establish a database connection
- List and explain the steps for database connectivity
- Write the MySQL connection URL format
- Create a utility class for database operations
- Handle SQLException properly
- Close database resources correctly
- Explain the importance of connection pooling
- Compare different JDBC driver types

### Further Reading

Refer to your prescribed textbook and official course materials.
