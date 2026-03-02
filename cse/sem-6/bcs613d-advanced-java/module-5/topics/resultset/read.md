# ResultSet

### Definition and Overview

A ResultSet is a collection of data that is retrieved from a database query. It is an interface provided by the JDBC (Java Database Connectivity) API that allows Java programs to access and manipulate data in a database. The ResultSet is a cursor-based interface, meaning it keeps track of the current position in the result set.

### Types of ResultSets

There are two main types of ResultSets:

- **Forward Only ResultSets**: These are the most commonly used type of ResultSet. They allow you to iterate through the result set in a single direction, either forward or backward.
- **Scrollable ResultSets**: These allow you to scroll through the result set in both forward and backward directions, giving you more control over how you access the data.

### ResultSet Methods

Here are some key methods used to manipulate a ResultSet:

- **next()**: Moves the cursor to the next row in the result set. Returns true if there is a next row, false otherwise.
- **previous()**: Moves the cursor to the previous row in the result set. Returns true if there is a previous row, false otherwise.
- **absolute(int index)**: Moves the cursor to the specified row in the result set. Returns true if the row exists, false otherwise.
- **relative(int rows)**: Moves the cursor the specified number of rows in the result set. Returns true if the row exists, false otherwise.
- **after last()**: Moves the cursor to the row after the last row in the result set. Returns true if there is a next row, false otherwise.
- **before first()**: Moves the cursor to the row before the first row in the result set. Returns true if there is a previous row, false otherwise.
- **last()**: Moves the cursor to the last row in the result set. Returns true if there is a next row, false otherwise.
- **before first()**: Moves the cursor to the row before the first row in the result set. Returns true if there is a previous row, false otherwise.

### ResultSet Metadata

The following methods are used to retrieve metadata about the ResultSet:

- **getMetaData()**: Returns the metadata for the ResultSet.
- **getColumnCount()**: Returns the number of columns in the ResultSet.
- **getMetaData().getColumnSize(index)**: Returns the size of the specified column.
- **getMetaData().getColumnLabel(index)**: Returns the label of the specified column.
- **getMetaData().getColumnTypeName(index)**: Returns the type of the specified column.
- **getMetaData().getSchemaName(index)**: Returns the schema name of the specified column.
- **getMetaData().getCatalogName(index)**: Returns the catalog name of the specified column.

### Example Code

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class ResultSetExample {
 public static void main(String[] args) {
 // Establish a connection to the database
 Connection conn = null;
 try {
 conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "username", "password");
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }

 // Create a statement object
 Statement stmt = null;
 try {
 stmt = conn.createStatement();
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }

 // Execute a query
 ResultSet rs = null;
 try {
 rs = stmt.executeQuery("SELECT * FROM mytable");
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }

 // Print the metadata for the ResultSet
 try {
 System.out.println("Column Count: " + rs.getMetaData().getColumnCount());
 System.out.println("Column Size: " + rs.getMetaData().getColumnSize(1));
 System.out.println("Column Label: " + rs.getMetaData().getColumnLabel(1));
 System.out.println("Column Type Name: " + rs.getMetaData().getColumnTypeName(1));
 System.out.println("Schema Name: " + rs.getMetaData().getSchemaName(1));
 System.out.println("Catalog Name: " + rs.getMetaData().getCatalogName(1));
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }

 // Iterate through the ResultSet
 try {
 while (rs.next()) {
 System.out.println(rs.getString(1) + " " + rs.getString(2));
 }
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }

 // Close the ResultSet, Statement, and Connection
 try {
 rs.close();
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }
 try {
 stmt.close();
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }
 try {
 conn.close();
 } catch (SQLException e) {
 System.out.println(e.getMessage());
 }
 }
}
```

This example code demonstrates the use of a ResultSet to retrieve data from a database table, as well as how to access and manipulate the metadata for the ResultSet.
