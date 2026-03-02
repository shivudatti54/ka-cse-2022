# Decomposition in Database Normalization

## What is Decomposition?

**Decomposition** is the process of breaking down a relation into smaller relations to eliminate redundancy and anomalies while preserving data integrity.

## Goals of Decomposition

1. **Eliminate redundancy** - Remove duplicate data
2. **Prevent anomalies** - Avoid insert, update, delete anomalies
3. **Preserve information** - No data loss (lossless join)
4. **Preserve dependencies** - Maintain all functional dependencies

## Types of Decomposition

### 1. Lossless-Join Decomposition

A decomposition of R into R1 and R2 is **lossless** if:

```
R1 ⋈ R2 = R (natural join recovers original relation)
```

**Test for Lossless Join**:
Decomposition into R1 and R2 is lossless if and only if:

- (R1 ∩ R2) → R1, OR
- (R1 ∩ R2) → R2

The common attributes must be a superkey of at least one decomposed relation.

### 2. Dependency-Preserving Decomposition

A decomposition **preserves dependencies** if all original FDs can be checked within individual decomposed relations without computing joins.

**Test**: For each FD X → Y in F:

- Either X → Y can be verified in some Ri
- Or X → Y can be derived from FDs in decomposed relations

## Decomposition Algorithm (BCNF)

```
Input: Relation R with FDs F
Output: Set of BCNF relations

1. If R is in BCNF, return {R}
2. Find violating FD: X → Y where X is not a superkey
3. Decompose R into:
   - R1 = X ∪ Y
   - R2 = R - (Y - X)
4. Recursively decompose R1 and R2
```

## Example: BCNF Decomposition

**Original**: Student(SID, Name, DeptID, DeptName, HOD)

**FDs**:

- SID → Name, DeptID
- DeptID → DeptName, HOD

**Problem**: DeptID → DeptName, HOD violates BCNF (DeptID is not a superkey)

**Decomposition**:

1. R1 = Department(DeptID, DeptName, HOD)
2. R2 = Student(SID, Name, DeptID)

**Verification**:

- R1 ∩ R2 = {DeptID}
- DeptID → DeptName, HOD (DeptID is key of R1) ✓
- Lossless: DeptID is superkey of R1 ✓

## 3NF vs BCNF Decomposition

| Aspect                | 3NF               | BCNF                |
| --------------------- | ----------------- | ------------------- |
| Lossless              | Always achievable | Always achievable   |
| Dependency Preserving | Always achievable | Not always possible |
| Redundancy            | Some may remain   | Minimal             |

## Common Pitfalls

1. **Lossy decomposition**: Always verify the lossless condition
2. **Lost dependencies**: Check if all FDs are preserved
3. **Over-decomposition**: Don't decompose beyond necessary

## Key Formulas

**Lossless Test**: R1 ∩ R2 must be a superkey of R1 or R2

**Chase Algorithm**: For complex decompositions, use chase test to verify losslessness
