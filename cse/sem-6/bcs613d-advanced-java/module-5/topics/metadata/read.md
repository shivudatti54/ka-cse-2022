# Metadata and Exception Handling in JDBC

## Introduction to JDBC Metadata

JDBC (Java Database Connectivity) provides a standard API for connecting Java applications to relational databases. Beyond basic CRUD (Create, Read, Update, Delete) operations, JDBC offers powerful metadata capabilities that allow developers to discover database structure information programmatically. Additionally, proper exception handling is crucial for building robust database applications.

**Metadata** refers to "data about data" - information that describes the structure and properties of the database itself rather than the actual data stored in it.

## Database Metadata

### What is DatabaseMetaData?

The `DatabaseMetaData` interface provides comprehensive information about the database as a whole. This includes information about database product name and version, supported features, schema information, and more.

```java
Connection conn = DriverManager.getConnection(url, user, password);
DatabaseMetaData dbMetaData = conn.getMetaData();

System.out.println("Database: " + dbMetaData.getDatabaseProductName());
System.out.println("Version: " + dbMetaData.getDatabaseProductVersion());
System.out.println("Driver: " + dbMetaData.getDriverName());
```

### Key Methods of DatabaseMetaData

| Method                        | Description                          | Return Type |
| ----------------------------- | ------------------------------------ | ----------- |
| `getDatabaseProductName()`    | Returns database product name        | String      |
| `getDatabaseProductVersion()` | Returns database version             | String      |
| `getDriverName()`             | Returns JDBC driver name             | String      |
| `getDriverVersion()`          | Returns JDBC driver version          | String      |
| `getURL()`                    | Returns database connection URL      | String      |
| `getUserName()`               | Returns database username            | String      |
| `supportsTransactions()`      | Checks if transactions are supported | boolean     |
| `getTables()`                 | Returns information about tables     | ResultSet   |
| `getColumns()`                | Returns information about columns    | ResultSet   |

### Retrieving Table Information

```java
DatabaseMetaData metaData = connection.getMetaData();
ResultSet tables = metaData.getTables(null, null, "%", new String[]{"TABLE"});

while (tables.next()) {
 String tableName = tables.getString("TABLE_NAME");
 String tableType = tables.getString("TABLE_TYPE");
 System.out.println("Table: " + tableName + " Type: " + tableType);
}
```

### Retrieving Column Information

```java
ResultSet columns = metaData.getColumns(null, null, "employees", "%");

while (columns.next()) {
 String columnName = columns.getString("COLUMN_NAME");
 String dataType = columns.getString("TYPE_NAME");
 int columnSize = columns.getInt("COLUMN_SIZE");
 System.out.println("Column: " + columnName + " Type: " + dataType + " Size: " + columnSize);
}
```

## ResultSet Metadata

### What is ResultSetMetaData?

The `ResultSetMetaData` interface provides information about the columns in a `ResultSet` object, such as column count, names, types, and properties.

```java
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("SELECT * FROM employees");
ResultSetMetaData rsMetaData = rs.getMetaData();

int columnCount = rsMetaData.getColumnCount();
System.out.println("Number of columns: " + columnCount);

for (int i = 1; i <= columnCount; i++) {
 System.out.println("Column " + i + ": " + rsMetaData.getColumnName(i));
 System.out.println("Type: " + rsMetaData.getColumnTypeName(i));
}
```

### Key Methods of ResultSetMetaData

| Method                             | Description                        | Return Type |
| ---------------------------------- | ---------------------------------- | ----------- |
| `getColumnCount()`                 | Returns number of columns          | int         |
| `getColumnName(int column)`        | Returns column name                | String      |
| `getColumnTypeName(int column)`    | Returns column type name           | String      |
| `getColumnDisplaySize(int column)` | Returns column display size        | int         |
| `isNullable(int column)`           | Checks if column allows NULL       | int         |
| `isAutoIncrement(int column)`      | Checks if column is auto-increment | boolean     |
| `getTableName(int column)`         | Returns source table name          | String      |

### Practical Example: Dynamic Result Processing

