# **Mapping Conceptual Design into a Logical Design: Relational Database Design using ER-to-Relational mapping**

## **Introduction**

Relational database design is a crucial step in the database management system (DBMS) development process. In this topic, we will explore how to map conceptual design into a logical design using ER-to-Relational mapping. This process involves translating the conceptual model into a relational model that can be implemented using a physical database management system.

## **Conceptual Design**

A conceptual design is the topmost level of the database design process. It represents the abstract structure of the database, without considering the physical storage or implementation details. A conceptual design typically consists of entities, attributes, and relationships.

- **Entities**: These are the objects or concepts that the database will store. For example, in a university database, entities might include students, courses, and professors.
- **Attributes**: These are the characteristics or properties of an entity. For example, a student entity might have attributes such as name, ID number, and GPA.
- **Relationships**: These are the connections between entities. For example, a student entity might be related to a course entity through a student-enrolled relationship.

## **Entity-Relationship (ER) Modeling**

ER modeling is a graphical representation of the conceptual design. It uses entities, attributes, and relationships to create a visual representation of the database structure.

- **ER Diagram**: An ER diagram consists of entities, attributes, and relationships represented as lines, boxes, and symbols.
- **Attribute Notation**: Attributes are represented as a pair of parentheses containing the attribute name and data type.
- **Relationship Notation**: Relationships are represented as lines connecting entities, with the following symbols:
  - **Solid line**: One-to-one relationship
  - **Dashed line**: One-to-many relationship
  - **Bold line**: Many-to-many relationship

## **ER-to-Relational Mapping**

ER-to-Relational mapping involves translating the ER model into a relational model that can be implemented using a physical database management system. The resulting relational model consists of tables, columns, and relationships.

- **Table**: A table represents an entity in the relational model.
- **Column**: A column represents an attribute in the table.
- **Primary Key**: A primary key is a unique identifier for a table.
- **Foreign Key**: A foreign key is a column that references the primary key of another table.

## **Relational Database Design**

Relational database design involves designing the physical database structure using the relational model.

- **Table Design**: The table design involves specifying the columns, primary keys, and foreign keys for each table.
- **Indexing**: Indexing involves creating a data structure that improves query performance.
- **Normalization**: Normalization involves organizing the data into separate tables to reduce data redundancy and improve data integrity.

## **Example**

Suppose we want to design a database for a university that includes students, courses, and professors. We can use ER modeling to create an ER diagram that represents the database structure.

ER Diagram:

```mermaid
classDiagram
    class Students {
        +id
        +name
        +GPA
        +courses
    }
    class Courses {
        +id
        +name
        +credits
        +professor
    }
    class Professors {
        +id
        +name
        +department
    }
    Students --|* Courses
    Courses --|* Professor
    Students --|* Professors
```

ER-to-Relational Mapping:

```sql
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    GPA DECIMAL(3, 2),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

CREATE TABLE Courses (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    credits INT,
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES Professors(id)
);

CREATE TABLE Professors (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255)
);
```

Relational Database Design:

```sql
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    GPA DECIMAL(3, 2),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

CREATE TABLE Courses (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    credits INT,
    professor_id INT,
    FOREIGN KEY (professor_id) REFERENCES Professors(id)
);

CREATE TABLE Professors (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(255)
);
```

This design includes three tables: Students, Courses, and Professors. The Students table has a foreign key to the Courses table, indicating that a student is enrolled in multiple courses. The Courses table has a foreign key to the Professors table, indicating that a course is taught by one professor. The Professors table has no foreign keys, indicating that a professor is not related to any other tables.

## **Conclusion**

In this topic, we explored how to map conceptual design into a logical design using ER-to-Relational mapping. We discussed the key concepts of ER modeling, ER-to-Relational mapping, and relational database design. We also provided an example of how to design a database for a university using ER modeling, ER-to-Relational mapping, and relational database design.
