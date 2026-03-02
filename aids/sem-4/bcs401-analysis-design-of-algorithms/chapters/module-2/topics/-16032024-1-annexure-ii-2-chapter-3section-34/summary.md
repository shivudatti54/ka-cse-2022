## Revision Notes: Exhaustive Search (Travelling Salesman Problem - Chapter 3.4)

=============================================

### Definitions and Notations

- **Travelling Salesman Problem (TSP):** A classic problem in combinatorial optimization and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the starting city.
- **Exhaustive Search:** A brute-force algorithm that explores all possible solutions to a problem.
- **Distance Matrix:** A matrix representing the distances between cities.

### Key Concepts

- **Greedy Algorithm:** A heuristic approach that makes locally optimal choices to find a global optimum.
- **Dynamic Programming:** A method for solving complex problems by breaking them down into smaller subproblems.
- **Backtracking:** A technique used in exhaustive search to explore all possible solutions.

### Important Formulas and Theorems

- **TSP Distance Formula:** `d(i, j) = |x_i - x_j| + |y_i - y_j|` (Euclidean distance)
- **TSP Traveling Salesman Problem Formulation:** `min ∑[d(i, j) | 1 ≤ i < j ≤ n]`
- **Bellman-Ford Algorithm:** A dynamic programming algorithm for finding the shortest path in a weighted graph.
- **Theorem:** The TSP is NP-hard, meaning that the running time of algorithms increases rapidly as the size of the input increases.

### Important Results

- **Christofides Algorithm:** A heuristic algorithm that finds a near-optimal solution to the TSP with a guaranteed performance ratio.
- **Concorde Algorithm:** A branch-and-bound algorithm for solving TSP instances.

### Important Problems

- **TSP of 3 cities:** `d(1, 2) = 10, d(2, 3) = 15, d(3, 1) = 20`
- **TSP of 4 cities:** `d(1, 2) = 10, d(2, 3) = 15, d(3, 4) = 20, d(4, 1) = 25`

### Time Complexity

- **Exhaustive Search:** O(n!), where n is the number of cities.
- **Greedy Algorithm:** O(n^2)
- **Dynamic Programming:** O(n^3)

### Space Complexity

- **Exhaustive Search:** O(n!), where n is the number of cities.
- **Greedy Algorithm:** O(n)
- **Dynamic Programming:** O(n^2)