```java
public void displayResultSet(ResultSet rs) throws SQLException {
 ResultSetMetaData metaData = rs.getMetaData();
 int columnCount = metaData.getColumnCount();

 // Print column headers
 for (int i = 1; i <= columnCount; i++) {
 System.out.printf("%-20s", metaData.getColumnName(i));
 }
 System.out.println();

 // Print data rows
 while (rs.next()) {
 for (int i = 1; i <= columnCount; i++) {
 System.out.printf("%-20s", rs.getString(i));
 }
 System.out.println();
 }
}
```

## Parameter Metadata

### What is ParameterMetaData?

The `ParameterMetaData` interface provides information about the parameters in a `PreparedStatement` object.

```java
PreparedStatement pstmt = conn.prepareStatement(
 "INSERT INTO employees (id, name, salary) VALUES (?, ?, ?)");
ParameterMetaData paramMetaData = pstmt.getParameterMetaData();

int paramCount = paramMetaData.getParameterCount();
System.out.println("Number of parameters: " + paramCount);

for (int i = 1; i <= paramCount; i++) {
 System.out.println("Parameter " + i + " type: " +
 paramMetaData.getParameterTypeName(i));
}
```

### Key Methods of ParameterMetaData

| Method                            | Description                             | Return Type |
| --------------------------------- | --------------------------------------- | ----------- |
| `getParameterCount()`             | Returns number of parameters            | int         |
| `getParameterTypeName(int param)` | Returns parameter type name             | String      |
| `getParameterMode(int param)`     | Returns parameter mode (IN, OUT, INOUT) | int         |
| `isNullable(int param)`           | Checks if parameter can be NULL         | boolean     |

## JDBC Exception Handling

### SQLException Hierarchy

JDBC uses the `SQLException` class to handle database-related errors. The exception hierarchy includes:

```
Throwable
 └── Exception
 └── SQLException
 ├── SQLWarning
 ├── BatchUpdateException
 └── DataTruncation
```

### Handling SQLExceptions

```java
try {
 Connection conn = DriverManager.getConnection(url, user, password);
 Statement stmt = conn.createStatement();
 ResultSet rs = stmt.executeQuery("SELECT * FROM non_existent_table");
 // Process results
} catch (SQLException e) {
 System.err.println("SQL State: " + e.getSQLState());
 System.err.println("Error Code: " + e.getErrorCode());
 System.err.println("Message: " + e.getMessage());
 e.printStackTrace();
}
```

### SQLException Methods

| Method               | Description                                         |
| -------------------- | --------------------------------------------------- |
| `getSQLState()`      | Returns SQLState code (X/Open or SQL:2003 standard) |
| `getErrorCode()`     | Returns vendor-specific error code                  |
| `getMessage()`       | Returns error description                           |
| `getNextException()` | Returns next exception in chain                     |

### SQL Warnings

SQL warnings don't stop execution but indicate potential issues:

```java
Connection conn = // get connection
SQLWarning warning = conn.getWarnings();
while (warning != null) {
 System.out.println("Warning: " + warning.getMessage());
 warning = warning.getNextWarning();
}
```

### BatchUpdateException

Thrown when a batch update operation fails:

```java
try {
 Statement stmt = conn.createStatement();
 stmt.addBatch("INSERT INTO table1 VALUES (1)");
 stmt.addBatch("INSERT INTO table2 VALUES (2)");
 int[] updateCounts = stmt.executeBatch();
} catch (BatchUpdateException e) {
 int[] updateCounts = e.getUpdateCounts();
 System.out.println("Failed at update: " + updateCounts.length);
}
```

### DataTruncation

Occurs when data is truncated during read or write operations:

```java
try {
 PreparedStatement pstmt = conn.prepareStatement(
 "INSERT INTO employees (name) VALUES (?)");
 pstmt.setString(1, veryLongString); // Might be truncated
 pstmt.executeUpdate();
} catch (DataTruncation e) {
 System.out.println("Data truncated: " + e.getMessage());
 System.out.println("Data size: " + e.getDataSize());
 System.out.println("Transfer size: " + e.getTransferSize());
}
```

## Best Practices for Exception Handling

### 1. Use Try-With-Resources

```java
try (Connection conn = DriverManager.getConnection(url, user, password);
 Statement stmt = conn.createStatement();
 ResultSet rs = stmt.executeQuery("SELECT * FROM employees")) {

 while (rs.next()) {
 // Process results
 }
} catch (SQLException e) {
 // Handle exception
}
```

