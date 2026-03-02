# **Three Schema Architecture and Data Independence, Database Languages, and Interfaces**

## **Three Schema Architecture**

- **First Normal Form (1NF)**:
  - Each table cell must contain a single value.
  - No repeating groups or arrays.
  - Formula: R(A, B, ... , X) -> ∃R1(A, B1), R2(A, B2), ..., Rn(A, Bn)
- **Second Normal Form (2NF)**:
  - If a table is in 1NF, and a non-prime attribute depends on another prime attribute, then it should be moved to a separate table.
  - Formula: R(A, B, ... , X) -> R(A, B1) and R(B, C) -> R1(A, B1), R2(B, C)
- **Third Normal Form (3NF)**:
  - If a table is in 2NF, and a non-prime attribute depends on another non-prime attribute, then it should be moved to a separate table.
  - Formula: R(A, B, ... , X) -> R1(A, B1) and R2(B, C) -> R3(A, B1, C)

## **Data Independence**

- **Physical Data Independence**:
  - A change in the physical storage of data does not affect the overall database behavior.
  - Formula: σX → σY and σZ → σY
- **Logical Data Independence**:
  - A change in the logical structure of the database does not affect the overall database behavior.
  - Formula: R(A, B, ... , X) → R1(A, B1), R2(A, B2), ...

## **Database Languages**

- **SQL (Structured Query Language)**:
  - A standard language for managing relational databases.
  - Querying, modifying, and manipulating data in databases.
- **DML (Data Manipulation Language)**:
  - Used to manage data in a database.
  - Includes commands like CREATE, INSERT, UPDATE, and DELETE.
- **DQL (Data Query Language)**:
  - Used to retrieve data from a database.
  - Includes commands like SELECT and FROM.

## **Database Interfaces**

- **Database Management System (DBMS)**:
  - A software system that manages a database.
  - Provides a layer of abstraction between the user and the database.
- **Database Interface**:
  - The interface between the user and the database.
  - Can be physical (e.g., keyboard, mouse) or logical (e.g., API, SQL).
