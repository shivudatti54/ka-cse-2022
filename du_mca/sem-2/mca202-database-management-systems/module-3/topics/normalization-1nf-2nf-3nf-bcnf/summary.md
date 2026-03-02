# Normalization: 1NF, 2NF, 3NF, and BCNF - Summary

## Key Definitions and Concepts

- **Normalization:** The process of organizing data into tables to minimize redundancy and eliminate anomalies (insertion, update, deletion).
- **Functional Dependency (FD):** A constraint where attribute A determines attribute B (A → B); for any two tuples with same A value, B value must be identical.
- **Candidate Key:** Minimal set of attributes that uniquely identifies each tuple; multiple candidate keys may exist.
- **Prime Attribute:** An attribute that is part of any candidate key.
- **Non-Prime Attribute:** An attribute not part of any candidate key.
- **Partial Dependency:** When a non-prime attribute depends on part of a composite candidate key.
- **Transitive Dependency:** When attribute C depends on B, and B depends on A (X → Y → Z form).

## Important Formulas and Theorems

- **1NF Condition:** All attributes contain atomic (indivisible) values only.
- **2NF Condition:** Relation in 1NF + no partial dependencies on proper subset of candidate key.
- **3NF Condition:** Relation in 2NF + no transitive dependencies (for X → Y where Y is non-prime, either X is a superkey or Y is prime).
- **BCNF Condition:** For every non-trivial FD X → Y, X must be a superkey.
- **Lossless-Join Test:** Decomposition of R into R1 and R2 is lossless if (R1 ∩ R2) → R1 or (R1 ∩ R2) → R2 holds.

## Key Points

1. Normalization progresses through stages: 1NF → 2NF → 3NF → BCNF; each builds upon the previous.
2. 1NF eliminates repeating groups and composite values; essential for any relational database.
3. 2NF eliminates partial dependencies where non-key attributes depend on part of a composite key.
4. 3NF eliminates transitive dependencies, ensuring non-key attributes depend only on the primary key.
5. BCNF is stricter than 3NF; handles anomalies with multiple candidate keys.
6. Every BCNF relation is in 3NF, but not every 3NF relation is in BCNF.
7. Decomposition may lose dependency preservation—BCNF decomposition sometimes sacrifices this.
8. Lossless-join property must always be verified after decomposition.

## Common Mistakes to Avoid

1. **Skipping 1NF:** Many students directly attempt higher normal forms without ensuring atomic values.
2. **Ignoring candidate keys:** Using only primary key for normalization analysis leads to incorrect conclusions.
3. **Confusing partial and transitive dependencies:** Partial involves attributes within a composite key; transitive involves non-key attributes.
4. **Forgetting that BCNF is stricter:** A relation can be in 3NF but not BCNF when left-side is not a superkey.
5. **Not verifying lossless-join:** Decompositions that lose information are invalid, regardless of normal form achieved.

## Revision Tips

1. Practice identifying functional dependencies from sample relations repeatedly—this is the foundation.
2. Create a decision flowchart: Check atomic values (1NF) → Check partial dependencies (2NF) → Check transitive dependencies (3NF) → Check superkey requirement (BCNF).
3. Solve at least 5-10 previous year DU examination questions on normalization to understand marking patterns.
4. Memorize the formal definitions but also understand the practical meaning—examiners expect both.
5. When in doubt about partial dependencies, always check all proper subsets of ALL candidate keys, not just the primary key.