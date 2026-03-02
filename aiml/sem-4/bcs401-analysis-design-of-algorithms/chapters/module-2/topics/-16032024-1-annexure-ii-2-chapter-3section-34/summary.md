# Revision Notes: Exhaustive Search (Travelling Salesman Problem)

===========================================================

### Overview

- Exhaustive search is a brute force approach to solve the Travelling Salesman Problem (TSP)
- It involves generating all possible permutations of the Tour and checking if they satisfy the constraints of TSP

### Key Points

- **Definition:** Travelling Salesman Problem (TSP) is a classic problem in combinatorial optimization and computer science that involves finding the shortest possible tour that visits a set of cities and returns to the original city
- **Exhaustive Search Algorithm:**
  - Generate all permutations of the cities
  - Calculate the total distance for each permutation
  - Check if the permutation satisfies the TSP constraints (e.g., non-negative distances, no self-loops, and no cycles)
  - Return the shortest permutation that satisfies the constraints
- **Time Complexity:** O(n!) where n is the number of cities, making it impractical for large inputs
- **Importance:** Exhaustive search is a theoretical approach to demonstrate the complexity of TSP and is not used in practice due to its high computational cost

### Important Formulas, Definitions, and Theorems

- **Tour:** A sequence of cities visited by the salesman
- **Distance Matrix:** A matrix representing the distances between each pair of cities
- **Hamiltonian Circuit:** A closed tour that visits each city exactly once and returns to the original city
- **TSP Lower Bound:** A lower bound on the solution quality for TSP using the brute force approach

### Practical Considerations

- Exhaustive search is not used in practice due to its high computational cost and is mainly used to demonstrate the complexity of TSP
- Heuristics and approximation algorithms are used to solve TSP in practice
