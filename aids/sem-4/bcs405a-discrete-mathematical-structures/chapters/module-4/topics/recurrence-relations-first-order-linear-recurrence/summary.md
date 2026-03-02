# Recurrence Relations: First Order Linear Recurrence Relation

## Definition and Notation

- A recurrence relation is a relationship between a sequence of numbers, where each term is defined recursively as a function of previous terms.
- First order linear recurrence relation: `a_n = r*a_(n-1) + c*n`, where `a_n` is the nth term, `r` is the ratio, and `c` is the constant.

## Important Formulas

- **Homogeneous recurrence relation**: `a_n = r*a_(n-1)`
- **Non-homogeneous recurrence relation**: `a_n = r*a_(n-1) + c*n`
- **Characteristic equation**: `x - r = 0`

## Theorems

- **Unique solution theorem**: If a recurrence relation has a unique solution, then it has a unique solution modulo some modulus.
- **Fibonacci sequence theorem**: The Fibonacci sequence is a solution to the homogeneous recurrence relation `a_n = a_(n-1) + a_(n-2)`.

## Important Definitions

- **Base case**: A starting condition for the recurrence relation.
- **Recurrence relation matrix**: A matrix representation of the recurrence relation.
- **Period**: The length of the cycle in a periodic sequence.

## Important Concepts

- **Linearity**: The ability to combine solutions of simple recurrence relations to obtain a solution of a more complex recurrence relation.
- **Periodicity**: A recurrence relation that produces a repeating sequence.
- **Convergence**: A sequence that approaches a finite limit as n approaches infinity.

## Important Theorems and Results

- **Existence and uniqueness of solutions**: Every linear recurrence relation has a unique solution modulo some modulus.
- **Periodicity of solutions**: If a recurrence relation has a periodic solution, then it has a finite period.
