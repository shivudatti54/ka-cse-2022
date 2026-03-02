# Mapping Conceptual Design into a Logical Design

## Introduction

After completing the Entity-Relationship (ER) model, which serves as the **conceptual blueprint** of the database, the next critical step is to translate this high-level, implementation-independent design into a **logical model**. This process, known as **Logical Database Design** or mapping, involves converting the ER diagram into a database schema—specifically, a set of relational tables, attributes, and constraints. This schema will be the direct basis for implementing the database in a Relational Database Management System (RDBMS) like MySQL or Oracle.

## Core Concepts of the Mapping Process

The goal is to systematically transform entities, relationships, and attributes from the ER model into a format the RDBMS can understand. The process follows a set of well-defined rules.

### 1. Mapping of Regular (Strong) Entities

A strong entity (with its own primary key) is mapped directly to a separate table (relation).

*   **Rule:** The name of the entity becomes the table name.
*   The simple attributes of the entity become the columns of the table.
*   The primary key of the entity becomes the primary key of the table.
*   Composite attributes are broken down into their simple components.
*   Multi-valued attributes require special treatment (see point 4).

**Example:**
The strong entity `Student` with attributes `Reg_No` (PK), `Name` (composite: `F_Name`, `L_Name`), `Email`, and `Phone_No` (multi-valued) is mapped as:

**Student Table**
| Reg_No (PK) | F_Name | L_Name | Email           |
|-------------|--------|--------|-----------------|
| 01VTUCS001  | Ramesh | Kumar  | ramesh@.com  |
| 01VTUCS002  | Suresh | Patel  | suresh@.com  |

*Note: `Phone_No` is handled separately.*

### 2. Mapping of Weak Entities

A weak entity is existence-dependent on a strong entity (owner entity).

*   **Rule:** The weak entity becomes a separate table.
*   The table includes all its simple attributes.
*   The primary key of this new table is a combination of its own partial key and the primary key of the owner entity.
*   The primary key of the owner entity is also designated as a **foreign key** in the weak entity's table.

**Example:**
The weak entity `Dependent` depends on the strong entity `Employee`. `Dependent` has a partial key `Name`.

**Dependent Table**
| Emp_ID (FK) | Name (Partial Key) | Age    | Relation |
|-------------|--------------------|--------|----------|
| E100        | Rohit              | 8      | Son      |
| E100        | Seema              | 40     | Spouse   |
| E200        | Arjun              | 10     | Son      |

*The primary key for the `Dependent` table is (Emp_ID, Name). `Emp_ID` is a foreign key referencing the `Employee` table.*

### 3. Mapping of Binary Relationships

The mapping of relationships depends on their cardinality ratio (1:1, 1:N, M:N).

*   **One-to-Many (1:N):** The most common case. The primary key of the entity on the "one" side is embedded as a foreign key in the table representing the entity on the "many" side.
    *   *Example:* `Department`(1) *has* `Employees`(N). The `Employee` table gets a new column `Dept_ID` as a foreign key.

*   **Many-to-Many (M:N):** A new **relationship table** (or composite table) is created.
    *   This new table contains the primary keys of the participating entities as foreign keys. Their combination forms the primary key of this new table.
    *   Any descriptive attributes of the relationship become columns in this new table.
    *   *Example:* The relationship `Enrolls` between `Student`(M) and `Course`(N) with an attribute `Grade` creates a new table:

    **Enrolls Table**
    | Reg_No (FK) | Course_Code (FK) | Grade |
    |-------------|------------------|-------|
    | 01VTUCS001  | CS101            | A     |
    | 01VTUCS001  | MA102            | B     |

*   **One-to-One (1:1):** Can be handled by placing a foreign key in either table. Typically, it's placed in the table where the relationship is mandatory or more frequently accessed.

### 4. Mapping of Multi-valued Attributes

*   **Rule:** A multi-valued attribute is not stored as a column in the main entity table. Instead, it is mapped to a new separate table.
*   This new table will have two columns: the primary key of the original entity (as a foreign key) and the multi-valued attribute.
*   The primary key of this new table is typically the combination of both attributes.

**Example:**
For the multi-valued attribute `Phone_No` in the `Student` entity:

**Student_Phone Table**
| Reg_No (FK) | Phone_No     |
|-------------|--------------|
| 01VTUCS001  | 9876543210   |
| 01VTUCS001  | 9123456789   |
| 01VTUCS002  | 9777744440   |

*The primary key is (Reg_No, Phone_No).*

## Key Points & Summary

*   **Purpose:** The mapping process creates a detailed, normalized relational schema ready for physical implementation in an RDBMS.
*   **Systematic Process:** It follows a strict set of rules to ensure data integrity and avoid redundancy.
*   **Foreign Keys are Crucial:** They are the mechanism used to establish relationships (links) between tables, enforcing referential integrity.
*   **Normalization:** The resulting tables should be checked against normal forms (like 3NF) to ensure they are free of insertion, deletion, and update anomalies. The mapping process itself often produces tables in at least 1NF.
*   **Order of Mapping:** It is generally recommended to map entities first, then relationships, and finally attributes to ensure a clear and error-free schema.

The final output of this phase is a complete logical design—a list of tables, their columns, data types, primary keys, foreign keys, and constraints—which serves as the perfect blueprint for the `CREATE TABLE` statements in SQL.