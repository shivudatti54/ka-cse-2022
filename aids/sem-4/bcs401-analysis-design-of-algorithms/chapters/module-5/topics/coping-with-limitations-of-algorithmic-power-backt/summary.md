# Revision Notes: COPING WITH LIMITATIONS OF ALGORITHMIC POWER

===========================================================

# Introduction

---

This topic focuses on algorithms that cope with the limitations of algorithmic power, including decision trees, P, NP, and NP-complete problems. We will explore three key techniques: Backtracking, Branch-and-Bound, and Approximation.

# Backtracking

---

- **Definition:** A search algorithm that explores all possible solutions to a problem by backtracking when a dead end is reached.
- **Applications:**
  - **n-Queens Problem:** Place n queens on an nxn chessboard such that no two queens attack each other.
  - **Subset-sum Problem:** Given a subset of integers, determine if the sum of a subset is equal to a given target value.
- **Key Formulas and Definitions:**
  - **Recursive Algorithm:** A function that solves a problem by breaking it down into smaller sub-problems of the same type.
  - **Backtracking Algorithm:** A search algorithm that explores all possible solutions by backtracking when a dead end is reached.

# Branch-and-Bound

---

- **Definition:** A search algorithm that prunes branches of the search tree by estimating the lower bound of the sub-problem.
- **Applications:**
  - **Knapsack Problem:** Given a set of items, each with a weight and a value, determine the subset of items to include in a knapsack of limited capacity to maximize the total value.
- **Key Formulas and Definitions:**
  - **Branch-and-Bound Algorithm:** A search algorithm that prunes branches of the search tree by estimating the lower bound of the sub-problem.
  - **Lower Bound:** An estimate of the minimum cost or value of a sub-problem.

# Approximation

---

- **Definition:** An algorithm that finds an approximate solution to a problem, often using heuristics or greedy algorithms.
- **Applications:**
  - **Approximation Algorithms:** Find approximate solutions to NP-hard problems, such as the Traveling Salesman Problem or the Assignment Problem.
- **Key Formulas and Definitions:**
  - **Greedy Algorithm:** An algorithm that makes the locally optimal choice at each step, hoping to find a global optimum.
  - **Heuristics:** Rules of thumb or shortcuts used to solve a problem approximately.

# Important Theorems

---

- **P vs. NP Problem:** A fundamental problem in computer science that asks whether every problem with a known efficient algorithm (P) can also be verified efficiently (NP).
- **NP-Completeness:** A class of problems that are at least as hard as the hardest problems in NP.
