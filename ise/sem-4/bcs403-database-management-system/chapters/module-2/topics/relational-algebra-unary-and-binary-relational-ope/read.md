# Relational Algebra: Unary and Binary Relational Operations, Additional Operations, and Examples of Queries

=====================================================

## Introduction

---

Relational algebra is a formal language used to express queries and operations on relational databases. It provides a way to manipulate relational databases in a declarative manner, without explicitly specifying how to store the data. This topic covers the basics of relational algebra, including unary and binary relational operations, additional operations, and examples of queries.

## Unary Relational Operations

---

Unary relational operations are used to manipulate individual tuples in a relational database. The following are some common unary relational operations:

- **Selection**: Returns a subset of tuples that satisfy a specified condition.
  - Example: `σ (age > 18) (students)`, where `students` is the relation containing information about students.
- **Projection**: Returns a subset of attributes from a relation.
  - Example: `π (name, age) (students)`, where `students` is the relation containing information about students.
- **Renaming**: Renames attributes in a relation.
  - Example: `ρ (name → student_name) (students)`, where `students` is the relation containing information about students.

## Binary Relational Operations

---

Binary relational operations are used to combine two relations. The following are some common binary relational operations:

- **Cartesian Product**: Returns the Cartesian product of two relations.
  - Example: `(students × courses)`, where `students` and `courses` are the relations containing information about students and courses, respectively.
- **Division**: Returns a relation that contains tuples from the first relation where the second relation contains a matching tuple.
  - Example: `(students ÷ courses)`, where `students` and `courses` are the relations containing information about students and courses, respectively.
- **Join**: Returns a relation that contains tuples from the first relation where the second relation contains a matching tuple.
  - Example: `(students × courses)`, where `students` and `courses` are the relations containing information about students and courses, respectively.

## Additional Relational Operations

---

### Aggregate Operations

Aggregate operations are used to perform calculations on a set of tuples in a relation.

- **Sum**: Returns the sum of a specified attribute in a relation.
  - Example: `Σ (age) (students)`, where `students` is the relation containing information about students.
- **Average**: Returns the average of a specified attribute in a relation.
  - Example: `Σ (age) / (SELECT COUNT(*) FROM (students))`, where `students` is the relation containing information about students.
- **Max**: Returns the maximum value of a specified attribute in a relation.
  - Example: `Σ (age) FROM (students)`, where `students` is the relation containing information about students.
- **Min**: Returns the minimum value of a specified attribute in a relation.
  - Example: `Σ (age) FROM (students)`, where `students` is the relation containing information about students.

### Grouping Operations

Grouping operations are used to group tuples in a relation based on a specified attribute.

- **Group by**: Returns a relation that contains groups of tuples based on a specified attribute.
  - Example: `GROUP BY (department) (students)`, where `students` is the relation containing information about students.

### Set Operations

Set operations are used to combine relations.

- **Union**: Returns a relation that contains all tuples from the first and second relations.
  - Example: `(students ∪ courses)`, where `students` and `courses` are the relations containing information about students and courses, respectively.
- **Intersection**: Returns a relation that contains tuples from the first and second relations where the tuples match.
  - Example: `(students ∩ courses)`, where `students` and `courses` are the relations containing information about students and courses, respectively.
- **Difference**: Returns a relation that contains tuples from the first relation where the tuples do not match the second relation.
  - Example: `(students \ courses)`, where `students` and `courses` are the relations containing information about students and courses, respectively.

## Examples of Queries

---

### Example 1: Finding all students who are older than 18

```sql
σ (age > 18) (students)
```

### Example 2: Finding the names and ages of all students who are older than 18

```sql
π (name, age) (σ (age > 18) (students))
```

### Example 3: Finding all students who are enrolled in at least one course

```sql
GROUP BY (department) (σ (department IN (SELECT department FROM courses)))
```

### Example 4: Finding the average age of all students

```sql
Σ (age) / (SELECT COUNT(*) FROM (students))
```

### Example 5: Finding all students who are older than 18 and enrolled in at least one course

```sql
σ (age > 18 AND department IN (SELECT department FROM courses)) (students)
```

In conclusion, relational algebra provides a powerful way to express queries and operations on relational databases. Understanding unary and binary relational operations, additional operations, and examples of queries is essential for working with relational databases.
