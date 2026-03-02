# **Recurrence Relations: First Order Linear Recurrence Relation**

## **Introduction**

Recurrence relations are a fundamental concept in discrete mathematics, used to describe the behavior of sequences and their properties. In this chapter, we will delve into the world of First Order Linear Recurrence Relations, a specific type of recurrence relation that has numerous applications in computer science, mathematics, and other fields.

## **Historical Context**

The concept of recurrence relations dates back to the 19th century, when mathematicians like Joseph-Louis Lagrange and Leonhard Euler studied the properties of sequences and series. However, the modern concept of recurrence relations as we know it today was developed in the mid-20th century by mathematicians like George Polya and Paul Erdős.

## **Definition**

A First Order Linear Recurrence Relation is an equation of the form:

$$a_n = r a_{n-1} + d$$

where:

- $a_n$ is the value of the sequence at position $n$
- $r$ is a constant, called the recurrence relation parameter
- $d$ is a constant, called the initial condition
- $a_{n-1}$ is the value of the sequence at position $n-1$

## **Example**

Consider the sequence $a_n$ defined by the recurrence relation $a_n = 2a_{n-1} + 1$ with initial condition $a_0 = 0$. We can calculate the first few terms of the sequence as follows:

- $a_0 = 0$
- $a_1 = 2a_0 + 1 = 2(0) + 1 = 1$
- $a_2 = 2a_1 + 1 = 2(1) + 1 = 3$
- $a_3 = 2a_2 + 1 = 2(3) + 1 = 7$

## **Case Study**

Consider a population of rabbits living in a forest. Each year, the population grows by a factor of $r$, and each rabbit is born to two parents. If the initial population is $a_0 = 1$, we can model the population size $a_n$ using the recurrence relation $a_n = 2a_{n-1} + 1$.

## **Diagram**

Here is a diagram illustrating the recurrence relation:

```
          +-----------+  (initial condition)
          |  a_0 = 0  |
          +-----------+
                    |
                    |
                    v
+-----------+---------------+  (recurrence relation)
|  a_1 = 2a_0 + 1  |
|  a_2 = 2a_1 + 1  |
|  a_3 = 2a_2 + 1  |
|  ...        |
+-----------+---------------+
```

## **Applications**

Recurrence relations have numerous applications in computer science, mathematics, and other fields, including:

- **Algorithms**: Recurrence relations are used to analyze the time and space complexity of algorithms.
- **Number Theory**: Recurrence relations are used to study the properties of numbers, such as primality and divisibility.
- **Combinatorics**: Recurrence relations are used to study the properties of combinatorial objects, such as permutations and combinations.

## **Solving Recurrence Relations**

To solve a recurrence relation, we can use various techniques, including:

- **Substitution**: We can substitute $a_{n-1}$ with its expression in terms of $a_{n-2}$, and so on.
- **Iteration**: We can iterate the recurrence relation to obtain a closed-form expression for $a_n$.
- **Transformations**: We can use transformations, such as changing the variable or the equation, to simplify the recurrence relation.

## **Example**

Consider the recurrence relation $a_n = 2a_{n-1} + 1$. We can solve it using substitution:

- $a_n = 2a_{n-1} + 1$
- $a_{n-1} = 2a_{n-2} + 1$
- Substituting $a_{n-1}$ into the first equation, we get:
  $a_n = 2(2a_{n-2} + 1) + 1$
- Simplifying, we get:
  $a_n = 4a_{n-2} + 3$
- We can continue this process until we reach the base case:
  $a_n = 2^{n-1}a_0 + (2^{n-1} - 1)$

## **General Solution**

The general solution to a First Order Linear Recurrence Relation is given by:

$$a_n = c r^n + d$$

where:

- $c$ is a constant, determined by the initial condition
- $d$ is a constant, determined by the initial condition
- $r$ is the recurrence relation parameter
- $n$ is the position in the sequence

## **Example**

Consider the recurrence relation $a_n = 2a_{n-1} + 1$ with initial condition $a_0 = 0$. We can find the general solution:

- $a_n = 2^{n-1}(0) + (2^{n-1} - 1)$
- Simplifying, we get:
  $a_n = 2^{n-1} - 1$

## **Conclusion**

In conclusion, First Order Linear Recurrence Relations are a fundamental concept in discrete mathematics, used to describe the behavior of sequences and their properties. We have seen how to define, solve, and apply recurrence relations, and how they have numerous applications in computer science, mathematics, and other fields.

## **Further Reading**

- **"Introduction to Recurrence Relations"** by George Polya
- **"Recurrence Relations and Combinatorial Algorithms"** by Herbert S. Wilf and Doron Zeilberger
- **"Linear Recurrence Relations"** by Gustav E. Klüppelberg and Jan Vereecken

Note: The further reading list is not exhaustive and is intended to provide additional resources for those interested in learning more about recurrence relations.
