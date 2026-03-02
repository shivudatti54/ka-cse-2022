# **Discrete Mathematical Structures**

## **Relations and Functions**

### Introduction

Relations and functions are fundamental concepts in discrete mathematics. A relation between two sets is a subset of the Cartesian product of the two sets. A function, on the other hand, is a special type of relation that assigns to each element in the domain a unique element in the codomain.

### Relations

#### Definition

A relation R between two sets A and B is a subset of the Cartesian product A × B.

#### Notation

R ⊆ A × B

#### Types of Relations

- **Equivalence Relation**: A relation R on a set A is an equivalence relation if it satisfies the following properties:
  - Reflexivity: aRa for all a ∈ A
  - Symmetry: if aRb then bRa
  - Transitivity: if aRb and bRc then aRc
- **Partial Order**: A relation R on a set A is a partial order if it satisfies the following properties:
  - Reflexivity: aRa
  - Anti-symmetry: if aRb and bRa then a = b
  - Transitivity: if aRb and bRc then aRc

#### Examples

- A teacher grades students on a scale of 0-100. The relation "student grade" is a relation between the set of students and the set of grades, where each student is related to a grade.
- A traffic light is a relation between the set of directions (north, south, east, west) and the set of actions (stop, go), where each direction is related to an action.

### Functions

#### Definition

A function f from a set A to a set B is a relation f ⊆ A × B that satisfies the following properties:

- **Injectivity**: for every two distinct elements a, b ∈ A, there exists an element b' ∈ B such that f(a) = b' and f(b) ≠ b'
- **Surjectivity**: for every element b' ∈ B, there exists an element a ∈ A such that f(a) = b'

#### Notation

f: A → B

#### Types of Functions

- **Injective Function**: A function f: A → B is injective if it is injective.
- **Surjective Function**: A function f: A → B is surjective if it is surjective.
- **Bijective Function**: A function f: A → B is bijective if it is both injective and surjective.

#### Examples

- A person's name is a function from the set of people to the set of names.
- A mathematical function, such as f(x) = 2x, is a function from the set of real numbers to the set of real numbers.

### Exercises

- Define and give examples of equivalence relations and partial orders.
- Determine whether the following relations are functions or not:
  - {(1, 2), (2, 1), (3, 3)}
  - {(1, 2), (2, 1), (3, 4)}
- Prove that a relation is injective if and only if it is one-to-one.
- Prove that a relation is surjective if and only if it is onto.

### Key Concepts

- **Domain**: The set of elements to which the function is applied.
- **Codomain**: The set of elements to which the function maps.
- **Range**: The set of elements to which the function maps.

### Conclusion

Relations and functions are fundamental concepts in discrete mathematics. Understanding the definition, types, and properties of relations and functions is essential for solving problems in computer science, mathematics, and other fields.
