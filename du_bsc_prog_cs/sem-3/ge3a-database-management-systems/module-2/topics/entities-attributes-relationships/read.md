# Entity-Relationship Model: Entities, Attributes, and Relationships

## Introduction

The Entity-Relationship (E-R) model, proposed by Peter Chen in 1976, serves as the foundational conceptual framework for designing databases. It provides a systematic approach to representing real-world data by identifying key components: entities, attributes, and relationships. This model acts as a blueprint for database construction, enabling designers to translate complex business requirements into a structured format that can be easily understood by stakeholders and implemented using relational database management systems.

In the context of University of Delhi's Computer Science curriculum, understanding the E-R model is crucial because it forms the bridge between abstract business requirements and physical database implementation. Whether you are designing a student information system for a college, an inventory management system for a retail store, or a hospital management system, the E-R model provides the necessary tools to capture data semantics accurately. The internal assessment and end semester examinations frequently test students' ability to draw E-R diagrams and convert them into relational schemas, making this topic absolutely essential for scoring well in DBMS papers.

## Key Concepts

### Entities and Entity Sets

An **entity** represents a real-world object or concept that exists independently and can be uniquely identified. Examples include a specific student, a particular course, an individual employee, or a singular product. Entities possess attributes that describe their properties, and each entity in an entity set shares the same attributes, though with different values.

An **entity set** is a collection of entities of the same type that share common properties. For instance, the set of all students enrolled in Delhi University colleges constitutes the Student entity set. Similarly, all courses offered by the university form the Course entity set. Entity sets are typically represented as rectangles in E-R diagrams, with the entity set name written inside.

It is important to distinguish between entity and entity set. While an entity refers to a single instance (like "Rahul Sharma"), an entity set refers to the collection of all such entities (like "all students"). In E-R diagrams, we typically draw the entity set, not individual entities.

**Strong and Weak Entities:** A strong entity is one that has a primary key and can exist independently. For example, a Student entity with a unique Roll Number is a strong entity. A weak entity, on the other hand, does not have a primary key of its own and depends on a strong entity for identification. The primary key of a weak entity is a combination of its partial key and the primary key of the owning strong entity. For instance, in a university database, the "Subject" entity might be weak if it depends on a "Department" strong entity—two departments might both have a subject called "Database Systems," so the subject is identified by its name combined with the department's ID.

### Attributes

**Attributes** are properties or characteristics of entities that hold information we want to store about them. Each attribute has a domain—the set of allowable values it can take. Attributes are represented as ovals in E-R diagrams, connected to their respective entity sets by lines.

**Types of Attributes:**

**Simple vs. Composite Attributes:** Simple attributes cannot be divided further and consist of a single atomic value. Examples include Age, Salary, or RollNumber. Composite attributes can be broken down into smaller components that carry independent meaning. For instance, the attribute "Name" can be decomposed into "FirstName," "MiddleName," and "LastName"; "Address" can be split into "Street," "City," "State," and "PinCode." The decision to decompose an attribute depends on whether we need to access its components individually in queries.

**Single-valued vs. Multi-valued Attributes:** Single-valued attributes hold exactly one value for each entity, such as DateOfBirth or MobileNumber. Multi-valued attributes can hold multiple values for a single entity—for example, a student might have multiple phone numbers or email addresses. In E-R diagrams, multi-valued attributes are represented by double ovals. In relational database implementation, multi-valued attributes typically require creating a separate relation.

**Derived Attributes:** Derived attributes are those whose values can be calculated or derived from other attributes rather than stored explicitly. For example, "Age" can be derived from "DateOfBirth" by calculating the difference from the current date. Similarly, "TotalMarks" can be derived by summing marks from individual subjects. Derived attributes are represented by dashed ovals in E-R diagrams. While they help in understanding the model, they are usually not stored in the database to avoid redundancy and update anomalies.

**Key Attributes:** A key attribute is an attribute or combination of attributes that uniquely identifies each entity in an entity set. The primary key concept in relational databases originates from key attributes in the E-R model. For the Student entity set, RollNumber serves as a key attribute; for Course, CourseCode is the key. Key attributes are underlined in E-R diagrams.

### Relationships and Relationship Sets

A **relationship** represents an association or connection between two or more entities. For example, the relationship "Enrolled" connects Student entities with Course entities—a student enrolls in a course. Similarly, "Teaches" connects Teacher entities with Course entities.

A **relationship set** is a collection of relationships of the same type. It consists of all instances of relationships between entities from participating entity sets. In E-R diagrams, relationship sets are represented as diamonds, connected to the participating entity sets by lines.

**Degree of a Relationship:** The degree of a relationship refers to the number of entity sets participating in it. A unary or recursive relationship involves only one entity set relating to itself—for example, an Employee "manages" another Employee. A binary relationship involves two entity sets, which is the most common type. A ternary relationship involves three entity sets simultaneously—for instance, a relationship "Supplies" connecting Supplier, Product, and Project entity sets. Higher-degree relationships are possible but less common.

**Cardinality Ratios:** Cardinality specifies the number of entities that can participate in a relationship. The three main types are:

- **One-to-One (1:1):** Each entity in one entity set is associated with exactly one entity in the other set, and vice versa. Example: Each student is assigned one unique locker, and each locker is assigned to one student.
- **One-to-Many (1:N) or Many-to-One (N:1):** An entity in one set can associate with multiple entities in the other set, but each entity in the second set associates with only one entity in the first. Example: A Department has many Faculty members, but each Faculty belongs to one Department.
- **Many-to-Many (M:N):** Entities on both sides can associate with multiple entities on the other side. Example: A Student can enroll in many Courses, and a Course can have many Students enrolled.

