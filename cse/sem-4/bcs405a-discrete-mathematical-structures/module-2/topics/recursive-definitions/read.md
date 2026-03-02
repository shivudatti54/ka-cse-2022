# Recursive Definitions

## Table of Contents

- [Recursive Definitions](#recursive-definitions)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Structure of Recursive Definitions](#structure-of-recursive-definitions)
  - [Recursively Defined Sets](#recursively-defined-sets)
  - [Recursively Defined Functions](#recursively-defined-functions)
  - [Recursively Defined Data Structures](#recursively-defined-data-structures)
  - [Structural Induction](#structural-induction)
  - [Well-Ordering Principle](#well-ordering-principle)
- [Examples](#examples)
  - [Example 1: Sum of First n Natural Numbers](#example-1-sum-of-first-n-natural-numbers)
  - [Example 2: Number of Binary Strings of Length n](#example-2-number-of-binary-strings-of-length-n)
  - [Example 3: Towers of Hanoi Move Count](#example-3-towers-of-hanoi-move-count)
- [Exam Tips](#exam-tips)

## Introduction

Recursive definitions are fundamental to discrete mathematics and computer science. A recursive definition (also called an inductive definition) defines an object in terms of simpler instances of itself. This powerful technique allows us to describe infinitely large sets or functions using a finite number of rules. In computer science, recursive definitions form the backbone of algorithm design, data structures, programming languages, and formal language theory.

The importance of recursive definitions in the the syllabus cannot be overstated. They appear in various contexts including the definition of natural numbers (Peano axioms), combinatorial counting (recurrence relations), tree data structures, grammars in compilers, and algorithm complexity analysis. Understanding recursive definitions is essential for mastering mathematical induction, which is a critical proof technique in computer science courses.

A recursive definition typically consists of two components: a **basis** (or base case) that establishes initial, simple elements, and a **recursive step** (or inductive case) that defines how to construct new elements from previously defined ones. Together, these components completely characterize the set or function being defined.

## Key Concepts

### Structure of Recursive Definitions

Every recursive definition has three essential parts:

1. **Base Case (Basis)**: Specifies the simplest elements of the set or the starting value of the function. These are explicitly defined without reference to other elements.

2. **Recursive Step (Inductive Case)**: Defines how to construct new elements from existing ones, or how to compute new values from previously computed values.

3. **Closure**: The assumption that the definition generates all elements of the set (no others exist). This is often implicit but crucial.

### Recursively Defined Sets

**Example 1: Natural Numbers**
The set of natural numbers N can be defined recursively as:

- **Base Case**: 0 ∈ N
- **Recursive Step**: If n ∈ N, then n+1 ∈ N

This simple definition generates the infinite set {0, 1, 2, 3, ...}.

**Example 2: Strings over an Alphabet**
Let Σ = {a, b} be an alphabet. The set Σ\* of all strings (including empty string) can be defined as:

- **Base Case**: ε ∈ Σ\* (ε denotes the empty string)
- **Recursive Step**: If w ∈ Σ* and x ∈ Σ, then wx ∈ Σ* (concatenation)

This generates: ε, a, b, aa, ab, ba, bb, aaa, ...

**Example 3: Well-Formed Parentheses**
The set of well-formed parentheses strings can be defined as:

- **Base Case**: ε ∈ P (empty string is well-formed)
- **Recursive Step**: If s, t ∈ P, then (s)t ∈ P

This generates: (), (()), ()(), ((())), ()(), and so on.

### Recursively Defined Functions

When defining functions recursively, we specify:

- The value of the function at the base case(s)
- A rule to compute f(n) using f of smaller arguments

**Example: Factorial Function**
The factorial function n! is defined as:

- **Base Case**: 0! = 1
- **Recursive Step**: n! = n × (n-1)! for n ≥ 1

To compute 4!:
4! = 4 × 3! = 4 × 3 × 2! = 4 × 3 × 2 × 1! = 4 × 3 × 2 × 1 × 0! = 4 × 3 × 2 × 1 × 1 = 24

**Example: Fibonacci Sequence**
The Fibonacci sequence is defined as:

- **Base Case**: F(0) = 0, F(1) = 1
- **Recursive Step**: F(n) = F(n-1) + F(n-2) for n ≥ 2

This generates: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

**Example: Length of a String**
Let l(w) denote the length of string w over alphabet Σ:

- **Base Case**: l(ε) = 0
- **Recursive Step**: l(wx) = l(w) + 1, where w ∈ Σ\*, x ∈ Σ

### Recursively Defined Data Structures

**Example: Binary Trees**
The set of binary trees can be defined as:

- **Base Case**: nil (empty tree) is a binary tree
- **Recursive Step**: If L and R are binary trees, then node(L, x, R) is a binary tree with root x, left subtree L, and right subtree R

**Example: Linked Lists**
The set of lists over a set S can be defined as:

- **Base Case**: nil (empty list) is a list
- **Recursive Step**: If head ∈ S and tail is a list, then cons(head, tail) is a list

### Structural Induction

Structural induction is a proof technique used to prove properties about recursively defined structures. To prove that property P holds for all elements of a recursively defined set:

1. **Base Case**: Prove P holds for the base case(s)
2. **Inductive Step**: Assume P holds for smaller elements and prove it holds for elements constructed using the recursive step

**Theorem**: For the recursively defined set of natural numbers, n! ≥ 2^(n-1) for all n ≥ 1.

**Proof by Structural Induction**:

- **Base Case**: For n = 1, 1! = 1 ≥ 2^0 = 1. ✓
- **Inductive Step**: Assume k! ≥ 2^(k-1) for some k ≥ 1
  Then (k+1)! = (k+1) × k! ≥ (k+1) × 2^(k-1)
  Since k+1 ≥ 2 for k ≥ 1, we have (k+1) × 2^(k-1) ≥ 2 × 2^(k-1) = 2^k
  Hence (k+1)! ≥ 2^k = 2^((k+1)-1)
- By structural induction, the property holds for all n ≥ 1.

### Well-Ordering Principle

The Well-Ordering Principle states: Every non-empty subset of natural numbers has a least element. This principle is equivalent to mathematical induction and is often used in proofs involving recursive definitions.

## Examples

### Example 1: Sum of First n Natural Numbers

Define S(n) = 1 + 2 + 3 + ... + n:

- **Base Case**: S(0) = 0
- **Recursive Step**: S(n) = S(n-1) + n for n ≥ 1

**Compute S(5)**:
S(5) = S(4) + 5
= (S(3) + 4) + 5
= ((S(2) + 3) + 4) + 5
= (((S(1) + 2) + 3) + 4) + 5
= ((((S(0) + 1) + 2) + 3) + 4) + 5
= (((((0 + 1) + 2) + 3) + 4) + 5)
= ((((1 + 2) + 3) + 4) + 5)
= (((3 + 3) + 4) + 5)
= ((6 + 4) + 5)
= (10 + 5)
= 15

### Example 2: Number of Binary Strings of Length n

Let b(n) be the number of binary strings of length n:

- **Base Case**: b(0) = 1 (empty string)
- **Recursive Step**: b(n) = 2 × b(n-1) for n ≥ 1

**Compute b(4)**:
b(4) = 2 × b(3) = 2 × 2 × b(2) = 2 × 2 × 2 × b(1) = 2 × 2 × 2 × 2 × b(0) = 2 × 2 × 2 × 2 × 1 = 16

This makes sense: there are 2^4 = 16 binary strings of length 4.

### Example 3: Towers of Hanoi Move Count

Let H(n) be the minimum number of moves to solve the Towers of Hanoi puzzle with n disks:

- **Base Case**: H(1) = 1
- **Recursive Step**: H(n) = 2H(n-1) + 1 for n ≥ 2

**Compute H(4)**:
H(4) = 2H(3) + 1 = 2(2H(2) + 1) + 1 = 2(2(2H(1) + 1) + 1) + 1
= 2(2(2(1) + 1) + 1) + 1 = 2(2(2 + 1) + 1) + 1 = 2(2(3) + 1) + 1
= 2(6 + 1) + 1 = 2(7) + 1 = 14 + 1 = 15

This formula yields: H(n) = 2^n - 1

## Exam Tips

1. **Understand the Two Parts**: Always identify the base case and recursive step clearly in any recursive definition. Many exam questions ask you to identify these components.

2. **Computing Recursive Functions**: Practice tracing through recursive definitions step by step. This is essential for both exams and practical programming.

3. **Proof by Induction**: Structure induction proofs identically to ordinary mathematical induction—base case, inductive hypothesis, inductive step. This is a favorite exam topic.

4. **Closure Verification**: Be prepared to prove that a recursively defined set contains exactly the intended elements. Show that the set is both minimal (contains only defined elements) and exhaustive (contains all elements).

5. **Recursive vs Closed Form**: You may be asked to find a closed form for recursively defined functions. For example, the Towers of Hanoi formula H(n) = 2^n - 1.

6. **Common Recursive Patterns**: Memorize standard recursive definitions—factorial, Fibonacci, sum of first n numbers, power function, and string length. These frequently appear in exams.

7. **Application to Data Structures**: Understand how recursive definitions apply to trees, lists, and other data structures. This connects to your data structures course.

8. **Well-Ordering Principle**: Remember that this principle underlies mathematical induction and is useful for proving properties about natural numbers defined recursively.
