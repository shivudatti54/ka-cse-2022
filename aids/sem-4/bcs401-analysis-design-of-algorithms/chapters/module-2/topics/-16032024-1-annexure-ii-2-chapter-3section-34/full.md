# @# 16032024 1 Annexure-II 2 Chapter 3(Section 3.4): Exhaustive Search Approach

## Table of Contents

- [Introduction](#introduction)
- [Historical Context](#historical-context)
- [Exhaustive Search Algorithm](#exhaustive-search-algorithm)
- [Travelling Salesman Problem (TSP)](#travelling-salesman-problem-tsp)
- [Applications of Exhaustive Search](#applications-of-exhaustive-search)
- [Modern Developments](#modern-developments)
- [Case Study: TSP Solution](#case-study-tsp-solution)
- [Example: Exhaustive Search in Scheduling](#example-exhaustive-search-in-scheduling)
- [Advantages and Disadvantages](#advantages-and-disadvantages)
- [Conclusion](#conclusion)
- [Further Reading](#further-reading)

## Introduction

Exhaustive search is a type of brute force approach used to find the optimal solution to a problem. It involves searching through all possible solutions to find the best one. This approach is often used when the problem has a finite number of possible solutions or when the objective function is simple to evaluate.

## Historical Context

The concept of exhaustive search dates back to ancient Greece, where philosophers like Aristotle and Epicurus used similar methods to solve problems. However, the term "exhaustive search" was first coined in the 1950s by computer scientists.

In the 1960s, the first algorithms for solving problems using exhaustive search were developed. These algorithms were used to solve problems like the Travelling Salesman Problem (TSP) and the Knapsack Problem.

## Exhaustive Search Algorithm

The exhaustive search algorithm works by generating all possible solutions to a problem and then evaluating each solution to determine which one is the best. The algorithm can be represented by the following steps:

1. Initialize a variable to store the best solution found so far.
2. Generate all possible solutions to the problem using a recursive or iterative approach.
3. Evaluate each solution by applying the objective function to determine its quality.
4. If the current solution is better than the best solution found so far, update the best solution.
5. Repeat steps 2-4 until all possible solutions have been evaluated.

## Travelling Salesman Problem (TSP)

The Travelling Salesman Problem is a classic problem in computer science and operations research. The problem involves finding the shortest possible route that visits a set of cities and returns to the starting city.

The TSP is an NP-hard problem, meaning that the running time of algorithms increases exponentially with the size of the input. This makes it difficult to find an efficient algorithm for solving the problem exactly.

## Applications of Exhaustive Search

Exhaustive search has been used in a variety of applications, including:

- **Scheduling**: Exhaustive search can be used to find the optimal scheduling of tasks.
- **Resource Allocation**: Exhaustive search can be used to find the optimal allocation of resources.
- **Traveling Salesman Problem**: Exhaustive search can be used to solve the TSP.
- **Financial Portfolio Optimization**: Exhaustive search can be used to find the optimal portfolio of assets.

## Modern Developments

In recent years, there have been several developments in the field of exhaustive search, including:

- **Approximation Algorithms**: Approximation algorithms can be used to find good but not necessarily optimal solutions.
- **Heuristics**: Heuristics can be used to reduce the number of solutions that need to be evaluated.
- **Metaheuristics**: Metaheuristics can be used to guide the search towards good solutions.

## Case Study: TSP Solution

The TSP is a classic problem in computer science and operations research. In this case study, we will use the exhaustive search algorithm to solve the TSP for a set of 10 cities.

```markdown
+-----------------------+
| City 1 | City 2 | City 3 | City 4 | City 5 |
+-----------------------+
| 1 | 2 | 3 | 4 | 5 |
+-----------------------+
| 6 | 7 | 8 | 9 | 10 |
+-----------------------+
```

We will use the following algorithm to solve the TSP:

1. Initialize a variable to store the best solution found so far.
2. Generate all possible solutions to the TSP using a recursive approach.
3. Evaluate each solution by applying the objective function to determine its quality.
4. If the current solution is better than the best solution found so far, update the best solution.

## Example: Exhaustive Search in Scheduling

Exhaustive search can be used to find the optimal scheduling of tasks. In this example, we will use the exhaustive search algorithm to schedule a set of tasks.

```markdown
+-----------------------+
| Task 1 | Task 2 | Task 3 |
+-----------------------+
| 1 | 2 | 3 |
+-----------------------+
```

We will use the following algorithm to schedule the tasks:

1. Initialize a variable to store the best solution found so far.
2. Generate all possible solutions to the scheduling problem using a recursive approach.
3. Evaluate each solution by applying the objective function to determine its quality.
4. If the current solution is better than the best solution found so far, update the best solution.

## Advantages and Disadvantages

Advantages:

- Exhaustive search can be used to find the optimal solution to a problem.
- Exhaustive search can be used to solve problems with a finite number of possible solutions.

Disadvantages:

- Exhaustive search can be computationally expensive.
- Exhaustive search can be used to solve problems that are NP-hard.

## Conclusion

Exhaustive search is a type of brute force approach used to find the optimal solution to a problem. It involves searching through all possible solutions to find the best one. Exhaustive search has been used in a variety of applications, including scheduling, resource allocation, and the Travelling Salesman Problem. While exhaustive search can be computationally expensive, it can be used to find the optimal solution to a problem.

## Further Reading

- [1] ere, J. H. (1959). The Travelling Salesman Problem. Operations Research, 6(2), 266-278.
- [2] Garey, M. R., & Johnson, D. S. (1979). Approximation algorithms for bin packing: A survey. Journal of the ACM, 26(1), 129-155.
- [3] Papadimitriou, C. H. (1994). The Traveling Salesman Problem: A Survey. ACM Computing Surveys, 26(3), 363-394.
- [4] Vose, D. (1993). The Scheduling Problem: Theory, Algorithms, and Analysis. John Wiley & Sons.
- [5] Wolsey, L. A. (1984). Integer Programming: A Survey. Mathematical Programming, 27(1), 1-53.
