# SQL Data Definition and Data Types - Summary

## Key Definitions and Concepts

- **Data Definition Language (DDL)**: Subset of SQL commands used to define and manage database structures including CREATE, ALTER, and DROP statements.
- **Data Types**: Classification specifying the type of data a column can hold (numeric, character, date/time, binary).
- **Constraints**: Rules enforced on table columns to maintain data integrity (PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT).
- **Referential Integrity**: Property ensuring relationships between tables remain consistent through foreign key constraints.

## Important Formulas and Theorems

- **CHAR(n)**: Fixed-length string of n characters, padded with spaces if shorter
- **VARCHAR(n)**: Variable-length string up to n characters, storage-efficient
- **DECIMAL(p,s)**: Exact numeric with p total digits and s decimal places (DECIMAL(5,2) = 123.45)
- **FLOAT(n)**: Approximate numeric with n bits of precision

## Key Points

- Use INT for whole numbers, DECIMAL for precise decimal values, VARCHAR for variable text
- PRIMARY KEY uniquely identifies rows; only one per table, cannot be NULL
- FOREIGN KEY maintains referential integrity between related tables
- ALTER TABLE modifies structure without losing existing data
- DROP permanently removes objects; TRUNCATE removes data but keeps structure
- Choose smaller data types (SMALLINT, TINYINT) when appropriate to save storage
- NOT NULL constraint forces columns to always contain values
- UNIQUE constraint allows multiple columns but permits NULL values (database-dependent)

## Common Mistakes to Avoid

1. Using CHAR for variable-length data (wastes storage with padding)
2. Forgetting to define primary key when creating tables
3. Mismatching foreign key and primary key data types
4. Using DROP instead of TRUNCATE when table structure is needed
5. Setting VARCHAR maximum too high (impacts index efficiency)

## Revision Tips

1. Practice writing CREATE TABLE statements with various constraints
2. Memorize the difference between all constraint types
3. Remember: PRIMARY KEY = UNIQUE + NOT NULL combined
4. Review ALTER TABLE variations (ADD, MODIFY, DROP)
5. Practice creating parent-child table relationships with foreign keys
