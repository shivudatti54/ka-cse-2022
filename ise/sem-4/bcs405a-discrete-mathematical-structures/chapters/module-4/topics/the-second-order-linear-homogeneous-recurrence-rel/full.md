# **The Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients**

## **Introduction**

A recurrence relation is a mathematical equation that defines a sequence of numbers recursively. In this section, we will explore the second order linear homogeneous recurrence relation with constant coefficients, a fundamental concept in discrete mathematics.

## **Definition**

A second order linear homogeneous recurrence relation with constant coefficients is a recurrence relation of the form:

$$a_n = r_1a_{n-1} + r_2a_{n-2}$$

where $a_n$ is the value of the sequence at the $n^{th}$ term, and $r_1$ and $r_2$ are constant coefficients.

## **Historical Context**

The study of recurrence relations dates back to ancient civilizations, with examples found in the works of Euclid and Fibonacci. However, the modern study of recurrence relations began in the 19th century with the work of mathematicians such as Leonhard Euler and Augustin-Louis Cauchy.

## **Mathematical Analysis**

To solve a second order linear homogeneous recurrence relation, we can use the following techniques:

1. **Characteristic Equations**: The characteristic equation is obtained by substituting $a_n = r^n$ into the recurrence relation. This yields the equation:

$$(r^2 - r_1r - r_2) = 0$$

Solving this equation gives us the roots $r_1$ and $r_2$, which can be used to find the general solution of the recurrence relation.

2. **Homogeneous Solutions**: If the characteristic equation has distinct roots, the homogeneous solution is given by:

$$a_n = A(r_1)^n + B(r_2)^n$$

where $A$ and $B$ are arbitrary constants.

3. **Particular Solutions**: If the characteristic equation has repeated roots, the homogeneous solution is given by:

$$a_n = (An + B)r^n$$

where $A$ and $B$ are arbitrary constants.

4. **General Solution**: The general solution of the recurrence relation is the sum of the homogeneous and particular solutions.

## **Examples**

### Example 1: Simplest Case

Consider the recurrence relation:

$$a_n = 2a_{n-1}$$

The characteristic equation is:

$$(r - 2) = 0$$

Solving this equation gives us the root $r = 2$. The homogeneous solution is:

$$a_n = A(2)^n$$

where $A$ is an arbitrary constant. Since the characteristic equation has a single root, the particular solution is zero.

The general solution is:

$$a_n = A(2)^n$$

### Example 2: Repeated Roots

Consider the recurrence relation:

$$a_n = 3a_{n-1} + a_{n-2}$$

The characteristic equation is:

$$(r^2 - 3r) = 0$$

Solving this equation gives us the repeated root $r = 3$. The homogeneous solution is:

$$a_n = (An + B)3^n$$

where $A$ and $B$ are arbitrary constants. The particular solution is:

$$a_n = (n + 1)3^n$$

The general solution is:

$$a_n = (An + B)3^n + (n + 1)3^n$$

### Example 3: Non-Constant Coefficients

Consider the recurrence relation:

$$a_n = 2na_{n-1}$$

This recurrence relation has non-constant coefficients, making it more challenging to solve. However, we can still use the characteristic equation method to find the solution.

The characteristic equation is:

$$(r^2 - 2r) = 0$$

Solving this equation gives us the roots $r = 0$ and $r = 2$. The homogeneous solution is:

$$a_n = A(2)^n$$

where $A$ is an arbitrary constant. Since the characteristic equation has repeated roots, the particular solution is:

$$a_n = (n^2 + n)2^n$$

The general solution is:

$$a_n = A(2)^n + (n^2 + n)2^n$$

## **Applications**

Recurrence relations have numerous applications in mathematics, computer science, and other fields. Some examples include:

1. **Random Walks**: Recurrence relations can be used to model random walks, which are essential in probability theory.
2. **Cryptography**: Recurrence relations can be used to design cryptographic algorithms, such as the Advanced Encryption Standard (AES).
3. **Computer Networks**: Recurrence relations can be used to model the behavior of computer networks, such as the Internet.
4. **Biology**: Recurrence relations can be used to model the growth of populations, such as the growth of bacteria.

## **Case Studies**

### Case Study 1: Fibonacci Sequence

The Fibonacci sequence is a classic example of a recurrence relation:

$$F_n = F_{n-1} + F_{n-2}$$

where $F_n$ is the $n^{th}$ term of the sequence. The characteristic equation is:

$$(r^2 - r - 1) = 0$$

Solving this equation gives us the roots $r = \frac{1 \pm \sqrt{5}}{2}$. The homogeneous solution is:

$$F_n = A\left(\frac{1 + \sqrt{5}}{2}\right)^n + B\left(\frac{1 - \sqrt{5}}{2}\right)^n$$

where $A$ and $B$ are arbitrary constants.

### Case Study 2: Pascal's Triangle

Pascal's triangle is a well-known example of a recurrence relation:

$$P_{n,k} = P_{n-1,k-1} + P_{n-1,k}$$

where $P_{n,k}$ is the $k^{th}$ term of the $n^{th}$ row of the triangle. The characteristic equation is:

$$(r^2 - 2r + 1) = 0$$

Solving this equation gives us the repeated root $r = 1$. The homogeneous solution is:

$$P_{n,k} = (An + B)1^n$$

where $A$ and $B$ are arbitrary constants. The particular solution is:

$$P_{n,k} = \frac{n!}{(n-k)!k!}$$

The general solution is:

$$P_{n,k} = (An + B)1^n + \frac{n!}{(n-k)!k!}$$

## **Further Reading**

For more information on recurrence relations, we recommend the following resources:

1. **"Recurrence Relations and Sequences"** by James Greenhill: This book provides a comprehensive introduction to recurrence relations and sequences.
2. **"The Art of Computer Programming"** by Donald Knuth: This book covers the theory of computer programming, including recurrence relations.
3. **"Discrete Mathematical Structures"** by Kenneth H. Rosen: This book covers discrete mathematical structures, including recurrence relations.
4. **"Recurrence Relations"** by J. H. van Lint: This book provides a comprehensive introduction to recurrence relations and their applications.

We hope this detailed guide has provided a thorough understanding of the second order linear homogeneous recurrence relation with constant coefficients.
