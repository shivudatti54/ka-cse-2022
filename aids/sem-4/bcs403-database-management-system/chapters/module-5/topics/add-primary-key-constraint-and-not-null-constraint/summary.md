# **Add Primary Key Constraint and Not Null Constraint to the Employee Table**

### Definition:

- **Primary Key (PK):** A unique identifier for each record in a table, ensuring data integrity.
- **Not Null (NN):** Ensures that a field cannot contain null values.

### Theorem:

- **Data Integrity:** The addition of PK and NN constraints ensures that data is consistent and accurate.

### Formulas:

- None

### Important Points:

- **Why add PK constraint to Employee table?**
  - Uniquely identifies each employee record
  - Ensures data integrity
  - Facilitates efficient data retrieval and manipulation
- **Why add NN constraint to Employee table?**
  - Ensures that employee details are always available
  - Reduces data inconsistencies
  - Facilitates efficient data analysis
- **Steps to add PK and NN constraint:**
  - **Identify the primary key field:** Determine the field that uniquely identifies each record (e.g., Employee ID).
  - **Add primary key constraint:** Run the following SQL command: `ALTER TABLE Employee ADD CONSTRAINT PK_Employee PRIMARY KEY (Employee ID);`
  - **Add not null constraint:** Run the following SQL command: `ALTER TABLE Employee MODIFY COLUMN [column name] NOT NULL;`
- **Benefits of adding PK and NN constraints:**
  - Improved data integrity
  - Reduced data inconsistencies
  - Enhanced data security
  - Efficient data retrieval and manipulation

### Formula for calculating the number of rows in a table:

None

### Formula for calculating the total storage space required:

None
