# Recurrence Relations: First Order Linear Recurrence Relation

===========================================================

## Overview

---

A recurrence relation is a mathematical equation that defines a sequence of numbers recursively. In this section, we will focus on first-order linear recurrence relations, which are equations of the form:

$$a_n = pa_{n-1} + qa_{n-2}$$

where $a_n$ is the nth term of the sequence, and $p$ and $q$ are constants.

## Key Concepts

---

- **First-order linear recurrence relation**: An equation of the form $a_n = pa_{n-1} + qa_{n-2}$.
- **Linear recurrence relation**: A recurrence relation in which each term is a linear combination of the previous terms.
- **Constant sequence**: A sequence in which each term is equal to a constant.
- **Non-constant sequence**: A sequence in which each term is not equal to a constant.

## Definitions

---

- **Initial condition**: The value of the sequence at a specific term, usually denoted as $a_0$ or $a_1$.
- **Recurrence relation**: A mathematical equation that defines a sequence of numbers recursively.

## Examples

---

### Example 1: Constant Sequence

Suppose we have a recurrence relation of the form $a_n = a_{n-1}$. If we are given the initial condition $a_0 = 2$, then the sequence would be:

$a_0 = 2$
$a_1 = 2$
$a_2 = 2$
...

This is a constant sequence, where each term is equal to 2.

### Example 2: Non-Constant Sequence

Suppose we have a recurrence relation of the form $a_n = 2a_{n-1} + a_{n-2}$. If we are given the initial conditions $a_0 = 1$ and $a_1 = 2$, then the sequence would be:

$a_0 = 1$
$a_1 = 2$
$a_2 = 2(2) + 1 = 5$
$a_3 = 2(5) + 2 = 12$
...

This is a non-constant sequence, where each term is not equal to a constant.

## Solution Methods

---

To solve a first-order linear recurrence relation, we can use the following methods:

- **Characteristic equation method**: This method involves finding the roots of the characteristic equation $r^2 - pr - q = 0$.
- **Closed-form solution method**: This method involves finding a closed-form expression for the sequence, which may involve trigonometric functions or other special functions.

## Key Formulas

---

- **Characteristic equation**: $r^2 - pr - q = 0$
- **Roots of the characteristic equation**: $r_1$ and $r_2$
- **Closed-form expression**: $a_n = A(r_1)^n + B(r_2)^n$

## Conclusion

---

In this section, we have covered the basics of first-order linear recurrence relations, including definitions, examples, and solution methods. We have also introduced key concepts, formulas, and techniques for solving these types of equations. With this knowledge, you should be able to tackle more complex recurrence relations and develop a deeper understanding of discrete mathematical structures.
