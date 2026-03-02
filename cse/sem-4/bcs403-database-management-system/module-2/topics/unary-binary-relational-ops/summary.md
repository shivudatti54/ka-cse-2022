# Unary and Binary Relational Operations - Summary

## Key Definitions and Concepts

- **Relational Algebra**: A set of mathematical operations that work on relations (tables) to produce new relations
- **Unary Operations**: Operations that work on a single relation (SELECT, PROJECT, RENAME)
- **Binary Operations**: Operations that combine two relations (UNION, INTERSECTION, SET DIFFERENCE, CARTESIAN PRODUCT)
- **Union Compatibility**: Two relations are union-compatible if they have the same number of attributes with compatible domains

## Important Formulas and Theorems

- **SELECT (σ)**: σ<sub>condition</sub>(R) - extracts rows satisfying condition
- **PROJECT (π)**: π<sub>attr1,attr2,...</sub>(R) - extracts specified columns
- **RENAME (ρ)**: ρ<sub>S(A1,A2,...)</sub>(R) - renames relation and attributes
- **UNION (∪)**: R ∪ S - combines all tuples from both relations
- **INTERSECTION (∩)**: R ∩ S - tuples in both R and S
- **SET DIFFERENCE (−)**: R − S - tuples in R but not in S
- **CARTESIAN PRODUCT (×)**: R × S - combines every tuple from R with every tuple from S

## Key Points

1. SELECT filters horizontally (rows), PROJECT filters vertically (columns)
2. Both PROJECT and UNION eliminate duplicate tuples automatically
3. UNION, INTERSECTION, and DIFFERENCE require union-compatible relations
4. CARTESIAN PRODUCT degree = degree(R) + degree(S); cardinality = |R| × |S|
5. SELECT and PROJECT are unary operations; set operations are binary
6. UNION and INTERSECTION are commutative; SET DIFFERENCE is not
7. RENAME is essential for self-joins and avoiding attribute name conflicts
8. Complex queries are solved by combining multiple operations
9. Relational algebra operations form the theoretical basis for SQL

## Common Mistakes to Avoid

1. Confusing SELECT (rows) with PROJECT (columns)
2. Forgetting that UNION, PROJECT automatically remove duplicates
3. Applying set operations to non-union-compatible relations
4. Confusing the order in SET DIFFERENCE (R − S ≠ S − R)
5. Not specifying complete conditions in SELECT operations

## Revision Tips

1. Practice writing relational algebra expressions for various query scenarios
2. Remember the symbolic notation (σ, π, ρ, ∪, −, ∩, ×) for quick recall
3. Always check union compatibility before applying binary set operations
4. Work through step-by-step examples to understand intermediate results
5. Connect relational algebra operations to their equivalent SQL statements
