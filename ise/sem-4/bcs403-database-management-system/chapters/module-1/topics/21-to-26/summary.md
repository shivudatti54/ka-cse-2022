# **2.1 to 2.6: Database Management System Revision Notes**

### Definitions

- **Database**: A collection of organized data that is stored in a way that allows for efficient retrieval and manipulation.
- **Database Management System (DBMS)**: Software that manages and maintains a database, providing tools for data definition, data manipulation, and data retrieval.

### Key Concepts

- **Data Independence**: The ability of a user to change the physical storage of data without affecting the logical structure of the data.
- **Data Control**: The ability of a user to control the data in a database, including data creation, modification, and deletion.
- **Data Integrity**: The property of a database that ensures data consistency and accuracy.

### Theorems

- **ACID (Atomicity, Consistency, Isolation, Durability)**: A set of principles that ensure database transactions are processed reliably and securely.
  - Atomicity: Ensures that database transactions are treated as a single, indivisible unit.
  - Consistency: Ensures that data remains in a consistent state.
  - Isolation: Ensures that database transactions do not interfere with each other.
  - Durability: Ensures that database transactions are permanent and survive system failures.

### Formulas

- **Relational Algebra**: A formal language for manipulating relational databases, defined as follows:
  - σ(x) (sigma): Selects a subset of rows based on a condition.
  - π(x) (pi): Selects a subset of columns based on a condition.
  - ∪ (union): Combines two or more sets of rows.
  - ∩ (intersection): Combines two or more sets of rows using a common condition.
  - ∘ (composition): Combines two or more sets of rows using a sequence of conditions.

### Important Concepts

- **Normalization**: The process of organizing data in a database to minimize data redundancy and improve data integrity.
- **Denormalization**: The process of organizing data in a database to improve query performance at the expense of data integrity.
- **Database Architecture**: The design and organization of a database, including the schema, indexes, and data storage.

### Study Tips

- Review the definitions and key concepts in 2.1-2.6.
- Practice solving problems using relational algebra and other database concepts.
- Focus on understanding the ACID theorem and its implications for database transactions.
- Review the formulas and concepts in normalization and denormalization.
