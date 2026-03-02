# Properties of Relations, Computer Recognition – Zero-One Matrices and Directed Graphs, Partial Orders – Hasse Diagrams, Equivalence Relations and Part

=====================================================

## Introduction

---

Relations are a fundamental concept in discrete mathematics, and they play a crucial role in computer science. In this study material, we will explore the properties of relations, computer recognition using zero-one matrices and directed graphs, partial orders, Hasse diagrams, equivalence relations, and partial orders.

## Properties of Relations

---

### Definition

A relation R on a set A is a subset of the Cartesian product A × A, i.e., R ⊆ A × A.

### Types of Relations

- **Equivalence Relation**: A relation R on a set A is said to be an equivalence relation if it satisfies the following properties:
  - Reflexive: (a, a) ∈ R for all a ∈ A
  - Symmetric: if (a, b) ∈ R, then (b, a) ∈ R
  - Transitive: if (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R
- **Partial Order**: A relation R on a set A is said to be a partial order if it satisfies the following properties:
  - Reflexive: (a, a) ∈ R for all a ∈ A
  - Antisymmetric: if (a, b) ∈ R and (b, a) ∈ R, then a = b
  - Transitive: if (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R

### Operations on Relations

- **Union**: The union of two relations R1 and R2 is defined as:
  - (a, b) ∈ R1 ∪ R2 if and only if (a, b) ∈ R1 or (a, b) ∈ R2
- **Intersection**: The intersection of two relations R1 and R2 is defined as:
  - (a, b) ∈ R1 ∩ R2 if and only if (a, b) ∈ R1 and (a, b) ∈ R2
- **Complement**: The complement of a relation R is defined as:
  - (a, b) ∈ R' if and only if (a, b) ∉ R

## Computer Recognition – Zero-One Matrices and Directed Graphs

---

### Definition

A zero-one matrix is a matrix where each entry is either 0 or 1. A directed graph is a graph where each edge has a direction.

### Representation of Relations Using Zero-One Matrices

A relation R on a set A can be represented using a zero-one matrix as follows:

| | a1 | a2 | ... | an |
| --- | --- | --- | ... | --- |
| a1 | 0 | 1 | ... | 0 |
| a2 | 1 | 0 | ... | 0 |
| ... | ... | ... | ... | ... |
| an | 0 | 0 | ... | 0 |

The entry (ai, j) is 1 if (ai, aj) ∈ R, and 0 otherwise.

### Representation of Relations Using Directed Graphs

A relation R on a set A can be represented using a directed graph as follows:

Create a vertex for each element in A, and draw an edge from a to b if (a, b) ∈ R.

## Partial Orders – Hasse Diagrams

---

### Definition

A partial order R on a set A is said to be a partial order if it satisfies the three properties mentioned earlier.

### Hasse Diagrams

A Hasse diagram is a graphical representation of a partial order R on a set A. Each vertex represents an element in A, and two vertices are joined by an edge if the corresponding elements are comparable in R.

### Example

Consider the partial order R on the set {a, b, c} defined as:

(a, b), (b, c), (a, c)

The Hasse diagram for R is:

        c
       / \
      b   a

## Equivalence Relations and Partitions

---

### Definition

An equivalence relation R on a set A is said to be an equivalence relation if it satisfies the three properties mentioned earlier.

### Partitions

A partition of a set A is a collection of non-empty subsets of A such that every element in A belongs to exactly one subset in the collection. The equivalence relation R on A is said to be a partition of A if and only if the equivalence classes of R are precisely the subsets in the partition.

### Example

Consider the equivalence relation R on the set {a, b, c} defined as:

(a, a), (b, b), (c, c), (a, b), (b, c), (a, c)

The partition of A induced by R is:

{a}, {b}, {c}

## Conclusion

---

In this study material, we have explored the properties of relations, computer recognition using zero-one matrices and directed graphs, partial orders, Hasse diagrams, equivalence relations, and partial orders. We have also discussed the representation of relations using zero-one matrices and directed graphs, and the use of Hasse diagrams to represent partial orders. Additionally, we have introduced the concept of equivalence relations and partitions, and provided an example of how to use equivalence relations to find partitions.
