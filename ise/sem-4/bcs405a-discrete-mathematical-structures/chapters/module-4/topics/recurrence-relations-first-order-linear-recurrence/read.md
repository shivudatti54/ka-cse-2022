# Recurrence Relations: First Order Linear Recurrence Relation

===========================================================

## Table of Contents

---

- [Definition and Explanation](#definition-and-explanation)
- [Types of First Order Linear Recurrence Relations](#types-of-first-order-linear-recurrence-relations)
- [Euler's Method](#eulers-method)
- [Solving First Order Linear Recurrence Relations](#solving-first-order-linear-recurrence-relations)
- [Example Problems](#example-problems)

## Definition and Explanation

---

A **first order linear recurrence relation** is an equation of the form:

F(n) = a \* F(n-1) + b \* F(n-2) + ... + c \* F(n-k)

where F(n) is the value of the function at n, a, b, ..., c, and k are constants, and n is a positive integer.

The given recurrence relation is said to be **linear** because it involves only addition and multiplication of the function values, and not any higher-order operations such as exponentiation or root extraction.

## Types of First Order Linear Recurrence Relations

---

There are two types of first order linear recurrence relations:

- **Homogeneous recurrence relations**: F(n) = a \* F(n-1) + b \* F(n-2)
- **Non-homogeneous recurrence relations**: F(n) = a \* F(n-1) + b \* F(n-2) + c

## Euler's Method

---

Euler's method is a technique used to solve non-homogeneous first order linear recurrence relations.

### General Solution

The general solution of a non-homogeneous recurrence relation is given by:

F(n) = r1 \* F(n-1) + r2 \* F(n-2) + ... + rk

where r1, r2, ..., rk are constants.

### Particular Solution

A particular solution of a non-homogeneous recurrence relation is given by:

Fp(n) = A \* n + B

where A and B are constants.

### General Solution of Non-Homogeneous Recurrence Relation

The general solution of a non-homogeneous recurrence relation is given by:

F(n) = Fh(n) + Fp(n)

where Fh(n) is the homogeneous solution and Fp(n) is the particular solution.

## Solving First Order Linear Recurrence Relations

---

To solve a first order linear recurrence relation, we need to find the homogeneous and particular solutions of the equation.

### Example

Solve the recurrence relation:

F(n) = 2 \* F(n-1) + 1

### Homogeneous Solution

The homogeneous solution of the equation is:

Fh(n) = C \* 2^n

where C is a constant.

### Particular Solution

The particular solution of the equation is:

Fp(n) = A \* n + B

Substituting Fp(n) in the recurrence relation, we get:

A \* n + B = 2 \* (A \* (n-1) + B) + 1

Simplifying the equation, we get:

A \* n + B = 2 \* A \* n - 2 \* A + 2 \* B + 1

Comparing the coefficients of n and constant terms, we get:

A = 2 \* A - 2 \* A + 1
B = -2 \* A + 2 \* B + 1

Solving the equations, we get:

A = 1/3
B = -1/3

### General Solution

The general solution of the equation is:

F(n) = Fh(n) + Fp(n)
= (1/3) \* 2^n + (1/3) \* n - (1/3)

## Example Problems

---

1.  Solve the recurrence relation:

F(n) = 3 \* F(n-1) - 2 \* F(n-2)

Solution:
Fh(n) = C \* 3^n
Fp(n) = A \* n + B
Substituting Fp(n) in the recurrence relation, we get:
A \* n + B = 3 \* (A \* (n-1) + B) - 2 \* A
Simplifying the equation, we get:
A \* n + B = 3 \* A \* n - 3 \* A + 3 \* B - 2 \* A
Comparing the coefficients of n and constant terms, we get:
A = 3 \* A - 3 \* A + 3 \* B - 2 \* A
B = -3 \* A + 3 \* B - 2 \* A
Solving the equations, we get:
A = 1
B = -1
F(n) = (1/3) \* 3^n - (1/3) \* n + 1

2.  Solve the recurrence relation:

F(n) = 2 \* F(n-1) - F(n-2)

Solution:
Fh(n) = C \* 2^n
Fp(n) = A \* n + B
Substituting Fp(n) in the recurrence relation, we get:
A \* n + B = 2 \* (A \* (n-1) + B) - A \* (n-2)
Simplifying the equation, we get:
A \* n + B = 2 \* A \* n - 2 \* A - 2 \* B - A \* (n-2)
Comparing the coefficients of n and constant terms, we get:
A = 2 \* A - 2 \* A - 2 \* B - A
B = - 2 \* A - 2 \* B - A
Solving the equations, we get:
A = 2
B = -2
