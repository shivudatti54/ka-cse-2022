# Binary Relations and Equivalence

## Introduction

Binary relations form one of the most fundamental concepts in discrete mathematics, serving as the cornerstone for understanding structured relationships between elements of sets. In computer science, binary relations appear in numerous practical applications: database systems use relations to represent tables and connections between data entities; directed graphs utilize relations to model networks and dependencies; formal language theory employs relations to define grammar productions; and object-oriented programming uses relations to establish class hierarchies and associations.

The study of equivalence relations holds particular significance in computer science because they enable us to categorize and partition sets based on shared properties. When we say two elements are "equivalent" under some criteria, we are essentially creating meaningful groups that simplify complex problems. For instance, in modular arithmetic, congruence modulo n creates equivalence classes that are crucial for cryptography and hash functions. In compilers, equivalence relations help identify tokens and in parsing algorithms, they assist in constructing state machines. Understanding these mathematical structures is therefore essential for any computer science student, particularly when studying formal languages, database management, and algorithm design.

This module will explore the formal definitions of binary relations, their properties (reflexive, symmetric, antisymmetric, and transitive), and most importantly, equivalence relations and their connection to partitions. These concepts will be reinforced through numerous examples and problem-solving techniques essential for semester examinations.

## Key Concepts

### Binary Relation: Definition and Representation

A **binary relation** R from set A to set B is a subset of the Cartesian product A × B. If (a, b) ∈ R, we say that "a is related to b" and denote this as aRb. When A = B, we say R is a relation on A.

**Formal Definition**: Let A and B be sets. A binary relation R from A to B is a subset of A × B, i.e., R ⊆ A × B.

For a relation on a set A (where R ⊆ A × A), we can represent it in multiple ways:

1. **Set Notation**: R = {(1,1), (1,2), (2,3), (3,3)}
2. **Matrix Representation (Adjacency Matrix)**: For finite sets, an n×n boolean matrix where entry M[i][j] = 1 if (a_i, a_j) ∈ R
3. **Digraph Representation**: A directed graph with vertices representing elements and directed edges representing ordered pairs

**Example**: Let A = {1, 2, 3}. The relation "less than" is R = {(1,2), (1,3), (2,3)}. As a matrix:
```
   1 2 3
1  0 1 1
2  0 0 1
3  0 0 0
```

### Properties of Relations

For a relation R on set A:

1. **Reflexive**: ∀a ∈ A, (a, a) ∈ R
   - Every element is related to itself
   - Matrix: All diagonal entries are 1

2. **Symmetric**: ∀a, b ∈ A, if (a, b) ∈ R then (b, a) ∈ R
   - The relation works both ways
   - Matrix: M = M^T (symmetric matrix)

3. **Antisymmetric**: ∀a, b ∈ A, if (a, b) ∈ R and (b, a) ∈ R then a = b
   - No two distinct elements relate mutually
   - Matrix: If M[i][j] = 1 and i ≠ j, then M[j][i] = 0

4. **Transitive**: ∀a, b, c ∈ A, if (a, b) ∈ R and (b, c) ∈ R then (a, c) ∈ R
   - Related elements propagate through the relation
   - If (a,b) and (b,c) exist, (a,c) must also exist

### Equivalence Relations

An **equivalence relation** is a relation that is simultaneously reflexive, symmetric, and transitive. Equivalence relations partition a set into disjoint equivalence classes.

**Examples of Equivalence Relations**:
- Equality on any set
- "Has the same remainder as" (congruence modulo n) on integers
- "Same first letter" on strings
- "Lives in the same city as" on people

### Equivalence Classes

Given an equivalence relation R on set A, the **equivalence class** of an element a ∈ A is defined as:
[a] = {x ∈ A | xRa} = {x ∈ A | (a, x) ∈ R}

**Properties of Equivalence Classes**:
1. For any a ∈ A, a ∈ [a] (by reflexivity)
2. If b ∈ [a], then [b] = [a] (classes are equal or disjoint)
3. The equivalence classes form a partition of A

### Partition of a Set

A **partition** of set A is a collection of non-empty, pairwise disjoint subsets whose union equals A. Each subset in the partition is called a **block** or **cell**.

**Theorem**: There is a one-to-one correspondence between equivalence relations on A and partitions of A. Given an equivalence relation, its equivalence classes form a partition, and given a partition, we can define an equivalence relation where elements are related if they belong to the same block.

### Composition of Relations

Let R be a relation from A to B, and S be a relation from B to C. The **composition** S ∘ R is a relation from A to C defined as:
S ∘ R = {(a, c) ∈ A × C | ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}

**Properties**:
- (R ∘ S) ∘ T = R ∘ (S ∘ T) (associativity)
- (R ∘ S)^(-1) = S^(-1) ∘ R^(-1)

### Inverse Relation

For a relation R ⊆ A × B, the **inverse relation** R^(-1) ⊆ B × A is defined as:
R^(-1) = {(b, a) | (a, b) ∈ R}

### Closure Operations

The **closure** of a relation R with respect to a property P is the smallest relation containing R that possesses property P.

- **Reflexive Closure**: R ∪ I_A (adds all diagonal pairs)
- **Symmetric Closure**: R ∪ R^(-1) (adds all reverse pairs)
- **Transitive Closure**: R ∪ R^2 ∪ R^3 ∪ ... (connects all reachable pairs)

## Examples

### Example 1: Analyzing Relation Properties

