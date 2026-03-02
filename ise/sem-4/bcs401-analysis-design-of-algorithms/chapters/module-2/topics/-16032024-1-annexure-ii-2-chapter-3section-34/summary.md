## Revision Notes: Exhaustive Search (Travelling Salesman Problem)

=====================================

### Introduction

---

- Exhaustive search is a brute force approach to solve the Travelling Salesman Problem (TSP).
- It involves generating all possible permutations of the cities and calculating the total distance traveled.

### Key Concepts

---

- **Travelling Salesman Problem (TSP)**: Given a set of cities and their pairwise distances, find the shortest possible tour that visits each city exactly once and returns to the starting city.
- **Exhaustive Search**: A brute force approach that generates all possible permutations of the cities and calculates the total distance traveled.

### Important Formulas

---

- **Distance Formula**: $d(A, B) = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
- **Total Distance**: $D = \sum_{i=1}^{n-1} d(c_i, c_{i+1}) + d(c_n, c_1)$

### Definitions

---

- **Permutation**: An arrangement of objects in a specific order.
- **Tour**: A path that visits each city and returns to the starting city.

### Theorem

---

- **TSP Lower Bound**: The optimal solution to the TSP has a lower bound of $\frac{2n}{3} \geq D$.

### Key Ideas

---

- Exhaustive search has an exponential time complexity of $O(n!)$, making it impractical for large instances of TSP.
- Heuristics and approximation algorithms are often used to solve TSP more efficiently.

### Important Definitions

---

- **Heuristic**: A method that uses a rule of thumb to find an optimal or near-optimal solution.
- **Approximation Algorithm**: An algorithm that provides a solution that is close to the optimal solution, but may not be exact.
