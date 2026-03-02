# Boyce-Codd Normal Form (BCNF) - Summary

## Key Definitions and Concepts

- **BCNF Definition**: A relation R is in BCNF if for every non-trivial functional dependency X → Y, X is a superkey of R. This is stricter than 3NF, which allows Y to be a prime attribute even if X is not a superkey.

- **Functional Dependency (FD)**: A constraint where attribute A determines attribute B (A → B), meaning for every value of A, there is exactly one value of B.

- **Candidate Key**: A minimal superkey that can uniquely identify all attributes in a relation. A relation can have multiple candidate keys.

- **Superkey**: A set of attributes that can uniquely identify tuples in a relation. Contains at least one candidate key.

## Important Formulas and Theorems

- **BCNF Condition**: For every FD X → Y in relation R, either X is a superkey of R, or the decomposition is lossless.

- **Lossless Join Test**: A decomposition of R into R1 and R2 is lossless if (R1 ∩ R2) → R1 or (R1 ∩ R2) → R2 holds (the common attributes form a key for at least one relation).

- **BCNF Decomposition Algorithm**:
  1. Find violating FD X → Y where X is not a superkey
  2. Decompose into R1 = X ∪ Y and R2 = R - Y
  3. Repeat until all relations are in BCNF

## Key Points

- Every relation in BCNF is in 3NF, but not vice versa

- BCNF eliminates more anomalies than 3NF by enforcing stricter conditions

- The candidate key must be identified before checking BCNF compliance

- BCNF decomposition may not preserve all functional dependencies

- A relation with all FDs having superkeys as determinants is automatically in BCNF

- Cyclic functional dependencies where each attribute determines another in a cycle are typically in BCNF if the cycle includes candidate keys

- BCNF decomposition is always lossless but not always dependency-preserving

## Common Mistakes to Avoid

1. **Forgetting to find candidate keys**: Always identify candidate keys first before checking if an FD violates BCNF

2. **Confusing 3NF and BCNF conditions**: Remember that BCNF does not allow prime attributes on the right-hand side when the left-hand side is not a superkey

3. **Ignoring implied/transitive dependencies**: Derived FDs like A → C from A → B and B → C must be considered

4. **Incomplete decomposition**: Continue decomposing until all resulting relations satisfy BCNF

## Revision Tips

1. Practice finding candidate keys for relations with 4-5 attributes and multiple FDs

2. Work through at least 3-4 BCNF decomposition examples step-by-step

3. Memorize the exact definition of BCNF and compare it with 3NF

4. Always verify your decomposition by checking each resulting relation satisfies BCNF

5. Remember that BCNF decomposition ensures lossless join but may lose dependency preservation
