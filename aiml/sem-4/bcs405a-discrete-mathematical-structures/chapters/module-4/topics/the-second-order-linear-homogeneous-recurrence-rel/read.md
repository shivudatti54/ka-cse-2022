# **The Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients**

## **Introduction**

A second order linear homogeneous recurrence relation with constant coefficients is a fundamental concept in discrete mathematics. It is a relationship between two consecutive terms in a sequence, defined using constant coefficients. In this study material, we will explore the definition, characteristics, and solution methods for such recurrence relations.

## **Definition**

A second order linear homogeneous recurrence relation with constant coefficients is defined as:

an+1 = bnan

where:

- an+1 is the (n+1)th term in the sequence
- an is the nth term in the sequence
- b1 and b2 are constant coefficients
- n is a non-negative integer

## **Characteristics**

The following are the key characteristics of a second order linear homogeneous recurrence relation with constant coefficients:

- **Homogeneous**: The recurrence relation is homogeneous, meaning that it does not involve any non-homogeneous terms.
- **Linear**: The recurrence relation is linear, meaning that it involves only linear combinations of the previous terms.
- **Constant coefficients**: The coefficients of the recurrence relation are constant, meaning that they do not change with the index of the terms.

## **Examples**

- Example 1: Fibbonacci sequence
  - an+1 = an-1 + an
  - a0 = 0, a1 = 1
  - Example 2: Square numbers
  - an+1 = an
  - a0 = 1, a1 = 1
- Example 3: Tribonacci sequence
  - an+1 = an-1 + an + an-2
  - a0 = 0, a1 = 1, a2 = 1

## **Solution Methods**

There are two main methods to solve a second order linear homogeneous recurrence relation with constant coefficients:

### 1. **Characteristic Equation Method**

The characteristic equation method involves finding the roots of the characteristic equation, which is obtained by substituting x into the recurrence relation.

- **Characteristic Equation**: ax^2 + bx + c = 0
- **Roots**: x1, x2

The general solution of the recurrence relation is given by:

an = A1x^(n-1) + A2x^(n-2)

where A1 and A2 are arbitrary constants.

### 2. **Guess and Check Method**

The guess and check method involves making an educated guess about the form of the solution and then checking it using the recurrence relation.

- **Guess**: an = An^n + Bn
- **Checking**: Substitute the guess into the recurrence relation and simplify.

## **Key Concepts**

- **Characteristic Equation**: A quadratic equation obtained by substituting x into the recurrence relation.
- **Roots**: The solutions of the characteristic equation.
- **General Solution**: A solution of the recurrence relation that satisfies the recurrence relation for all n.
- **Arbitrary Constants**: Constants that appear in the general solution.

## **Practice Problems**

1.  Solve the recurrence relation: an+1 = 2an
2.  Solve the recurrence relation: an+1 = an - 2a(n-1)
3.  Solve the recurrence relation: an+1 = 3an - 2a(n-1)

## **Conclusion**

In conclusion, the second order linear homogeneous recurrence relation with constant coefficients is a fundamental concept in discrete mathematics. The characteristic equation method and the guess and check method are two main methods to solve such recurrence relations. By understanding the definition, characteristics, and solution methods, you can solve a wide range of recurrence relations.
