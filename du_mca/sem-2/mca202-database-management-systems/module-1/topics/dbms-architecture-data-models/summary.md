# DBMS Architecture & Data Models - Summary

## Key Definitions and Concepts
- **Three-Tier Architecture**: External (views), Conceptual (logic), Internal (storage)
- **Data Model**: Abstract representation of data organization (e.g., relational tables)
- **Data Independence**: Immunity of user applications to changes in storage/logic

## Important Formulas and Theorems
- **CAP Theorem**: NoSQL systems can only guarantee 2/3 of Consistency, Availability, Partition Tolerance
- **ACID Properties**: Atomicity, Consistency, Isolation, Durability (Relational DBs)
- **Brewer's Conjecture**: Formal basis for CAP theorem (2000)

## Key Points
- Relational models use SQL and enforce strict schema
- NoSQL sacrifices ACID for horizontal scalability
- Conceptual schema acts as intermediary between views and storage
- Logical independence > Physical independence in maintenance complexity
- Network model uses CODASYL DBTG standard
- Object-relational mapping (ORM) bridges OOP and relational models

## Common Mistakes to Avoid
1. Confusing external schema (user view) with conceptual schema (global logic)
2. Assuming NoSQL = "No SQL" (many support SQL-like queries)
3. Overlooking physical-level optimizations like indexing in exam answers
4. Misapplying hierarchical model for many-to-many relationships

## Revision Tips
1. Create layered diagrams comparing 3-tier architecture with OSI model
2. Practice converting JSON documents (NoSQL) to relational tables
3. Use flashcards for model comparisons: e.g., "Joins: Supported in Relational, Not in Document DB"
4. Study real-world migrations: e.g., Airbnb moving from MySQL to Amazon DynamoDB

Length: 650 words