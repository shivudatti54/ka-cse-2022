# Examples of Queries in Relational Algebra - Summary

## Key Definitions and Concepts

- **Selection (σ)**: Filters rows based on a condition; preserves all attributes
- **Projection (π)**: Selects specific columns, eliminating duplicates
- **Union (∪)**: Combines tuples from two compatible relations
- **Set Difference (-)**: Returns tuples in first but not in second relation
- **Cartesian Product (×)**: Creates all possible combinations between two relations
- **Natural Join (⋈)**: Joins on common attribute names, removes duplicate columns
- **Theta Join (⋈θ)**: Join based on any condition (θ)
- **Division (÷)**: Returns tuples that match all tuples in second relation

## Important Formulas and Theorems

- **Selection with AND**: σ_c1∧c2(R) = σ_c1(σ_c2(R))
- **Selection with OR**: σ_c1∨c2(R) = σ_c1(R) ∪ σ_c2(R)
- **Projection chaining**: π_A1(π_A1,A2(R)) = π_A1(R)
- **Theta join equivalent**: R ⋈θ S = σθ(R × S)
- **Intersection via difference**: R ∩ S = R - (R - S)
- **Division relationship**: If T = R ÷ S, then T × S ⊆ R

## Key Points

1. Relational algebra provides theoretical foundation for SQL and query processing
2. Selection reduces horizontal data (fewer rows), projection reduces vertical data (fewer columns)
3. Set operations require schema compatibility between relations
4. Natural join automatically uses equijoin on all matching attribute names
5. Division operation solves "for all" queries (universal quantification)
6. Outer joins preserve unmatched tuples from one or both relations
7. Complex queries are built by composing basic operators in expression trees
8. The rename operator (ρ) is essential for self-joins and avoiding ambiguity

## Common Mistakes to Avoid

1. Forgetting that projection removes duplicate tuples - this differs from SQL's ALL keyword
2. Applying union/difference on incompatible schemas - ensure same number and type of attributes
3. Confusing natural join with theta join - natural join uses all common attribute names
4. Incorrectly ordering operations - remember selection before projection unless parentheses indicate otherwise
5. Using division incorrectly - the second relation must be a proper subset of attributes from the first

## Revision Tips

1. Practice converting English queries to relational algebra expressions repeatedly
2. Draw expression trees for complex queries to visualize operator ordering
3. Memorize the set of eight basic operators and their purposes
4. Work through at least 10-15 varied examples to understand different query patterns
5. Compare relational algebra expressions with equivalent SQL queries to strengthen understanding
6. Focus on join operations as they are most frequently tested in exams
