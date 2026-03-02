# Set Theory Fundamentals

## Introduction to Sets
Set theory is the branch of mathematical logic that studies sets, which are collections of objects. In computer science, set theory provides the foundation for data structures, database theory, and algorithm design. A set is a well-defined collection of distinct objects, considered as an object in its own right.

**Basic Notation:**
- Sets are usually denoted by capital letters: A, B, C, ...
- Elements are denoted by lowercase letters: a, b, c, ...
- The notation a ∈ A means "a is an element of A"
- The notation a ∉ A means "a is not an element of A"

## Methods of Describing Sets

### 1. Roster Method
Listing all elements between curly braces.

**Example:**
- A = {1, 2, 3, 4, 5}
- B = {a, e, i, o, u}

### 2. Set-Builder Notation
Describing a set by specifying a property that its members must satisfy.

**Example:**
- C = {x | x is an even integer}
- D = {x | x > 0 and x is a real number}

### 3. Interval Notation
Used primarily for sets of real numbers.

**Example:**
- E = [0, 5] = {x | 0 ≤ x ≤ 5}
- F = (2, 8) = {x | 2 < x < 8}

## Types of Sets

### Finite Sets
Sets with a countable number of elements.

**Example:** {1, 2, 3}, {a, b, c, d}

### Infinite Sets
Sets with an unlimited number of elements.

**Example:** ℕ = {1, 2, 3, ...}, ℝ (all real numbers)

### Empty Set (Null Set)
The set containing no elements, denoted by ∅ or {}.

**Important:** ∅ ≠ {∅} (the latter is a set containing the empty set)

### Singleton Set
A set with exactly one element.

**Example:** {5}, {∅}

### Equal Sets
Two sets A and B are equal if they contain exactly the same elements.

**Example:** {1, 2, 3} = {3, 2, 1} (order doesn't matter)

### Equivalent Sets
Two sets have the same cardinality (number of elements) if there exists a bijection between them.

## Subsets

### Definition
A set A is a subset of B (written A ⊆ B) if every element of A is also an element of B.

**Properties:**
- For any set A, ∅ ⊆ A and A ⊆ A
- If A ⊆ B and B ⊆ C, then A ⊆ C

### Proper Subset
A is a proper subset of B (A ⊂ B) if A ⊆ B but A ≠ B.

**Example:** {1, 2} ⊂ {1, 2, 3}

### Power Set
The set of all subsets of a set S, denoted by P(S).

**Example:** If S = {1, 2}, then P(S) = {∅, {1}, {2}, {1, 2}}

**Fact:** If |S| = n, then |P(S)| = 2ⁿ

## Set Operations

### Union
A ∪ B = {x | x ∈ A or x ∈ B}

```
    A          B
   ___        ___
  /   \      /   \
 /     \    /     \
|  A   |  |   B   |
 \     /    \     /
  \___/      \___/
     \        /
      \______/
         A ∪ B
```

### Intersection
A ∩ B = {x | x ∈ A and x ∈ B}

```
    A          B
   ___        ___
  /   \      /   \
 /     \    /     \
| A∩B  |  | A∩B   |
 \     /    \     /
  \___/      \___/
```

### Difference
A - B = {x | x ∈ A and x ∉ B}

```
    A          B
   ___        ___
  /   \      /   \
 / A-B \    /     \
|       |  |       |
 \     /    \     /
  \___/      \___/
```

### Complement
Aᶜ = {x | x ∉ A} (relative to some universal set U)

```
      U
  ┌─────────┐
  │    Aᶜ   │
  │  ┌───┐  │
  │  │ A │  │
  │  └───┘  │
  └─────────┘
```

### Symmetric Difference
A Δ B = (A - B) ∪ (B - A) = {x | x ∈ A or x ∈ B but not both}

```
    A          B
   ___        ___
  /   \      /   \
 / A-B \    / B-A \
|       |  |       |
 \     /    \     /
  \___/      \___/
```

## Venn Diagrams

Venn diagrams are visual representations of sets and their relationships.

**Basic Venn Diagram for Two Sets:**
```
      U
  ┌─────────┐
  │ A       │
  │  ┌───┐  │
  │  │A∩B│  │
  │  └───┘  │
  │       B │
  └─────────┘
```

**Three-Set Venn Diagram:**
```
        U
    ┌─────────┐
    │   A     │
    │  ┌───┐  │
    │  │A∩B│  │
    │  └───┘  │
    │ B     C │
    └─────────┘
```

## Set Identities

| Identity Name | Law |
|---------------|-----|
| Identity Laws | A ∪ ∅ = A, A ∩ U = A |
| Domination Laws | A ∪ U = U, A ∩ ∅ = ∅ |
| Idempotent Laws | A ∪ A = A, A ∩ A = A |
| Complement Laws | A ∪ Aᶜ = U, A ∩ Aᶜ = ∅ |
| Commutative Laws | A ∪ B = B ∪ A, A ∩ B = B ∩ A |
| Associative Laws | (A ∪ B) ∪ C = A ∪ (B ∪ C), (A ∩ B) ∩ C = A ∩ (B ∩ C) |
| Distributive Laws | A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C), A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| De Morgan's Laws | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ, (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ |
| Absorption Laws | A ∪ (A ∩ B) = A, A ∩ (A ∪ B) = A |

## Cartesian Product

The Cartesian product of two sets A and B is:
A × B = {(a, b) | a ∈ A and b ∈ B}

**Example:** If A = {1, 2} and B = {a, b}, then:
A × B = {(1, a), (1, b), (2, a), (2, b)}

**Note:** |A × B| = |A| × |B|

## Cardinality

The cardinality of a set A, denoted |A|, is the number of elements in A.

**Inclusion-Exclusion Principle:**
|A ∪ B| = |A| + |B| - |A ∩ B|
|A ∪ B ∪ C| = |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|

## Applications in Computer Science

1. **Database Systems:** SQL operations (UNION, INTERSECT, EXCEPT) are based on set operations
2. **Data Structures:** Sets, hash tables, and bloom filters
3. **Algorithm Design:** Set cover problems, clustering algorithms
4. **Programming Languages:** Type systems, set data structures
5. **Networking:** IP address ranges and subnet calculations

## Exam Tips

1. **Memorize Key Identities:** Focus on De Morgan's Laws and distributive laws
2. **Practice Venn Diagrams:** Draw them for complex problems to visualize solutions
3. **Use Set Notation Properly:** Pay attention to ∈ vs ⊆ and ∅ vs {∅}
4. **Cardinality Calculations:** Remember the inclusion-exclusion principle
5. **Proof Strategies:** For proving set equality, show A ⊆ B and B ⊆ A
6. **Watch for Empty Set Cases:** Many proofs have special cases when sets are empty