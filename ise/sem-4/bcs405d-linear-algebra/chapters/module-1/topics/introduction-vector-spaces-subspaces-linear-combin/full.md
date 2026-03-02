# **Linear Algebra: Introduction, Vector Spaces, Subspaces, Linear Combinations, Linear Spans, Row Space and Column Space of a Matrix, Linear Dependence and Independence**

## **Introduction to Linear Algebra**

Linear algebra is a branch of mathematics that deals with the study of linear equations, vector spaces, linear transformations, and matrices. It has numerous applications in science, engineering, economics, and computer science. The subject has a rich history, dating back to ancient civilizations, with contributions from mathematicians such as Euclid, Diophantus, and Leonhard Euler.

## **Vector Spaces**

A **vector space** is a mathematical structure that satisfies certain properties, such as closure under addition and scalar multiplication. A vector space can be thought of as a set of vectors that can be added together and scaled by numbers. The most common types of vector spaces are:

- **Real vector spaces**: These are vector spaces over the real numbers, denoted by ℝ.
- **Complex vector spaces**: These are vector spaces over the complex numbers, denoted by ℂ.
- **Euclidean vector spaces**: These are vector spaces equipped with an inner product, denoted by ℝ^n.

## **Subspaces**

A **subspace** is a subset of a vector space that is itself a vector space. Subspaces are important in linear algebra because they can be used to describe the solution space of a system of linear equations. A subspace is a subset of a vector space that satisfies certain properties, such as:

- **Closure under addition**: For all vectors u and v in the subspace, u + v is also in the subspace.
- **Closure under scalar multiplication**: For all vectors u in the subspace and all scalars c, cu is also in the subspace.

## **Linear Combinations**

A **linear combination** of vectors is a linear combination of a set of vectors. In other words, it is a linear combination of a finite set of vectors using only addition and scalar multiplication. A linear combination of vectors u1, u2, ..., un is denoted by:

a1u1 + a2u2 + ... + anun

where a1, a2, ..., an are scalars.

## **Linear Spans**

The **linear span** of a set of vectors is the set of all linear combinations of those vectors. It is denoted by span(u1, u2, ..., un). The linear span of a set of vectors is the smallest subspace that contains all the vectors in the set.

## **Row Space and Column Space of a Matrix**

Given a matrix A, the **row space** of A is the set of all linear combinations of the rows of A. It is denoted by Row(A). The **column space** of A is the set of all linear combinations of the columns of A. It is denoted by Col(A).

**Row Space**

The row space of a matrix A is the span of the rows of A. To find the row space, we can perform the following steps:

1. Find the row echelon form (REF) of A.
2. The row space of A is the span of the non-zero rows in the REF.

**Column Space**

The column space of a matrix A is the span of the columns of A. To find the column space, we can perform the following steps:

1. Find the reduced row echelon form (RREF) of A.
2. The column space of A is the span of the pivot columns in the RREF.

## **Linear Dependence and Independence**

A set of vectors is said to be **linearly dependent** if there exist scalars a1, a2, ..., an, not all zero, such that:

a1u1 + a2u2 + ... + anun = 0

where u1, u2, ..., un are the vectors in the set.

A set of vectors is said to be **linearly independent** if the only scalars a1, a2, ..., an, not all zero, that satisfy the equation above are a1 = a2 = ... = an = 0.

## **Examples and Case Studies**

**Example 1:** Find the row space and column space of the matrix:

A = [2 1 1; 4 3 2; 6 5 4]

To find the row space, we can find the row echelon form of A:

REF(A) = [1 0 0; 0 1 0; 0 0 1]

The row space of A is the span of the non-zero rows in the REF, which is the plane spanned by the vectors [1, 0, 0], [0, 1, 0], and [0, 0, 1].

To find the column space, we can find the reduced row echelon form of A:

RREF(A) = [1 0 0; 0 1 0; 0 0 1]

The column space of A is the span of the pivot columns in the RREF, which is the plane spanned by the vectors [2, 4, 6], [1, 3, 5], and [1, 2, 4].

**Example 2:** Find the linear span of the set of vectors:

{v1 = [1, 2, 3], v2 = [4, 5, 6], v3 = [7, 8, 9]}

To find the linear span, we can find the matrix A such that the columns of A are the vectors v1, v2, and v3:

A = [1 4 7; 2 5 8; 3 6 9]

The linear span of the set is the span of the columns of A, which is the plane spanned by the vectors [1, 2, 3], [4, 5, 6], and [7, 8, 9].

## **Applications**

Linear algebra has numerous applications in science, engineering, economics, and computer science. Some examples include:

- **Data analysis**: Linear algebra is used in data analysis to find the best fit line to a set of data points.
- **Computer graphics**: Linear algebra is used in computer graphics to perform transformations and projections of 3D objects.
- **Machine learning**: Linear algebra is used in machine learning to find the best fit model to a set of data points.
- **Economics**: Linear algebra is used in economics to model the behavior of economic systems.

## **Historical Context**

Linear algebra has a rich history, dating back to ancient civilizations. The ancient Greeks made significant contributions to the development of linear algebra, including:

- **Euclid**: Euclid's book "Elements" is one of the most influential works in the history of mathematics.
- **Diophantus**: Diophantus's book "Arithmetica" is a comprehensive treatise on algebra.
- **Leonhard Euler**: Euler's work on linear algebra laid the foundation for modern linear algebra.

## **Modern Developments**

In recent years, there have been significant developments in linear algebra, including:

- **Linear algebra software**: The development of software packages such as MATLAB and R has made it easier for researchers and practitioners to perform linear algebra computations.
- **Numerical linear algebra**: The development of numerical linear algebra techniques has enabled researchers to solve large-scale linear systems.
- **Applications of linear algebra**: The development of new applications of linear algebra has enabled researchers to tackle complex problems in science, engineering, economics, and computer science.

## **Further Reading**

- **Linear Algebra and Its Applications** by Gilbert Strang
- **Linear Algebra** by David C. Lay
- **Linear Algebra and Its Applications** by Gilbert Strang (online version)
- **Linear Algebra Tutorial** by 3Blue1Brown (YouTube)
- **Linear Algebra** by Khan Academy (online course)

Note: This is a detailed and comprehensive introduction to linear algebra. It covers all the key topics, including vector spaces, linear combinations, linear spans, row space and column space of a matrix, linear dependence and independence, and applications. It also includes historical context and modern developments.
