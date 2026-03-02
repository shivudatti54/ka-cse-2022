# **DATABASE MANAGEMENT SYSTEM**

## **Module: Ch 8.1 to 8.5**

### Hours: 8

---

### Chapter 8: Database Design

---

### 8.1: Data Model

---

#### Definition:

A data model is a conceptual representation of the data in a database.

#### Types of Data Models:

- Physical Data Model: represents the database schema.
- Logical Data Model: represents the relationships between the data.
- Conceptual Data Model: represents the data in a high-level, abstract way.

#### Example:

Consider a university database. A conceptual data model might include entities such as "student", "course", and "department", with relationships such as "a student takes multiple courses" and "a course is offered by a department".

### 8.2: Entity-Relationship Model

---

#### Definition:

An entity-relationship model is a data model that uses entities and relationships to represent the data.

#### Key Components:

- Entities: represent real-world objects or concepts.
- Attributes: represent the characteristics of an entity.
- Relationships: represent the connections between entities.

#### Example:

Using the university database example, an entity-relationship model might include entities such as "Student", "Course", and "Department", with attributes such as "Student ID", "Name", and "GPA", and relationships such as "a student takes multiple courses" and "a course is offered by a department".

### 8.3: Relational Model

---

#### Definition:

A relational model is a data model that uses tables and relationships to store and manage data.

#### Key Components:

- Tables: represent the entities and their attributes.
- Primary Key: uniquely identifies each row in a table.
- Foreign Key: uniquely identifies each row in a related table.

#### Example:

Using the university database example, a relational model might include tables such as "Student", "Course", and "Department", with attributes and relationships such as "Student ID", "Name", and "GPA", and relationships such as "a student takes multiple courses".

### 8.4: Normalization

---

#### Definition:

Normalization is the process of organizing data in a database to minimize data redundancy and improve data integrity.

#### Key Concepts:

- First Normal Form (1NF): each table cell contains a single value.
- Second Normal Form (2NF): each non-key attribute depends on the entire primary key.
- Third Normal Form (3NF): if a table is in 2NF, and a non-key attribute depends on another non-key attribute, then it should be moved to a separate table.

#### Example:

Consider a table with columns "Student ID", "Name", and "Address". This table is not in 1NF because the "Address" column contains multiple values. Normalization would involve splitting this table into two tables: "Student" and "Address", with a relationship between the two tables.

### 8.5: Database Design Tools

---

#### Definition:

Database design tools are software applications used to create and manage database designs.

#### Key Tools:

- Entity-Relationship Diagram (ERD) tools: used to create and manage entity-relationship models.
- Object-Relational Mapping (ORM) tools: used to create and manage relational models.
- Data Modeling tools: used to create and manage data models.

#### Example:

Using a database design tool such as ER/Studio, an entity-relationship model for the university database might be created and managed.

### Key Concepts

---

- Data model: a conceptual representation of the data in a database.
- Entity-relationship model: a data model that uses entities and relationships to represent the data.
- Relational model: a data model that uses tables and relationships to store and manage data.
- Normalization: the process of organizing data in a database to minimize data redundancy and improve data integrity.
- Database design tools: software applications used to create and manage database designs.
