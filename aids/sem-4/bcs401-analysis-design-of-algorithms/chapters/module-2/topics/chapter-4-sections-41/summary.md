# **Chapter 4 (Sections 4.1) Analysis & Design of Algorithms**

## **Brute Force Approaches: Exhaustive Search**

### Definitions and Theorems

- **Exhaustive Search**: A brute force algorithm that checks all possible solutions to a problem.
- **Travelling Salesman Problem (TSP)**: A classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the origin city.
- **Bellman's Theorem**: States that if there are n cities and n-1 edges, then there must be at least one TSP tour that is at least as long as the shortest tour.

### Key Points

- **Time Complexity**: O(n!), where n is the number of cities.
- **Space Complexity**: O(n), for storing the distances between cities.
- **Approach**:
  - Define the problem and identify the search space.
  - Choose an initial solution (e.g., starting from the first city).
  - Generate all possible permutations of the remaining cities.
  - Evaluate each permutation and find the shortest tour.
- **Formulas**:
  - **Distance Formula**: The distance between two cities is calculated using the Euclidean distance formula (e.g., √((x2 - x1)^2 + (y2 - y1)^2)).
  - **Tour Length Formula**: The length of a tour is calculated by summing the distances between consecutive cities.

### Important Formulas

- **Euclidean Distance Formula**: √((x2 - x1)^2 + (y2 - y1)^2)
- **Tour Length Formula**: √\*∑(d_ij \* 1) where d_ij is the distance between cities i and j.

### Important Theorems

- **Bellman's Theorem**: If there are n cities and n-1 edges, then there must be at least one TSP tour that is at least as long as the shortest tour.
