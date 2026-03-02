# Travelling Salesman Problem

## Introduction

The Travelling Salesman Problem (TSP) stands as one of the most famous and extensively studied problems in computer science and operations research. It belongs to the class of NP-hard optimization problems, meaning there is no known polynomial-time algorithm to solve it exactly for large instances. The problem asks a deceptively simple question: Given a set of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the starting city?

The TSP has profound practical applications in logistics, transportation, manufacturing, and DNA sequencing. Delivery companies use TSP concepts to optimize delivery routes, airlines apply similar principles for crew scheduling, and even genome sequencing algorithms draw from TSP research. Understanding TSP is essential for any computer science student because it introduces fundamental concepts in algorithm design, complexity theory, and optimization techniques that appear repeatedly throughout the field.

This topic is particularly important for the university's Graph Theory syllabus (BCS405B, Module 2) as it demonstrates how graph theory concepts like Hamiltonian cycles and weighted graphs apply to real-world optimization problems. The study of TSP also introduces students to various problem-solving approaches including brute force, heuristics, approximation algorithms, and dynamic programming.

## Key Concepts

### Definition and Mathematical Formulation

The Travelling Salesman Problem can be formally defined as follows: Given a complete weighted graph G = (V, E) with n vertices (cities) and edge weights w(i,j) representing distances between cities, find a Hamiltonian cycle (a cycle that visits each vertex exactly once) with minimum total weight.

Mathematically, we seek to minimize:

$$\sum_{i=1}^{n} \sum_{j=1, j \neq i}^{n} x_{ij} \cdot w_{ij}$$

subject to the constraint that each city is visited exactly once, where x\_{ij} = 1 if the route goes from city i to city j, and 0 otherwise.

### Complete Graph and Metric TSP

In the standard TSP formulation, we assume a complete graph where every pair of vertices is connected by an edge. This represents the real-world scenario where one can travel directly between any two cities (possibly through intermediate connections).

The Metric TSP is a special case where the distance function satisfies the triangle inequality: d(i,j) + d(j,k) ≥ d(i,k) for all cities i, j, k. This is a realistic assumption for most practical applications, as taking a indirect route should never be shorter than the direct route.

### Hamiltonian Cycle

A Hamiltonian cycle is a fundamental concept in TSP. It is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. Not all graphs contain Hamiltonian cycles, but complete graphs always do. The TSP problem is essentially asking us to find the minimum weight Hamiltonian cycle in a weighted complete graph.

### Exact Solution Methods

**Brute Force Approach**: For n cities, there are (n-1)! possible routes (considering we fix the starting city). This becomes computationally infeasible even for moderate values of n (beyond 15-20 cities).

**Dynamic Programming (Held-Karp Algorithm)**: The Held-Karp algorithm solves TSP in O(n² × 2^n) time using dynamic programming. This is significantly better than brute force but still exponential. The approach builds solutions by considering subsets of cities and computing optimal costs for each subset ending at each city.

The recurrence relation is:

- Let dp(S, i) represent the minimum cost to visit all cities in set S, ending at city i
- Base case: dp({j}, j) = distance(start, j)
- Transition: dp(S ∪ {k}, k) = min(dp(S, j) + distance(j, k)) for all j in S

### Heuristic Methods

**Nearest Neighbor Heuristic**: This is a simple greedy algorithm that always visits the nearest unvisited city. Starting from a city, repeatedly choose the closest unvisited city until all cities are visited, then return to the starting city. While fast, it does not guarantee optimality.

**Multi-Fragment Heuristic**: An improvement over nearest neighbor, this algorithm sorts all edges by weight and adds edges if they don't create a degree-2 vertex or a cycle until a Hamiltonian cycle is formed.

**2-Opt Improvement**: Starting from any tour, repeatedly swap two edges if the swap reduces total cost. This is a local search technique that improves any initial solution.

### Approximation Algorithms

For Metric TSP, the Double MST (or 2-approximation) algorithm provides a solution within twice the optimal cost. The algorithm:

1. Find a Minimum Spanning Tree (MST) of the graph
2. Perform a preorder walk of the MST
3. Shortcut repeated vertices (using triangle inequality)

Another important result is that for Metric TSP, the Christofides algorithm provides a 3/2-approximation, though it is more complex to implement.

### Branch and Bound

Branch and bound is a systematic method for finding optimal solutions to combinatorial optimization problems. For TSP:

- **Branching**: Divide the problem into subproblems by fixing which edge goes out of the current city
- **Bounding**: Compute a lower bound for each subproblem (often using the reduced cost matrix or 1-tree bound)
- **Pruning**: Discard subproblems whose lower bound exceeds the best solution found so far

## Examples

### Example 1: Solving TSP using Dynamic Programming

Consider 4 cities (1, 2, 3, 4) with the following distance matrix:

```
 1 2 3 4
1 0 10 15 20
2 10 0 35 25
3 15 35 0 30
4 20 25 30 0
```

Solve starting from city 1 using dynamic programming.

**Solution:**

We compute dp(S, i) for all subsets S containing city 1 and ending at city i.

Step 1: Base cases (subsets of size 1)

- dp({1,2}, 2) = distance(1,2) = 10
- dp({1,3}, 3) = distance(1,3) = 15
- dp({1,4}, 4) = distance(1,4) = 20

Step 2: Subsets of size 2

- dp({1,2,3}, 3) = min(dp({1,2},2) + distance(2,3), dp({1,2},1) + distance(1,3))
- But dp({1,2},1) is undefined (must end at 2), so: 10 + 35 = 45
- dp({1,2,4}, 4) = dp({1,2},2) + distance(2,4) = 10 + 25 = 35
- dp({1,3,4}, 4) = dp({1,3},3) + distance(3,4) = 15 + 30 = 45
- Similarly compute for all size-2 subsets ending at each city

