# Relational Model Constraints and Relational Database Schemas - Summary

## Key Definitions and Concepts

- **Constraint**: A rule that restricts what data values can be stored in a database
- **Domain**: The set of atomic values permitted for an attribute
- **Superkey**: A set of attributes that uniquely identifies each tuple in a relation
- **Candidate Key**: A minimal superkey (no proper subset is a superkey)
- **Primary Key**: The chosen candidate key used to uniquely identify tuples
- **Foreign Key**: An attribute that references the primary key of another relation
- **Database Schema**: The logical structure defining relations, attributes, and constraints
- **Database Instance**: The actual data stored in the database at a given time

## Important Formulas and Theorems

- **Entity Integrity**: Primary key ≠ NULL for every tuple
- **Referential Integrity**: Foreign key values must match primary key values in the referenced relation or be NULL
- **Domain Constraint**: All values in an attribute must belong to its defined domain

## Key Points

- The relational model supports three main integrity constraints: entity, referential, and domain integrity
- Domain constraints ensure attribute values are from valid, atomic domains
- A relation can have multiple candidate keys, but only one primary key
- Entity integrity guarantees each tuple has a unique, non-NULL identifier
- Referential integrity prevents dangling references between related tables
- Foreign keys can reference the same relation (recursive relationship) or different relations
- Referential integrity violations can be handled using CASCADE, SET NULL, SET DEFAULT, or RESTRICT
- Constraints are enforced by the DBMS at all times, not just during application development
- Schema is static and defines structure; instance is dynamic and contains actual data

## Common Mistakes to Avoid

- Confusing candidate keys with primary keys (all candidate keys are valid; one is chosen as primary)
- Forgetting that foreign keys can be NULL (representing optional relationships)
- Believing NULL equals zero or empty string (NULL means "unknown")
- Thinking domain constraints only apply to data types (they also include value ranges and formats)
- Ignoring that referential integrity must be maintained during both INSERT and DELETE operations

## Revision Tips

- Practice identifying different types of constraints in given relation schemas
- Remember: Entity (primary key), Referential (foreign key), Domain (attribute values)
- When solving problems, first identify keys, then check referential relationships
- Review SQL constraint syntax (PRIMARY KEY, FOREIGN KEY, CHECK, NOT NULL, UNIQUE)
- Draw entity-relationship diagrams to visualize referential integrity connections
