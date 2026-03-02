# Functional Dependencies

## Table of Contents

- [Functional Dependencies](#functional-dependencies)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Functional Dependency](#definition-of-functional-dependency)
  - [Types of Functional Dependencies](#types-of-functional-dependencies)
  - [Armstrong's Axioms](#armstrongs-axioms)
  - [Additional Inference Rules (Derived from Armstrong's Axioms)](#additional-inference-rules-derived-from-armstrongs-axioms)
  - [Closure of Attributes](#closure-of-attributes)
  - [Minimal Cover (Canonical Cover)](#minimal-cover-canonical-cover)
  - [Keys in Relations](#keys-in-relations)
- [Examples](#examples)
  - [Example 1: Computing Attribute Closure](#example-1-computing-attribute-closure)
  - [Example 2: Finding Candidate Keys](#example-2-finding-candidate-keys)
  - [Example 3: Minimal Cover](#example-3-minimal-cover)
- [Exam Tips](#exam-tips)

## Introduction

Functional Dependencies (FDs) form the theoretical foundation of relational database design and normalization. A functional dependency describes a relationship between attributes in a relation schema. When we say "X → Y" (X determines Y), it means that for any given value of X, there is exactly one corresponding value of Y in the relation. This concept was introduced by Edgar F. Codd as part of his relational model and is crucial for eliminating data redundancy and preventing anomalies in database systems.

Understanding functional dependencies is essential for any database professional because they help identify the logical relationships between attributes and determine whether a database schema is well-designed. In the context of the university's Database Management System course, functional dependencies are fundamental to learning normalization forms (1NF, 2NF, 3NF, BCNF) and solving exam problems related to decomposition of relations. This topic typically carries significant weightage in internal assessments and end-semester examinations.

## Key Concepts

### Definition of Functional Dependency

A functional dependency is a constraint between two sets of attributes in a relation schema. Let R be a relation schema, and let X and Y be subsets of R. The functional dependency X → Y holds if and only if for every possible relation r(R), whenever two tuples t1 and t2 in r have the same values for attributes in X, they must also have the same values for attributes in Y.

**Formal Definition:** X → Y if ∀t1, t2 ∈ r, (t1[X] = t2[X]) ⇒ (t1[Y] = t2[Y])

The set X is called the **determinant** or left-hand side (LHS), and Y is called the **dependent** or right-hand side (RHS) of the functional dependency.

### Types of Functional Dependencies

**1. Trivial Functional Dependency:**
A functional dependency X → Y is trivial if Y is a subset of X.

- Example: AB → A, AB → B are trivial FDs
- These are always true and do not add any meaningful information

**2. Non-Trivial Functional Dependency:**
A functional dependency X → Y is non-trivial if Y is not a subset of X.

- Example: Student_ID → Student_Name (non-trivial)

**3. Completely Non-Trivial Functional Dependency:**
X → Y is completely non-trivial if X ∩ Y = ∅ (X and Y share no common attributes)

- Example: Emp_ID → Dept_ID (assuming no common attributes)

### Armstrong's Axioms

Armstrong's axioms are a set of inference rules used to derive all functional dependencies from a given set of FDs:

**1. Reflexivity (Axiom of Reflexivity):**
If Y ⊆ X, then X → Y

- Example: If we have attributes {A, B, C}, then A → A, AB → A, ABC → BC

**2. Augmentation (Axiom of Augmentation):**
If X → Y, then XZ → YZ (adding same attributes to both sides)

- Example: If Student_ID → Student_Name, then Student_ID + Address → Student_Name + Address

**3. Transitivity (Axiom of Transitivity):**
If X → Y and Y → Z, then X → Z

- Example: If Emp_ID → Dept_ID and Dept_ID → Manager_ID, then Emp_ID → Manager_ID

### Additional Inference Rules (Derived from Armstrong's Axioms)

**1. Decomposition (or Projectivity):**
If X → YZ, then X → Y and X → Z

- Example: If Stud_ID → (Name, Address), then Stud_ID → Name and Stud_ID → Address

**2. Union (or Additivity):**
If X → Y and X → Z, then X → YZ

- Example: If Emp_ID → Name and Emp_ID → Address, then Emp_ID → Name + Address

**3. Pseudotransitivity:**
If X → Y and WY → Z, then WX → Z

- Example: If Emp_ID → Dept_ID and Dept_ID + Project → Manager, then Emp_ID + Project → Manager

### Closure of Attributes

**Attribute Closure (X⁺):**
The attribute closure of a set of attributes X is the set of all attributes that can be functionally determined by X using Armstrong's axioms.

**Algorithm to compute X⁺:**

```
X⁺ = X
repeat
 for each functional dependency Y → Z in F do
 if Y ⊆ X⁺ then
 X⁺ = X⁺ ∪ Z
 until (no change)
```

**FD Closure (F⁺):**
The closure of a set of functional dependencies F, denoted F⁺, is the set of all functional dependencies that can be inferred from F using Armstrong's axioms.

### Minimal Cover (Canonical Cover)

A minimal cover of a set of functional dependencies F is a set of functional dependencies F_c such that:

1. F_c is equivalent to F (F_c⁺ = F⁺)
2. Every RHS has a single attribute (all FDs are in canonical form)
3. No FD in F_c can be derived from other FDs in F_c
4. Removing any attribute from the LHS of an FD makes it not equivalent

**Steps to find Minimal Cover:**

1. Split RHS attributes: Break all FDs so that each has a single attribute on RHS
2. Minimize LHS: For each FD X → A, try to remove attributes from X one by one
3. Remove redundant FDs: Check if an FD can be derived from others

### Keys in Relations

**Super Key:**
A set of attributes SK is a super key of relation R if SK → all attributes of R (SK → R).

**Candidate Key:**
A minimal super key (no proper subset is a super key). There can be multiple candidate keys.

**Primary Key:**
One of the candidate keys selected as the primary key for the relation.

## Examples

### Example 1: Computing Attribute Closure

**Problem:** Given F = {A → BC, B → D, C → E}, compute (AB)⁺

**Solution:**

- Start: X⁺ = {A, B}
- Using A → BC: since A ∈ X⁺, add B and C → X⁺ = {A, B, C}
- Using B → D: since B ∈ X⁺, add D → X⁺ = {A, B, C, D}
- Using C → E: since C ∈ X⁺, add E → X⁺ = {A, B, C, D, E}
- No more attributes can be added
- **Result: (AB)⁺ = {A, B, C, D, E}**

### Example 2: Finding Candidate Keys

**Problem:** Given relation R(A, B, C, D, E) with F = {A → B, B → C, C → D, D → E}, find all candidate keys.

**Solution:**

- Since A determines all other attributes through the chain A → B → C → D → E, A is a candidate key
- Check if any proper subset of {A} can be a key: No (single attribute)
- Since A → R (all attributes), {A} is a candidate key
- Is there any other candidate key? Let's check: A⁺ = {A, B, C, D, E} = R
- Since A alone determines all attributes and is minimal, A is the only candidate key
- **Result: Candidate Key = {A}**

### Example 3: Minimal Cover

**Problem:** Find minimal cover for F = {AB → CD, A → E, C → D}

**Solution:**
**Step 1: Split RHS**
F1 = {AB → C, AB → D, A → E, C → D}

**Step 2: Minimize LHS**

- For AB → C: Check if A alone → C? From A → E, we cannot derive C. So keep AB → C
- For AB → D: Check if A alone → D? Cannot derive. Keep AB → D

**Step 3: Remove redundant FDs**

- Is AB → C redundant? F' = {AB → D, A → E, C → D}. From AB → D and C → D, cannot derive C. So keep AB → C
- Is AB → D redundant? F' = {AB → C, A → E, C → D}. Cannot derive D. So keep it
- Is A → E redundant? Cannot derive from others. Keep it
- Is C → D redundant? Cannot derive from others. Keep it

**Result: Minimal Cover F_c = {AB → C, AB → D, A → E, C → D}**

Alternatively, we can simplify to: {A → E, AB → C, AB → D, C → D} or further decompose AB → C, AB → D to {A → E, A → B, B → C, C → D} depending on closure.

## Exam Tips

1. **Understanding FD Notation:** Remember that X → Y means X determines Y, not the reverse. The arrow indicates functional determination, not equality.

2. **Armstrong's Axioms are Essential:** Memorize all three axioms (reflexivity, augmentation, transitivity) as they form the basis for solving most exam problems.

3. **Computing Attribute Closure:** This is the most frequently asked problem type. Practice the algorithm thoroughly - it's a systematic approach that always yields correct results.

4. **Trivial vs Non-Trivial:** For trivial FDs, the RHS is always a subset of LHS. In exams, carefully check whether the FD is trivial before applying rules.

5. **Finding Candidate Keys:** Compute the closure of each attribute or combination of attributes. If X⁺ = all attributes of R, then X is a super key. Check minimality to confirm it's a candidate key.

6. **Minimal Cover Questions:** Follow the three-step process systematically: split RHS, minimize LHS, remove redundant FDs. Many students lose marks by skipping steps.

7. **Applying Derived Rules:** Know when to use decomposition (to split RHS) and union (to combine FDs with same LHS) - these simplify problem-solving significantly.

8. **Understanding Relationship between FDs and Normalization:** Remember that functional dependencies determine how relations should be decomposed to achieve higher normal forms.

9. **Common Exam Patterns:** Most university questions ask for attribute closure computation, finding candidate keys, or determining whether a decomposition is lossless. Practice these thoroughly.

10. **Time Management:** In exams, first identify what's given (relation schema, set of FDs) and what needs to be found. Write the given information clearly before attempting the solution.