Let A = {1, 2, 3, 4} and R = {(1,1), (1,2), (2,1), (2,2), (3,3), (3,4), (4,3), (4,4)}. Determine which properties (reflexive, symmetric, antisymmetric, transitive) R satisfies.

**Solution**:

- **Reflexive**: Check (1,1), (2,2), (3,3), (4,4) ∈ R.
  - All four diagonal pairs exist → **Reflexive** ✓

- **Symmetric**: If (a,b) ∈ R, check (b,a) ∈ R.
  - (1,2) ∈ R and (2,1) ∈ R ✓
  - (3,4) ∈ R and (4,3) ∈ R ✓
  - All pairs have their symmetric counterparts → **Symmetric** ✓

- **Antisymmetric**: If (a,b) ∈ R and (b,a) ∈ R, then a = b.
  - (1,2) ∈ R and (2,1) ∈ R but 1 ≠ 2 → **Not Antisymmetric** ✗

- **Transitive**: If (a,b) ∈ R and (b,c) ∈ R, check (a,c) ∈ R.
  - (1,2) ∈ R and (2,1) ∈ R → need (1,1) ∈ R. It's there ✓
  - (1,2) ∈ R and (2,2) ∈ R → need (1,2) ∈ R. It's there ✓
  - (3,4) ∈ R and (4,3) ∈ R → need (3,3) ∈ R. It's there ✓
  - (3,4) ∈ R and (4,4) ∈ R → need (3,4) ∈ R. It's there ✓
  - All valid → **Transitive** ✓

**Answer**: R is reflexive, symmetric, and transitive (but not antisymmetric). Therefore, R is an equivalence relation.

### Example 2: Finding Equivalence Classes

Define relation R on integers Z by aRb iff a - b is divisible by 3 (i.e., a ≡ b (mod 3)). Find the equivalence classes.

**Solution**:

We need to verify R is an equivalence relation:
- **Reflexive**: a - a = 0, divisible by 3 → aRa ✓
- **Symmetric**: If a - b = 3k, then b - a = -3k, divisible by 3 → bRa ✓
- **Transitive**: If a - b = 3k and b - c = 3l, then a - c = 3(k+l), divisible by 3 → aRc ✓

Thus R is an equivalence relation.

**Finding Equivalence Classes**:

For any integer a, [a] = {x ∈ Z | x ≡ a (mod 3)}

- [0] = {..., -6, -3, 0, 3, 6, ...} = {3k | k ∈ Z}
- [1] = {..., -5, -2, 1, 4, 7, ...} = {3k + 1 | k ∈ Z}
- [2] = {..., -4, -2, 2, 5, 8, ...} = {3k + 2 | k ∈ Z}

These three classes partition Z. No other distinct classes exist.

**Answer**: The equivalence classes are [0], [1], and [2], often denoted as 0̅, 1̅, 2̅ (the integers modulo 3).

### Example 3: Relation Composition

Let A = {1, 2, 3, 4}, R = {(1,2), (2,3), (3,4)} and S = {(2,1), (3,2), (4,3)}. Find S ∘ R.

**Solution**:

S ∘ R = {(a, c) | ∃b such that (a, b) ∈ R and (b, c) ∈ S}

Check each pair in R:
- For (1,2) ∈ R: Need b = 2. Check if (2, c) ∈ S for any c.
  - (2,1) ∈ S → So (1,1) ∈ S ∘ R
- For (2,3) ∈ R: Need b = 3. Check (3, c) ∈ S.
  - (3,2) ∈ S → So (2,2) ∈ S ∘ R
- For (3,4) ∈ R: Need b = 4. Check (4, c) ∈ S.
  - (4,3) ∈ S → So (3,3) ∈ S ∘ R

**Answer**: S ∘ R = {(1,1), (2,2), (3,3)}

Notice that S ∘ R = identity relation on {1,2,3}, a subset of A.

## Exam Tips

1. **Know the Properties Thoroughly**: In exams, you'll often be given a relation in set or matrix form and asked to determine which properties it satisfies. Remember: reflexive needs all diagonal 1s; symmetric needs mirror image; transitive needs closure under "chaining."

2. **Quick Test for Antisymmetric**: Instead of checking all pairs, remember that if you find any (a,b) with a ≠ b where both (a,b) and (b,a) exist, the relation is NOT antisymmetric.

3. **Equivalence Relation = Three Properties**: When asked "Is this relation an equivalence relation?" always check all three: reflexive, symmetric, AND transitive. Missing any one means NO.

4. **Partition-Equivalence Connection**: If asked to find the partition induced by an equivalence relation, find all distinct equivalence classes. Conversely, if given a partition, the equivalence relation is "belong to the same block."

5. **Matrix Power Method for Transitive Closure**: For transitive closure on finite sets, compute R, R², R³,... until no new pairs are added. In matrix form, use Boolean multiplication: R+ = R ∨ R² ∨ R³ ∨ ...

6. **Practice Matrix to Digraph Conversions**: Many exam questions present a relation as a matrix and ask about properties. Know that row i column j entry gives (i,j), diagonal = reflexive check, symmetry = mirror images.

7. **Modular Arithmetic is Key**: The relation "a ≡ b (mod n)" is the most common example of equivalence relations in exams. Know that it creates exactly n equivalence classes: [0], [1], ..., [n-1].

8. **Inverse Relation Trick**: To find inverse quickly, just swap each ordered pair: (a,b) becomes (b,a). In matrix form, transpose the matrix.