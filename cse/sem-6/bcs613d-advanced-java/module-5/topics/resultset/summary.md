# ResultSet Summary

### Overview

- A ResultSet is a read-only record set that contains the result of a SQL query.
- It is used to traverse the result set of a SQL query and retrieve the data.

### Key Points

- **Types of Result Sets**:
  - `ResultSet`: a read-only record set.
  - `Statement.HashSetResult`: a read-only record set with a set data type.
  - `Statement.fetchallResult`: a read-only record set with a fetch-all data type.
- **Methods**:
  - `next()`: moves to the next row in the result set.
  - `previous()`: moves to the previous row in the result set.
  - `last()`: moves to the last row in the result set.
  - `beforeFirst()`: moves to the first row in the result set.
  - `isBeforeFirst()`: checks if the result set has a row before the first row.
  - `isAfterLast()`: checks if the result set has a row after the last row.
  - `isClosed()`: checks if the result set is closed.
- **Types of Result Set Fetching**:
  - `ResultSet.FETCH_SCROLL`: a row-by-row fetch.
  - `ResultSet.FETCH_STREAM`: a stream-based fetch.
- **Important Formulas and Theorems**:
  - `ResultSet.next()`: `next()` method is used to move to the next row in the result set.
  - `ResultSet.last()`: `last()` method is used to move to the last row in the result set.

### Example Use Cases

- Creating a `Statement` object and executing a SQL query.
- Using `ResultSet` to retrieve the result of a SQL query.
- Using `ResultSet` to iterate over the rows of a result set.

### Key Terms

- **SQL Query**: a request to retrieve data from a database.
- **Database**: a collection of organized data.
- **ResultSet**: a read-only record set that contains the result of a SQL query.
