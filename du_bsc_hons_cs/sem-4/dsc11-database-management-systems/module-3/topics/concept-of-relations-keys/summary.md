# Concept of Relations and Keys - Summary

## Key Definitions and Concepts

- **Relation**: A two-dimensional table with rows (tuples) and columns (attributes)
- **Tuple**: A single row/record in a relation
- **Attribute**: A column/field representing a property of an entity
- **Degree**: Number of attributes in a relation
- **Cardinality**: Number of tuples in a relation
- **Super Key**: Set of attributes that uniquely identifies tuples
- **Candidate Key**: Minimal super key (no subset is a super key)
- **Primary Key**: Selected candidate key; unique and NOT NULL
- **Alternate Key**: Unchosen candidate key
- **Composite Key**: Key with multiple attributes
- **Foreign Key**: Attribute referencing another relation's primary key
- **Unique Key**: Like primary key but allows one NULL value

## Important Formulas and Theorems

- **Key Hierarchy**: Super Key ⊇ Candidate Key ⊇ Primary Key
- **Minimality Principle**: For candidate key, if K is a candidate key, no proper subset of K can be a super key
- **Referential Integrity**: Foreign key value must match referenced primary key or be NULL
- **Entity Integrity**: Primary key cannot contain NULL values

## Key Points

1. Every relation must have at least one candidate key
2. A table can have multiple unique keys but only one primary key
3. Primary key ensures entity integrity; foreign key ensures referential integrity
4. Composite keys are used when no single attribute can uniquely identify tuples
5. Foreign keys create relationships between tables and enable JOIN operations
6. Keys are fundamental to normalization and database design
7. Candidate keys are minimal—removing any attribute destroys uniqueness
8. A foreign key can reference the same table (recursive relationship)

## Common Mistakes to Avoid

1. **Confusing primary key with unique key**: Primary key allows NO NULLs; unique key allows ONE NULL
2. **Selecting non-minimal keys as candidate keys**: Always check if a subset can serve as a key
3. **Forgetting referential integrity**: Foreign keys must reference existing primary keys
4. **Using mutable attributes as primary keys**: Choose stable, rarely changing attributes

## Revision Tips

1. Practice identifying keys in different table scenarios
2. Draw key hierarchies to memorize the relationship between key types
3. Work through JOIN examples to understand foreign key practical usage
4. Remember: Primary Key ⊆ Candidate Key ⊆ Super Key (subset relationships)
5. Review previous year DU exam questions on keys and relations