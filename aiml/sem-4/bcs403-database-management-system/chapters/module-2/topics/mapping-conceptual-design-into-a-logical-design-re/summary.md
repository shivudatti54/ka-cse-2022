# Mapping Conceptual Design into a Logical Design: Relational Database Design using ER-to-Relational Mapping

=====================================

## Introduction

---

- Relational database design is a method for mapping conceptual design into a logical design using Entity-Relationship (ER) diagrams.
- ER-to-Relational mapping involves converting ER models into relational database schema.

## Key Concepts

---

- **Entity-Relationship (ER) Model**:
  - Definition: A graphical representation of data entities and their relationships.
  - Components: Entity, Attribute, Relationship, and Cardinality.
- **Entity**:
  - Definition: A thing or concept in the real world.
  - Attributes: Properties or characteristics of an entity.
- **Attribute**:
  - Definition: A characteristic or feature of an entity.
- **Relationship**:
  - Definition: A connection between two or more entities.
  - Cardinality: The number of entities involved in a relationship.
- **Relational Database Schema**:
  - Definition: A set of tables and relationships that define the structure of a database.

## ER-to-Relational Mapping

---

- **Table Schema**:
  - Definition: A set of attributes that define a table in a relational database.
  - Attributes: Primary Key, Foreign Key, and Composite Key.
- **Primary Key**:
  - Definition: A unique identifier for each record in a table.
  - Formula: `PK = {attr1, attr2, ..., attrn}`
- **Foreign Key**:
  - Definition: A field in a table that references the primary key of another table.
  - Formula: `FK = {table1 PK, table2 PK}`
- **Composite Key**:
  - Definition: A primary key that consists of multiple attributes.
  - Formula: `PK = {attr1, attr2, ..., attrn}`

## Important Formulas and Definitions

---

- **Boyce-Codd Normal Form (BCNF)**:
  - Definition: A normalization rule that eliminates partial dependencies.
  - Formula: `R → NK iff ∃X ⊆ A such that R = NK and R ⊆ X`
- **Third Normal Form (3NF)**:
  - Definition: A normalization rule that eliminates transitive dependencies.
  - Formula: `R → 3NF iff ∃X ⊆ A such that R = 3NF and R ⊆ X`
- **Entity Relationship Diagram (ERD)**:
  - Definition: A graphical representation of data entities and their relationships.

## Important Theorems

---

- **Entity-Relationship Theorem**:
  - Definition: A theorem that states that an ER model can be used to define a relational database schema.
  - Formula: `ER Model → Relational Database Schema`

Note: This summary is a concise revision guide and is not intended to be a comprehensive study guide. It covers key concepts, formulas, and definitions related to ER-to-Relational mapping.
