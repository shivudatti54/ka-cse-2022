# **Chapter 4 (Sections 4.1) Analysis & Design of Algorithms: Brute Force Approaches**

### Overview

- **Exhaustive Search**: A brute force approach that involves trying all possible solutions to a problem.
- **Travelling Salesman Problem (TSP)**: A classic example of an NP-hard problem that involves finding the shortest possible tour that visits a set of cities and returns to the starting city.

### Key Points

- **Definition**: A brute force algorithm is an algorithm that tries all possible solutions to a problem, often using a lot of time and resources.
- **Types of Brute Force Algorithms**:
  - **Exhaustive Search**: Tries all possible solutions.
  - **Binary Search**: Finds an element in an array by dividing the search space in half.
- **Travelling Salesman Problem (TSP)**:
  - **NP-hard**: The problem is computationally intractable and requires an unfeasible amount of time to solve exactly.
  - **Approximation Algorithms**: Use heuristics to find a good but not necessarily optimal solution.

### Important Formulas, Definitions, and Theorems

- **Big O Notation**:
  - **O(1)**: Constant time complexity.
  - **O(log n)**: Logarithmic time complexity.
  - **O(n)**: Linear time complexity.
  - **O(n log n)**: Linearithmic time complexity.
  - **O(n!)**: Exponential time complexity.
- **Backtracking Algorithm**:
  - **State Space Tree**: A tree data structure used to represent the search space.
  - **Pruning**: Removing branches of the tree that are not promising.
- **Heuristics**:
  - **Nearest Neighbor**: A simple heuristic that chooses the closest city first.

### Key Theorems

- **Cook-Levin Theorem**: States that NP is equal to NP-complete if and only if SAT is NP-complete.
- **Karp's Reduction**: A reduction algorithm that transforms a problem into a known NP-complete problem.

### Important Terms

- **NP-complete**: A class of problems that are computationally intractable.
- **NP-hard**: A class of problems that are at least as hard as the NP-complete problems.

### Key Concepts

- **Dynamic Programming**: A method for solving problems by breaking them down into smaller subproblems.
- **Greedy Algorithm**: An algorithm that makes the locally optimal choice at each stage with the hope of finding a global optimum.
