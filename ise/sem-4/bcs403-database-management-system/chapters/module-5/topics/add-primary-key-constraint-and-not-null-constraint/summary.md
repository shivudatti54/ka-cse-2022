# **Database Management System Revision Notes**

## **Topic: Add Primary Key Constraint and Not Null Constraint to the Employee Table**

### Key Terms and Definitions

- **Primary Key**: A unique identifier for each row in a table, ensuring data integrity.
- **Not Null Constraint**: A constraint that ensures a column cannot contain null values.
- **Unique Constraint**: A constraint that ensures all values in a column are unique.

### Key Points

- **Step 1: Identify the Columns to Add Constraints**
  - Choose the columns that contain unique identifiers (e.g., Employee ID)
  - Choose the columns that cannot contain null values (e.g., Employee Name)
- **Step 2: Add Primary Key Constraint**
  - Use the `ALTER TABLE` statement with the `ADD CONSTRAINT` clause
  - Specify the constraint name and column(s) affected
  - Example: `ALTER TABLE Employees ADD PRIMARY KEY (EmployeeID);`
- **Step 3: Add Not Null Constraint**
  - Use the `ALTER TABLE` statement with the `ADD CONSTRAINT` clause
  - Specify the constraint name and column(s) affected
  - Example: `ALTER TABLE Employees ADD CONSTRAINT NotNullEmployeeName NOT NULL (EmployeeName);`
- **Step 4: Verify Constraints**
  - Use the `DESCRIBE` statement to verify the constraints
  - Use the `EXPLAIN` statement to verify the execution plan

### Important Formulas and Theorems

- **Database Normalization Theorem**: A well-normalized database ensures data integrity and minimizes data redundancy.

### Quick Revision Tips

- Identify the columns to add constraints
- Use the `ALTER TABLE` statement with the `ADD CONSTRAINT` clause
- Specify the constraint name and column(s) affected
- Verify constraints using `DESCRIBE` and `EXPLAIN` statements

By following these steps and key points, you can effectively add primary key and not null constraints to the employee table, ensuring data integrity and consistency in your database.
