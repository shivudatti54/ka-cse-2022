# Functional Dependencies — Quick Revision Summary

**Database Management Systems | BSc (Hons) CS | Delhi University (NEP 2024 UGCF)**

---

## Introduction

Functional Dependencies (FDs) form the theoretical foundation of **relational database design** and **normalization**. Introduced in the Delhi University UG-CF syllabus under the Database Management Systems (DMS) paper, FDs describe relationships between attributes and help eliminate data redundancy and anomalies.

---

## Key Concepts

### 1. Definition
- A functional dependency **X → Y** holds in a relation R if for every pair of tuples, whenever X has the same value, Y must also have the same value.
- **X** is the *determinant* (LHS); **Y** is the *dependent* (RHS).

### 2. Types of Functional Dependencies
- **Trivial FD**: X → Y where Y ⊆ X (always holds)
- **Non-trivial FD**: X → Y where Y ⊄ X
- **Completely Non-trivial**: X → Y where X ∩ Y = ∅
- **Multivalued Dependency (MVD)**: X →→ Y (each X value determines a set of Y values)
- **Transitive Dependency**: X → Y, Y → Z ⇒ X → Z

### 3. Armstrong's Axioms (Inference Rules)
- **Reflexivity**: If Y ⊆ X, then X → Y
- **Augmentation**: If X → Y, then XZ → YZ
- **Transitivity**: If X → Y and Y → Z, then X → Z

*Derived rules*: Union, Decomposition, Pseudotransitivity

### 4. Closure
- **Attribute Closure (X⁺)**: Set of all attributes functionally determined by X
- **FD Closure (F⁺)**: Complete set of all FDs derivable from F using axioms

### 5. Minimal Cover (Canonical Cover)
- FDs with single RHS attributes
- No redundant LHS attributes
- No redundant FDs

### 6. Keys and Superkeys
- **Superkey**: Attribute set K where K → R (all attributes)
- **Candidate Key**: Minimal superkey (no proper subset is a key)
- **Prime Attribute**: Part of any candidate key

### 7. Functional Dependencies in Normalization
| Normal Form | Condition Based on FDs |
|-------------|------------------------|
| 1NF | Atomic values (relation must be relational) |
| 2NF | 1NF + No partial dependencies (non-prime attributes depend on whole candidate key) |
| 3NF | 1NF + No transitive dependencies (for each X → Y, X is a superkey or Y is prime) |
| BCNF | 1NF + For every FD X → Y, X must be a superkey |

### 8. Additional Properties
- **Lossless Join Decomposition**: R ⊇ (R1 ⋈ R2); ensures no spurious tuples
- **Dependency Preservation**: All FDs from original relation should be enforceable in decomposed relations

---

## Conclusion

Functional dependencies are essential for designing anomaly-free relational databases. Understanding Armstrong's axioms, closure computation, and normalization based on FDs is crucial for the Delhi University B.Sc. (Hons) CS examination. Master these concepts to solve problems on finding candidate keys, minimal covers, and normal form violations effectively.

---

*Refer: DBMS Unit 3 — Relational Database Design, Delhi University NEP 2024 UG-CF Syllabus*