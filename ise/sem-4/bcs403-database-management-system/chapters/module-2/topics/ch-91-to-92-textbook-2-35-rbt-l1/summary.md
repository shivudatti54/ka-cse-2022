### Database Management System Revision Notes

#### Ch 9.1 to 9.2 Textbook 2: 3.5 RBT: L1

**Definitions:**

- **Database Management System (DBMS):** software that manages and controls data in a database.
- **Database:** a collection of organized data stored in a way that allows for efficient access and manipulation.
- **Relational Database:** a type of database that stores data in tables with defined relationships between them.

**Key Concepts:**

- **Database Entities:** real-world objects or concepts that the database represents.
- **Database Attributes:** individual pieces of information about a database entity.
- **Primary Key:** a unique identifier for each database entity.
- **Foreign Key:** a field in one table that references the primary key of another table.

**Database Design:**

- **Entity-Relationship Diagram (ERD):** a visual representation of the relationships between database entities.
- ** normalization:** the process of organizing data in a database to minimize data redundancy and improve data integrity.

**Database Operations:**

- **Insert:** adding new data to a database.
- **Update:** modifying existing data in a database.
- **Delete:** removing data from a database.

**Important Formulas and Theorems:**

- **Database Normalization Rules:**
  - First Normal Form (1NF): each cell in the table contains a single value.
  - Second Normal Form (2NF): each non-key attribute depends on the entire primary key.
  - Third Normal Form (3NF): if a table is in 2NF, and a non-key attribute depends on another non-key attribute, then it should be moved to a separate table.
- **Database Relationships:**
  - One-to-One (1:1): one entity is related to one other entity.
  - One-to-Many (1:m): one entity is related to multiple other entities.
  - Many-to-Many (m:m): multiple entities are related to each other.

**Important Theorems:**

- **Database Independence Theorem:** a DBMS should be able to work with different database management systems.
- **Data Independence Theorem:** a DBMS should be able to modify the physical storage of data without affecting the user's view of the data.
