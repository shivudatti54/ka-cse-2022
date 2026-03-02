# ER-to-Relational Mapping

## Introduction

The Entity-Relational (ER) model provides a high-level, conceptual view of data, allowing database designers to visualize entities, attributes, and relationships before implementing the database. However, the relational model, which underlies modern database management systems like MySQL, PostgreSQL, and Oracle, requires data to be organized into tables (relations). The process of **ER-to-Relational Mapping** (also known as ERD to Relational Schema Conversion) is the critical bridge that transforms an abstract ER diagram into a concrete relational database schema that can be implemented in SQL.

This topic is fundamental to database design and is frequently tested in DU semester examinations. Understanding this mapping process is essential for any Computer Science student, as it demonstrates the complete database design cycle—from conceptual modeling using ER diagrams to logical modeling using relational schema. In real-world software development, tools like Oracle SQL Developer, MySQL Workbench, and DbVisualizer often automate this conversion, but a thorough understanding of the underlying rules is necessary for handling complex scenarios and optimizing database designs.

## Key Concepts

### Step 1: Mapping Regular (Strong) Entity Types

Regular entity types that have a primary key and exist independently are mapped directly to relations. Each attribute of the entity becomes a column in the relation, and the primary key of the entity becomes the primary key of the relation.

**Mapping Rules:**
- Create a relation with the same name as the entity type
- Include all simple attributes of the entity
- For composite attributes, include only the simple component attributes
- Choose the primary key of the entity as the primary key of the relation

**Example:** Consider an entity **STUDENT** with attributes: StudentID (primary key), Name, Age, and Address (composite with components: HouseNo, Street, City).

**Relational Schema:**
```
STUDENT(StudentID, Name, Age, HouseNo, Street, City)
```

### Step 2: Mapping Weak Entity Types

Weak entities are those that do not have a complete primary key and depend on a strong (owner) entity for their identification. The mapping process must incorporate both the weak entity's attributes and the primary key of the owner entity.

**Mapping Rules:**
- Create a relation that includes all attributes of the weak entity
- Include the primary key of the owner entity as a foreign key attribute
- The combination of the foreign key and the partial key of the weak entity forms the primary key of the new relation

**Example:** Consider a weak entity **DEPENDENT** belonging to entity **EMPLOYEE** (primary key: EmpID). DEPENDENT has attributes: Name (partial key), Relationship, and Age.

**Relational Schema:**
```
EMPLOYEE(EmpID, Name, Salary, Department)
DEPENDENT(EmpID, Name, Relationship, Age)
```
Here, (EmpID, Name) together form the primary key of DEPENDENT.

### Step 3: Mapping Binary 1:1 Relationships

One-to-one relationships require careful handling based on participation constraints. There are three approaches: merging relations, using foreign keys, or creating a separate relation.

**Mapping Rules:**
- **Option A (Both entities participate fully):** Merge the two entities into a single relation by adding the primary key of one entity as a foreign key to the other
- **Option B (Partial participation on one side):** Add the primary key of the entity with total participation as a foreign key in the other relation
- **Option C (Separate relation):** Create a new relation with primary keys of both entities as foreign keys, forming a composite primary key

**Example:** Consider a 1:1 relationship **MANAGES** between **DEPARTMENT** (primary key: DeptID) and **MANAGER** (primary key: ManagerID). A department has exactly one manager, and a manager manages exactly one department.

**Relational Schema (using Option B):**
```
DEPARTMENT(DeptID, DeptName, ManagerID)
MANAGER(ManagerID, ManagerName, Qualification)
```
Here, ManagerID in DEPARTMENT is both a foreign key and acts as a partial key to ensure 1:1 nature.

### Step 4: Mapping Binary 1:N Relationships

One-to-many relationships are the most common type and are mapped using the "foreign key approach."

**Mapping Rules:**
- Identify the "one" side (parent entity) and "many" side (child entity)
- Add the primary key of the "one" side entity as a foreign key in the relation representing the "many" side entity
- The foreign key in the "many" side becomes part of its primary key if the relationship is identifying

