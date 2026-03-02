# ER Diagram Notation — Quick Revision Summary

## Introduction
Entity-Relationship (ER) diagrams are a fundamental tool in Database Management Systems (DBMS) for visualizing database structure. This notation, introduced by Peter Chen in 1976, is essential for conceptual database design and is a key topic in the Delhi University BSc (Hons) Computer Science syllabus (Unit 3: Database Design & Normalization).

---

## Key Concepts

### 1. **Entities & Entity Sets**
- **Entity**: A real-world object distinguishable from others (e.g., *Student*, *Course*)
- **Entity Set**: Collection of similar entities
- **Representation**: Rectangle

### 2. **Attributes**
- **Simple Attribute**: Single atomic value (e.g., *Age*)
- **Composite Attribute**: Split into sub-attributes (e.g., *Address* → *City*, *Pincode*)
- **Multivalued Attribute**: Multiple values (shown with double oval)
- **Derived Attribute**: Calculated from other attributes (shown with dashed oval)
- **Key Attribute**: Uniquely identifies an entity (underline)

### 3. **Relationships**
- **Relationship**: Association between entities
- **Relationship Set**: Collection of similar relationships
- **Representation**: Diamond
- **Degree**: Number of entities involved (Unary, Binary, Ternary, N-ary)

### 4. **Cardinality**
- **One-to-One (1:1)**: Each entity relates to only one entity
- **One-to-Many (1:N)**: One entity relates to many
- **Many-to-Many (M:N)**: Many entities relate to many
- **Notation**: Parameters (1, N) on relationship lines

### 5. **Participation Constraints**
- **Total Participation (Strong)**: All entities must participate (double line)
- **Partial Participation**: Participation is optional (single line)

### 6. **Weak Entities**
- Entities without a primary key; depend on a strong entity
- Identified by owner entity + partial key
- **Representation**: Double rectangle

### 7. **Generalization, Specialization & Aggregation**
- **Generalization**: Bottom-up design (common attributes merged)
- **Specialization**: Top-down design (attributes refined)
- **Aggregation**: Treating relationships as higher-level entities

---

## Conclusion
ER diagram notation is crucial for translating real-world requirements into logical database structures. For exams, focus on identifying entities, attributes, relationships, and correctly applying cardinalities and participation constraints. Practice drawing ER diagrams for scenarios like *Library Management*, *Online Shopping*, or *University Database* to ensure thorough preparation.

---

**Delhi University Reference**: NEP 2024 UGCF — Unit 3: Database Design & Normalization