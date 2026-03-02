# Multivalued Dependency and Fourth Normal Form - Summary

## Key Definitions and Concepts

- **Multivalued Dependency (MVD)**: A constraint where attribute B has multiple independent values for each value of attribute A. Denoted as A �师范学院 B, meaning "A multidetermines B."

- **Fourth Normal Form (4NF)**: A relation R is in 4NF if for every non-trivial MVD A �师范学院 B in R, A is a candidate key of R.

- **Trivial MVD**: A �师范学院 B is trivial if B ⊆ A or A ∪ B contains all attributes of R. Trivial MVDs do not cause redundancy.

- **Non-Trivial MVD**: A �师范学院 B is non-trivial if B is not a subset of A and A ∪ B does not contain all attributes. Non-trivial MVDs cause redundancy and violate 4NF.

## Important Formulas and Theorems

- **4NF Condition**: For all non-trivial MVDs A �师范学院 B, A must be a candidate key.

- **Decomposition Algorithm**: For MVD A �师范学院 B, decompose into:
  - R1(A, B)
  - R2(A, (R - A - B))
- **Symmetry Property**: If A �师范学院 B holds, then A �师范学院 (R - A - B) also holds.

- **Relationship**: 4NF ⊂ BCNF ⊂ 3NF (all 4NF relations are in BCNF, but not vice versa)

## Key Points

- 4NF eliminates redundancy caused by independent multivalued attributes in a relation
- Every relation in 4NF is automatically in BCNF, but BCNF relations may violate 4NF
- MVDs are distinct from functional dependencies and require separate analysis
- The determining attribute in a 4NF MVD must be a candidate key (stricter than BCNF's superkey requirement)
- 4NF decomposition is always lossless but may not preserve dependencies
- Symmetry property of MVDs means if A �师范学院 B exists, A �师范学院 (all other attributes excluding A and B) also exists
- Practical databases with attributes like hobbies, language skills, or certifications typically require 4NF consideration

## Common Mistakes to Avoid

- Confusing functional dependencies with multivalued dependencies (FDs: single value; MVDs: multiple independent values)
- Forgetting to check for trivial MVDs before decomposition
- Assuming BCNF compliance guarantees 4NF compliance
- Applying 4NF decomposition when trivial MVDs exist that don't cause redundancy
- Ignoring the symmetry property when identifying MVDs in a relation

## Revision Tips

1. Always first identify functional dependencies and check BCNF before analyzing multivalued dependencies
2. Create sample data to visualize how independent multivalued attributes create redundant rows
3. Practice decomposing relations with multiple independent MVDs from the same attribute
4. Remember that 4NF is the final normal form addressing dependency types in standard normalization theory
