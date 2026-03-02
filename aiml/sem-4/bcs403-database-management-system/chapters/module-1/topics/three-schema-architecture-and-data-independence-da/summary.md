### Three Schema Architecture and Data Independence, Database Languages, and Interfaces, The Database System Environment

#### Key Concepts

- **Three Schema Architecture:**
  - **Physical Schema:** lowest level, represents physical database structure
  - **Logical Schema:** represents internal structure of database
  - **Conceptual Schema:** represents overall database structure, abstract view

- **Data Independence:**
  - **Horizontal Data Independence:** ability to change database structure without affecting application programs
  - **Vertical Data Independence:** ability to add or remove data without affecting application programs

- **Database Languages:**
  - **SQL (Structured Query Language):** standard language for managing relational databases
  - **Procedural Languages:** support programming, e.g., PL/SQL
  - **Object-Oriented Languages:** support object-oriented programming, e.g., OSQL

- **Interfaces:**
  - **Application Interface:** between application program and database
  - **Data Interface:** between data and the application program
  - **Network Interface:** between database and other systems

#### Important Formulas, Definitions, Theorems

- **First Normal Form (1-NF):** each table cell contains a single value
- **Second Normal Form (2-NF):** each non-key attribute depends on the entire key
- **Third Normal Form (3-NF):** each non-key attribute depends on the entire key and is not dependent on another non-key attribute
- **Boyce-Codd Normal Form (BCNF):** a table is in BCNF if and only if it is in 3NF and each non-key attribute depends on the entire key
- **Database Dependency:** relationship between two tables
- **Entity-Relationship Model (ERM):** graphical representation of entities and their relationships
