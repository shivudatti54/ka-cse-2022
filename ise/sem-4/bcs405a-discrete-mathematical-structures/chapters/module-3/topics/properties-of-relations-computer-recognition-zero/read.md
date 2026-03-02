# **Properties of Relations, Computer Recognition – Zero-One Matrices and Directed Graphs, Partial Orders – Hasse Diagrams, Equivalence Relations and Part**

## **Properties of Relations**

A relation R on a set A is a subset of the Cartesian product A × A. The following are some important properties of relations:

- **Reflexivity**: A relation R on a set A is said to be reflexive if (a, a) ∈ R for all a ∈ A.
- **Symmetry**: A relation R on a set A is said to be symmetric if (a, b) ∈ R implies (b, a) ∈ R for all a, b ∈ A.
- **Transitivity**: A relation R on a set A is said to be transitive if (a, b) ∈ R and (b, c) ∈ R implies (a, c) ∈ R for all a, b, c ∈ A.
- **Antisymmetry**: A relation R on a set A is said to be antisymmetric if (a, b) ∈ R and (b, a) ∈ R implies a = b for all a, b ∈ A.

## **Computer Recognition – Zero-One Matrices and Directed Graphs**

A zero-one matrix is a matrix with all elements being either 0 or 1.

- **Representing Relations using Zero-One Matrices**: A zero-one matrix can be used to represent a relation R on a set A. The entry at row i and column j, denoted as R(i, j), is 1 if (i, j) ∈ R and 0 otherwise.
- **Directed Graphs**: A directed graph is a graph with directed edges. Each edge has a direction and can be represented using a zero-one matrix.

## **Partial Orders – Hasse Diagrams**

A partial order on a set A is a relation R that is reflexive, antisymmetric, and transitive.

- **Hasse Diagrams**: A Hasse diagram is a graphical representation of a partial order. It consists of nodes representing elements of the set, and edges representing the relation.

## **Equivalence Relations and Partitions**

An equivalence relation on a set A is a relation R that is reflexive, symmetric, and transitive.

- **Equivalence Classes**: The equivalence classes of an equivalence relation R on a set A are the sets {a ∈ A | (a, a) ∈ R} for all a ∈ A.
- **Partitions**: A partition of a set A is a collection of non-empty subsets of A such that every element of A is in exactly one subset.

## **Key Concepts**

- **Relation**: A subset of the Cartesian product of two sets.
- **Zero-One Matrix**: A matrix with all elements being either 0 or 1.
- **Directed Graph**: A graph with directed edges.
- **Partial Order**: A relation that is reflexive, antisymmetric, and transitive.
- **Hasse Diagram**: A graphical representation of a partial order.
- **Equivalence Relation**: A relation that is reflexive, symmetric, and transitive.
- **Equivalence Classes**: The sets {a ∈ A | (a, a) ∈ R} for all a ∈ A.
- **Partition**: A collection of non-empty subsets of a set A such that every element of A is in exactly one subset.

## **Examples**

1.  **Reflexive Relation**: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3)}. Then R is reflexive.
2.  **Symmetric Relation**: Let A = {1, 2, 3} and R = {(1, 2), (2, 1)}. Then R is symmetric.
3.  **Transitive Relation**: Let A = {1, 2, 3} and R = {(1, 2), (2, 3)}. Then R is transitive.
4.  **Antisymmetric Relation**: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}. Then R is antisymmetric.
5.  **Hasse Diagram**: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}. Then the Hasse diagram of R is:
    - 1
    - |
    - 2
    - |
    - 3
6.  **Equivalence Relation**: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (1, 3), (3, 1)}. Then R is an equivalence relation.
7.  **Partition**: Let A = {1, 2, 3} and R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}. Then the partition of A with respect to R is {{1}, {2}, {3}}.