Step 3: Subset of size 3

- dp({1,2,3,4}, 4) = min of paths through 2 and 3
- Through 2: dp({1,2,3}, 3) + distance(3,4) = 45 + 30 = 75
- Through 3: dp({1,2,4}, 4) + distance(4,4)... wait, distance(4,4) = 0

Actually, let's recalculate systematically:

- dp({1,2,3,4}, 4) = min(dp({1,2,3}, 2) + distance(2,4), dp({1,2,3}, 3) + distance(3,4))

We need dp({1,2,3}, 2) = min(dp({1,2},1) + distance(1,2), dp({1,2},2) + distance(2,2)) — undefined cases

Better approach: For {1,2,3,4}, we must compute min cost to visit all and end at each intermediate city first.

Let me recalculate properly:

Base: dp({1,2}, 2) = 10, dp({1,3}, 3) = 15, dp({1,4}, 4) = 20

Size 2 (ending at city):

- dp({1,2,3}, 2) = dp({1,3}, 3) + d(3,2) = 15 + 35 = 50
- dp({1,2,3}, 3) = dp({1,2}, 2) + d(2,3) = 10 + 35 = 45
- dp({1,2,4}, 2) = dp({1,4}, 4) + d(4,2) = 20 + 25 = 45
- dp({1,2,4}, 4) = dp({1,2}, 2) + d(2,4) = 10 + 25 = 35
- dp({1,3,4}, 3) = dp({1,4}, 4) + d(4,3) = 20 + 30 = 50
- dp({1,3,4}, 4) = dp({1,3}, 3) + d(3,4) = 15 + 30 = 45

Size 3:

- dp({1,2,3,4}, 4) going via 2: dp({1,2,3}, 2) + d(2,4) = 50 + 25 = 75
- dp({1,2,3,4}, 4) going via 3: dp({1,2,3}, 3) + d(3,4) = 45 + 30 = 75
- dp({1,2,3,4}, 3) going via 2: dp({1,2,4}, 2) + d(2,3) = 45 + 35 = 80
- dp({1,2,3,4}, 3) going via 4: dp({1,2,4}, 4) + d(4,3) = 35 + 30 = 65
- dp({1,2,3,4}, 2) going via 3: dp({1,3,4}, 3) + d(3,2) = 50 + 35 = 85
- dp({1,2,3,4}, 2) going via 4: dp({1,3,4}, 4) + d(4,2) = 45 + 25 = 70

Full tour cost = min(dp({1,2,3,4}, 2) + d(2,1), dp({1,2,3,4}, 3) + d(3,1), dp({1,2,3,4}, 4) + d(4,1))

- Via 2: 70 + 10 = 80
- Via 3: 65 + 15 = 80
- Via 4: 75 + 20 = 95

Optimal cost = 80

### Example 2: Nearest Neighbor Heuristic

Using the same distance matrix, apply the nearest neighbor heuristic starting from city 1.

**Solution:**

Step 1: Start at city 1. Unvisited cities: {2,3,4}. Nearest: city 2 (distance = 10). Route: 1 → 2

Step 2: At city 2. Unvisited: {3,4}. Nearest: city 4 (distance = 25). Route: 1 → 2 → 4

Step 3: At city 4. Unvisited: {3}. Only choice: city 3 (distance = 30). Route: 1 → 2 → 4 → 3

Step 4: Return to city 1. Distance = 15. Final route: 1 → 2 → 4 → 3 → 1

Total cost = 10 + 25 + 30 + 15 = 80

Note: The nearest neighbor heuristic found the optimal solution in this case, but this is not guaranteed.

### Example 3: Branch and Bound Concept

For a small 3-city TSP with distances: d(1,2)=10, d(2,3)=15, d(3,1)=20.

**Solution:**

The possible tours are:

- 1 → 2 → 3 → 1: 10 + 15 + 20 = 45
- 1 → 3 → 2 → 1: 20 + 15 + 10 = 45

For branch and bound:

- Root node: no edges fixed
- Branch on first edge choice (1→2 or 1→3)
- Compute lower bounds using reduced cost matrices
- Prune branches that cannot beat current best

The lower bound can be computed by summing half the sum of the two smallest edges connected to each vertex, adjusted for the matrix reduction.

## Exam Tips

1. **Understand the problem definition clearly**: Know that TSP seeks a minimum weight Hamiltonian cycle in a complete weighted graph visiting each vertex exactly once.

2. **Know the difference between Hamiltonian cycle and Eulerian circuit**: A Hamiltonian cycle visits each vertex exactly once; an Eulerian circuit traverses each edge exactly once. This is a common exam confusion.

3. **Master the dynamic programming solution**: The Held-Karp algorithm is a favorite in university exams. Remember the recurrence relation and understand how to build solutions incrementally.

4. **Remember time complexities**: Know that brute force is O(n!), dynamic programming is O(n² × 2^n), and why these matter for practical computation.

5. **Heuristics don't guarantee optimality**: When answering questions about heuristic methods, always mention that they provide good solutions but not necessarily optimal ones.

6. **Know the approximation ratios**: For Metric TSP, MST-based approximation gives a 2-approximation, and Christofides gives 1.5-approximation. These are important theoretical results.

7. **Application contexts**: Be prepared to explain practical applications of TSP in logistics, routing, and scheduling to demonstrate understanding of real-world relevance.

8. **NP-hardness**: Understand that TSP is NP-hard, meaning there is no known polynomial-time algorithm for exact solution, which motivates the study of heuristics and approximations.