### 2. Proper Resource Cleanup

```java
Connection conn = null;
Statement stmt = null;
ResultSet rs = null;

try {
 conn = DriverManager.getConnection(url, user, password);
 stmt = conn.createStatement();
 rs = stmt.executeQuery("SELECT * FROM employees");
 // Process results
} catch (SQLException e) {
 // Handle exception
} finally {
 try { if (rs != null) rs.close(); } catch (SQLException e) { /* log */ }
 try { if (stmt != null) stmt.close(); } catch (SQLException e) { /* log */ }
 try { if (conn != null) conn.close(); } catch (SQLException e) { /* log */ }
}
```

### 3. Transaction Rollback

```java
try {
 conn.setAutoCommit(false);
 // Execute multiple statements
 conn.commit();
} catch (SQLException e) {
 try {
 conn.rollback();
 } catch (SQLException rollbackEx) {
 // Handle rollback exception
 }
 // Handle original exception
} finally {
 conn.setAutoCommit(true);
}
```

## Real-World Applications of Metadata

### 1. Database Exploration Tools

```java
public void exploreDatabase(Connection conn) throws SQLException {
 DatabaseMetaData dbMeta = conn.getMetaData();

 // Get all tables
 ResultSet tables = dbMeta.getTables(null, null, "%", null);
 while (tables.next()) {
 String tableName = tables.getString("TABLE_NAME");
 exploreTable(conn, tableName);
 }
}

private void exploreTable(Connection conn, String tableName) throws SQLException {
 DatabaseMetaData dbMeta = conn.getMetaData();
 ResultSet columns = dbMeta.getColumns(null, null, tableName, "%");

 System.out.println("Table: " + tableName);
 while (columns.next()) {
 System.out.println(" Column: " + columns.getString("COLUMN_NAME") +
 " Type: " + columns.getString("TYPE_NAME"));
 }
}
```

### 2. Dynamic Form Generation

```java
public Map<String, String> getFormFields(String tableName) throws SQLException {
 Map<String, String> fields = new HashMap<>();
 DatabaseMetaData metaData = connection.getMetaData();
 ResultSet columns = metaData.getColumns(null, null, tableName, "%");

 while (columns.next()) {
 String columnName = columns.getString("COLUMN_NAME");
 String columnType = columns.getString("TYPE_NAME");
 fields.put(columnName, mapToHtmlInputType(columnType));
 }
 return fields;
}
```

### 3. Data Validation

```java
public void validateInsert(Connection conn, String tableName,
 Map<String, Object> values) throws SQLException {
 DatabaseMetaData metaData = conn.getMetaData();
 ResultSet columns = metaData.getColumns(null, null, tableName, "%");

 while (columns.next()) {
 String columnName = columns.getString("COLUMN_NAME");
 int isNullable = columns.getInt("NULLABLE");
 int columnSize = columns.getInt("COLUMN_SIZE");

 if (values.containsKey(columnName)) {
 Object value = values.get(columnName);
 // Validate null constraints
 if (value == null && isNullable == DatabaseMetaData.columnNoNulls) {
 throw new SQLException("Column " + columnName + " cannot be null");
 }
 // Validate size constraints
 if (value instanceof String && ((String) value).length() > columnSize) {
 throw new SQLException("Value too long for column " + columnName);
 }
 }
 }
}
```

## ASCII Diagram: JDBC Metadata Flow

```
Application Code
 │
 │ 1. getMetaData()
 ▼
DatabaseMetaData/ResultSetMetaData
 │
 │ 2. Query metadata information
 ▼
Database Management System
 │
 │ 3. Return metadata results
 ▼
ResultSet (metadata information)
 │
 │ 4. Process metadata
 ▼
Dynamic application behavior
```

## Exam Tips

1. **Remember the three types of metadata**: DatabaseMetaData, ResultSetMetaData, and ParameterMetaData
2. **SQLException provides multiple error details**: SQLState, error code, and message
3. **Use try-with-resources** for automatic resource management in modern Java code
4. **Always check for SQL warnings** after database operations
5. **BatchUpdateException** contains update counts for successful operations before failure
6. **DataTruncation** can occur during both read and write operations
7. **Metadata operations can be expensive** - cache results when possible
8. **Different databases may return different metadata** - test with your target database
