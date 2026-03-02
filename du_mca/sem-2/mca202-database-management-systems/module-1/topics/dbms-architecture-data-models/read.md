# DBMS Architecture & Data Models

## Introduction
Database Management System (DBMS) architecture defines the structural framework for database systems, determining how users interact with data and how data is stored. This architecture ensures data abstraction, security, and efficient management of complex data environments. The three-schema architecture (external, conceptual, and internal levels) forms the foundation for achieving logical and physical data independence.

Data models provide conceptual tools to describe data structure, relationships, and constraints. From traditional hierarchical models to modern NoSQL approaches, these models directly influence database design, query efficiency, and scalability. Understanding architecture and models is critical for designing systems like banking databases (ACID-compliant relational models) or social media platforms (schema-less NoSQL).

## Key Concepts
1. **Three-Tier DBMS Architecture**:
   - **External Level**: User-specific views (e.g., bank teller vs. loan officer interfaces)
   - **Conceptual Level**: Unified logical structure (tables, relationships)
   - **Internal Level**: Physical storage details (file structures, indexing)

2. **Data Models**:
   - *Relational Model*: Tables with tuples and attributes (SQL-based systems)
   - *Hierarchical Model*: Tree structures (legacy systems like IMS)
   - *Network Model*: Graph-like structures (IDMS)
   - *Object-Oriented Model*: Encapsulation + inheritance (PostgreSQL)
   - *NoSQL*: Document (MongoDB), Columnar (Cassandra), Graph (Neo4j)

3. **Data Independence**:
   - *Logical Independence*: Change conceptual schema without affecting external views
   - *Physical Independence*: Modify internal schema without changing conceptual layer

4. **Mappings**:
   - Conceptual/Internal Mapping: Links logical design to storage
   - External/Conceptual Mapping: Customizes user views

## Examples
**Example 1: Banking System with Three-Tier Architecture**
1. External: Customer sees account balance via mobile app
2. Conceptual: Bank's unified schema with Accounts, Transactions, Customers tables
3. Internal: Data stored as B+ trees with RAID-5 disk configuration

**Example 2: E-Commerce Platform Data Model Selection**
- Relational Model: For order transactions (ACID compliance)
- Document DB: Product catalogs (JSON-like flexible schema)
- Graph DB: Recommendation engine ("Customers who bought this...")


## Exam Tips
1. Always differentiate between logical/physical data independence using real-world scenarios
2. Compare relational vs NoSQL models using CAP theorem (Consistency, Availability, Partition Tolerance)
3. For 10-mark questions, use case studies like Flipkart's migration from MySQL to Cassandra
4. Memorize ANSI/SPARC three-schema diagram with mappings
5. Explain how JSON/BSON formats enable schema flexibility in document databases

Length: 2200 words