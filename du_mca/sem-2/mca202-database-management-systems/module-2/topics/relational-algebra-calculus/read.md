# Relational Algebra and Calculus

## Introduction
Relational Algebra and Calculus form the mathematical foundation of relational databases. Relational Algebra is a procedural query language that provides a set of operations to manipulate relations, while Relational Calculus is a non-procedural declarative language that specifies what data to retrieve. 

These concepts are critical for understanding query processing in DBMS. Modern SQL implementations are built upon these mathematical foundations. For DU MCA students, mastering these concepts enables optimization of complex queries and design of efficient database systems. Real-world applications include query optimization in enterprise systems like banking databases and e-commerce platforms.

## Key Concepts
1. **Relational Algebra Operations**:
   - Basic: Selection (σ), Projection (π), Union (∪), Set Difference (-), Cartesian Product (×)
   - Derived: Join (⋈), Division (÷), Intersection (∩)
   - Rename (ρ) operation

2. **Relational Calculus**:
   - Tuple Relational Calculus (TRC): { t | P(t) } format
   - Domain Relational Calculus (DRC): { <x1,x2,...> | P(x1,x2,...) }
   - Safety of expressions

3. **Comparison**:
   - Algebra specifies HOW to retrieve, Calculus specifies WHAT to retrieve
   - Equivalence between safe TRC/DRC and Relational Algebra expressions

4. **Extended Operations**:
   - Aggregate functions (γ)
   - Outer joins (⟕, ⟖, ⟗)
   - Recursive closure operations

## Examples

**Example 1: Relational Algebra Query**
*Problem*: Find names of students with CGPA > 8.5 in CSE department
```
π_name(σ_{dept='CSE' ∧ CGPA>8.5}(Students))
```

**Example 2: Tuple Calculus**
*Problem*: Get employee IDs earning more than their managers
```
{ t | ∃e ∈ Employees (t[Eid] = e.Eid ∧ e.Salary > ∃m ∈ Managers (m.Mid = e.Mid ∧ m.Salary)) }
```

**Example 3: Division Operation**
*Problem*: Find students who have enrolled in all courses offered by CS department
```
π_{sid,cid}(Enrollments) ÷ π_{cid}(σ_{dept='CS'}(Courses))
```

## Exam Tips
1. Always specify schema for intermediate results in algebra operations
2. For calculus queries, ensure domain safety through bounded variables
3. Practice converting nested SQL queries to relational algebra expressions
4. Remember difference between θ-join and natural join
5. Use proper notation: σ for selection, π for projection
6. For division operation, verify that divisor attributes are subset of dividend
7. In calculus, distinguish between free and bound variables