**Example:** Consider a 1:N relationship **WORKS_IN** between **DEPARTMENT** (primary key: DeptID) and **EMPLOYEE** (primary key: EmpID). One department has many employees, but each employee works in exactly one department.

**Relational Schema:**
```
DEPARTMENT(DeptID, DeptName, Location)
EMPLOYEE(EmpID, EmpName, Salary, DeptID)
```
Here, DeptID in EMPLOYEE is a foreign key referencing DEPARTMENT.

### Step 5: Mapping Binary M:N Relationships

Many-to-many relationships cannot be represented using a single foreign key. They require the creation of a separate relation, often called an "associate" or "junction" relation.

**Mapping Rules:**
- Create a new relation to represent the relationship
- Include the primary keys of both participating entities as foreign keys
- The combination of both foreign keys forms the primary key of the new relation
- Include any attributes of the relationship itself as additional columns

**Example:** Consider an M:N relationship **ENROLLED_IN** between **STUDENT** (primary key: StudentID) and **COURSE** (primary key: CourseID). A student can enroll in many courses, and a course can have many students enrolled. The relationship has an attribute Grade.

**Relational Schema:**
```
STUDENT(StudentID, StudentName, Email)
COURSE(CourseID, CourseName, Credits)
ENROLLED_IN(StudentID, CourseID, Grade)
```
Here, (StudentID, CourseID) together form the primary key of ENROLLED_IN.

### Step 6: Mapping Multivalued Attributes

Multivalued attributes must be represented by a separate relation because relational tables cannot contain multivalued fields.

**Mapping Rules:**
- Create a new relation that includes the primary key of the entity as a foreign key
- Include the multivalued attribute as a separate column in this new relation
- The combination of the foreign key and the multivalued attribute forms the primary key

**Example:** Consider an entity **EMPLOYEE** with multivalued attribute **PhoneNumber**.

**Relational Schema:**
```
EMPLOYEE(EmpID, EmpName, Salary)
EMPLOYEE_PHONE(EmpID, PhoneNumber)
```
Here, (EmpID, PhoneNumber) forms the primary key of EMPLOYEE_PHONE.

### Step 7: Mapping N-ary Relationships

Relationships involving more than two entity types (ternary, quaternary, etc.) are mapped using a separate relation similar to M:N relationships.

**Mapping Rules:**
- Create a new relation to represent the n-ary relationship
- Include the primary keys of all participating entities as foreign keys
- The combination of all foreign keys forms the primary key of the new relation
- Include any attributes of the relationship itself

**Example:** Consider a ternary relationship **TEACHES** involving **PROFESSOR**, **COURSE**, and **SEMESTER**. A professor teaches a specific course in a specific semester.

**Relational Schema:**
```
PROFESSOR(ProfID, ProfName, Department)
COURSE(CourseID, CourseName, Credits)
SEMESTER(SemID, Year, Term)
TEACHES(ProfID, CourseID, SemID, HoursAssigned)
```
Here, (ProfID, CourseID, SemID) forms the composite primary key.

### Step 8: Mapping Derived Attributes

Derived attributes are those whose values can be computed from other attributes. They are not stored in the relational schema.

**Mapping Rules:**
- Do not include derived attributes as columns in the relation
- They can be computed at query time using SQL queries

**Example:** Consider an entity **EMPLOYEE** with attributes: BirthDate and Age (derived). The mapping would only include BirthDate.

**Relational Schema:**
```
EMPLOYEE(EmpID, EmpName, BirthDate)
```
Age can be computed as: `TIMESTAMPDIFF(YEAR, BirthDate, CURDATE())`

## Examples

### Worked Example 1: Comprehensive ER-to-Relational Mapping

Consider an ER diagram for a **LIBRARY MANAGEMENT SYSTEM** with the following specifications:

