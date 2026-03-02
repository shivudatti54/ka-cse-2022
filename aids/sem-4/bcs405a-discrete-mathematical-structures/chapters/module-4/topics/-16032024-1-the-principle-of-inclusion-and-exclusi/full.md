# Discrete Mathematical Structures

## Module: The Principle of Inclusion and Exclusion

### Table of Contents

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [The Principle of Inclusion and Exclusion](#the-principle-of-inclusion-and-exclusion)
   - [Statement of the Principle](#statement-of-the-principle)
   - [Proof of the Principle](#proof-of-the-principle)
   - [Applications of the Principle](#applications-of-the-principle)
4. [Generalizations of the Principle](#generalizations-of-the-principle)
   - [Union of More Than Two Sets](#union-of-more-than-two-sets)
   - [Intersection of More Than Two Sets](#intersection-of-more-than-two-sets)
   - [Multiple Set Union and Intersection](#multiple-set-union-and-intersection)
5. [Derangements – Nothing is in its Right Place](#derangements-nothing-is-in-its-right-place)
6. [Rook Polynomials](#rook-polynomials)

### Introduction

---

The Principle of Inclusion and Exclusion (PIE) is a fundamental concept in combinatorics, which provides a powerful tool for counting the number of elements in the union of multiple sets. This principle has far-reaching applications in various fields, including computer science, mathematics, and statistics.

### Historical Context

---

The concept of PIE has its roots in the 19th century, when mathematicians such as Augustus De Morgan and William Rowan Hamilton first discovered its significance. However, it wasn't until the 20th century that the principle gained widespread acceptance and was applied to a wide range of problems.

### The Principle of Inclusion and Exclusion

---

### Statement of the Principle

Given a finite number of sets A_1, A_2, ..., A_n, the Principle of Inclusion and Exclusion states that:

|A_1 ∪ A_2 ∪ ... ∪ A_n| = ∑|A_i| - ∑|A_i ∩ A_j| + ∑|A_i ∩ A_j ∩ A_k| - ... + (-1)^n|A_1 ∩ A_2 ∩ ... ∩ A_n|

where |A_i| denotes the number of elements in set A_i, |A_i ∩ A_j| denotes the number of elements in the intersection of sets A_i and A_j, and so on.

### Proof of the Principle

The proof of PIE involves a simple induction argument. We start with the base case, where n = 1, in which case the principle holds trivially.

Assume that the principle holds for n = k, i.e.,

|A_1 ∪ A_2 ∪ ... ∪ A_k| = ∑|A_i| - ∑|A_i ∩ A_j| + ... + (-1)^k|A_1 ∩ A_2 ∩ ... ∩ A_k|

Now, consider the case where n = k + 1. We can apply the principle to the sets A*1, A_2, ..., A_k, ∪ (A*(k+1) \ A*1) ∪ ... ∪ (A*(k+1) \ A*k), where (A*(k+1) \ A*i) denotes the set difference of A*(k+1) and A_i.

Using the distributive property of set operations, we can rewrite the union as:

|A*1 ∪ A_2 ∪ ... ∪ A_k ∪ A*(k+1)| = |A*1 ∪ A_2 ∪ ... ∪ A_k| + |A*(k+1) \ A*1| + ... + |A*(k+1) \ A_k|

Substituting the expression for |A_1 ∪ A_2 ∪ ... ∪ A_k| from the inductive hypothesis, we get:

|A*1 ∪ A_2 ∪ ... ∪ A_k ∪ A*(k+1)| = (∑|A*i| - ∑|A_i ∩ A_j| + ... + (-1)^k|A_1 ∩ A_2 ∩ ... ∩ A_k|) + ∑|A*(k+1) \ A_i|

Simplifying the expression, we get:

|A*1 ∪ A_2 ∪ ... ∪ A_k ∪ A*(k+1)| = ∑|A*i| - ∑|A_i ∩ A_j| + ... + (-1)^(k+1)|A_1 ∩ A_2 ∩ ... ∩ A_k ∪ A*(k+1)|

This completes the inductive step, and we have established that the principle holds for n = k + 1.

### Applications of the Principle

The Principle of Inclusion and Exclusion has numerous applications in various fields:

- **Computer Science:** PIE is used in algorithms for counting the number of elements in the union of multiple sets, such as in the context of database query optimization.
- **Mathematics:** PIE is used in combinatorial problems, such as counting the number of perfect matchings in a graph.
- **Statistics:** PIE is used in hypothesis testing, such as in the context of testing for independence between multiple variables.

### Generalizations of the Principle

#### Union of More Than Two Sets

The Principle of Inclusion and Exclusion can be generalized to the union of more than two sets. Let A_1, A_2, ..., A_n and B_1, B_2, ..., B_m be two sets of elements. Then, the union of these two sets can be expressed as:

|A_1 ∪ A_2 ∪ ... ∪ A_n ∪ B_1 ∪ B_2 ∪ ... ∪ B_m| = ∑|A_i| - ∑|A_i ∩ A_j| + ... + ∑|A_i ∩ A_j ∩ B_k| - ... + (-1)^n ∑|A_i ∩ A_j ∩ B_k ∩ B_l|

where |A_i| denotes the number of elements in set A_i, |A_i ∩ A_j| denotes the number of elements in the intersection of sets A_i and A_j, and so on.

#### Intersection of More Than Two Sets

The Principle of Inclusion and Exclusion can also be generalized to the intersection of more than two sets. Let A_1, A_2, ..., A_n and B_1, B_2, ..., B_m be two sets of elements. Then, the intersection of these two sets can be expressed as:

|A_1 ∩ A_2 ∩ ... ∩ A_n ∩ B_1 ∩ B_2 ∩ ... ∩ B_m| = ∑|A_i ∩ A_j| - ∑|A_i ∩ A_j ∩ B_k| + ... + ∑|A_i ∩ A_j ∩ B_k ∩ B_l|

where |A_i| denotes the number of elements in set A_i, |A_i ∩ A_j| denotes the number of elements in the intersection of sets A_i and A_j, and so on.

#### Multiple Set Union and Intersection

The Principle of Inclusion and Exclusion can be generalized to the union and intersection of multiple sets. Let A_1, A_2, ..., A_n and B_1, B_2, ..., B_m be two sets of elements. Then, the union of these sets can be expressed as:

|A_1 ∪ A_2 ∪ ... ∪ A_n ∪ B_1 ∪ B_2 ∪ ... ∪ B_m| = ∑|A_i| - ∑|A_i ∩ A_j| + ... + ∑|A_i ∩ A_j ∩ B_k| - ... + (-1)^n|A_1 ∩ A_2 ∩ ... ∩ A_n ∩ B_1 ∩ B_2 ∩ ... ∩ B_m|

Similarly, the intersection of these sets can be expressed as:

|A_1 ∩ A_2 ∩ ... ∩ A_n ∩ B_1 ∩ B_2 ∩ ... ∩ B_m| = ∑|A_i ∩ A_j| - ∑|A_i ∩ A_j ∩ B_k| + ... + ∑|A_i ∩ A_j ∩ B_k ∩ B_l|

### Derangements – Nothing is in its Right Place

A derangement is a permutation of the elements of a set, such that no element is in its original position. In other words, a derangement is a permutation that is "nothing in its right place".

The number of derangements of a set with n elements is given by the formula:

!n = n! - ∑n!/k!

where !n denotes the number of derangements of a set with n elements.

### Rook Polynomials

A rook polynomial is a polynomial that counts the number of ways to place n rooks on an m × n board, such that no two rooks are in the same row or column.

The rook polynomial is defined as:

R_n,m = ∑x^i y^j

where x^i denotes the number of ways to place i rooks in the first n rows, and y^j denotes the number of ways to place j rooks in the first m columns.

The rook polynomial can be expressed as:

R_n,m = (1 + x + x^2 + ... + x^n)(1 + y + y^2 + ... + y^m)

where x and y are the rook polynomials for n and m rooks, respectively.

### Further Reading

- "Combinatorial Mathematics" by Richard P. Stanley
- "Discrete Mathematics and Its Applications" by Kenneth H. Rosen
- "The Principle of Inclusion and Exclusion" by Richard A. Brualdi
