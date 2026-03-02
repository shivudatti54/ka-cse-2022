# ER Diagrams (Entity-Relationship Diagrams)

## Table of Contents

- [ER Diagrams (Entity-Relationship Diagrams)](#er-diagrams-entity-relationship-diagrams)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Entities and Entity Sets](#entities-and-entity-sets)
  - [Attributes](#attributes)
  - [Keys](#keys)
  - [Relationships and Relationship Sets](#relationships-and-relationship-sets)
  - [Cardinality](#cardinality)
  - [Participation Constraints](#participation-constraints)
  - [Enhanced ER Diagrams](#enhanced-er-diagrams)
- [Examples](#examples)
  - [Example 1: University Database ER Diagram](#example-1-university-database-er-diagram)
  - [Example 2: Library Management System](#example-2-library-management-system)
  - [Example 3: Banking System with Weak Entity](#example-3-banking-system-with-weak-entity)
- [Exam Tips](#exam-tips)

## Introduction

Entity-Relationship (ER) Diagrams are fundamental modeling tools used in database design to represent the logical structure of data in a system. Developed by Peter Chen in 1976, ER modeling provides a visual representation of entities, their attributes, and the relationships between them. This conceptual model serves as a blueprint for designing relational databases and is essential for understanding how data elements interact within an organization.

ER diagrams play a crucial role in the database development lifecycle, particularly in the requirements gathering and conceptual design phases. They help database designers, stakeholders, and developers communicate effectively about the data requirements of a system. By abstracting real-world objects into entities and defining their associations, ER diagrams bridge the gap between human understanding and technical implementation. Whether designing a simple student record system or a complex enterprise resource planning application, ER modeling provides the foundation for creating well-structured, efficient databases that accurately represent business requirements.

## Key Concepts

### Entities and Entity Sets

An **entity** represents a real-world object or concept that can be uniquely identified and about which data is stored. Examples include Student, Employee, Product, or Account. An **entity set** is a collection of similar entities that share the same properties or attributes. For instance, all students in a university form the Student entity set. Entities are represented as rectangles in ER diagrams, with the entity name written inside.

Entities are classified into two categories: **strong entities** and **weak entities**. A strong entity has a primary key that uniquely identifies each instance and does not depend on any other entity for its existence. For example, Department is a strong entity because each department has a unique Department_ID. A weak entity, on the other hand, depends on a strong entity for its identification and cannot exist independently. The primary key of a weak entity is typically a combination of its own partial key and the primary key of the owning strong entity. Example: Dependent entity weak to Employee entity.

### Attributes

**Attributes** are properties or characteristics of entities that hold specific information. Each attribute has a domain (set of permissible values). Attributes are represented as ovals connected to their respective entities in ER diagrams.

Types of attributes include:

- **Simple Attributes**: Indivisible attributes that cannot be broken down further, such as Age or Salary
- **Composite Attributes**: Attributes that can be divided into smaller components, such as Address (which can be split into Street, City, State, Zip)
- **Single-Valued Attributes**: Attributes that hold only one value for each entity instance, such as Date_of_Birth
- **Multi-Valued Attributes**: Attributes that can hold multiple values for each entity instance, such as Phone_Numbers or Email_Addresses (represented as double ovals)
- **Derived Attributes**: Attributes whose values can be computed from other attributes, such as Age (derived from Date_of_Birth), represented with dashed lines

### Keys

Keys are essential for uniquely identifying entities within an entity set:

- **Candidate Key**: A minimal set of attributes that can uniquely identify an entity
- **Primary Key**: The selected candidate key used to uniquely identify entities (represented with underline)
- **Alternate Key**: Candidate keys not chosen as primary key
- **Foreign Key**: An attribute that references the primary key of another entity, used to establish relationships

### Relationships and Relationship Sets

A **relationship** represents an association between two or more entities. A **relationship set** is a collection of similar relationships. Relationships are represented as diamonds in ER diagrams, connecting the participating entities.

Types of relationship attributes include descriptive attributes that provide additional information about the relationship itself, such as the date when a relationship was established.

### Cardinality

**Cardinality** specifies the number of instances of one entity that can be associated with a single instance of another entity. The three types of cardinality are:

- **One-to-One (1:1)**: Each entity in one set is associated with exactly one entity in the other set. Example: One Department has one Manager.
- **One-to-Many (1:N)**: One entity is associated with multiple entities in the other set. Example: One Department has many Employees.
- **Many-to-Many (M:N)**: Multiple entities are associated with multiple entities in the other set. Example: Students enroll in many Courses, and Courses have many Students.

### Participation Constraints

Participation constraints define whether the existence of an entity depends on its association with another entity:

- **Total Participation (Mandatory)**: Every entity in the entity set must participate in the relationship. Denoted by double lines connecting entity to relationship. Example: Every Employee must work in a Department.
- **Partial Participation (Optional)**: Entities may or may not participate in the relationship. Denoted by single lines. Example: An Employee may manage a Department (optional).

### Enhanced ER Diagrams

Enhanced ER diagrams extend basic ER modeling with additional concepts:

- **Specialization**: Top-down process of identifying subcategories of an entity. Example: Employee specialized into Manager, Engineer, Technician.
- **Generalization**: Bottom-up process of combining similar entities into a higher-level entity. Example: Car, Truck, Bus generalized into Vehicle.
- **Aggregation**: Treating a relationship as a higher-level entity to represent relationships between relationships.
- **Composition**: Strong entity that owns its weak entities; if the parent is deleted, child entities are automatically deleted.

## Examples

### Example 1: University Database ER Diagram

**Problem**: Design an ER diagram for a university database with the following requirements:

- The university has multiple departments
- Each department has a unique ID, name, and location
- Each department offers various courses
- Each course has course code, title, and credits
- Students enroll in courses
- Professors teach courses

**Solution**:

**Step 1: Identify Entities**

- Department (Strong Entity)
- Course (Strong Entity)
- Student (Strong Entity)
- Professor (Strong Entity)

**Step 2: Identify Attributes**

- Department: Dept_ID (PK), Dept_Name, Location
- Course: Course_Code (PK), Title, Credits
- Student: Student_ID (PK), Name, Date_of_Birth, Address
- Professor: Professor_ID (PK), Name, Specialization, Salary

**Step 3: Identify Relationships**

- Department offers Course (1:N)
- Professor teaches Course (1:N or M:N depending on interpretation)
- Student enrolls in Course (M:N) - with attribute Enrollment_Date

**Step 4: Identify Cardinality and Participation**

- Department (1) → offers → Course (N): Total participation for Course
- Professor (1) → teaches → Course (N): Partial participation
- Student (M) → enrolls → Course (N): Total participation for enrollment

### Example 2: Library Management System

**Problem**: Create an ER diagram for a library system where:

- Library has members
- Members can borrow books
- Each book has multiple copies
- Authors write books
- Publishers publish books

**Solution**:

**Entities**:

- Member (Member_ID as PK, Name, Address, Membership_Date)
- Book (ISBN as PK, Title, Edition, Year)
- Copy (Copy_ID as PK, Status) - Weak entity dependent on Book
- Author (Author_ID as PK, Name, Biography)
- Publisher (Publisher_ID as PK, Name, Address)

**Relationships**:

- Member borrows Copy (1:M with attribute Borrow_Date, Return_Date)
- Author writes Book (M:N with attribute Contribution_Type)
- Publisher publishes Book (1:N)

**Key Constraints**:

- Total participation of Copy in "borrows" relationship
- Total participation of Book in "writes" relationship

### Example 3: Banking System with Weak Entity

**Problem**: Design ER diagram for a bank where:

- Accounts belong to customers
- Each account has multiple transactions
- A customer can have joint accounts

**Solution**:

**Entities**:

- Customer (Customer_ID as PK, Name, Address, Phone)
- Account (Account_Number as PK, Type, Balance, Open_Date) - Could be weak if Account_Number is not globally unique
- Transaction (Transaction_ID as PK, Date, Amount, Type) - Weak entity

**Relationships**:

- Customer owns Account (1:N)
- Account has Transaction (1:N)

**Key Points**:

- Account is weak entity with Customer as owner (Account_Number + Customer_ID as composite key)
- Transaction is weak entity with Account as owner
- Joint account represented by relationship with both customers participating

## Exam Tips

1. **Remember Chen's Notation**: For university exams, understand both Chen notation (diamond for relationships, oval for attributes) and alternative notations like Crow's Foot notation commonly used in industry.

2. **Identifying Keys**: Always clearly underline primary keys in ER diagrams. Remember that a weak entity's primary key is the combination of its partial key and the owning entity's primary key.

3. **Cardinality Determination**: When asked to determine cardinality, read the sentence carefully: "Department has many Employees" indicates 1:N relationship from Department to Employee.

4. **Participation Constraints**: Draw double lines for total participation and single lines for partial participation. Total participation means the entity cannot exist without the relationship.

5. **Converting M:N to Relational Schema**: Remember that many-to-many relationships become separate tables with foreign keys referencing both participating entities.

6. **Enhanced ER Concepts**: Understand the difference between specialization (is-a relationship going downward) and generalization (is-a relationship going upward). Use triangles or circles with "ISA" for these.

7. **Common ERD Errors to Avoid**: Not identifying all necessary entities, missing attributes, incorrect cardinalities, and confusing weak entities with strong entities are common mistakes that examiners look for.
