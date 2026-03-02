# Travelling Salesman Problem (TSP)

**Definition:**
TSP is a classic problem in graph theory and computer science, where a salesman needs to visit a set of cities and returns to the origin city, minimizing the total distance travelled.

**Key Points:**

- **Problem Formulation:** Given a set of cities (vertices) and their pairwise distances (edges), find the shortest possible tour that visits each city exactly once and returns to the origin city.
- **Notations:**
  - `n`: number of cities (vertices)
  - `d_ij`: distance between cities `i` and `j`
  - `T`: minimum total distance (tour length)
- **Types of TSP:**
  - **Exact Methods:** brute force, dynamic programming, branch and bound
  - **Approximation Methods:** greedy algorithms, genetic algorithms, simulated annealing

**Important Formulas and Theorems:**

- **TSP Lower Bound:** `T >= n (1 + 1/2) / 2`
- **Christofides Algorithm:** `T <= 3/2 n (1 + 1/2) (diameter)`
- **Concorde Algorithm:** a branch and bound algorithm that can find an optimal solution for small instances of TSP

**Key Results:**

- **TSP is NP-hard:** no known efficient algorithm can solve TSP exactly for large instances.
- **TSP is APX-hard:** approximation algorithms have a polynomial-time approximation factor.

**Key Concepts:**

- **TSP Tour:** a Hamiltonian cycle in the complete graph of cities
- **TSP Traveling Time:** the sum of distances between consecutive cities in a tour
- **TSP Routing:** a tour with a minimum total traveling time
