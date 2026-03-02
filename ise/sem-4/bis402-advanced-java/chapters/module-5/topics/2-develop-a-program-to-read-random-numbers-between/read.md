# **Study Material: Developing a Program to Read Random Numbers between a Given Range that are Multiples of 2 and 5**

## **Introduction**

In this topic, we will learn how to develop a Java program to read random numbers between a given range that are multiples of 2 and 5. We will explore the concept of JDBC, JDBC driver types, and JDBC packages, and apply our knowledge to create a simple program that meets the requirements.

## **What are JDBC, JDBC Driver Types, and JDBC Packages?**

### JDBC (Java Database Connectivity)

JDBC is a Java API that allows Java applications to connect to a relational database management system (RDBMS) and perform CRUD (Create, Read, Update, Delete) operations. JDBC provides a way to interact with databases using a Java-based interface.

### JDBC Driver Types

There are two types of JDBC drivers:

- **Type 1 JDBC Driver**: A Type 1 JDBC driver is a server-side driver that resides on the database server. It translates JDBC calls into the corresponding SQL commands and executes them on the database server.
- **Type 2 JDBC Driver**: A Type 2 JDBC driver is a client-side driver that resides on the client (Java application). It translates JDBC calls into the corresponding SQL commands and executes them on the database server remotely.

### JDBC Packages

JDBC provides several packages that support different database connections:

- **java.sql**: This package provides the basic classes for JDBC, such as `Connection`, `Statement`, and `ResultSet`.
- **com.mysql.jdbc**: This package provides the JDBC driver for MySQL databases.
- **oracle.jdbc**: This package provides the JDBC driver for Oracle databases.

## **Developing a Program to Read Random Numbers between a Given Range that are Multiples of 2 and 5**

### Problem Statement

Develop a Java program that reads random numbers between a given range (e.g., 1 to 100) that are multiples of 2 and 5.

### Solution

We will use the `java.util.Random` class to generate random numbers and the `java.sql` package to connect to a database (in this case, an in-memory SQLite database).

```java
import java.sql.*;
import java.util.Random;

public class MultipleOf2And5 {
    public static void main(String[] args) {
        // Create an in-memory SQLite database
        Connection conn = JDBCUtils.createConnection("jdbc:sqlite:random_numbers.db");

        // Create a statement object
        Statement stmt = conn.createStatement();

        // Generate random numbers between 1 and 100
        Random rand = new Random();
        for (int i = 1; i <= 100; i++) {
            if (rand.nextInt(20) % 2 == 0 && rand.nextInt(20) % 5 == 0) {
                // Insert the number into the database
                stmt.execute("INSERT INTO numbers (number) VALUES (" + i + ")");
            }
        }

        // Close the connection
        JDBCUtils.closeConnection(conn);
        JDBCUtils.closeStatement(stmt);

        // Read the numbers from the database
        PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM numbers");
        ResultSet rs = pstmt.executeQuery();

        while (rs.next()) {
            System.out.println(rs.getInt("number"));
        }

        // Close the result set and prepared statement
        JDBCUtils.closeResultSet(rs);
        JDBCUtils.closePreparedStatement(pstmt);

        // Close the connection
        JDBCUtils.closeConnection(conn);
    }
}

class JDBCUtils {
    public static Connection createConnection(String url) throws SQLException {
        return DriverManager.getConnection(url);
    }

    public static void closeConnection(Connection conn) throws SQLException {
        conn.close();
    }

    public static void closeStatement(Statement stmt) throws SQLException {
        stmt.close();
    }

    public static void closeResultSet(ResultSet rs) throws SQLException {
        rs.close();
    }

    public static void closePreparedStatement(PreparedStatement pstmt) throws SQLException {
        pstmt.close();
    }
}
```

### Explanation

1.  We create an in-memory SQLite database using the `jdbc:sqlite` URL.
2.  We generate random numbers between 1 and 100 using the `Random` class.
3.  We check if the generated number is a multiple of 2 and 5 using the modulo operator (`%`).
4.  If the number is a multiple of 2 and 5, we insert it into the database using a `PreparedStatement`.
5.  We read the numbers from the database using a `PreparedStatement` and `ResultSet`.
6.  We print the numbers to the console.

## **Key Concepts**

- JDBC: Java Database Connectivity
- JDBC Driver Types: Type 1 and Type 2
- JDBC Packages: `java.sql`, `com.mysql.jdbc`, and `oracle.jdbc`
- `Random` class: generates random numbers
- `Connection` class: represents a database connection
- `Statement` class: represents a SQL statement
- `ResultSet` class: represents a set of query results
- `PreparedStatement` class: represents a prepared SQL statement

## **Example Use Cases**

- Developing a program to read random numbers between a given range that are multiples of 2 and 5
- Creating a data generator for testing purposes
- Reading data from a database and performing calculations on it

## **Conclusion**

In this study material, we learned how to develop a Java program to read random numbers between a given range that are multiples of 2 and 5. We explored the concept of JDBC, JDBC driver types, and JDBC packages, and applied our knowledge to create a simple program that meets the requirements.
