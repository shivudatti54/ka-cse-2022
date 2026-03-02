# Relational Algebra Revision Notes

### Unary and Binary Relational Operations

- **Unary Operations:**
  - Projection (σ): Selects a subset of attributes from a relation
    - Formula: πX(R) = {t | t ∈ R and X(t)}
  - Renaming (ρ): Renames an attribute in a relation
    - Formula: ρX ⇔ Y(R) = {t | t ∈ R and X(t) = Y(t)}
  - Union (∪): Combines two relations
    - Formula: R ∪ S = {(t1, t2) | t1 ∈ R or t1 ∈ S}
  - Difference (-): Returns the difference between two relations
    - Formula: R - S = {(t1, t2) | t1 ∈ R and t1 ∉ S}
- **Binary Operations:**
  - Cartesian Product (∞): Combines two relations
    - Formula: R × S = {(t1, t2) | t1 ∈ R and t2 ∈ S}
  - Join (∘): Combines two relations based on a common attribute
    - Formula: R ∘ S = {(t1, t2) | t1 ∈ R and t2 ∈ S and X(t1) = Y(t2)}
  - Intersection (∩): Returns the intersection of two relations
    - Formula: R ∩ S = {(t1, t2) | t1 ∈ R and t1 ∈ S}

### Additional Relational Operations

- **Aggregate Operations:**
  - Aggregate (σag): Groups a relation based on an attribute and applies an aggregate function
    - Formula: σag(X, f)(R) = {t | t ∈ R and X(t) = X and f(X(t))}
  - Grouping (σg): Groups a relation based on an attribute
    - Formula: σg(X)(R) = {t | t ∈ R and X(t) = X}
- **Sorting and Ordering:**
  - Selection (σ): Selects a subset of tuples from a relation based on an attribute
    - Formula: σX > Y(R) = {t | t ∈ R and X(t) > Y(t)}
  - Sort (σo): Sorts a relation based on an attribute
    - Formula: sort(R) = {t | t ∈ R and X(t) ≤ X}

### Examples of Queries in Relational Algebra

- Query 1: Select all tuples from the students relation where the grade is greater than 85
  - Formula: σgrade > 85(students)
- Query 2: Join the employees relation with the departments relation on the employee ID attribute
  - Formula: employees ∘ departments

Theorems:

- **First Normal Form (1NF)**: A relation is in 1NF if each tuple contains a unique combination of attributes.
- **Boyce-Codd Normal Form (BCNF)**: A relation is in BCNF if and only if it is in 1NF and there are no transitive dependencies.

Formulas:

- **Select Formula**: σX = V(R) = {t | t ∈ R and X(t) = V}
- **Project Formula**: πX(R) = {t | t ∈ R and X(t)}
- **Join Formula**: R ∘ S = {(t1, t2) | t1 ∈ R and t2 ∈ S and X(t1) = Y(t2)}
