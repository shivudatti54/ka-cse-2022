# Normal Forms Based on Primary Keys - Summary

## Key Definitions and Concepts

- **Normalization**: The process of organizing data in a database to reduce redundancy and improve data integrity through table decomposition.

- **Functional Dependency (A → B)**: A constraint where if two tuples have the same values for attribute set A, they must have the same values for attribute set B.

- **Candidate Key**: A minimal set of attributes that uniquely identifies each tuple in a relation.

- **Prime Attribute**: An attribute that is part of any candidate key.

- **Partial Dependency**: When a non-prime attribute depends on part of a composite candidate key.

- **Transitive Dependency**: When a non-prime attribute depends on another non-prime attribute, which in turn depends on the candidate key.

## Important Formulas and Theorems

- **1NF Condition**: Relation must contain only atomic (indivisible) values with no repeating groups.

- **2NF Condition**: Must be in 1NF + no partial dependencies (non-prime attributes fully dependent on entire candidate key).

- **3NF Condition**: Must be in 2NF + no transitive dependencies (non-prime attributes depend only on candidate key).

- **BCNF Condition**: For every non-trivial FD X → Y, X must be a superkey.

- **Hierarchy**: BCNF ⇒ 3NF ⇒ 2NF ⇒ 1NF

## Key Points

- The primary key uniquely identifies each tuple and is fundamental to normalization analysis.

- Normalization progresses from 1NF through BCNF, with each level eliminating specific types of dependencies.

- 2NF only applies to relations with composite candidate keys; single-attribute keys automatically satisfy 2NF if in 1NF.

- BCNF is stricter than 3NF and may not always preserve all functional dependencies during decomposition.

- The goal of normalization is to eliminate insert, delete, and update anomalies while maintaining data integrity.

- Lossless-join decomposition ensures that natural joins of decomposed relations restore the original relation.

- Dependency preservation ensures that all original functional dependencies can be enforced in the decomposed schema.

## Common Mistakes to Avoid

- Confusing candidate keys with primary keys - a relation can have multiple candidate keys but one primary key.

- Forgetting that 2NF is only relevant when composite keys exist; a relation with a single-attribute key is automatically in 2NF if in 1NF.

- Assuming BCNF decomposition always preserves dependencies - it sometimes doesn't, making 3NF acceptable in such cases.

- Not checking all functional dependencies when determining if a relation satisfies a normal form.

## Revision Tips

1. Practice identifying candidate keys from given functional dependencies - this is the first step in any normalization problem.

2. Work through at least 5-10 decomposition problems covering all normal forms from 1NF to BCNF.

3. Create a flowchart for solving normalization problems: identify keys → check 1NF → check 2NF (partial dependencies) → check 3NF (transitive dependencies) → check BCNF.

4. Memorize the exact definitions of each normal form as they appear in textbook and class notes.

5. Understand the practical implications: why we need each normal form and what anomalies each eliminates.
