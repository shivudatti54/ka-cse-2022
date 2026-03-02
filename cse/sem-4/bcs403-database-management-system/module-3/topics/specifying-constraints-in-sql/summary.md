# Specifying Constraints in SQL - Summary

## Key Definitions and Concepts

- **Constraint**: A database object that enforces data integrity by defining rules that data must follow
- **Column-level constraint**: Applied to a single column, defined within the column definition
- **Table-level constraint**: Applied to one or more columns, defined after all column definitions
- **Referential Integrity**: The consistency between related tables maintained through foreign key relationships

## Important Formulas and Theorems

- **PRIMARY KEY**: Uniquely identifies rows; one per table; cannot be NULL
- **UNIQUE**: Ensures distinct values; multiple allowed per table; allows one NULL
- **FOREIGN KEY**: Establishes parent-child relationship between tables
- **CHECK**: Validates conditions using Boolean expressions
- **DEFAULT**: Provides fallback values during INSERT operations
- **NOT NULL**: Prohibits NULL values in a column

## Key Points

1. Constraints are automatically enforced by the DBMS and prevent invalid data entry
2. PRIMARY KEY combines UNIQUE and NOT NULL functionality for a single column or composite key
3. FOREIGN KEY constraints maintain referential integrity between related tables
4. CHECK constraints can validate complex business rules including multi-column conditions
5. Composite keys (multiple columns as PRIMARY KEY or UNIQUE) are useful for junction tables
6. Constraints can be added to existing tables using ALTER TABLE with ADD/DROP/MODIFY
7. Naming constraints explicitly improves error messages and database maintainability
8. The order of table creation matters when foreign key relationships exist

## Common Mistakes to Avoid

1. Confusing PRIMARY KEY with UNIQUE—remember primary keys cannot be NULL
2. Forgetting that CHECK constraints evaluate conditions that must be TRUE
3. Creating child tables before parent tables, causing foreign key violations
4. Attempting to drop a parent table while child tables still reference it
5. Using NULL inappropriately in columns that should have mandatory values

## Revision Tips

1. Practice writing CREATE TABLE statements with various constraint combinations
2. Memorize the syntax differences between column-level and table-level constraints
3. Understand the behavior of ON DELETE and ON UPDATE actions for foreign keys
4. Review constraint-related error messages by attempting to violate them intentionally
5. Focus on understanding when to use each constraint type based on business requirements
