# Relational Algebra and Calculus - Summary

## Key Definitions and Concepts
- **Relational Algebra**: Procedural language with operators for relation manipulation
- **Relational Calculus**: Non-procedural declarative query language
- **Selection**: σ_{predicate}(R) filters tuples
- **Projection**: π_{attributes}(R) selects columns
- **Natural Join**: R ⋈ S combines relations on common attributes

## Important Formulas and Theorems
- Join: R ⋈_{θ} S = σ_{θ}(R × S)
- Division: R ÷ S = π_{R-S}(R) - π_{R-S}((π_{R-S}(R) × S) - R)
- Codd's Theorem: Safe TRC/DRC ≡ Relational Algebra in expressive power

## Key Points
- Relational algebra is closed: operations return relations
- Calculus variables range over tuples (TRC) or domains (DRC)
- Outer joins preserve dangling tuples with null values
- Division finds maximal subsets matching all divisor tuples
- Query optimization uses algebraic equivalence rules
- Safety condition prevents infinite relations in calculus
- Recursive operations enable transitive closure queries

## Common Mistakes to Avoid
- Confusing projection with selection operations
- Forgetting to handle duplicate tuples in union operations
- Creating unsafe calculus expressions with infinite domains
- Misapplying join conditions leading to Cartesian products
- Overlooking attribute naming conflicts in renaming operations

## Revision Tips
1. Practice visual representation of operations using table diagrams
2. Create cheat sheet of operator symbols and precedence rules
3. Solve previous years' DU question papers on query translation
4. Use online relational algebra calculators for instant feedback
5. Focus on 5NF and dependency preservation applications