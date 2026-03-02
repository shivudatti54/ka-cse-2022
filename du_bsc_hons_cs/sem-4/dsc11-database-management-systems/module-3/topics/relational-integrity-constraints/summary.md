# Relational Integrity Constraints - Summary

## Key Definitions and Concepts

- **Integrity Constraints**: Rules enforced at the database level to ensure data accuracy, consistency, and reliability.
- **Domain Constraints**: Define permissible values for attributes based on data type, format, and range.
- **Entity Integrity**: Primary key must have unique, non-null values for each tuple.
- **Referential Integrity**: Foreign key values must match primary key values in referenced tables or be NULL.
- **Key Constraints**: Rules governing keys (candidate, primary, foreign, super, composite).

## Important Formulas and Theorems

- Entity Integrity Rule: Primary Key ≠ NULL
- Referential Integrity Rule: FK value = PK value OR FK = NULL (if allowed)
- CHECK Constraint: Condition must evaluate to TRUE or UNKNOWN for success

## Key Points

- **Three Fundamental Integrity Types**: Entity, Referential, and Domain integrity form the core of relational database integrity.
- **Primary Key Characteristics**: One per table, unique, non-null, cannot be composite (but can be).
- **Foreign Key Actions**: CASCADE propagates changes; RESTRICT prevents deletion; SET NULL allows NULL values.
- **Candidate Key vs Primary Key**: Candidate keys are potential primary keys; one is chosen as primary.
- **NULL Handling**: NULL ≠ NULL; constraints pass when evaluating to UNKNOWN, fail only on FALSE.
- **CHECK Constraints**: User-defined conditions on column or table values.
- **Composite Keys**: Multiple attributes together form a unique identifier; all must be non-null.
- **Assertions**: Table-independent constraints involving multiple tables.
- **Triggers**: Procedural integrity enforcement through automatic code execution.

## Common Mistakes to Avoid

- Confusing DELETE CASCADE with DROP TABLE—CASCADE removes related rows, DROP removes the entire table structure.
- Forgetting that primary key columns cannot contain NULL values.
- Assuming foreign key constraints automatically prevent NULL entries—NULL is allowed unless NOT NULL is specified.
- Using CASCADE delete without understanding it will permanently delete dependent records.

## Revision Tips

1. Practice writing CREATE TABLE statements with multiple constraints—common in practical exams.
2. Memorize the difference between all referential actions with practical examples.
3. Draw entity-relationship diagrams showing primary and foreign key relationships before writing SQL.
4. Remember: Entity integrity applies to primary keys; referential integrity applies to foreign keys.
5. Review previous years' DU question papers to understand the exam pattern and frequently asked questions.