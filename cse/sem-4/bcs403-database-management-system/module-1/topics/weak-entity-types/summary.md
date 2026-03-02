# Weak Entity Types - Summary

## Key Definitions and Concepts

- **Weak Entity Type**: An entity that lacks a primary key of its own and depends on a strong entity (identifying owner) for unique identification.
- **Identifying Owner**: The strong entity type on which a weak entity depends for its identification.
- **Identifying Relationship**: The relationship connecting a weak entity to its owner, always having total participation from the weak entity side.
- **Partial Key (Discriminator)**: An attribute that uniquely identifies weak entities within a single owner entity.

## Important Formulas and Theorems

- **Primary Key of Weak Entity**: Primary Key (Weak) = Primary Key (Owner) + Partial Key (Weak)
- The owner entity's primary key becomes a foreign key in the weak entity table.
- Total participation constraint: Every weak entity instance must be associated with exactly one owner instance.

## Key Points

- Weak entities are represented by double rectangles in ER diagrams.
- Identifying relationships are shown using double diamonds in ER diagrams.
- Partial keys are underlined with a dashed line.
- Weak entities cannot exist without their identifying owner.
- The relationship between owner and weak entity is typically one-to-many.
- Common examples include Employee-Dependent, Building-Room, and Order-OrderItem.
- When the owner entity is deleted, associated weak entities are also deleted (cascading deletion).
- A weak entity can have only one identifying owner.

## Common Mistakes to Avoid

- Confusing weak entities with strong entities that have optional relationships.
- Forgetting that weak entities always have total participation in the identifying relationship.
- Incorrectly identifying the partial key—must uniquely identify entities within ONE owner, not across all owners.

## Revision Tips

- Practice drawing ER diagrams with both strong and weak entities to reinforce notation.
- Memorize the primary key formula: Owner_PK + Partial_Key = Weak_Entity_PK.
- Review common exam examples like Employee-Dependent to understand pattern recognition.
- Remember the visual distinction: double rectangle = weak entity, double diamond = identifying relationship.
