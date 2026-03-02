# Relational Database Design Using ER-to-Relational Mapping

## Table of Contents

- [Relational Database Design Using ER-to-Relational Mapping](#relational-database-design-using-er-to-relational-mapping)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Fundamentals of ER-to-Relational Mapping](#fundamentals-of-er-to-relational-mapping)
  - [Mapping Regular Entity Sets](#mapping-regular-entity-sets)
  - [Mapping Weak Entity Sets](#mapping-weak-entity-sets)
  - [Mapping Binary 1:1 Relationships](#mapping-binary-11-relationships)
  - [Mapping Binary 1:N Relationships](#mapping-binary-1n-relationships)
  - [Mapping Binary N:M Relationships](#mapping-binary-nm-relationships)
  - [Mapping Multi-valued Attributes](#mapping-multi-valued-attributes)
  - [Mapping Attributes with Default Values](#mapping-attributes-with-default-values)
  - [Handling Derived Attributes](#handling-derived-attributes)
  - [Mapping Participation Constraints](#mapping-participation-constraints)
- [Examples](#examples)
  - [Worked Example 1: Comprehensive Mapping](#worked-example-1-comprehensive-mapping)
  - [Worked Example 2: Handling Complex Constraints](#worked-example-2-handling-complex-constraints)
  - [Worked Example 3: N-ary Relationship Mapping](#worked-example-3-n-ary-relationship-mapping)
- [Exam Tips](#exam-tips)

## Introduction

Relational Database Design is a critical phase in the database development lifecycle that transforms conceptual data models into implementable database structures. The ER-to-Relational mapping process is a systematic approach that converts an Entity-Relationship (ER) diagram into a set of relational schemas, making the design ready for implementation in relational database management systems like MySQL, PostgreSQL, or Oracle.

This mapping process is essential because the ER model provides a high-level, abstract representation of data requirements, while the relational model offers a concrete, implementation-ready structure. Understanding this transformation is fundamental for database designers, as it bridges the gap between conceptual design and logical design phases. The process ensures that all entities, attributes, relationships, and constraints defined in the ER model are accurately represented in the relational schema.

In the context of the university's BCS403 Database Management System, this topic carries significant weightage in examinations. Students must master various mapping rules for different types of entities, relationships, and constraints. The ability to systematically convert ER diagrams to relational schemas demonstrates a student's comprehensive understanding of both conceptual and logical database design.

## Key Concepts

### Fundamentals of ER-to-Relational Mapping

The mapping process follows a set of well-defined rules that transform each component of the ER model into corresponding relational constructs. The primary components that require mapping include entity sets, weak entity sets, relationship sets, attributes (simple, composite, and multi-valued), and various types of constraints.

The overall mapping algorithm follows these steps in sequence:

1. **Mapping of Regular (Strong) Entity Sets**: Create a relation for each strong entity set
2. **Mapping of Weak Entity Sets**: Create a relation including the primary key of the owner entity
3. **Mapping of Binary 1:1 Relationships**: Handle through foreign key or merge approaches
4. **Mapping of Binary 1:N Relationships**: Implement using foreign key in the "many" side
5. **Mapping of Binary N:M Relationships**: Create a new relation with foreign keys
6. **Mapping of Multi-valued Attributes**: Create a separate relation
7. **Mapping of N-ary Relationships**: Create a new relation with all participating keys

### Mapping Regular Entity Sets

For each regular (strong) entity set in the ER diagram, create a relational schema with the same name as the entity set. Include all simple attributes of the entity set in the relation. For composite attributes, include only the simple component attributes.

**Example**: Consider an entity set **STUDENT** with attributes: Student_ID (primary key), Name (composite with First_Name and Last_Name), Age, and Address (composite with Street and City).

The mapped relation would be:

```
STUDENT(Student_ID, First_Name, Last_Name, Age, Street, City)
```

Here, Student_ID serves as the primary key, and the composite attribute Name has been decomposed into its constituent attributes First_Name and Last_Name.

### Mapping Weak Entity Sets

Weak entity sets depend on strong entities for their identity and cannot exist independently. The mapping process creates a relation that includes all attributes of the weak entity set, plus the primary key of the owner entity set as a foreign key. The combination of the foreign key and the partial key of the weak entity forms the composite primary key.

**Example**: Consider a weak entity set **DEPENDENT** belonging to an entity set **EMPLOYEE**, where Employee_ID is the primary key of EMPLOYEE, and Dependent_Name is the partial key of DEPENDENT.

The mapped relation would be:

```
DEPENDENT(Employee_ID, Dependent_Name, Relationship, Date_of_Birth)
```

The primary key is (Employee_ID, Dependent_Name), where Employee_ID is a foreign key referencing EMPLOYEE.

### Mapping Binary 1:1 Relationships

Three different approaches exist for mapping binary 1:1 relationships:

**Approach 1: Foreign Key Approach**
Choose one of the participating entity sets (preferably the one with total participation) and include the primary key of the other entity as a foreign key in its relation. This is the most commonly used approach.

**Example**: Consider a 1:1 relationship **MANAGES** between DEPARTMENT and EMPLOYEE, where each department has one manager (total participation on DEPARTMENT side).

The mapped relations would be:

```
DEPARTMENT(Dept_ID, Dept_Name, Manager_ID)
EMPLOYEE(Emp_ID, Emp_Name, Salary)
```

Here, Manager_ID in DEPARTMENT is a foreign key referencing EMPLOYEE.

**Approach 2: Merge Approach**
If both entity sets have total participation, merge them into a single relation.

**Approach 3: Cross-Reference Approach**
Create a separate relation containing the primary keys of both entity sets. This approach is less frequently used for 1:1 relationships.

### Mapping Binary 1:N Relationships

For binary 1:N relationships, the mapping is straightforward. The entity on the N-side (many side) includes the primary key of the entity on the 1-side (one side) as a foreign key. This foreign key represents the relationship.

**Example**: Consider a 1:N relationship **WORKS_IN** between EMPLOYEE and DEPARTMENT, where an employee works in one department and a department can have multiple employees.

The mapped relations would be:

```
DEPARTMENT(Dept_ID, Dept_Name)
EMPLOYEE(Emp_ID, Emp_Name, Dept_ID)
```

Here, Dept_ID in EMPLOYEE is a foreign key referencing DEPARTMENT. This foreign key attribute represents the WORKS_IN relationship.

### Mapping Binary N:M Relationships

Many-to-many relationships cannot be represented using foreign keys alone. The mapping requires creating a new relation (sometimes called a junction table or associative relation) that includes the primary keys of both participating entity sets as a composite foreign key. The primary key of the new relation is the combination of these foreign keys.

**Example**: Consider an N:M relationship **ENROLLED** between STUDENT and COURSE, where a student can enroll in multiple courses and each course can have multiple students.

The mapped relations would be:

```
STUDENT(Student_ID, Student_Name, Age)
COURSE(Course_ID, Course_Name, Credits)
ENROLLED(Student_ID, Course_ID, Enrollment_Date, Grade)
```

The primary key of ENROLLED is (Student_ID, Course_ID), and both attributes serve as foreign keys referencing STUDENT and COURSE respectively.

### Mapping Multi-valued Attributes

Multi-valued attributes cannot be stored within the main entity relation because they can have multiple values for a single entity instance. A separate relation is created to store these attributes, with the primary key of the main entity included as a foreign key.

**Example**: Consider an entity set STUDENT with a multi-valued attribute Phone_Number.

The mapped relations would be:

```
STUDENT(Student_ID, Student_Name, Age)
PHONE(Student_ID, Phone_Number)
```

The primary key of PHONE is (Student_ID, Phone_Number), and Student_ID is a foreign key referencing STUDENT.

### Mapping Attributes with Default Values

When mapping attributes that have default values defined in the ER model, the default value is specified during table creation in SQL. For example, if a Student entity has an attribute Status with a default value as "Active", this constraint is enforced during table creation.

### Handling Derived Attributes

Derived attributes are those whose values can be computed from other attributes. In the ER-to-relational mapping, derived attributes are not stored in the database. Instead, they are computed when needed using queries or views.

**Example**: If the ER model includes a derived attribute Age computed from Date_of_Birth, the mapped relation would include only Date_of_Birth, and Age would be computed as needed using database functions.

### Mapping Participation Constraints

Participation constraints specify whether the existence of an entity depends on its association with another entity through a relationship. Total participation (existence dependency) means every entity in the set must participate in the relationship, while partial participation allows optional participation.

In the relational model, total participation is enforced through NOT NULL constraints on foreign keys. For example, if an EMPLOYEE must work in a DEPARTMENT (total participation), the Dept_ID foreign key in EMPLOYEE would have a NOT NULL constraint.

## Examples

### Worked Example 1: Comprehensive Mapping

**Problem**: Map the following ER diagram to relational schemas:

An entity set **LIBRARY** with attributes: Library_ID (PK), Library_Name, Address
An entity set **BOOK** with attributes: Book_ID (PK), Title, ISBN, Publisher
A weak entity set **COPY** with attributes: Copy_Number, Condition, belonging to LIBRARY
A 1:N relationship **HOUSES** between LIBRARY and COPY
A N:M relationship **AUTHORED** between BOOK and AUTHOR (not shown, assume exists)
An entity set **AUTHOR** with attributes: Author_ID (PK), Author_Name

**Solution**:

1. **Mapping LIBRARY (Regular Entity Set)**:

```
LIBRARY(Library_ID, Library_Name, Address)
```

2. **Mapping BOOK (Regular Entity Set)**:

```
BOOK(Book_ID, Title, ISBN, Publisher)
```

3. **Mapping AUTHOR (Regular Entity Set)**:

```
AUTHOR(Author_ID, Author_Name)
```

4. **Mapping COPY (Weak Entity Set)**:
   The owner is LIBRARY, so we include Library_ID as foreign key:

```
COPY(Library_ID, Copy_Number, Condition)
```

Primary Key: (Library_ID, Copy_Number)

5. **Mapping HOUSES (1:N Relationship)**:
   Since COPY is on the many side, we add Library_ID to COPY relation (already done above as COPY is weak entity with owner LIBRARY)

6. **Mapping AUTHORED (N:M Relationship)**:
   Create a junction table:

```
AUTHORED(Book_ID, Author_ID)
```

Primary Key: (Book_ID, Author_ID)

### Worked Example 2: Handling Complex Constraints

**Problem**: Map the following scenario:

**HOSPITAL** entity set with attributes: Hospital_ID (PK), Hospital_Name, Location
**DOCTOR** entity set with attributes: Doctor_ID (PK), Doctor_Name, Specialization
A 1:1 relationship **HEAD** where HOSPITAL has total participation and DOCTOR has partial participation
A 1:N relationship **WORKS** where DOCTOR works in HOSPITAL
A multi-valued attribute Phone for HOSPITAL
A derived attribute Doctor_Count for HOSPITAL (computed from number of doctors)

**Solution**:

1. **Mapping HOSPITAL**:

```
HOSPITAL(Hospital_ID, Hospital_Name, Location)
```

2. **Mapping Phone (Multi-valued attribute)**:

```
PHONE(Hospital_ID, Phone_Number)
```

3. **Mapping DOCTOR**:

```
DOCTOR(Doctor_ID, Doctor_Name, Specialization, Hospital_ID)
```

Here, Hospital_ID serves dual purpose: represents WORKS relationship (1:N) and is also the foreign key for HEAD relationship (1:1)

4. **For HEAD relationship**: Since HOSPITAL has total participation, we include Doctor_ID in HOSPITAL with NOT NULL constraint:

```
HOSPITAL(Hospital_ID, Hospital_Name, Location, Head_Doctor_ID)
```

Head_Doctor_ID is foreign key referencing DOCTOR with NOT NULL constraint

5. **Doctor_Count** is a derived attribute and is not stored; it would be computed when needed

### Worked Example 3: N-ary Relationship Mapping

**Problem**: Map a ternary relationship **ENROLL** between STUDENT, COURSE, and SEMESTER with attributes Enrollment_Date and Grade.

**Solution**: For N-ary relationships where N > 2, create a separate relation including foreign keys to all participating entity sets:

```
STUDENT(Student_ID, Student_Name)
COURSE(Course_ID, Course_Name)
SEMESTER(Semester_ID, Term, Year)
ENROLL(Student_ID, Course_ID, Semester_ID, Enrollment_Date, Grade)
```

Primary Key of ENROLL: (Student_ID, Course_ID, Semester_ID)
All three foreign keys reference their respective tables.

## Exam Tips

1. **Always identify entity types first**: Begin mapping by creating relations for all regular (strong) entity sets, as they form the foundation of the schema.

2. **Remember weak entity mapping rule**: Weak entities always include the primary key of their owner entity as part of their primary key and as a foreign key.

3. **1:N relationship handling**: For 1:N relationships, always add the primary key of the "one" side entity to the "many" side entity's relation.

4. **N:M requires new relation**: Never attempt to represent many-to-many relationships using a single foreign key; always create a junction table.

5. **Multi-valued attributes**: These always require a separate relation with a composite primary key consisting of the owner entity's key and the multi-valued attribute.

6. **Primary key selection**: When creating junction tables for N:M or N-ary relationships, the primary key is typically the combination of all foreign keys.

7. **Participation constraints**: Use NOT NULL constraints to enforce total participation in the relational schema.

8. **Composite attributes**: Decompose composite attributes into their simple component attributes during mapping.

9. **Avoid storing derived attributes**: Derived attributes should be computed when needed, not stored in the database.

10. **ER diagram interpretation**: Carefully analyze the ER diagram to identify cardinality ratios (1:1, 1:N, N:M) and participation constraints before applying mapping rules.

11. **N-ary relationships**: Remember that any relationship with degree greater than 2 requires a separate relation with foreign keys to all participating entities.

12. **Review your mapping**: After mapping, verify that all original ER diagram components are represented and all relationships can be navigated.
