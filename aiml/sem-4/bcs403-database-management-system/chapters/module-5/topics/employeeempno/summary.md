# Employee (EMPNO) Revision Notes

=====================================

### Definitions

- **EMPNO (Employee Number)**: A unique identifier assigned to each employee in the database.
- **Primary Key**: A column or field that uniquely identifies each record in a table.

### Importance of EMPNO

- Serves as a unique identifier for each employee.
- Used to track employee data and perform queries.

### EMPNO Features

- **Uniqueness**: Each EMPNO value must be unique across the entire database.
- **Nullability**: EMPNO is typically not nullable, as each employee must have a unique identifier.

### Relationships

- **One-to-One (1:1) Relationship**: EMPNO is uniquely linked to an individual employee.

### Important Formulas

- None specific to EMPNO, but used in conjunction with other database operations.

### Important Theorems

- **Entity Integrity**: A database satisfies entity integrity if each entity (e.g., employee) has a unique identifier (e.g., EMPNO).
- **Referential Integrity**: A database satisfies referential integrity if each foreign key (e.g., EMPNO in a department table) references a unique primary key (e.g., EMPNO in the employee table).

### Important SQL Operations

- **INSERT**: Use EMPNO to insert a new employee record.
- **UPDATE**: Use EMPNO to update employee data.
- **DELETE**: Use EMPNO to delete an employee record.

### Best Practices

- Use a combination of EMPNO and other unique identifiers (e.g., Social Security Number) to minimize errors.
- Ensure EMPNO is securely encrypted and protected to maintain data integrity.
