# Functions – Plain and One-to-One

=====================================

## Introduction

---

In the context of discrete mathematical structures, a function is a relation between two sets that assigns to each element in the first set exactly one element in the second set. Functions play a crucial role in mathematics, particularly in the study of relations and algebraic structures.

## Plain Functions

---

A plain function, also known as a function without any restrictions, is a relation between two sets that assigns to each element in the first set exactly one element in the second set.

### Definition:

A relation R between sets A and B is a plain function if for every a in A, there exists a unique b in B such that (a, b) is in R.

### Example:

Let A = {1, 2, 3} and B = {a, b, c}. Define a plain function f: A → B as follows:

| a   | b   |
| --- | --- |
| 1   | a   |
| 2   | b   |
| 3   | c   |

In this example, f(1) = a, f(2) = b, and f(3) = c.

### Properties of Plain Functions:

- **Unique output**: For every element in the domain, there exists a unique element in the range.
- **No repeated inputs**: No input element can be mapped to more than one output element.

## One-to-One Functions

---

A one-to-one function, also known as an injective function, is a plain function that assigns to each element in the domain exactly one element in the range, and no two elements in the domain are assigned to the same element in the range.

### Definition:

A relation R between sets A and B is one-to-one if for every a and b in A, if a ≠ b, then f(a) ≠ f(b).

### Example:

Let A = {1, 2, 3} and B = {a, b, c}. Define a one-to-one function f: A → B as follows:

| a   | b   |
| --- | --- |
| 1   | a   |
| 2   | b   |
| 3   | c   |

In this example, f(1) = a, f(2) = b, and f(3) = c. This function is one-to-one because no two elements in the domain (1 and 2) are assigned to the same element in the range (a and b).

### Properties of One-to-One Functions:

- **Unique output**: For every element in the domain, there exists a unique element in the range.
- **No repeated inputs**: No input element can be mapped to the same output element.
- **Injective**: The function is injective if every element in the range is assigned to at most one element in the domain.

## Key Concepts

---

- **Plain function**: A relation between two sets that assigns to each element in the first set exactly one element in the second set.
- **One-to-one function**: A plain function that assigns to each element in the domain exactly one element in the range, and no two elements in the domain are assigned to the same element in the range.
- **Injective**: A function that is one-to-one.

## Exercises

---

1. Define a plain function f: {1, 2, 3} → {a, b, c} and show that it is one-to-one.
2. Prove that a function is one-to-one if and only if it is injective.
3. Give an example of a one-to-one function between two sets that are not the same size.

## References

---

- [Discrete Mathematical Structures](https://en.wikipedia.org/wiki/Discrete_mathematics)
- [Relations and Functions](<https://en.wikipedia.org/wiki/Function_(mathematics)>)
