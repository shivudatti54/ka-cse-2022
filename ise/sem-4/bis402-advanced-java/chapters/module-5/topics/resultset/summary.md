# ResultSet Revision Notes

### Definition and Concept

- A ResultSet is a data structure that represents a set of records from the database.
- It is a cursor-based object, meaning it keeps track of the current record being processed.

### Types of ResultSet

- **Forward Only**: allows traversal in only one direction (from first to last record).
- **Scrollable**: allows traversal in both forward and backward directions.
- **Updatable**: allows updating of records.

### Methods and Operations

- **next()**: moves the cursor to the next record.
- **previous()**: moves the cursor to the previous record.
- **last()**: moves the cursor to the last record.
- **first()**: moves the cursor to the first record.
- **absolute(int)**: moves the cursor to a specific record position.
- **relative(int)**: moves the cursor a specified number of records.

### Close and Finalize

- **close()**: releases system resources associated with the ResultSet.
- **finalize()**: called before closing the ResultSet to release any remaining resources.

### ResultSet Types

- **Statement ResultSet**: returns records from a single statement.
- **Query Result**: returns records from a query.

### Important Formulas and Theorems

- None specific to ResultSet, but understanding SQL queries and database concepts is essential.

### Key Formulas

- None specific to ResultSet, but understanding SQL queries and database concepts is essential.

### Key Terms

- Cursor: a pointer to the current record being processed.
- Record: a single row in a database table.
- Statement: a SQL query or instruction sent to the database.
