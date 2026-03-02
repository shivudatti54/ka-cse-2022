# **The Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients**

## **Introduction**

A recurrence relation is a mathematical relationship between the terms of a sequence. In this study, we will focus on the second order linear homogeneous recurrence relation with constant coefficients. This type of recurrence relation is commonly encountered in mathematics, computer science, and physics.

## **Definition**

A second order linear homogeneous recurrence relation with constant coefficients is defined as:

an = a(n-1) + a(n-2)

where a(n) is the nth term of the sequence, and a(n-1) and a(n-2) are the previous two terms.

## **Key Concepts**

- **Homogeneous**: The recurrence relation does not contain any non-homogeneous terms.
- **Linear**: The recurrence relation can be written in the form of a linear equation.
- **Recurrence relation with constant coefficients**: The coefficients of the recurrence relation are constant.

## **Solving Methods**

There are several methods to solve second order linear homogeneous recurrence relations with constant coefficients:

### 1. **Characteristic Equation Method**

The characteristic equation is obtained by substituting a(n) = r^n into the recurrence relation.

an = a(n-1) + a(n-2)
r^n = r^(n-1) + r^(n-2)

Simplifying the equation, we get:

r^2 = r + 1

This is a quadratic equation, which can be factored as:

(r - 1)(r + 1) = 0

Solving for r, we get:

r = 1 or r = -1

The general solution to the recurrence relation is:

a(n) = c1 \* 1^n + c2 \* (-1)^n

where c1 and c2 are arbitrary constants.

### 2. **Gauss's Method**

Gauss's method is a technique used to solve recurrence relations. The idea is to express the recurrence relation in terms of a matrix equation.

Let A be a 2x2 matrix, and define a column vector b as:

b = (1, 1)

The recurrence relation can be written as:

a(n) = A \* a(n-1) + b

To solve the recurrence relation, we need to find the inverse of matrix A.

The inverse of A can be found using the formula:

A^(-1) = 1 / (ad - bc)

where a, b, c, and d are the elements of matrix A.

Once we have the inverse of A, we can multiply both sides of the recurrence relation by A^(-1) to get:

a(n-1) = A^(-1) \* b

Substituting the values of A and b, we can solve for the initial conditions.

### 3. **Iterative Method**

The iterative method is a straightforward approach to solve recurrence relations. We can start with the initial conditions and iteratively apply the recurrence relation to find the solution.

Let's consider an example to illustrate the iterative method.

## **Example**

Suppose we have the recurrence relation:

a(n) = 2a(n-1) - a(n-2)

We can start by finding the initial conditions. Let's assume that a(1) = 1 and a(2) = 2.

We can iteratively apply the recurrence relation to find the solution:

a(3) = 2a(2) - a(1) = 2 \* 2 - 1 = 3

a(4) = 2a(3) - a(2) = 2 \* 3 - 2 = 4

a(5) = 2a(4) - a(3) = 2 \* 4 - 3 = 5

The solution to the recurrence relation is:

a(n) = 2^n - 1

## **Conclusion**

In conclusion, the second order linear homogeneous recurrence relation with constant coefficients is a fundamental concept in discrete mathematical structures. We have discussed the characteristic equation method, Gauss's method, and the iterative method for solving such recurrence relations. These methods are useful for solving a wide range of mathematical and computational problems.
