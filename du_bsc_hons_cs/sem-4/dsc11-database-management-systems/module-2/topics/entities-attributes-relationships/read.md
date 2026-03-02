# Entities, Attributes, and Relationships in DBMS

## Introduction

The Entity-Relationship (ER) model, developed by Peter Chen in 1976, serves as the foundational blueprint for designing relational databases. It provides a high-level, abstract view of data that enables database designers to conceptualize the logical structure of a database before implementing it physically. For students pursuing Computer Science at the University of Delhi, understanding ER modeling is not merely an academic exercise—it forms the critical first step in building robust, efficient, and scalable database systems that power modern applications.

The ER model represents real-world scenarios by identifying **entities** (objects that exist and can be distinctly identified), **attributes** (properties that describe entities), and **relationships** (associations between entities). This three-component approach mirrors how humans naturally perceive the world, making it an intuitive yet powerful tool for database design. Whether you are designing a student information system for a college like Miranda House or a library management system for Hindu College, the ER model provides the systematic methodology needed to transform vague requirements into a structured database schema.

In the context of DU's Computer Science curriculum, this topic carries significant weight in both internal assessments and end-semester examinations. A strong grasp of entities, attributes, and relationships directly prepares students for questions on ER diagram construction, entity set identification, and relationship modeling—all essential skills for database administrators and software developers.

## Key Concepts

### Entities and Entity Sets

An **entity** is a real-world object or concept that exists and can be uniquely identified from other objects. Examples include a specific student (like a student named "Aditi" at SRCC), a particular book in a library, or an individual employee in a company. Entities possess distinct existence and can be either concrete (such as a person, car, or product) or abstract (such as a course, account, or loan).

An **entity set** is a collection of entities of the same type that share common properties or attributes. For instance, the entity set "STUDENT" encompasses all students in the university; the entity set "COURSE" includes all courses offered by the Department of Computer Science. Entity sets are typically represented as rectangles in ER diagrams, with the entity set name written in uppercase.

It is crucial to distinguish between an entity and an entity set: an entity represents a single instance, while an entity set represents a collection. Think of it as the difference between a specific book (entity) and the entire library collection (entity set).

### Attributes

**Attributes** are properties or characteristics that describe an entity. Each attribute assigns a value to an entity's characteristic. In the ER diagram, attributes are represented as ovals connected to their corresponding entity sets by straight lines.

#### Types of Attributes

**Simple attributes** (or atomic attributes) cannot be divided further. Examples include `age`, `salary`, or `roll_number`. These are represented as single ovals in ER diagrams.

**Composite attributes** can be broken down into smaller components that carry independent meaning. For instance, the attribute `address` can be decomposed into `street`, `city`, `state`, and `pin_code`. The `name` attribute can be split into `first_name`, `middle_name`, and `last_name`. Composite attributes are depicted as ovals connected to other ovals representing their component simple attributes.

**Single-valued attributes** hold exactly one value for a particular entity. For example, a student has exactly one `date_of_birth` and one `CGPA`.

**Multi-valued attributes** can have multiple values for a single entity. Examples include `phone_number` (a student may have multiple phone numbers), `email` (multiple email addresses), or `qualification` (multiple degrees). In ER diagrams, multi-valued attributes are represented by double ovals.

**Derived attributes** are those whose values can be computed from other related attributes. For instance, `age` can be derived from `date_of_birth`, and `experience` can be calculated from `date_of_joining`. Derived attributes are shown as dashed or dotted ovals in ER diagrams.

Every entity in an entity set must have a **key attribute**—an attribute (or combination of attributes) that uniquely identifies each entity within the set. For the STUDENT entity set, `roll_number` serves as the key attribute. Key attributes are underlined in ER diagrams.

### Relationships and Relationship Sets

A **relationship** is an association between two or more entities. For example, "Aditi enrolls in Database Systems" represents a relationship between the student entity "Aditi" and the course entity "Database Systems."

A **relationship set** is a collection of relationships of the same type. It represents the logical association among entity sets. In ER diagrams, relationship sets are represented as diamonds connected to the participating entity sets by straight lines.

Consider the relationship "ENROLLED_IN" that connects STUDENT and COURSE entity sets. This relationship set encompasses all such enrollment associations in the university.

#### Degree of a Relationship

The **degree** of a relationship refers to the number of entity sets participating in that relationship:

- **Unary relationships** (or recursive relationships) involve only one entity set associating with itself. Example: an employee manages another employee. The "MANAGES" relationship has the EMPLOYEE entity set participating twice (once as manager, once as managed).

- **Binary relationships** involve exactly two entity sets. These are the most common type in database design. Example: STUDENT takes COURSE, or EMPLOYEE works in DEPARTMENT.

- **Ternary relationships** involve three entity sets. Example: PROFESSOR teaches COURSE in DEPARTMENT—here, three entity sets participate in a single relationship.

- **N-ary relationships** involve more than two entity sets. While possible, they are less common and often can be decomposed into binary relationships for simplicity.

#### Relationship Cardinality

**Cardinality** specifies the number of instances of one entity that can be associated with a single instance of another entity. The three main types are:

**One-to-One (1:1)**: Each entity in one entity set is associated with exactly one entity in the other set. Example: each student is assigned one unique locker, and each locker is assigned to one student. In ER diagrams, cardinality is indicated by placing "1" near the entity sets connected to the relationship.

**One-to-Many (1:N)** or **Many-to-One (N:1)**: One entity in the first set is associated with multiple entities in the second set, but each entity in the second set is associated with only one entity in the first. Example: a department has many employees, but each employee belongs to exactly one department.

