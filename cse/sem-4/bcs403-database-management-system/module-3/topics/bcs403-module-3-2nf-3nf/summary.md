# Second and Third Normal Forms - Summary

## Key Definitions and Concepts

- **Second Normal Form (2NF):** A relation in 1NF where no non-prime attribute is partially dependent on any candidate key. Requires elimination of partial dependencies.

- **Third Normal Form (3NF):** A relation in 2NF where no non-prime attribute is transitively dependent on any candidate key. Requires elimination of transitive dependencies.

- **Partial Dependency:** Exists when a non-prime attribute depends on only a part of a composite candidate key.

- **Transitive Dependency:** Exists when a non-prime attribute depends on another non-prime attribute, which in turn depends on the candidate key.

- **Prime Attribute:** An attribute that is part of any candidate key in a relation.

- **Non-Prime Attribute:** An attribute that is not part of any candidate key.

## Important Formulas and Theorems

- **2NF Condition:** Relation R is in 2NF if ∀(X → A) ∈ F+, if X ⊂ candidate key then A must be a prime attribute.

- **3NF Condition:** Relation R is in 3NF if ∀(X → A) ∈ F+, either X is a superkey or A is a prime attribute.

- **Lossless Join Decomposition:** A decomposition of R into R1 and R2 is lossless if (R1 ∩ R2) → R1 or (R1 ∩ R2) → R2 holds.

## Key Points

1. Normalization proceeds sequentially: 1NF → 2NF → 3NF (and beyond like BCNF).

2. A relation in 2NF may still have transitive dependencies and thus may not be in 3NF.

3. Every relation in 3NF is also in 2NF, but the converse is not always true.

4. The goal of normalization is to minimize insert, update, and delete anomalies in database operations.

5. Finding candidate keys is the first and most crucial step before checking for any normal form violations.

6. Decomposition should maintain lossless joins and preferably preserve dependencies.

7. In 2NF, focus is primarily on relations with composite candidate keys; simple candidate keys automatically satisfy 2NF.

8. Transitive dependencies cause redundancy when the same information is repeated across multiple tuples.

## Common Mistakes to Avoid

1. **Skipping candidate key identification:** Never check for partial/transitive dependencies without first identifying all candidate keys.

2. **Confusing partial and transitive dependencies:** Partial involves part of a key; transitive involves non-key to non-key dependencies.

3. **Assuming simple keys are problematic:** Single-attribute candidate keys cannot have partial dependencies, so they are automatically in 2NF.

4. **Ignoring dependency closure:** Always consider the closure of functional dependencies, not just the given FDs.

## Revision Tips

1. Practice identifying candidate keys from various FD sets repeatedly until confident.

2. Create a decision tree: Is it in 1NF? → Is it in 2NF (check partial dependencies)? → Is it in 3NF (check transitive dependencies)?

3. Solve at least 5-10 normalization problems from previous years' question papers to understand common patterns.

4. Remember that decomposing to higher normal forms may sometimes sacrifice dependency preservation.

5. When stuck, always go back to basics: What are the candidate keys? What depends on what?
