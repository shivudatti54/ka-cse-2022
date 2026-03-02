# **Recurrence Relations: First Order Linear Recurrence Relation**

## **Introduction**

Recurrence relations are a fundamental concept in discrete mathematics, used to define sequences of numbers recursively. In this study material, we will focus on first-order linear recurrence relations, which are used to model a wide range of phenomena, such as population growth, chemical reactions, and electrical circuits.

## **Definition**

A first-order linear recurrence relation is a recursive formula of the form:

$f(n) = a f(n-1) + b$

where:

- $f(n)$ is the value of the sequence at time $n$
- $a$ is the recurrence coefficient
- $b$ is the initial condition
- $n$ is a non-negative integer

## **Explanation**

The key idea behind recurrence relations is that each term in the sequence is defined recursively as a function of the previous term. The recurrence relation is used to generate the next term in the sequence, given the previous term.

For example, consider the recurrence relation:

$f(n) = 2 f(n-1) + 1$

To find the value of $f(5)$, we need to know the value of $f(4)$, which in turn requires us to know the value of $f(3)$. We can continue this process until we reach the initial condition $f(0)$.

## **Key Concepts**

- **Recurrence relation**: A recursive formula that defines a sequence of numbers.
- **Recurrence coefficient**: The coefficient of the previous term in the recurrence relation.
- **Initial condition**: The value of the sequence at the starting point.
- **Closed-form solution**: An explicit formula that describes the sequence exactly.
- **Partial solution**: A formula that describes the sequence exactly for a specific range of values.

## **Examples**

### Example 1: Fibonacci Sequence

The Fibonacci sequence is a classic example of a first-order linear recurrence relation:

$f(n) = f(n-1) + f(n-2)$

with initial conditions $f(0) = 0$ and $f(1) = 1$. The closed-form solution to this recurrence relation is the Fibonacci sequence itself.

### Example 2: Population Growth

Consider a population of rabbits that grows according to the recurrence relation:

$f(n) = 2 f(n-1) + 1$

with initial condition $f(0) = 1$. This recurrence relation models population growth, where the population at time $n$ is twice the population at time $n-1$, plus one new rabbit.

## **Solving Recurrence Relations**

There are several methods to solve recurrence relations, including:

- **Iterative method**: By iteratively applying the recurrence relation, we can compute the value of the sequence at any given time.
- **Closed-form solution**: By solving the recurrence relation analytically, we can obtain an explicit formula that describes the sequence exactly.
- **Partial solution**: By solving the recurrence relation for a specific range of values, we can obtain a formula that describes the sequence exactly for that range.

## **Conclusion**

Recurrence relations are a powerful tool in discrete mathematics, used to model a wide range of phenomena. By understanding the basics of first-order linear recurrence relations, we can solve a variety of problems, from simple population growth models to more complex systems.
