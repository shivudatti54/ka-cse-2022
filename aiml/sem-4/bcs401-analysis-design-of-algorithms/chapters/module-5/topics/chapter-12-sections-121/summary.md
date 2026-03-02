### Chapter 12 (Sections 12.1) Revision Notes

#### Analysis & Design of Algorithms

#### LIMITATIONS OF ALGORITHMIC POWER: Decision Trees, P, NP, and NP-Complete Problems

**Key Points:**

- **Decision Trees:**
  - A tree-like model for making decisions
  - Each internal node represents a test on an input
  - Each leaf node represents an outcome or action
- **P (Polynomial Time) Complexity:**
  - A measure of an algorithm's computational complexity
  - An algorithm is P if it can solve a problem in polynomial time (O(n^k) where k is constant)
  - P = NP if every problem in NP can be solved in polynomial time
- **NP (Nondeterministic Polynomial Time) Complexity:**
  - A class of problems that can be solved in polynomial time by a nondeterministic Turing machine
  - A problem is in NP if it can be verified in polynomial time
- **NP-Complete Problems:**
  - A subclass of NP problems that are at least as hard as the hardest problems in NP
  - A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time
- **Cook-Levin Theorem:**
  - A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time
  - Proved in 1971 by Stephen Cook and Jonathan Levin

**Important Formulas and Definitions:**

- **Big O Notation:** O(f(n)) represents an upper bound on the time complexity of an algorithm
- **Polynomial Time:** An algorithm is P if it can solve a problem in polynomial time (O(n^k) where k is constant)
- **Nondeterministic Turing Machine (NTM):** A model of computation that can solve a problem in polynomial time

**Important Theorems:**

- **P vs NP Problem:** The question of whether P equals NP remains one of the most important open problems in computer science
- **Cook-Levin Theorem:** A problem is NP-complete if it is in NP and every problem in NP can be reduced to it in polynomial time
