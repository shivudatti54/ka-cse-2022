# Relational Database Design Using ER-to-Relational Mapping - Summary

## Key Definitions and Concepts

- **ER-to-Relational Mapping**: The systematic process of transforming an Entity-Relationship (ER) diagram into a set of relational database schemas ready for implementation.

- **Strong Entity Set**: An entity set that has its own primary key and can exist independently; mapped by creating a relation with all its simple attributes.

- **Weak Entity Set**: An entity set that depends on a strong entity for identification; mapped by including the owner's primary key in its relation.

- **Junction Table**: A relation created to represent many-to-many or N-ary relationships, containing foreign keys to all participating entity sets.

## Important Formulas and Theorems

- **Regular Entity Mapping**: Entity(E) → Relation(E) with same attributes and primary key

- **Weak Entity Mapping**: Entity W(owner E) → Relation W(attributes of W + PK of E) with composite PK

- **1:1 Relationship Mapping**: Add PK of one entity as FK to the other entity's relation (preferably total participation side)

- **1:N Relationship Mapping**: Add PK of "one" side entity as FK to "many" side entity's relation

- **N:M Relationship Mapping**: Create new relation with PKs of both entities as composite FK and PK

- **Multi-valued Attribute Mapping**: Create separate relation with entity PK and the multi-valued attribute as composite PK

- **N-ary Relationship Mapping**: Create relation with FKs to all N participating entities; composite PK typically includes all FKs

## Key Points

- The mapping process follows a specific order: regular entities → weak entities → 1:1 → 1:N → N:M → attributes

- Composite attributes should be decomposed into simple component attributes during mapping

- Derived attributes are never stored; they are computed when needed using queries

- Total participation is enforced using NOT NULL constraints on foreign keys

- A weak entity's primary key consists of the owner's primary key plus the weak entity's partial key

- For N:M relationships, the junction table's primary key is the combination of both foreign keys

- N-ary relationships always require a separate relation regardless of the degree

- When both entities in a 1:1 relationship have total participation, they can be merged into a single relation

## Common Mistakes to Avoid

1. **Forgetting to include foreign keys**: Many students forget to add foreign keys for relationships, especially for 1:N relationships

2. **Creating separate relations for 1:1 relationships unnecessarily**: This is inefficient; use the foreign key approach instead

3. **Not making composite primary keys**: For weak entities and multi-valued attributes, the primary key must be composite

4. **Storing derived attributes**: This violates normalization principles and wastes storage

5. **Incorrect cardinality identification**: Misidentifying 1:N as N:M leads to unnecessary junction tables

## Revision Tips

1. **Practice with different ER diagrams**: Work through multiple examples to solidify understanding of mapping rules

2. **Memorize the mapping rules by heart**: Know the specific approach for each type of entity, relationship, and attribute

3. **Always identify cardinality first**: Before mapping, clearly determine whether each relationship is 1:1, 1:N, or N:M

4. **Draw the final schema after mapping**: Verify that all original information from the ER diagram is preserved

5. **Focus on weak entities and N:M relationships**: These are the most commonly tested concepts in university examinations
