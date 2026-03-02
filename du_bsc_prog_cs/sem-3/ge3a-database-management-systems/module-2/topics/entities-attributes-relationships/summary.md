# Entity-Relationship Model - Summary

## Key Definitions and Concepts

- **Entity:** A real-world object that can be uniquely identified; an **entity set** is a collection of similar entities
- **Attribute:** A property or characteristic of an entity; types include simple (atomic), composite, single-valued, multi-valued, derived, and key attributes
- **Relationship:** An association between entities; a **relationship set** is a collection of similar relationships
- **Weak Entity:** Depends on a strong entity for identification; uses partial key combined with owner's primary key
- **Cardinality:** Number of entities participating in a relationship (1:1, 1:N, M:N)
- **Participation Constraint:** Whether entity existence requires relationship participation (total vs. partial)

## Important Formulas and Theorems

- **Key Attribute → Primary Key:** Key attributes in E-R become primary keys in relational schema
- **Composite Attribute Decomposition:** Split into component attributes during implementation
- **Multi-valued Attribute:** Requires separate relation in relational model
- **M:N Relationship Conversion:** Creates junction table with foreign keys to both parent tables
- **Weak Entity Implementation:** Includes foreign key to owner entity plus partial key as primary key

## Key Points

- Chen's notation uses rectangles for entities, ovals for attributes, and diamonds for relationships
- Key attributes are underlined in E-R diagrams
- Double lines indicate total participation; single lines indicate partial participation
- Derived attributes (dashed ovals) are calculated, not stored, to avoid redundancy
- Recursive relationships involve a single entity set relating to itself
- Ternary relationships represent associations among three entity sets simultaneously
- Relationship attributes depend on both participating entities

## Common Mistakes to Avoid

- Confusing entity with entity set; an entity is an instance, entity set is the collection
- Forgetting to underline key attributes or incorrectly identifying them
- Placing attributes on the wrong side of relationships (should be on relationship if dependent on both entities)
- Incorrectly identifying cardinality (read from both directions)
- Drawing M:N relationships directly without creating junction tables during implementation

## Revision Tips

- Practice drawing E-R diagrams for at least 5 different scenarios (library, hospital, university, banking, e-commerce)
- Memorize Chen's notation symbols before the exam
- Practice E-R to relational schema conversions multiple times
- Remember: composite attributes branch downward from main oval, not connect separately to entity
- Focus on weak entity identification and proper primary key formation for exams