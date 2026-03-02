# Discrete Mathematical Structures

## **Module: Relations and Functions**

### Properties of Relations

In discrete mathematics, a relation is a connection between elements of a set. Relations are used to describe relationships between objects, and they have several properties that make them useful in various applications.

#### Definition

A relation R on a set A is a subset of the Cartesian product A × A, denoted as R ⊆ A × A. The relation R is said to be true or satisfied for two elements a, b ∈ A if (a, b) ∈ R.

#### Properties of Relations

A relation R on a set A has the following properties:

1.  **Reflexivity**: A relation R on a set A is reflexive if (a, a) ∈ R for all a ∈ A. This means that every element is related to itself.

    Beispiel: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3)}. Then R is reflexive.

2.  **Symmetry**: A relation R on a set A is symmetric if (a, b) ∈ R implies (b, a) ∈ R for all a, b ∈ A. This means that if a is related to b, then b is also related to a.

    Beispiel: Let A = {1, 2, 3} and R = {(1, 2), (2, 1), (3, 3)}. Then R is symmetric.

3.  **Transitivity**: A relation R on a set A is transitive if (a, b) ∈ R and (b, c) ∈ R implies (a, c) ∈ R for all a, b, c ∈ A. This means that if a is related to b and b is related to c, then a is also related to c.

    Beispiel: Let A = {1, 2, 3} and R = {(1, 2), (2, 3), (1, 3)}. Then R is transitive.

4.  **Antisymmetry**: A relation R on a set A is antisymmetric if (a, b) ∈ R and (b, a) ∈ R implies a = b for all a, b ∈ A. This means that if a is related to b and b is related to a, then a and b must be the same element.

    Beispiel: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3)}. Then R is antisymmetric.

5.  **Irreflexivity**: A relation R on a set A is irreflexive if (a, a) ∉ R for all a ∈ A. This means that no element is related to itself.

    Beispiel: Let A = {1, 2, 3} and R = {(1, 2), (2, 3)}. Then R is irreflexive.

6.  **Asymmetry**: A relation R on a set A is asymmetric if (a, b) ∈ R and (b, a) ∉ R for all a, b ∈ A. This means that if a is related to b, then b cannot be related to a.

    Beispiel: Let A = {1, 2, 3} and R = {(1, 2), (2, 3)}. Then R is asymmetric.

### Computer Recognition – Zero-One Matrices and Directed Graphs

Zero-one matrices and directed graphs are used to represent relations in computer science.

#### Zero-One Matrices

A zero-one matrix is a matrix where all elements are either 0 or 1. The value of a matrix is used to indicate whether a relation exists between two elements.

|     | A   | B   |
| --- | --- | --- |
| A   | 0   | 1   |
| B   | 1   | 0   |

In this matrix, there is a relation between A and B.

#### Directed Graphs

A directed graph is a graph where edges have direction. Each edge represents a relation between two elements.

## Directed Graph Example

|     | A   | B   | C   |
| --- | --- | --- | --- |
| A   |     | 1   | 1   |
| B   | 1   |     | 1   |
| C   | 1   | 1   |     |

In this graph, there are directed edges from A to B, from B to A, from A to C, and from C to A.

### Partial Orders – Hasse Diagrams

A partial order is a relation that is reflexive, antisymmetric, and transitive.

#### Definition

A partial order on a set A is a binary relation R that satisfies the following properties:

- Reflexivity: (a, a) ∈ R for all a ∈ A.
- Antisymmetry: (a, b) ∈ R and (b, a) ∈ R implies a = b for all a, b ∈ A.
- Transitivity: (a, b) ∈ R and (b, c) ∈ R implies (a, c) ∈ R for all a, b, c ∈ A.

#### Hasse Diagrams

A Hasse diagram is a graphical representation of a partial order. Each element is represented as a node, and there is an edge from one node to another if the corresponding elements are related.

## Hasse Diagram Example

`A = {1, 2, 3, 4, 5}`

- Relations:
  - (1, 2), (2, 3), (3, 4), (4, 5)
  - (2, 3), (3, 4), (5, 4)
  - (1, 4), (2, 5), (5, 3)
  - (3, 5), (4, 5)

  Hasse Diagram:

        5
      / | \

  3 4
  / \ / \
   2 1

In this Hasse diagram, the partial order on A is represented by the relations.

### Equivalence Relations and Partitions

An equivalence relation is a relation that is reflexive, symmetric, and transitive.

#### Definition

An equivalence relation on a set A is a binary relation R that satisfies the following properties:

- Reflexivity: (a, a) ∈ R for all a ∈ A.
- Symmetry: (a, b) ∈ R implies (b, a) ∈ R for all a, b ∈ A.
- Transitivity: (a, b) ∈ R and (b, c) ∈ R implies (a, c) ∈ R for all a, b, c ∈ A.

#### Partitions

A partition is a set of subsets of a set such that every element is in exactly one subset.

#### Equivalence Classes

An equivalence class is a set of elements that are related to each other.

## Equivalence Class Example

`A = {1, 2, 3, 4, 5}`

- Relations:
  - (1, 2), (2, 3), (3, 4), (4, 5)
  - (2, 3), (3, 4), (5, 4)

  Equivalence Classes:
  - [1] = {1, 2}
  - [3] = {3, 4}
  - [5] = {5}

In this example, the equivalence classes are [1], [3], and [5].

## Further Reading

- [1] "Discrete Mathematical Structures" by Kenneth H. Rosen
- [2] "Introduction to Algorithms" by Thomas H. Cormen
- [3] "Graph Theory" by Douglas B. West
- [4] "Partial Orders and Total Orders" by Robin Hartshorne
- [5] "Equivalence Relations" by Bryan P. Kowalski

This list includes some of the most influential texts in the field of discrete mathematical structures. They provide a comprehensive overview of the subject and offer a range of perspectives and approaches to the study of relations, functions, and discrete structures.
