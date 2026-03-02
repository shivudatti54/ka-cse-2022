**Chapter 4: Analysis & Design of Algorithms**
**Module: BRUTE FORCE APPROACHES (continued)**
**Exhaustive Search: Travelling Salesman Problem (TSP) - Section 4.1**

**Key Concepts:**

- **Definition:** Travelling Salesman Problem (TSP) is an NP-hard problem that involves finding the shortest possible tour that visits a set of cities and returns to the original city.
- **Objective:** Minimize the total distance traveled by the salesman.
- **Evaluation Function:** `d(i, j)` represents the distance between city `i` and city `j`.

**Important Formulas and Notations:**

- **Distance Matrix (D):** A square matrix `D` with dimensions `n x n`, where `n` is the number of cities.
- **Tour Cost (C):** The sum of the distances between consecutive cities in a tour, i.e., `C = d(c1, c2) + d(c2, c3) + ... + d(cn, c1)`.
- **Genetic Algorithm (GA):** A heuristic search algorithm inspired by natural selection and genetics.

**Theorems:**

- **TSP Lower Bound:** There exists no polynomial-time algorithm for solving TSP exactly, and the best known algorithm has a time complexity of O(2^n).
- **TSP Upper Bound:** There exists a polynomial-time algorithm for solving a variant of TSP (e.g., TSP with 2-approximation).

**Key Techniques:**

- **Brute Force Approach:** A naive approach that tries all possible permutations of cities.
- **Greedy Algorithm:** A heuristic approach that chooses the closest city at each step.
- **Dynamic Programming:** A technique for solving problems by breaking them down into smaller sub-problems.

**Important Definitions:**

- **Nearest Neighbor (NN):** The algorithm that chooses the closest city at each step.
- **2-Approximation:** A heuristic approach that guarantees a solution that is at most twice the optimal solution.
