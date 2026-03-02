# Entities, Attributes, and Relationships - Summary

## Key Definitions and Concepts

- **Entity**: A real-world object that exists independently and can be uniquely identified (e.g., a specific student, a particular book)

- **Entity Set**: A collection of entities of the same type sharing common properties (e.g., all students, all books)

- **Attribute**: A property or characteristic that describes an entity (e.g., name, age, address)

- **Key Attribute**: An attribute that uniquely identifies each entity in a set (underlined in ER diagrams)

- **Relationship**: An association between two or more entities

- **Relationship Set**: A collection of relationships of the same type

- **Weak Entity**: An entity that cannot be uniquely identified by its own attributes and depends on a strong entity for identification (double rectangle in ER diagrams)

## Important Formulas and Theorems

- **Primary Key Identification**: Each entity set must have exactly one primary key—a minimal set of attributes that uniquely identifies each entity

- **Composite Key for Weak Entities**: Primary Key = Partial Key (of weak entity) + Primary Key (of owner entity)

- **Cardinality Types**: One-to-One (1:1), One-to-Many (1:N), Many-to-Many (M:N)

- **Relationship Degree**: Number of entity sets participating (Unary=1, Binary=2, Ternary=3, N-ary=n)

## Key Points

- ER modeling is the foundation of relational database design, providing a high-level abstraction of data structure

- Attributes can be simple (atomic), composite, single-valued, multi-valued, or derived—each represented differently in ER diagrams

- Key attributes must be underlined; derived attributes shown as dashed ovals; multi-valued as double ovals

- Total participation (double line) means every entity MUST participate; partial participation (single line) means optional participation

- Weak entities have double rectangles and are identified through relationships with owner entities (double diamonds)

- Many-to-many relationships cannot be directly implemented in relational databases—they require an associative table

- Binary relationships are most common; higher-degree relationships should be reconsidered for simplification

## Common Mistakes to Avoid

1. **Confusing entity with attribute**: If something has its own attributes and can exist independently, it should be an entity, not an attribute

2. **Missing key attributes**: Every entity set MUST have a primary key—always identify it first

3. **Incorrect cardinality direction**: Ensure the "1" and "N" sides are correctly assigned based on business rules

4. **Forgetting total participation**: Not marking total participation can lead to incomplete database designs that violate business rules

5. **Treating multi-valued attributes as single-valued**: Phone numbers, email addresses—these should be separate tables, not single attributes

## Revision Tips

1. Practice drawing ER diagrams for at least 5 different scenarios (library, university, hospital, banking, e-commerce)

2. Memorize the standard ER notation: rectangles=entities, ovals=attributes, diamonds=relationships

3. For weak entities, always identify: (a) the owner entity, (b) the identifying relationship, and (c) the partial key

4. When converting M:N relationships to relational schema, create a new table with primary keys of both participating entities as composite key

5. Review past DU examination questions on ER modeling to understand the expected answer format and common question patterns