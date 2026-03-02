# **Chapter 5 (Section 5.1) - Exhaustive Search: Travelling Salesman Problem**

**Definition:**

- Exhaustive Search: A brute-force approach that involves checking all possible solutions to find the optimal one.

**Key Concepts:**

- **Travelling Salesman Problem (TSP):** A classic problem in computer science and operations research that involves finding the shortest possible tour that visits a set of cities and returns to the original city.
- **TSP Example:** Suppose we have 5 cities (A, B, C, D, E) and their pairwise distances:
  - A-B: 10
  - A-C: 20
  - A-D: 15
  - A-E: 30
  - B-C: 25
  - B-D: 18
  - B-E: 22
  - C-D: 12
  - C-E: 28
  - D-E: 20

**Formulas:**

- **TSP Formulation:** Minimize ∑d(i, j) subject to: ∀i, j ∈ V, d(i, j) ≥ 0, and ∀v ∈ V, ∑d(v, i) = d(v, v) = 0
- **TSP Constraint:** ∑d(v, i) = d(v, v) = 0 ∀v ∈ V

**Theorems:**

- **TSP Complexity:** The TSP is NP-hard, meaning that there is no known efficient algorithm to solve it exactly for large instances.
- **TSP Lower Bounds:** The TSP has a lower bound of Ω(2^n/3) for n cities, where n is the number of cities.

**Important Observations:**

- **TSP Branch and Bound:** A heuristic approach that involves dividing the search space into smaller sub-problems and using bounds to prune the search tree.
- **TSP Genetic Algorithm:** A metaheuristic approach that uses principles of natural selection and genetics to search for optimal solutions.

**Quick Revision Tips:**

- Understand the definition of Exhaustive Search and its application to the TSP.
- Familiarize yourself with the TSP formulation and constraints.
- Be aware of the TSP complexity and lower bounds.
- Review the TSP branch and bound and genetic algorithm approaches.
