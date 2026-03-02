# Approximation Algorithms

## Introduction

Approximation algorithms are essential for solving NP-hard optimization problems where finding exact solutions is computationally infeasible. These algorithms provide near-optimal solutions within provable performance bounds, making them fundamental to the Advanced Algorithms syllabus for MSc CS at Delhi University.

## Key Concepts

- **Approximation Ratio**: The worst-case ratio between the algorithm's solution and the optimal solution
  - α-approximation algorithm guarantees solution within α times optimal
  - For minimization problems: algorithm ≤ α × optimal
  - For maximization problems: algorithm ≥ (1/α) × optimal

- **PTAS & FPTAS**: Polynomial-Time Approximation Schemes
  - PTAS: For any ε > 0, achieves (1+ε) approximation in polynomial time
  - FPTAS: Runtime polynomial in both input size and 1/ε

## Classic Approximation Algorithms

- **Vertex Cover**: 2-approximation using maximal matching
- **Set Cover**: ln(n)-approximation using greedy method
- **Metric TSP**: 1.5-approximation using Christofides algorithm
- **Knapsack**: FPTAS achieving (1+ε) approximation
- **Load Balancing**: 2-approximation for makespan minimization

## Design Techniques

- **Greedy Approach**: Local optimization with guaranteed bounds
- **Local Search**: Iterative improvement until local optimum
- **Linear Programming**: Rounding fractional solutions
- **Primal-Dual Method**: Combining combinatorial and LP techniques

## Inapproximability

- PCP Theorem establishes limits on approximability
- Some problems cannot be approximated within certain factors (unless P=NP)
- Examples: MAX-3SAT, Graph Coloring

## Delhi University Syllabus Focus

According to the MSc CS Advanced Algorithms syllabus, students must understand:
- Classification of problems by approximability
- Analysis of approximation ratios
- Relationship between NP-hardness and approximation
- Practical applications in scheduling, routing, and resource allocation

## Conclusion

Approximation algorithms provide efficient, near-optimal solutions for intractable optimization problems. Mastery of approximation techniques, ratio analysis, and classic algorithms is crucial for solving real-world computational challenges where exact solutions are impossible.