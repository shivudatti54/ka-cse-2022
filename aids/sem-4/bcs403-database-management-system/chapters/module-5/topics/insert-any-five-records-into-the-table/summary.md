# **Database Management System Revision Notes**

## **Topic: Inserting Records into a Table**

### Key Points

- **Insert Statement**: Used to add new records to a table.
- **INSERT INTO**: Keyword used to specify the table name.
- **SELECT**: Clause used to specify the columns to be inserted.
- **VALUES**: Clause used to specify the values to be inserted.
- **Tuple**: A set of values inserted into a table.

### Formula/Definition/ Theorem

- **Insertion Rule**: INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...).
- **SQL Syntax**: INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...).

### Important Notes

- **Primary Key**: A unique identifier for each record.
- **Foreign Key**: A reference to the primary key of another table.
- **Join**: Used to combine records from two or more tables.

### Example

| Table Name: Employees |
| --------------------- | --------- | ------ |
| Employee ID (PK)      | Name      | Salary |
| 1                     | John Doe  | 50000  |
| 2                     | Jane Doe  | 60000  |
| 3                     | Bob Smith | 70000  |

INSERT INTO Employees (Name, Salary) VALUES ('Mike Brown', 80000);

### Quick Revision Tips

- Practice writing INSERT statements.
- Understand the importance of primary keys and foreign keys.
- Familiarize yourself with the SQL syntax.
