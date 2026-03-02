# ER-to-Relational Mapping - Summary

## Key Definitions and Concepts

- **ER-to-Relational Mapping:** The process of converting an Entity-Relational (ER) conceptual model into a relational database schema consisting of tables

- **Strong Entity (Regular Entity):** An entity that has its own primary key and exists independently

- **Weak Entity:** An entity that depends on a strong entity for identification and lacks a complete primary key

- **Identifying Relationship:** A relationship where a weak entity participates, used to uniquely identify the weak entity

- **Composite Attribute:** An attribute composed of multiple simple components (e.g., Address with Street, City, State)

- **Multivalued Attribute:** An attribute that can hold multiple values for a single entity instance

- **Derived Attribute:** An attribute whose value can be computed from other attributes (e.g., Age from BirthDate)

## Important Formulas and Theorems

**Regular Entity Mapping:**
```
Entity E(A1, A2, ..., An) with PK → Relation E(PK, A1, A2, ..., An)
```

**Weak Entity Mapping:**
```
Weak Entity W with owner Entity E(PK) → Relation W(PK, PartialKey, other_attrs)
```

**1:1 Relationship Mapping:**
- Option: Add PK of one entity as FK in the other's relation

**1:N Relationship Mapping:**
- Add PK of "one" side entity as FK in "many" side relation

**M:N Relationship Mapping:**
- Create new relation with PKs of both entities as FKs: R(PK1, PK2, relationship_attrs)
- Composite key (PK1, PK2) forms the primary key

**Multivalued Attribute Mapping:**
```
Entity E with multivalued attribute M → Relation E(PK, other_attrs) and Relation M(PK, M)
```

**N-ary Relationship Mapping:**
- Create relation with all participating entities' PKs as foreign keys
- Composite of all FKs forms the primary key

## Key Points

- Always map entities (strong and weak) before mapping relationships
- Foreign keys establish relationships between tables and maintain referential integrity
- For weak entities, the owner's primary key becomes a foreign key in the weak entity's relation
- Multivalued attributes cannot be stored in a single tuple—they require a separate relation
- Derived attributes are never stored; they are computed when needed
- Composite attributes should be flattened to their simple component attributes
- M:N and n-ary relationships always require separate junction/associate relations
- Participation constraints affect how relationships are mapped but don't change the fundamental rules

## Common Mistakes to Avoid

1. **Forgetting foreign keys:** Many students forget to include primary keys of related entities as foreign keys when mapping relationships

2. **Incorrect primary key selection:** For weak entities, failing to combine the owner's key with the partial key as the primary key

3. **Mapping multivalued attributes incorrectly:** Attempting to store multiple values in a single column instead of creating a separate relation

4. **Confusing 1:N and M:N mappings:** Using only foreign keys for M:N relationships instead of creating a junction table

5. **Including derived attributes:** Storing calculated attributes like Age instead of computing them from BirthDate

## Revision Tips

1. **Practice with diagrams:** Draw ER diagrams and convert them to relational schemas repeatedly until the process becomes automatic

2. **Memorize mapping rules by relationship type:** Keep a quick reference table for 1:1, 1:N, M:N, and n-ary relationship mappings

3. **Focus on weak entities:** These are most commonly tested and are often the trickiest part of the mapping process

4. **Solve previous year questions:** DU exams frequently ask for relational schema from given ER diagrams—practice with actual exam questions

5. **Verify your schema:** Always check that every relationship is properly represented and all primary key-foreign key relationships make sense