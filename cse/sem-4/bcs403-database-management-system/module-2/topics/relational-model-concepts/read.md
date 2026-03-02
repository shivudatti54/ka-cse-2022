# Relational Model Concepts

## Table of Contents

- [Relational Model Concepts](#relational-model-concepts)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Entities and Entity Sets](#entities-and-entity-sets)
  - [Attributes](#attributes)
  - [Keys](#keys)
  - [Relationships and Relationship Sets](#relationships-and-relationship-sets)
  - [Relational Schema and Instance](#relational-schema-and-instance)
  - [Domains](#domains)
  - [Integrity Constraints](#integrity-constraints)
- [Examples](#examples)
  - [Example 1: Identifying Keys in a Student Database](#example-1-identifying-keys-in-a-student-database)
  - [Example 2: Converting ER Diagram to Relational Schema](#example-2-converting-er-diagram-to-relational-schema)
  - [Example 3: Verifying Referential Integrity](#example-3-verifying-referential-integrity)
- [Exam Tips](#exam-tips)

## Introduction

The Relational Model, introduced by Edgar F. Codd in 1970, represents one of the most significant advancements in database management systems. This model provides a theoretical foundation for organizing and manipulating data in a structured format using tables, also known as relations. The simplicity and mathematical rigor of the relational model have made it the dominant approach to database design and implementation in both academic and industrial settings.

The importance of the relational model in modern computing cannot be overstated. It serves as the backbone for virtually all contemporary database management systems (DBMS) including Oracle, MySQL, PostgreSQL, and Microsoft SQL Server. Understanding relational model concepts is essential for database administrators, software developers, and anyone working with data-intensive applications. The model enables efficient data storage, retrieval, and manipulation while maintaining data integrity and reducing redundancy through normalization processes.

This topic covers the fundamental building blocks of the relational model including entities, attributes, keys, relationships, and various integrity constraints. Mastery of these concepts is crucial for designing efficient database schemas and writing effective SQL queries. The relational model's declarative nature allows users to specify what data they need without worrying about how to physically access it, making it accessible and powerful for both beginners and experienced practitioners.

## Key Concepts

### Entities and Entity Sets

An **entity** represents a real-world object or concept that can be uniquely identified and about which data can be stored. Examples include a student, a product, an employee, or a bank account. Each entity has certain properties or characteristics that describe it, and these properties are called attributes.

An **entity set** is a collection of entities of the same type that share common properties. For example, the set of all students in a university forms the STUDENT entity set. Entity sets are conceptually similar to tables in a relational database, where each row represents an entity and each column represents an attribute.

### Attributes

**Attributes** are the properties or characteristics of entities that hold specific values. In the relational model, attributes correspond to columns in a table. Attributes can be classified into several types:

**Simple Attributes**: Attributes that cannot be divided further into meaningful components. For example, a student's roll number or age.

**Composite Attributes**: Attributes that can be broken down into smaller sub-attributes. For example, a student's address can be divided into street, city, state, and pin code.

**Single-valued Attributes**: Attributes that hold only one value for each entity. For example, a person's date of birth.

**Multi-valued Attributes**: Attributes that can hold multiple values for a single entity. For example, a person may have multiple phone numbers.

**Derived Attributes**: Attributes whose values can be computed from other attributes. For example, a person's age can be derived from their date of birth.

### Keys

Keys play a fundamental role in ensuring data integrity and enabling efficient data retrieval in relational databases.

A **superkey** is an attribute or set of attributes that uniquely identifies each tuple (row) in a relation. A superkey can contain extra attributes beyond what is necessary for uniqueness.

A **candidate key** is a minimal superkey, meaning it is a superkey with no proper subset that is also a superkey. A relation can have multiple candidate keys, and one of these is selected as the primary key.

The **primary key** is the chosen candidate key that uniquely identifies each record in a table. Primary keys cannot contain NULL values and must contain unique values.

A **foreign key** is an attribute or set of attributes in one relation that references the primary key of another relation. Foreign keys establish relationships between tables and enforce referential integrity.

A **unique key** is similar to a primary key but allows NULL values and is not used to identify records uniquely across the entire database.

### Relationships and Relationship Sets

A **relationship** is an association among two or more entities. For example, the relationship "enrolled in" associates students with courses. Relationships can have attributes of their own, called relationship attributes.

A **relationship set** is a collection of relationships of the same type. For instance, all "enrolled in" relationships between students and courses form the ENROLLED relationship set.

**Degree of a Relationship** refers to the number of entity sets participating in a relationship. A relationship involving two entity sets is called a binary relationship, three entity sets makes it ternary, and so on.

**Cardinality** specifies the number of instances of one entity that can be associated with a single instance of another entity. The three main types are:

- **One-to-One (1:1)**: Each entity in one set is associated with at most one entity in the other set
- **One-to-Many (1:M)**: One entity in the first set can be associated with multiple entities in the second set
- **Many-to-Many (M:N)**: Multiple entities in one set can be associated with multiple entities in the other set

### Relational Schema and Instance

A **relational schema** defines the structure of a relation, including its name and the set of attributes along with their domains. For example, STUDENT(Roll_No, Name, Age, Branch) represents a relational schema.

A **relational instance** or **relation state** is the actual data stored in the relation at a particular moment in time. It consists of a set of tuples, where each tuple represents a single record.

### Domains

A **domain** is the set of allowable values for an attribute. Domains define the type of data that can be stored in an attribute and help maintain data integrity. For example, the domain for age might be integers between 15 and 100, while the domain for names might be character strings of length up to 50.

### Integrity Constraints

Integrity constraints ensure that the data in a database remains accurate and consistent.

**Domain Constraints** specify that each attribute must contain values from its defined domain. This includes specifying data types and valid ranges for attributes.

**Key Constraints** require that each relation must have a primary key, and the primary key values must be unique and not NULL.

**Entity Integrity Constraint** states that the primary key cannot contain NULL values. This ensures that each entity can be uniquely identified.

**Referential Integrity Constraint** requires that foreign key values must either match a primary key value in the referenced relation or be NULL. This maintains consistency between related tables.

**Null Constraints** specify whether an attribute can accept NULL values or must have a value.

## Examples

### Example 1: Identifying Keys in a Student Database

Consider a relation STUDENT with attributes: Roll_No, Name, Age, Branch, Email, Phone.

**Solution**:

First, identify all superkeys. A superkey must uniquely identify each tuple. Let's analyze:

- {Roll_No} is a superkey because each student has a unique roll number
- {Email} is a superkey because each student has a unique email
- {Roll_No, Name} is a superkey because roll numbers are already unique
- {Roll_No, Name, Age} is also a superkey

Now, find candidate keys by removing extra attributes:

- {Roll_No} is a candidate key (minimal - removing any attribute leaves just Name, which is not unique)
- {Email} is also a candidate key (minimal)

Since Roll_No is typically chosen as the primary key:

- Primary Key: Roll_No
- Foreign Key: None in this relation (unless referencing another table)
- Unique Key: Email

### Example 2: Converting ER Diagram to Relational Schema

Convert the following scenario to relational schema:

- STORES (Store_ID, Store_Name, Location)
- PRODUCTS (Product_ID, Product_Name, Price)
- A many-to-many relationship "Sells" between STORES and PRODUCTS with attribute Quantity

**Solution**:

For entities, create separate relations:

- STORE(Store_ID, Store_Name, Location)
- PRODUCT(Product_ID, Product_Name, Price)

For the many-to-many relationship "Sells", create a new relation:

- SELLS(Store_ID, Product_ID, Quantity)

Here, Store_ID and Product_ID together form the primary key (composite primary key), and they both serve as foreign keys referencing STORE and PRODUCT tables respectively.

### Example 3: Verifying Referential Integrity

Given two relations:

- EMPLOYEE(Emp_ID, Emp_Name, Dept_ID)
- DEPARTMENT(Dept_ID, Dept_Name, Location)

With Dept_ID in EMPLOYEE referencing DEPARTMENT:

**Valid State Example**:

- EMPLOYEE: {(E01, John, D01), (E02, Mary, D02)}
- DEPARTMENT: {(D01, Sales, Building A), (D02, HR, Building B)}

This satisfies referential integrity because every Dept_ID in EMPLOYEE has a matching Dept_ID in DEPARTMENT.

**Invalid State Example**:

- EMPLOYEE: {(E01, John, D03), (E02, Mary, D02)}
- DEPARTMENT: {(D01, Sales, Building A), (D02, HR, Building B)}

This violates referential integrity because D03 in EMPLOYEE does not exist in DEPARTMENT. The DBMS would reject this transaction or require explicit handling.

## Exam Tips

1. **Remember the order of keys**: Superkey → Candidate Key → Primary Key. Understand that every primary key is a candidate key, and every candidate key is a superkey, but the reverse is not true.

2. **Difference between entity integrity and referential integrity**: Entity integrity applies to primary keys (cannot be NULL), while referential integrity applies to foreign keys (must match primary key values or be NULL).

3. **Multi-valued attributes become separate relations**: When converting ER diagrams to relational schema, multi-valued attributes must be stored in a separate table with a reference to the main entity.

4. **Relationship types determine table creation**: Binary 1:1 relationships can be merged into either entity table; 1:M relationships are implemented by adding the primary key of the "one" side to the "many" side; M:N relationships require a separate relation.

5. **NULL values**: Remember that primary keys cannot have NULL values, but foreign keys can have NULL values when appropriate.

6. **Composite keys**: When a primary key consists of multiple attributes, all attributes together must be unique, but individual attributes need not be unique.

7. **Domain constraints**: Always consider data types, length, and valid ranges when defining attributes in a relational schema.
