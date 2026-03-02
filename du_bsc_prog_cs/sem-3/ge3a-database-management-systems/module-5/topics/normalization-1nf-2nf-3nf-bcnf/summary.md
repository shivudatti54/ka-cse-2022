# Normalization (1NF, 2NF, 3NF, BCNF) - Summary

## Key Definitions and Concepts

- **Normalization:** The process of organizing data into tables to minimize redundancy and avoid insertion, deletion, and update anomalies
- **Functional Dependency:** A constraint where attribute A determines attribute B (A → B), meaning identical A values guarantee identical B values
- **Candidate Key:** A minimal superkey that uniquely identifies all attributes in a relation
- **Prime Attribute:** An attribute that is part of any candidate key
- **Partial Dependency:** When a non-prime attribute depends on only part of a composite candidate key
- **Transitive Dependency:** When a non-prime attribute depends on another non-prime attribute, which depends on the candidate key

## Important Formulas and Theorems

- **1NF Criterion:** All attributes must contain atomic (indivisible) values only
- **2NF Criterion:** Relation in 1NF + no partial dependencies (all non-prime attributes fully dependent on entire candidate key)
- **3NF Criterion:** Relation in 2NF + no transitive dependencies (for X → A: X is superkey OR A is prime attribute)
- **BCNF Criterion:** For every non-trivial FD X → Y, X must be a superkey

## Key Points

- Normalization progresses from 1NF → 2NF → 3NF → BCNF, each eliminating specific types of redundancy
- A relation in BCNF is always in 3NF, but a relation in 3NF may not be in BCNF
- The three database anomalies are insertion, deletion, and update anomalies
- Decomposition should ideally be lossless (common attribute must be a key in at least one relation) and dependency-preserving
- To check normal form, first identify all candidate keys and functional dependencies
- BCNF is more restrictive than 3NF because it does not allow FDs where right side is a prime attribute unless left side is a superkey

## Common Mistakes to Avoid

- Assuming a relation in 1NF is automatically in higher normal forms—it must satisfy each level's criteria
- Confusing partial dependencies with transitive dependencies—partial involves candidate key parts, transitive involves non-prime attributes
- Forgetting that 3NF has an exception clause (allows right side to be prime attribute) while BCNF does not
- Incorrectly identifying candidate keys, which leads to wrong determination of prime attributes and normal form

## Revision Tips

- Practice identifying functional dependencies from sample relations—this is the foundation for determining normal forms
- Memorize the formal definitions of each normal form along with practical rules
- Solve previous years' DU exam questions on normalization to understand the question patterns
- When given a relation with FDs, always check normal forms in order: 1NF → 2NF → 3NF → BCNF