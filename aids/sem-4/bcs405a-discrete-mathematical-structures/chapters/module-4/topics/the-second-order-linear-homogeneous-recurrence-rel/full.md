# **The Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients**

## **Introduction**

A recurrence relation is a mathematical concept used to define a sequence of numbers recursively. In this chapter, we will delve into the world of second-order linear homogeneous recurrence relations with constant coefficients. These relations are fundamental in discrete mathematics and have numerous applications in computer science, physics, and other fields.

## **Historical Context**

The study of recurrence relations dates back to the early 20th century. One of the pioneers in this field was the mathematician and computer scientist, Alan Turing. In his 1937 paper, "On Computable Numbers," Turing introduced the concept of a recurrence relation to model simple programs on a hypothetical machine.

## **Definition**

A second-order linear homogeneous recurrence relation with constant coefficients is a relation of the form:

$$a_n = p a_{n-1} + q a_{n-2}$$

where:

- $a_n$ is the nth term of the sequence
- $p$ and $q$ are constant coefficients
- $a_{n-1}$ and $a_{n-2}$ are the previous two terms of the sequence

## **Solving Methods**

There are several methods to solve second-order linear homogeneous recurrence relations with constant coefficients. We will discuss three common methods:

### 1. Characteristic Equation Method

The characteristic equation method involves finding the roots of the characteristic equation:

$$x^2 - px - q = 0$$

The roots of the characteristic equation determine the general solution of the recurrence relation.

### 2. Generating Function Method

The generating function method involves finding a generating function for the sequence and then manipulating it to obtain the solution.

### 3. Iterative Method

The iterative method involves iterating the recurrence relation to obtain the solution.

## **Characteristic Equation Method**

The characteristic equation method is a popular method for solving second-order linear homogeneous recurrence relations with constant coefficients. The steps involved are:

1. Write down the characteristic equation.
2. Find the roots of the characteristic equation.
3. Write down the general solution using the roots.

Let's consider an example:

**Example 1**

Solve the recurrence relation:

$$a_n = 2 a_{n-1} - 3 a_{n-2}$$

**Step 1:** Write down the characteristic equation:

$$x^2 - 2x + 3 = 0$$

**Step 2:** Find the roots of the characteristic equation:

$$x_1 = 3$$
$$x_2 = 1$$

**Step 3:** Write down the general solution:

$$a_n = c_1 (3)^n + c_2 (1)^n$$

## **Iterative Method**

The iterative method involves iterating the recurrence relation to obtain the solution. The steps involved are:

1. Start with the initial conditions.
2. Iterate the recurrence relation to obtain the next term.
3. Repeat step 2 until we reach the desired term.

Let's consider an example:

**Example 2**

Solve the recurrence relation:

$$a_n = a_{n-1} + 2 a_{n-2}$$

**Initial conditions:** $a_0 = 0$, $a_1 = 1$

**Iteration:** $a_2 = a_1 + 2 a_0 = 1 + 2 (0) = 1$
$a_3 = a_2 + 2 a_1 = 1 + 2 (1) = 3$
$a_4 = a_3 + 2 a_2 = 3 + 2 (1) = 5$

**General solution:** $a_n = F (2n + 1)$

## **Generating Function Method**

The generating function method involves finding a generating function for the sequence and then manipulating it to obtain the solution.

**Definition:** The generating function for a sequence $a_n$ is a function $f(x)$ defined as:

$$f(x) = \sum_{n=0}^{\infty} a_n x^n$$

Let's consider an example:

**Example 3**

Solve the recurrence relation:

$$a_n = 2 a_{n-1} - 3 a_{n-2}$$

**Generating function:** $f(x) = \sum_{n=0}^{\infty} a_n x^n$

**Manipulation:** $f(x) = a_0 + a_1 x + \sum_{n=2}^{\infty} (2 a_{n-1} - 3 a_{n-2}) x^n$

$$f(x) = a_0 + a_1 x + 2 x f(x) - 3 x^2 f(x)$$

**Solving for f(x):**

$$f(x) (1 - 2x + 3x^2) = a_0 + (a_1 - 2 a_0) x$$

$$f(x) = \frac{a_0 + (a_1 - 2 a_0) x}{1 - 2x + 3x^2}$$

## **Case Studies**

**Example 4**

Solve the recurrence relation:

$$a_n = a_{n-1} + 2 a_{n-2}$$

**Initial conditions:** $a_0 = 0$, $a_1 = 1$

**Solution:** $a_n = F (2n + 1)$

**Example 5**

Solve the recurrence relation:

$$a_n = 2 a_{n-1} - 3 a_{n-2}$$

**Initial conditions:** $a_0 = 1$, $a_1 = 1$

**Solution:** $a_n = c_1 (3)^n + c_2 (1)^n$

## **Applications**

**Example 6**

The Fibonacci sequence is a classic example of a second-order linear homogeneous recurrence relation with constant coefficients. The Fibonacci sequence is defined as:

$$F_n = F_{n-1} + F_{n-2}$$

**Applications:** The Fibonacci sequence appears in many areas of mathematics and science, including finance, biology, and computer science.

## **Conclusion**

In this chapter, we have explored the world of second-order linear homogeneous recurrence relations with constant coefficients. We have discussed three common methods for solving these relations: the characteristic equation method, the generating function method, and the iterative method. We have also provided several examples and case studies to illustrate the use of these methods.

## **Further Reading**

- "The Fibonacci Sequence" by Donald J. Hardy
- "Recurrence Relations" by George Pólya
- "Generating Functions" by Richard P. Stanley
- "The Theory of Recurrence Relations" by Hans Lewiner
