# Chapter 11 (Section 11.2) Revision Notes

=============================================

### Decision Trees

- Decision Tree: A tree-like model of decisions and their possible outcomes.
- Definition: A decision tree is a tree-like model where each internal node represents a decision, and each leaf node represents an outcome.
- Types:
  - Binary Decision Tree (2 possible outcomes per node)
  - M-ary Decision Tree (m possible outcomes per node)
- Advantages:
  - Simple to implement
  - Easy to visualize
- Disadvantages:
  - Can be slow for large inputs
  - May not be optimal

### P, NP, and NP-Complete Problems

- **P (Polynomial Time) Problems**:
  - A set of problems solvable by a deterministic Turing machine in polynomial time.
  - E.g., sorting, searching, and graph traversal.
- **NP (Nondeterministic Polynomial Time) Problems**:
  - A set of problems solvable by a nondeterministic Turing machine in polynomial time.
  - E.g., satisfiability (SAT), traveling salesman problem (TSP).
- **NP-Complete Problems**:
  - A subset of NP problems that are at least as hard as the hardest problems in NP.
  - E.g., Boolean satisfiability (SAT), traveling salesman problem (TSP).
- Definition of NP-Completeness:
  - A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time.

### Important Formulas and Definitions

- **Definition of NP-Completeness**:
  - A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time.
  - `L` is a language if there exists a deterministic Turing machine that can solve it in polynomial time.
- **Cook-Levin Theorem**:
  - If a problem is NP-complete, it is also NP-hard.
  - `NP-hard` means that a problem is at least as hard as the hardest problems in NP.

### Important Theorems

- **Cook-Levin Theorem**:
  - If a problem is NP-complete, it is also NP-hard.
  - `NP-hard` means that a problem is at least as hard as the hardest problems in NP.
- **Karp-Levin Theorem**:
  - If a problem is in NP, it is also NP-complete if it is NP-hard.
