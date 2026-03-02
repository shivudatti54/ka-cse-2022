# Polynomials

## Overview

Polynomials are mathematical expressions represented in C using arrays or linked lists. The coefficient array is simple but wasteful for sparse polynomials, while the term-based array and linked list representations are more efficient.

## Key Points

- Coefficient array: simple, but wastes memory for sparse polynomials.
- Term-based array: stores only non-zero terms as (coefficient, exponent) pairs.
- Linked list representation: dynamically allocates memory for each term, efficient for sparse polynomials.
- Polynomial addition: uses a two-pointer merge-like technique in all representations.
- Polynomial multiplication: requires multiplying every term pair and combining like terms.

## Important Definitions

- **Polynomial**: a mathematical expression of the form P(x) = a*n \* x^n + a*(n-1) _ x^(n-1) + ... + a_1 _ x^1 + a_0 \* x^0.
- **Coefficient array**: an array where the index represents the exponent and the value at that index represents the coefficient.
- **Term-based array**: an array storing only non-zero terms as (coefficient, exponent) pairs.
- **Linked list representation**: a linked list where each node stores one term of the polynomial.

## Key Formulas / Syntax

- `struct PolyNode { int coeff; int expo; struct PolyNode *next; };`
- `PolyPtr createNode(int coeff, int expo) { ... }`
- `void insertTerm(PolyPtr *head, int coeff, int expo) { ... }`

## Comparisons

| Feature                | Coefficient Array    | Term Array (pairs)   | Linked List            |
| ---------------------- | -------------------- | -------------------- | ---------------------- |
| Memory for degree n    | O(n+1) always        | O(t) where t = terms | O(t) where t = terms   |
| Sparse poly efficiency | Poor (wastes memory) | Good                 | Good                   |
| Dense poly efficiency  | Good                 | Good                 | Slightly more overhead |

## Exam Tips

- Practice drawing array and linked list representations for a given polynomial.
- Memorize the polynomial addition algorithm using the two-pointer technique.
- Always write the complete `struct PolyNode` with `coeff`, `expo`, and `next`.
- Explain the benefits of linked list representation for sparse polynomials.
- Practice writing a complete C program for polynomial addition using linked lists.
