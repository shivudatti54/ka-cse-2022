# Normalization: 1NF, 2NF, 3NF, and BCNF - Summary

## Key Definitions and Concepts

- **Functional Dependency (X → Y)**: Attribute Y is functionally dependent on X if each X value determines exactly one Y value
- **Candidate Key**: Minimal superkey that uniquely identifies all tuples; chosen as primary key
- **Prime Attribute**: Attribute that appears in any candidate key
- **Partial Dependency**: When a non-prime attribute depends on part of a composite candidate key
- **Transitive Dependency**: When X → Y, Y → Z, and Y ↛ X, creating X → Z indirectly

## Important Formulas and Theorems

- **1NF Requirement**: All attribute values must be atomic (indivisible)
- **2NF Condition**: Relation in 1NF + no partial dependencies (non-prime attributes fully dependent on entire candidate key)
- **3NF Condition**: Relation in 2NF + no transitive dependencies (for X → Y, either X is superkey or Y is prime)
- **BCNF Condition**: For every non-trivial FD X → Y, X must be a superkey

## Key Points

- Normalization proceeds from 1NF → 2NF → 3NF → BCNF; each form is stricter than the previous
- A relation in BCNF is always in 3NF, 2NF, and 1NF (but not vice versa)
- 2NF only applies to relations with composite candidate keys; single-attribute keys are automatically in 2NF if in 1NF
- BCNF decomposition may not preserve all functional dependencies; 3NF always preserves dependencies
- The goal is achieving lossless-join decompositions that eliminate update, insertion, and deletion anomalies

## Common Mistakes to Avoid

- Forgetting to identify ALL candidate keys before checking normal forms
- Confusing partial dependencies with transitive dependencies—partial involves parts of the key, transitive involves non-key attributes
- Assuming BCNF is always achievable without losing dependencies—sometimes trade-offs are necessary
- Failing to verify that decomposition preserves the ability to reconstruct original data (lossless join)

## Revision Tips

1. Practice identifying candidate keys from given functional dependencies—start with closure computation
2. Memorize the formal definitions of each normal form, not just informal descriptions
3. Work through at least 5-10 decomposition problems to become proficient in the algorithm
4. Remember: 3NF allows exceptions where left side isn't a superkey if right side is prime; BCNF does not
5. Review the relationship between normal forms and anomaly prevention for conceptual questions