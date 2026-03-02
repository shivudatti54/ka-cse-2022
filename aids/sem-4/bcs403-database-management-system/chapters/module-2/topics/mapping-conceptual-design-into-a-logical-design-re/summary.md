# Mapping Conceptual Design into a Logical Design: Relational Database Design using ER-to-Relational mapping

=====================================================

## Overview

---

Relational Database Design using ER-to-Relational mapping involves translating conceptual database design into a logical database design using Entity-Relationship (ER) diagrams.

## Key Concepts

---

- **Entity-Relationship (ER) Diagrams**: Visual representation of the relationships between entities in a database.
- **Conceptual Schema**: High-level representation of the database structure, focusing on entities, attributes, and relationships.
- **Logical Schema**: Mid-level representation of the database structure, focusing on relations, attributes, and constraints.
- **ER-to-Relational Mapping**: Process of translating ER diagrams into relational database design.
- **Normalized Database**: Database design that minimizes data redundancy and dependency.

## Important Formulas and Definitions

---

- **First Normal Form (1NF)**: Each table cell contains a single value; each column contains atomic values.
- **Second Normal Form (2NF)**: Each non-key attribute depends on the entire primary key.
- **Third Normal Form (3NF)**: If a table is in 2NF, and a non-key attribute depends on another non-key attribute, then it should be moved to a separate table.
- **Boyce-Codd Normal Form (BCNF)**: Table is in 3NF and there are no transitive dependencies.

## Theorems

---

- **Data Independence Theorem**: A database design is independent of the underlying storage if it is designed using relational algebra or relational calculus.
- **Data Reusability Theorem**: A database design is reusable if it is based on a concept or theme that can be applied to different situations.

## Key Steps in ER-to-Relational Mapping

---

- Identify entities and attributes
- Define relationships between entities
- Determine primary and foreign keys
- Normalize the database
- Create a logical schema

## Quick Revision Tips

---

- Focus on understanding ER diagrams and their relationships
- Practice translating ER diagrams into relational database design
- Review normalization rules and Boyce-Codd normal form
- Practice applying data independence and data reusability theorems.
