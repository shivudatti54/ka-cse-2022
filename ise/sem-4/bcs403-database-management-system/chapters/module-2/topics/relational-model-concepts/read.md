# Relational Model Concepts

## What is the Relational Model?

A data model based on mathematical relation theory, introduced by E.F. Codd in 1970.

**Key Idea**: Data organized as tables (relations) with rows and columns.

## Terminology

| Formal Term  | Informal Term     | Example             |
| ------------ | ----------------- | ------------------- |
| Relation     | Table             | Students            |
| Tuple        | Row               | (101, "Alice", 3.8) |
| Attribute    | Column            | Name, GPA           |
| Domain       | Data Type         | INTEGER, VARCHAR    |
| Cardinality  | Number of rows    | 100 tuples          |
| Degree/Arity | Number of columns | 5 attributes        |

## Relation Schema vs Instance

### Schema (Structure)

```
Student(StudentID: INT, Name: VARCHAR(50), GPA: DECIMAL)
```

- Describes structure
- Relatively static
- Like a template

### Instance (Data)

```
| StudentID | Name  | GPA |
|-----------|-------|-----|
| 101       | Alice | 3.8 |
| 102       | Bob   | 3.2 |
```

- Actual data at a point in time
- Changes frequently
- Conforms to schema

## Properties of Relations

1. **Atomic values**: Each cell contains single value (1NF)
2. **No duplicate tuples**: Each row is unique
3. **Tuple order**: Rows have no inherent order
4. **Attribute order**: Columns have no inherent order
5. **Unique attribute names**: No two columns share same name

## Relational Algebra

Mathematical operations on relations.

### Basic Operations

| Operation         | Symbol    | Description      |
| ----------------- | --------- | ---------------- |
| Select            | σ (sigma) | Filter rows      |
| Project           | π (pi)    | Choose columns   |
| Union             | ∪         | Combine tuples   |
| Difference        | −         | Remove tuples    |
| Cartesian Product | ×         | All combinations |
| Rename            | ρ (rho)   | Rename relation  |

### Select (σ)

Filter rows by condition.

```
σ_GPA>3.5 (Student)
Result: Students with GPA > 3.5
```

### Project (π)

Choose specific columns.

```
π_Name,GPA (Student)
Result: Only Name and GPA columns
```

### Combined Example

```
π_Name (σ_GPA>3.5 (Student))
Names of students with GPA > 3.5
```

## Join Operations

### Natural Join (⋈)

Join on common attributes.

```
Student ⋈ Enrollment
Joins where Student.ID = Enrollment.StudentID
```

### Theta Join

Join with arbitrary condition.

```
R ⋈_θ S  where θ is any condition
```

### Equijoin

Theta join with equality condition.

## Relational Calculus

Declarative query language (what, not how).

### Tuple Relational Calculus

```
{t | Student(t) ∧ t.GPA > 3.5}
Tuples t from Student where GPA > 3.5
```

### Domain Relational Calculus

```
{<n> | ∃i,g (Student(i,n,g) ∧ g > 3.5)}
Names n where there exists Student with that name and GPA > 3.5
```

## Codd's 12 Rules

Key rules for true RDBMS:

1. **Information Rule**: All data in tables
2. **Guaranteed Access**: Every value accessible by table+column+key
3. **NULL Treatment**: Systematic NULL handling
4. **Dynamic Catalog**: Database describes itself in tables
5. **Comprehensive Data Sublanguage**: SQL-like language
6. **View Updateability**: Views should be updatable
7. **High-Level Operations**: Set operations supported
8. **Physical Independence**: Physical changes don't affect apps
9. **Logical Independence**: Logical changes minimally affect apps
10. **Integrity Independence**: Constraints in catalog
11. **Distribution Independence**: Data distribution transparent
12. **Non-Subversion**: No bypassing integrity via low-level access

## Exam Tips

1. **Relation = Table**, Tuple = Row, Attribute = Column
2. **Schema**: Structure, **Instance**: Data
3. **Select (σ)**: Rows, **Project (π)**: Columns
4. **Natural join**: Automatic on common attributes
5. **Cardinality**: Row count, **Degree**: Column count
