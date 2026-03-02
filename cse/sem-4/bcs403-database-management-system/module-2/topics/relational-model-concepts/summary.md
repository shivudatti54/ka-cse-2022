# Relational Model Concepts - Summary

## Key Definitions and Concepts

- **Entity**: Real-world object uniquely identifiable and about which data can be stored
- **Entity Set**: Collection of entities of the same type (similar to a database table)
- **Attribute**: Property or characteristic of an entity; corresponds to columns in a table
- **Tuple**: A single row/record in a relation
- **Relation**: A table with rows and columns; the fundamental structure in the relational model
- **Domain**: Set of allowable values for an attribute

## Important Keys

- **Superkey**: Attribute set that uniquely identifies tuples (may have extra attributes)
- **Candidate Key**: Minimal superkey with no proper subset being a superkey
- **Primary Key**: Selected candidate key; must be unique and NOT NULL
- **Foreign Key**: Attribute referencing another relation's primary key
- **Unique Key**: Similar to primary key but allows NULL values

## Integrity Constraints

- **Domain Constraint**: Values must come from defined domain
- **Key Constraint**: Each relation must have a unique primary key
- **Entity Integrity**: Primary key cannot contain NULL values
- **Referential Integrity**: Foreign key must match primary key or be NULL

## Key Points

- The relational model was introduced by E.F. Codd in 1970
- Entities are represented as rows, attributes as columns in a table
- Primary key selection should be based on minimality and stability
- Multi-valued attributes require separate relations in the schema
- Many-to-many relationships need a separate relation with composite primary key
- Relationship cardinality determines how the relationship is implemented in relations

## Common Mistakes to Avoid

1. Confusing candidate keys with primary keys (not every candidate key becomes primary key)
2. Forgetting that primary keys cannot be NULL (violates entity integrity)
3. Creating separate tables for derived attributes (they can be computed)
4. Using composite attributes directly in relations (they should be broken down)
5. Not establishing foreign key constraints leads to orphaned records

## Revision Tips

1. Practice converting ER diagrams to relational schemas with different relationship cardinalities
2. Memorize the hierarchy: Superkey → Candidate Key → Primary Key
3. Remember the referential integrity rule: foreign key must reference existing primary key or be NULL
4. Review example problems to understand how to identify keys in given relations
5. Focus on understanding the difference between entity and referential integrity constraints