**Entities:**
- **BOOK** (BookID as primary key, Title, ISBN, PublishedYear)
- **AUTHOR** (AuthorID as primary key, Name, Country)
- **PUBLISHER** (PublisherID as primary key, Name, Address)

**Relationships:**
- A book can have multiple authors (M:N) - relationship attribute: Order
- A book is published by exactly one publisher (1:N)
- An author can write many books (1:N)

**Step-by-Step Solution:**

**Step 1:** Map strong entities
```
BOOK(BookID, Title, ISBN, PublishedYear, PublisherID)
AUTHOR(AuthorID, Name, Country)
PUBLISHER(PublisherID, Name, Address)
```

**Step 2:** Map M:N relationship between BOOK and AUTHOR
```
WRITTEN_BY(BookID, AuthorID, AuthorOrder)
```

**Step 3:** Map 1:N relationship between PUBLISHER and BOOK
- PublisherID already added to BOOK as foreign key in Step 1

**Final Relational Schema:**
```
BOOK(BookID, Title, ISBN, PublishedYear, PublisherID)
AUTHOR(AuthorID, Name, Country)
PUBLISHER(PublisherID, Name, Address)
WRITTEN_BY(BookID, AuthorID, AuthorOrder)
```

### Worked Example 2: Handling Weak Entities and Complex Relationships

Consider an ER diagram for a **HOSPITAL MANAGEMENT SYSTEM**:

**Entities:**
- **PATIENT** (PatientID as primary key, Name, Address)
- **WARD** (WardNumber as primary key, WardName, Capacity)
- **TREATMENT** (TreatmentID as primary key, TreatmentType) - weak entity depending on WARD

**Relationships:**
- A patient is admitted to exactly one ward (1:N)
- A ward can have many patients
- A patient undergoes multiple treatments in a ward (M:N) - attributes: Date, Duration

**Step-by-Step Solution:**

**Step 1:** Map strong entities
```
PATIENT(PatientID, Name, Address, WardNumber)
WARD(WardNumber, WardName, Capacity)
```

**Step 2:** Map weak entity TREATMENT
- Primary key of owner (WARD) is WardNumber
- Partial key of TREATMENT is TreatmentID (assuming uniqueness within ward)
```
TREATMENT(TreatmentID, TreatmentType, WardNumber)
```

**Step 3:** Map M:N relationship between PATIENT and WARD (with treatment details)
- Since this represents the admission and treatment together:
```
ADMISSION(PatientID, WardNumber, AdmissionDate, DischargeDate)
```

**Final Relational Schema:**
```
PATIENT(PatientID, Name, Address, WardNumber)
WARD(WardNumber, WardName, Capacity)
TREATMENT(TreatmentID, TreatmentType, WardNumber)
ADMISSION(PatientID, WardNumber, AdmissionDate, DischargeDate)
```

## Exam Tips

1. **Start with entity mapping first:** Always map regular entities and weak entities before handling relationships. This creates the foundation for foreign key placement.

2. **Identify relationship cardinality correctly:** Before mapping, clearly determine whether each relationship is 1:1, 1:N, or M:N. This determines whether you need a separate relation or can use foreign keys.

3. **Remember weak entity rules:** For weak entities, always include the owner's primary key as a foreign key and combine it with the partial key to form the new primary key.

4. **Handle composite and multivalued attributes:** Composite attributes should be flattened (only include simple components), while multivalued attributes always require a separate relation.

5. **Know when NOT to store derived attributes:** Derived attributes are not mapped to columns—they are computed during queries.

6. **Practice with past DU exam questions:** Most questions provide an ER diagram and ask for the corresponding relational schema. Practice drawing the schema step-by-step.

7. **Check foreign key constraints:** Always verify that primary keys and foreign keys maintain referential integrity. A foreign key in a relation should always reference an existing primary key in another relation.

8. **Time management in exams:** Spend the first 2-3 minutes analyzing the ER diagram, then systematically apply each mapping rule. Don't skip any step to avoid errors.