**Many-to-Many (M:N)**: Entities on both sides can have multiple associations. Example: a student can enroll in many courses, and a course can have many students enrolled.

#### Participation Constraints

**Total participation** (or existence dependency) means that every entity in an entity set must participate in at least one relationship of that type. In ER diagrams, total participation is shown by a double line connecting the entity set to the relationship. For instance, every student must enroll in at least one course—STUDENT has total participation in the ENROLLED_IN relationship.

**Partial participation** (or existence independence) means an entity may or may not participate in any relationship of that type. Represented by a single line. For example, a professor may or may not supervise any student research projects.

### Weak Entities

A **weak entity** is an entity that cannot be uniquely identified by its own attributes alone and relies on another entity (called the identifying or owner entity) for its identification. The weak entity's primary key is a combination of its own partial key and the primary key of the related strong entity.

For example, consider a university database where `DEPENDENT` is a weak entity under `EMPLOYEE`. A dependent (like a child or spouse of an employee) cannot be uniquely identified by `dependent_name` alone, as multiple employees might have dependents with the same name. The identification requires combining `employee_id` (from EMPLOYEE) with `dependent_name` (the partial key of DEPENDENT).

Weak entities are represented by double rectangles in ER diagrams, and their identifying relationships are shown with double diamonds. Weak entity attributes that are part of the composite key are underlined with a dashed line.

## Examples

### Example 1: University Database ER Diagram

Consider designing a database for a DU college with the following requirements:
- The college offers multiple programs (B.Sc, B.Com, B.A.)
- Students enroll in programs and register for courses
- Professors teach courses
- Each course belongs to one department

**Solution:**

Entity Sets:
- STUDENT (key: roll_number)
- COURSE (key: course_code)
- PROFESSOR (key: professor_id)
- PROGRAM (key: program_code)
- DEPARTMENT (key: dept_id)

Relationships:
- ENROLLED_IN: STUDENT-PROGRAM (1:N)
- OFFERED_BY: COURSE-DEPARTMENT (N:1)
- TEACHES: PROFESSOR-COURSE (1:N, total participation on COURSE side)
- REGISTERED_IN: STUDENT-COURSE (M:N)

Attributes:
- STUDENT: roll_number (key), student_name, dob, email, phone
- COURSE: course_code (key), course_name, credits
- PROFESSOR: professor_id (key), prof_name, qualification, salary
- PROGRAM: program_code (key), program_name, duration
- DEPARTMENT: dept_id (key), dept_name, location

### Example 2: Library Management System

Design an ER diagram for a college library where:
- Members can borrow multiple books
- Books have multiple copies
- Each book borrowing is tracked with return date
- Authors write multiple books, books can have multiple authors

**Solution:**

Entity Sets:
- MEMBER (key: member_id)
- BOOK (key: isbn)
- COPY (key: copy_id) - Weak entity under BOOK
- AUTHOR (key: author_id)
- BORROW (relationship between MEMBER and COPY)

Relationships:
- BORROWS: MEMBER-COPY (1:N)
- HAS: BOOK-COPY (1:N, total participation for COPY)
- WRITTEN_BY: BOOK-AUTHOR (M:N)

Key insight: The COPY entity is weak because copy_id alone doesn't uniquely identify a copy—we need the book's isbn to fully identify it.

### Example 3: Identifying Entity Types and Attributes

For an online examination system:
- Students appear for tests
- Each test has multiple questions
- Questions have options (multiple choice)
- Students submit answers

**Solution:**

Entity Sets and their attributes:
- STUDENT: student_id (key), name, email, password
- TEST: test_id (key), test_name, duration, total_marks
- QUESTION: question_id (key), question_text, marks, correct_option
- OPTION: option_id (key), option_text (composite: option_a, option_b, option_c, option_d)
- SUBMISSION: (relationship entity capturing student responses)

Relationships:
- APPEARS_FOR: STUDENT-TEST (M:N)
- CONTAINS: TEST-QUESTION (1:N)
- HAS: QUESTION-OPTION (1:N, since each question has multiple options)
- SUBMITS: STUDENT-TEST (derived through SUBMISSION relationship)

## Exam Tips

1. **Carefully identify entity sets**: Look for nouns in the problem statement that represent objects with independent existence. Students, courses, professors, departments are typical entities in university databases.

2. **Distinguish between attributes and entities**: If something can exist independently and has its own attributes, it is likely an entity. Attributes describe entities.

3. **Remember to underline key attributes**: In ER diagrams, primary keys must be underlined. Composite keys have all participating attributes underlined.

4. **Cardinality direction matters**: When specifying 1:N, ensure you identify which side is "1" and which is "N" based on the business rule.

5. **Use double lines for total participation**: This is a common exam question—identifying which entity has total participation in a relationship.

6. **Weak entity identification**: Ask yourself—can this entity exist independently? If not, and it needs another entity to identify it uniquely, it is weak.

7. **Relationship naming**: Use meaningful names like "ENROLLED_IN" or "TEACHES" rather than vague terms. Active verbs work best.

8. **Multi-valued vs derived attributes**: Multi-valued attributes (like phone_number) become separate tables, while derived attributes (like age) are not stored but computed when needed.

9. **Practice diagram drawing**: ER diagrams are visual—practice drawing clean, properly labeled diagrams. Use standard notation (rectangles for entities, ovals for attributes, diamonds for relationships).

10. **Convert M:N to associative entity**: In practical implementation, many-to-many relationships become separate tables in the relational model.