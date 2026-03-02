# **Chapter 5 (Section 5.1) - Exhaustive Search (Travelling Salesman Problem)**

**Key Points:**

- **Definition:** Exhaustive Search is a brute-force approach that involves checking all possible solutions to a problem.
- **Travelling Salesman Problem (TSP):** A classic problem in combinatorial optimization that involves finding the shortest possible tour that visits a set of cities and returns to the starting city.
- **Time Complexity:** O(n!), where n is the number of cities.
- **Space Complexity:** O(n), where n is the number of cities.
- **Example:** Given a set of cities, the exhaustive search algorithm would generate all possible permutations of the cities and calculate the total distance for each permutation.

**Important Formulas and Definitions:**

- **Hamiltonian Path:** A path in a graph that visits each vertex exactly once.
- **Tour:** A path that visits each vertex exactly once and returns to the starting vertex.
- **Nearest Neighbor (NN) Algorithm:** A heuristic algorithm that starts at a random city and repeatedly chooses the closest unvisited city.
- **Nearest Neighbor Bound:** A bound on the optimum solution of the TSP that is derived from the NN algorithm.

**Theorems and Results:**

- **Pigeonhole Principle:** A theorem that states that if n items are put into m containers, with n > m, then at least one container must contain more than one item.
- **Strassen's Algorithm:** A fast algorithm for matrix multiplication that has a time complexity of O(n^2.81) for 2x2 matrices.

**Important Theorems:**

- **The Travelling Salesman Problem is NP-hard:** This means that the problem is at least as hard as the hardest problems in NP (nondeterministic polynomial time).

**Revision Notes:**

- Exhaustive Search is a brute-force approach that involves checking all possible solutions to a problem.
- The Travelling Salesman Problem is a classic problem in combinatorial optimization that involves finding the shortest possible tour that visits a set of cities and returns to the starting city.
- The time and space complexity of the exhaustive search algorithm are O(n!) and O(n), respectively.
- The nearest neighbor algorithm is a heuristic algorithm that starts at a random city and repeatedly chooses the closest unvisited city.
