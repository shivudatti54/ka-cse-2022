# Statement Objects

=====================================

## Definition

---

- A Statement object is a JDBC object that represents a SQL statement.
- It is used to execute SQL commands and retrieve data from a database.

## Properties

---

- `executeQuery()`: executes a SQL query and returns a ResultSet.
- `executeUpdate()`: executes a SQL update statement and returns the number of rows affected.
- `close()`: closes the Statement object.

## Types of Statement Objects

---

- `Statement`: the most basic type of Statement object.
- `PreparedStatement`: a Statement object that allows for parameterized queries.
- `CallableStatement`: a Statement object that can be used to execute stored procedures.

## Important Formulas

---

- `executeQuery()`: `Statement statement = connection.createStatement(); ResultSet resultSet = statement.executeQuery(query);`
- `executeUpdate()`: `Statement statement = connection.createStatement(); int rowsAffected = statement.executeUpdate(query);`

## Theorems

---

- "For every SQL statement, there is a corresponding Statement object."
- "The Statement object is used to execute SQL commands and retrieve data from a database."

## Key Points

---

- Statement objects are used to execute SQL commands.
- There are three types of Statement objects: Statement, PreparedStatement, and CallableStatement.
- Each type of Statement object has its own use case.
- Statement objects are used to retrieve data from a database.
- It is essential to close Statement objects after use to free up resources.
