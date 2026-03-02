# ER Diagram Notation – Quick Revision Summary

## Introduction
ER (Entity-Relationship) diagrams are essential tools in database design, providing a visual representation of the logical structure of a database. They help in identifying entities, their attributes, and the relationships among entities, forming the blueprint for relational database schema. This is a fundamental concept in the Delhi University BSc Physical Science (CS) syllabus under NEP 2024.

## Key Concepts

- **Entity**: An object with independent existence in the real world (e.g., STUDENT, COURSE, DEPARTMENT). Represented as **rectangles** in Chen notation.
- **Entity Set**: A collection of similar entities.
- **Attributes**: Properties or characteristics of entities.
  - **Simple**: Atomic, indivisible (e.g., RollNo).
  - **Composite**: Can be divided into sub-attributes (e.g., Address → Street, City).
  - **Single-valued**: One value per entity (e.g., Age).
  - **Multivalued**: Multiple values per entity (e.g., PhoneNos), shown as **double ovals**.
  - **Derived**: Computed from other attributes (e.g., Age from DateOfBirth), shown as **dashed ovals**.
- **Keys**: Attributes that uniquely identify entities.
  - **Primary Key**: Underlined in ER diagram.
  - **Candidate Key**: All keys that can uniquely identify (one becomes primary).
  - **Foreign Key**: An attribute referencing the primary key of another entity.
- **Relationships**: Associations among two or more entities.
  - **Degree**: Unary (recursive), Binary (two entities), Ternary (three entities), etc.
  - **Cardinality**: Number of instances.
    - **One-to-One (1:1)**
    - **One-to-Many (1:N)**
    - **Many-to-Many (M:N)**
  - **Participation**: 
    - **Total (Strong)**: Every entity must participate (double line).
    - **Partial (Weak)**: Participation is optional (single line).
- **Weak Entities**: Entities without a full key; they depend on a strong entity for identification. Represented by **double rectangles** (e.g., DEPENDENT linked to EMPLOYEE). Their primary key includes the foreign key from the owner entity.
- **Notations**:
  - **Chen Notation**: Entities as rectangles, attributes as ovals, relationships as diamonds.
  - **Crow's Foot Notation**: Uses symbols like "crow's foot" for "many", straight line for "one". Commonly used in industry and exams.
- **Specialization/Generalization**: 
  - **Generalization**: Combining lower-level entities into a higher-level entity (bottom-up).
  - **Specialization**: Dividing a higher-level entity into lower-level entities (top-down).
  - Represented by a **triangle** (ISA relationship).

## Conclusion
A thorough understanding of ER diagram notation is crucial for designing efficient databases. Practice drawing ER diagrams for various scenarios, as this is a high-frequency exam topic. Refer to the Delhi University syllabus for DBMS (Unit III: Data Modeling) to ensure complete coverage.