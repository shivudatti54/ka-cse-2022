# Revision Notes: Chapter 12 (Sections 12.1) - Analysis & Design of Algorithms

## Introduction

- This chapter focuses on the limitations of algorithmic power, including decision trees, P, NP, and NP-Complete problems.

## Decision Trees

- Definition: A decision tree is a flowchart that represents a set of rules for making decisions.
- Key points:
  - A decision tree is a tree-like structure where each internal node represents a decision, and each leaf node represents an outcome.
  - Decision trees can be used for classification and regression problems.

## P (Polynomial Time)

- Definition: A problem is in P if it can be solved in polynomial time, i.e., its running time is bounded by a polynomial function of the input size.
- Key points:
  - Examples of problems in P include sorting, searching, and graph traversal.
  - P is a class of problems that can be solved efficiently.

## NP (Nondeterministic Polynomial Time)

- Definition: A problem is in NP if it can be verified in polynomial time, i.e., given a proposed solution, it can be checked in polynomial time whether it is correct.
- Key points:
  - Examples of problems in NP include graph isomorphism and subset sum.
  - NP is a class of problems that can be verified efficiently.

## NP-Complete Problems

- Definition: A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time.
- Key points:
  - Examples of NP-complete problems include the traveling salesman problem and knapsack problem.
  - NP-complete problems are computationally hard to solve exactly.

## Important Formulas and Definitions

- **Cook-Levin Theorem**: A problem is NP-complete if and only if every problem in NP can be reduced to it in polynomial time.
- **Karp's Reduction**: A polynomial-time reduction from problem A to problem B means that given an instance of A, we can construct an instance of B in polynomial time such that A is solvable if and only if B is solvable.

## Important Theorems

- **P vs NP Problem**: The question of whether P = NP or P ≠ NP is one of the most famous open problems in computer science.
