# Chapter 11 (Section 11.2) Revision Notes

=====================================

## Decision Trees

---

- A decision tree is a tree-like model of decisions and their possible consequences.
- It consists of nodes (representing decisions) and edges (representing the consequences of each decision).
- Decision trees can be used for both prediction and optimization problems.

## P, NP, and NP-Complete Problems

---

### P Problems

---

- A decision problem is in P if it can be solved in polynomial time.
- P is the set of all decision problems that can be solved in polynomial time.

### NP Problems

---

- An optimization problem is in NP if a proposed solution can be verified in polynomial time.
- NP is the set of all optimization problems that can be verified in polynomial time.

### NP-Complete Problems

---

- A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time.
- Examples of NP-complete problems include the traveling salesman problem and the knapsack problem.

## Important Formulas and Definitions

---

### Decision Trees

- Tree height (h) is the number of edges between the root and a leaf.
- Tree size (s) is the number of edges in the tree.

### P Problems

- P = P(n) if there exists a polynomial-time algorithm that can solve the problem on inputs of size n.

### NP Problems

- NP = NP(n) if there exists a polynomial-time algorithm that can verify the optimality of a solution on inputs of size n.

### NP-Complete Problems

- NP-complete = NP ∩ NP-hard.

## Important Theorems

---

### Cook-Levin Theorem

- A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time.

### reductions

- A reduction from problem A to problem B is an algorithm that can solve problem A in polynomial time using as input the solution to problem B.
