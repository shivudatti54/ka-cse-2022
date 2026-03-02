# Database Connection in JDBC

## Overview

Establishing database connection is the first step in JDBC programming, involving loading the JDBC driver and using DriverManager.getConnection() to obtain a Connection object. The connection provides the communication link between Java application and database for executing SQL statements.

## Key Points

- **Load Driver**: Class.forName("com.mysql.jdbc.Driver") or automatic with JDBC 4.0+
- **Connection URL**: jdbc:mysql://hostname:port/database format
- **DriverManager.getConnection()**: Accepts URL, username, password parameters
- **Connection Object**: Represents active database session
- **createStatement()**: Create Statement object for executing queries
- **prepareStatement()**: Create PreparedStatement for parameterized queries
- **close()**: Release database and JDBC resources
- **Connection Pooling**: Reuse connections for better performance

## Important Concepts

- Connection URL syntax varies by database (MySQL, Oracle, PostgreSQL)
- Username and password for authentication
- Connection must be closed to release resources
- Try-with-resources ensures automatic closing
- Connection pooling improves performance in production

## Notes

- Remember connection URL format: jdbc:subprotocol://host:port/database
- For exams, practice complete connection code with try-catch
- Know difference between Statement and PreparedStatement creation
