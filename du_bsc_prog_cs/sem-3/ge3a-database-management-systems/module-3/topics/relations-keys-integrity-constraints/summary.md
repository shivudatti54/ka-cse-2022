# Relations, Keys, and Integrity Constraints - Summary

## Key Definitions and Concepts

- **Relation**: A two-dimensional table with rows (tuples) and columns (attributes) that satisfies atomicity, unique column names, unique rows, and order independence
- **Super Key**: An attribute set that uniquely identifies tuples; may contain redundant attributes
- **Candidate Key**: A minimal super key—no proper subset is a super key; these are the true identifiers
- **Primary Key**: The selected candidate key that uniquely identifies tuples; cannot be NULL
- **Foreign Key**: An attribute referencing another relation's primary key; establishes table relationships
- **Composite Key**: A key with multiple attributes where the combination is unique
- **Alternate Key**: Any candidate key not chosen as primary key

## Important Formulas and Theorems

- A relation with n attributes can have up to 2ⁿ - 1 super keys
- A relation must have at least one candidate key
- Foreign key constraints enforce referential integrity: (Foreign Key Value ∈ Primary Key Values) OR (Foreign Key IS NULL)

## Key Points

1. Relations in DBMS must be in First Normal Form (atomic values in each cell)
2. Primary keys enforce entity integrity—no NULL values allowed
3. Foreign keys enforce referential integrity—referenced values must exist or be NULL
4. Domain integrity ensures attribute values belong to defined domains (data types, CHECK constraints)
5. A table can have multiple foreign keys but only one primary key
6. Composite keys are used when no single attribute can uniquely identify tuples
7. CASCADE, SET NULL, and NO ACTION are referential integrity actions on delete/update

## Common Mistakes to Avoid

1. Confusing Super Key with Candidate Key—candidate keys are minimal
2. Thinking foreign keys must always reference existing values—NULL is allowed
3. Believing NULL equals zero or empty string—NULL represents missing/unknown
4. Using composite keys incorrectly—it's the combination that matters, not individual attributes

## Revision Tips

1. Practice identifying candidate keys from given relation schemas by checking minimality
2. Write CREATE TABLE statements with all constraint types to reinforce practical knowledge
3. Draw ER diagrams showing how foreign keys represent relationships between entities
4. Remember: Primary Key = Entity Integrity, Foreign Key = Referential Integrity
5. Solve previous year DU exam questions on keys and constraints for pattern familiarity