# Database Management System

### Overview of Database Languages and Architectures: Data Models

#### Key Concepts

- **Data Model:** A conceptual representation of data in a database.
- **Entity-Relationship Model (ERM):** A data model that uses entities and relationships to represent data.
  - **Entity:** A thing or concept in the real world.
  - **Attribute:** A characteristic of an entity.
  - **Relationship:** A connection between entities.
- **Object-Relational Model (ORM):** A data model that combines object-oriented and relational concepts.
- **Data Schema:** A blueprint of the database structure.
- **Normalized Database:** A database that minimizes data redundancy and dependency.

#### Important Formulas and Definitions

- **Entity-Relationship Model (ERM) Diagrams:**
  - **1NF (First Normal Form):** Each table cell contains a single value.
  - **2NF (Second Normal Form):** Each non-key attribute depends on the entire primary key.
  - **3NF (Third Normal Form):** If a table is in 2NF, and a non-key attribute depends on another non-key attribute, then it should be moved to a separate table.
- **Data Integrity:** The ability of a database to ensure data consistency and accuracy.
- **ACID (Atomicity, Consistency, Isolation, Durability) Properties:**
  - **Atomicity:** Ensures that database transactions are treated as a single, indivisible unit.
  - **Consistency:** Ensures that the database remains in a consistent state.
  - **Isolation:** Ensures that concurrent transactions do not interfere with each other.
  - **Durability:** Ensures that database transactions are permanent.

#### Important Theorems

- **Gödel's Incompleteness Theorem:** States that any formal system is either incomplete or inconsistent.
- **Church-Turing Thesis:** States that any effectively calculable function can be computed by a Turing machine.

#### Additional Notes

- **ERD (Entity-Relationship Diagram):** A graphical representation of the entities and relationships in an ERM.
- **Database Design:** The process of creating a database structure that meets the requirements of the application.
- **Database Normalization:** The process of organizing data in a database to minimize data redundancy and dependency.
