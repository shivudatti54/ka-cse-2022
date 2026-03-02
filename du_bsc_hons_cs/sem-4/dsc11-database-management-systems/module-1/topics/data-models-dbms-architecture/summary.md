# Data Models & DBMS Architecture

## Introduction

Data models define how data is organized, structured, and manipulated within a database system. The DBMS architecture provides the framework for implementing these models, ensuring data independence, efficient processing, and user accessibility. These concepts form the foundation of Database Management Systems (DBMS) as per the Delhi University BSc (Hons) Computer Science NEP 2024 syllabus.

---

## Data Models

### Types of Data Models

- **Hierarchical Model**: Tree-like structure with parent-child relationships; used in early mainframe systems
- **Network Model**: More flexible than hierarchical; allows many-to-many relationships through pointers
- **Relational Model**: Tabular structure with rows (tuples) and columns (attributes); uses keys (primary, foreign, candidate) for relationships
- **Object-Oriented Model**: Represents data as objects with attributes and methods; supports encapsulation and inheritance
- **Entity-Relationship (ER) Model**: Conceptual model using entities, attributes, and relationships; used for database design

### Key Components

- **Schema**: Overall structure of the database (logical, physical, view)
- **Data Independence**: Ability to change schema at one level without affecting another level
- **Keys**: Primary key (unique identifier), Foreign key (references), Composite key, Candidate key

---

## DBMS Architecture

### Three-Schema Architecture (per ANSI/SPARC)

1. **External Schema (View Level)**: Individual user perspective; defines how different users perceive the data
2. **Conceptual Schema (Logical Level)**: Global view of the entire database; defines all entities, relationships, and constraints
3. **Internal Schema (Physical Level)**: Storage structure details; defines indexing, data compression, and access paths

### Data Independence

- **Logical Data Independence**: Changing conceptual schema without affecting external schemas
- **Physical Data Independence**: Changing internal schema without affecting conceptual schema

### DBMS Components

- **Storage Manager**: Handles physical storage, buffer management, file access
- **Query Processor**: Parses, optimizes, and executes SQL queries
- **Transaction Manager**: Ensures ACID properties (Atomicity, Consistency, Isolation, Durability)
- **Recovery Manager**: Handles system failures and ensures data recovery

---

## Conclusion

Understanding data models and DBMS architecture is essential for designing efficient database systems. The three-schema architecture provides a standardized approach for achieving data independence, while various data models offer different methodologies for organizing and representing real-world data. These concepts are crucial for exam success and practical database implementation.