**Participation Constraints:** Participation constraints specify whether the existence of an entity depends on its being related to another entity through a relationship.

- **Total Participation (existence-dependent):** Every entity in an entity set must participate in the relationship. This is also called "mandatory participation." In E-R diagrams, this is shown by a double line connecting the entity set to the relationship. For example, every Student must Enroll in at least one Course.
- **Partial Participation:** Entities may or may not participate in the relationship. This is "optional participation" and is shown by a single line. For example, a Teacher may or may not Teach a Course.

**Attributes on Relationships:** Relationships can also have attributes, just like entities. For example, the "Enrolled" relationship between Student and Course can have an attribute "Grade" that stores the grade obtained by the student in that course. This attribute cannot belong to either entity set alone because its value depends on the combination of both entities.

## Examples

### Example 1: University Database E-R Diagram

Consider designing an E-R diagram for a University database with the following requirements:

- The university has multiple Departments (DeptID, DeptName, Location)
- Each Department offers several Courses (CourseID, CourseName, Credits)
- Faculty members work in Departments (EmpID, Name, Designation, Salary)
- Students enroll in Courses (RollNo, Name, Semester, CGPA)
- Each Course is taught by one Faculty member
- Each Course can have multiple Students enrolled
- Students receive Grades for courses they enroll in

**Step-by-step Solution:**

1. **Identify Entity Sets:**
   - Department (strong entity)
   - Course (weak entity - identified by CourseID along with Department)
   - Faculty (strong entity)
   - Student (strong entity)

2. **Identify Attributes:**
   - Department: DeptID (key), DeptName, Location
   - Course: CourseID (partial key), CourseName, Credits
   - Faculty: EmpID (key), Name, Designation, Salary
   - Student: RollNo (key), Name, Semester, CGPA

3. **Identify Relationships:**
   - BelongsTo (Faculty, Department) - 1:N, total participation for Faculty
   - Offers (Department, Course) - 1:N, total participation for Course
   - Teaches (Faculty, Course) - 1:1, partial participation for Faculty
   - EnrolledIn (Student, Course) - M:N, with Grade attribute

4. **E-R Diagram Construction:**
   - Draw rectangles for each entity set
   - Draw ovals for attributes, connecting them to entities
   - Underline key attributes
   - Draw diamonds for relationships
   - Label relationship lines with cardinality (1, N, M)

### Example 2: Converting E-R to Relational Schema

Given the E-R model from Example 1, convert it to relational schema:

**Solution:**

- **DEPARTMENT**(DeptID PK, DeptName, Location)
- **FACULTY**(EmpID PK, Name, Designation, Salary, DeptID FK→DEPARTMENT)
- **COURSE**(CourseID PK, CourseName, Credits, DeptID FK→DEPARTMENT, EmpID FK→FACULTY)
- **STUDENT**(RollNo PK, Name, Semester, CGPA)
- **ENROLLED**(RollNo PK/FK→STUDENT, CourseID PK/FK→COURSE, Grade)

Note: The M:N relationship "EnrolledIn" becomes a separate relation with the primary keys of both participating entities forming a composite primary key, plus the relationship attribute Grade.

### Example 3: Identifying Relationship Cardinalities

For each scenario, identify the entity sets and determine cardinality:

**Scenario:** A hospital management system where Doctors treat Patients.

**Analysis:**

- Entity Sets: Doctor, Patient
- Relationship: Treats (or "Treats" between Doctor and Patient)
- Cardinality: One Doctor can treat many Patients, and one Patient can be treated by many Doctors (if they have multiple ailments requiring different specialists)
- Therefore: M:N relationship

**Scenario:** A library system where each Book has exactly one Publisher.

**Analysis:**

- Entity Sets: Book, Publisher
- Relationship: PublishedBy
- Cardinality: One Publisher can publish many Books, but each Book has exactly one Publisher
- Therefore: 1:N relationship (Publisher to Book)

## Exam Tips

1. **Remember Chen's Notation:** Understand the standard E-R diagram symbols—rectangles for entities, ovals for attributes, diamonds for relationships, double ovals for multi-valued attributes, and dashed ovals for derived attributes.

2. **Key vs. Composite Attributes:** Always underline key attributes. For composite attributes, show the component attributes attached to the main attribute oval, not directly to the entity.

3. **Weak Entity Identification:** Remember that weak entities have a partial key (underlined but not uniquely identifying) and require the owner entity's key for complete identification.

4. **Cardinality from Business Rules:** Practice extracting cardinality from verbal descriptions. Words like "each," "only," "must," and "can" provide clues about participation and cardinality.

5. **Relationship Attributes Placement:** If a relationship has an attribute that could belong to either entity, ask: "Does this attribute depend on both entities existing together?" If yes, it belongs on the relationship.

6. **Converting M:N Relationships:** Always remember that many-to-many relationships cannot be implemented directly in relational databases—they require a separate junction table with foreign keys referencing both parent tables.

7. **Participation Constraints:** Double lines mean total participation (mandatory), single lines mean partial participation (optional). This matters when implementing referential integrity constraints.

8. **Recursive Relationships:** When drawing recursive relationships, ensure the roles are clearly labeled on both sides of the relationship diamond.

9. **Attribute vs. Entity Decision:** If an attribute needs to have relationships of its own or needs to be identified independently, consider making it a separate entity. For example, if Address needs to be associated with multiple entities and queried independently, make it an entity.

10. **Practice Previous Years' Questions:** DU exam papers frequently ask students to draw E-R diagrams for given scenarios and to convert E-R models to relational schemas. Practice these conversions thoroughly.