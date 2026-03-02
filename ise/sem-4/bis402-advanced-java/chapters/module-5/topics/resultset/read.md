# ResultSet Study Material

### Introduction

A ResultSet is a collection of data retrieved from a database using JDBC. It's an object that stores the result of a SQL query. The ResultSet is an iterator, meaning that it allows you to traverse through the records and access their values.

### Definition

- ResultSet is a Java object that holds the result of a SQL query.
- It's a collection of data that can be accessed using various methods.

### Types of ResultSet

- **Forward Only**: The user can only move forward in the result set.
- **Forward and Backward**: The user can move both forward and backward in the result set.
- **Static**: The user can't move backward in the result set.

### Creating a ResultSet

- A ResultSet can be created using the `executeQuery()` method.
- The `executeQuery()` method returns a ResultSet object.

### ResultSet Methods

- **next()**: Moves the cursor to the next row in the result set.
- **previous()**: Moves the cursor to the previous row in the result set.
- **last()**: Moves the cursor to the last row in the result set.
- **first()**: Moves the cursor to the first row in the result set.
- **absolute(int)**: Moves the cursor to the specified row.
- \*\*relative(int)`: Moves the cursor to the specified row.

### Accessing ResultSet Values

- **getInt()**: Returns the value of the column as an integer.
- **getString()**: Returns the value of the column as a string.
- **getBoolean()**: Returns the value of the column as a boolean.
- **getBigDecimal()**: Returns the value of the column as a BigDecimal.

### Caching ResultSet

- ResultSet is an iterator and it doesn't cache the data it returns.
- To cache the data, you need to store the data in a collection.

### Best Practices

- Always close the ResultSet after use to avoid resource leaks.
- Use `ResultSet.close()` method to close the ResultSet.
- Always check for `ResultSet.next()` before accessing values in the ResultSet.

### Example

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class ResultSetExample {
    public static void main(String[] args) {
        // Establish a connection to the database
        Connection con = null;
        try {
            con = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "username", "password");
        } catch (SQLException e) {
            System.out.println("Error connecting to database: " + e.getMessage());
            return;
        }

        // Create a statement object
        Statement stmt = null;
        try {
            stmt = con.createStatement();
        } catch (SQLException e) {
            System.out.println("Error creating statement: " + e.getMessage());
            return;
        }

        // Create a ResultSet
        ResultSet rs = null;
        try {
            rs = stmt.executeQuery("SELECT * FROM mytable");
        } catch (SQLException e) {
            System.out.println("Error querying database: " + e.getMessage());
            return;
        }

        // Iterate through the ResultSet
        while (rs.next()) {
            System.out.println(rs.getString("column1") + " " + rs.getString("column2"));
        }

        // Close the ResultSet
        try {
            rs.close();
        } catch (SQLException e) {
            System.out.println("Error closing ResultSet: " + e.getMessage());
        }

        // Close the statement object
        try {
            stmt.close();
        } catch (SQLException e) {
            System.out.println("Error closing statement: " + e.getMessage());
        }

        // Close the connection object
        try {
            con.close();
        } catch (SQLException e) {
            System.out.println("Error closing connection: " + e.getMessage());
        }
    }
}
```

### Conclusion

In this study material, we covered the concept of ResultSet, its types, methods, and best practices. We also provided an example of how to use a ResultSet to retrieve and iterate through data from a database. By following the guidelines and examples provided, you should be able to effectively use ResultSet in your Java applications.
