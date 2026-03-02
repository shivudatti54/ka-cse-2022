# DML: SELECT, INSERT, UPDATE, DELETE
## Database Management Systems (DU NEP 2024 UGCF)

### Introduction
Data Manipulation Language (DML) is a subset of SQL used to insert, modify, retrieve, and delete data in relational databases. These commands form the foundation of database interaction and are essential for managing data within DBMS. For Delhi University's BSc (Hons) Computer Science NEP 2024 curriculum, understanding DML operations is crucial for practical database handling.

---

### SELECT Statement
The SELECT statement retrieves data from one or more tables:

- **Basic Syntax**: `SELECT column1, column2 FROM table_name;`
- **Projection**: Selecting specific columns
- **Selection**: Filtering rows using WHERE clause
- **Wildcards**: Using `*` to select all columns
- **DISTINCT**: Removing duplicate values
- **ORDER BY**: Sorting results (ASC/DESC)
- **GROUP BY**: Grouping rows for aggregate functions
- **HAVING**: Filtering grouped data
- **Aggregate Functions**: COUNT, SUM, AVG, MAX, MIN
- **Joins**: INNER, LEFT, RIGHT, FULL joins to combine tables

---

### INSERT Statement
Adds new records to a table:

- **Single Row**: `INSERT INTO table (col1, col2) VALUES (val1, val2);`
- **Multiple Rows**: `INSERT INTO table VALUES (...), (...), (...);`
- **INSERT INTO...SELECT**: Copy data from other tables
- **Column Order**: Can omit columns if values match table structure

---

### UPDATE Statement
Modifies existing data in a table:

- **Basic Syntax**: `UPDATE table SET column = value WHERE condition;`
- **Multiple Columns**: `UPDATE table SET col1=val1, col2=val2 WHERE condition;`
- **WHERE Clause**: Critical—omitting it updates ALL rows
- **Subqueries**: Can use subqueries in UPDATE operations

---

### DELETE Statement
Removes rows from a table:

- **Basic Syntax**: `DELETE FROM table WHERE condition;`
- **WHERE Clause**: Essential for specific row deletion
- **TRUNCATE**: Faster removal of all rows (cannot be rolled back in some DBs)
- **Difference**: DELETE removes rows conditionally; TRUNCATE removes all

---

### Key Differences

| Command | Purpose | Effect on Data |
|---------|---------|----------------|
| SELECT | Retrieves data | No change |
| INSERT | Adds new data | Increases rows |
| UPDATE | Modifies existing | Changes values |
| DELETE | Removes data | Decreases rows |

---

### Conclusion
DML commands are fundamental to database operations. Mastery of SELECT, INSERT, UPDATE, and DELETE enables efficient data management in any DBMS. These operations form the practical foundation for database administration and are essential for exam success in DU's DBMS paper.

---

*For quick revision: Focus on syntax variations, WHERE clause importance, and differences between DML operations.*