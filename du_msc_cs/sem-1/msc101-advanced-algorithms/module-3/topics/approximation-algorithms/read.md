# Comprehensive Study Material: Approximation Algorithms

## Advanced Algorithms - MSc CS, Delhi University

---

## 1. Introduction and Real-World Relevance

### What are Approximation Algorithms?

Approximation algorithms are efficient algorithms that find near-optimal solutions to NP-hard optimization problems. Instead of guaranteeing the optimal solution (which would require impractical computation time), these algorithms provide solutions with a provable quality guarantee, expressed as a ratio bound relative to the optimal solution.

### Why Do We Need Approximation Algorithms?

In the real world, numerous optimization problems are NP-hard, meaning there is no known polynomial-time algorithm to solve them exactly. Consider these scenarios:

- **Route Planning**: A delivery company needs to find the shortest route to deliver packages to 1000 customers — this is the Traveling Salesman Problem (TSP).
- **Resource Allocation**: A cloud computing provider must allocate virtual machines to physical servers efficiently — this relates to bin packing.
- **Network Design**: Building a network that connects all cities with minimum cost — this is the Steiner Tree problem.
- **Scheduling**: Assigning tasks to processors to minimize total completion time — this is load balancing.

For large instances of these problems, even the most powerful computers cannot find optimal solutions in reasonable time. Approximation algorithms bridge this gap by providing **provably good** solutions efficiently.

### The Approximation Ratio

For a minimization problem, an algorithm has approximation ratio α if for every input instance, the algorithm produces a solution with cost at most α × OPT (where OPT is the optimal cost). For maximization problems, the solution is at least (1/α) × OPT.

---

## 2. Fundamental Concepts

### Classification of Problems by Approximability

| Class | Description | Examples |
|-------|-------------|----------|
| **APX** | Problems with constant-factor approximations | Vertex Cover, TSP (metric) |
| **PTAS** | Problems admitting (1-ε)-approximation for any ε | Knapsack, Bin Packing |
| **FPTAS** | PTAS with runtime polynomial in both n and 1/ε | Knapsack (pseudo-polynomial → FPTAS) |
| **NPO-PB** | Problems with polynomial-time approximation schemes | Many scheduling problems |
| **APX-Hard** | Problems unlikely to have constant-factor approximations | Set Cover (log n hardness) |

### Key Theorem: No Free Lunch

It is impossible to approximate every NP-hard problem well. The ** PCP Theorem** and **Hardness of Approximation** results show that for many problems, achieving better approximation ratios is as hard as solving NP-hard problems exactly.

---

## 3. Classic Approximation Algorithms

### 3.1 Vertex Cover Problem

**Problem**: Given a graph G = (V, E), find the smallest subset of vertices such that every edge has at least one endpoint in the subset.

**2-Approximation Algorithm**:

```python
def vertex_cover_approx(graph):
    """
    2-approximation for Vertex Cover using maximal matching.
    
    Args:
        graph: Adjacency list representation {vertex: [neighbors]}
    
    Returns:
        Set of vertices forming the vertex cover
    """
    vertex_cover = set()
    edges_remaining = set()
    
    # Initialize all edges
    for u in graph:
        for v in graph[u]:
            if u < v:  # Avoid duplicates
                edges_remaining.add((u, v))
    
    # Find maximal matching greedily
    matching = set()
    for (u, v) in list(edges_remaining):
        if (u, v) not in matching and (v, u) not in matching:
            # Check if u and v are already matched
            matched = False
            for (a, b) in matching:
                if u == a or u == b or v == a or v == b:
                    matched = True
                    break
            if not matched:
                matching.add((u, v))
                # Remove all edges incident to u and v
                edges_remaining = {e for e in edges_remaining 
                                   if u not in e and v not in e}
    
    # Add both endpoints of each matched edge to vertex cover
    for (u, v) in matching:
        vertex_cover.add(u)
        vertex_cover.add(v)
    
    return vertex_cover

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

cover = vertex_cover_approx(graph)
print(f"Approximate Vertex Cover: {cover}")
```

**Analysis**:
- Let M be the maximal matching found
- Every edge in M is covered by at least one vertex in any vertex cover
- Therefore, |VC| ≥ |M| (any vertex cover must cover all matching edges)
- Our algorithm returns 2|M| vertices
- Thus, |VC_approx| ≤ 2 × |VC_opt|

### 3.2 Set Cover Problem

**Problem**: Given a universe U of elements and a collection S of subsets, find the minimum number of subsets whose union covers all elements in U.

**Greedy Algorithm (ln n - Approximation)**:

```python
import math

def greedy_set_cover(universe, subsets):
    """
    Greedy ln(n)-approximation for Set Cover.
    
    Args:
        universe: Set of elements to cover
        subsets: Dictionary {subset_name: set_of_elements}
    
    Returns:
        Selected subsets and total cost
    """
    covered = set()
    selected = []
    n = len(universe)
    
    while covered != universe:
        best_subset = None
        max_new_elements = 0
        
        # Find subset covering most uncovered elements
        for name, elements in subsets.items():
            new_elements = elements - covered
            if len(new_elements) > max_new_elements:
                max_new_elements = len(new_elements)
                best_subset = name
        
        if best_subset is None:
            break  # Cannot cover remaining elements
            
        selected.append(best_subset)
        covered |= subsets[best_subset]
    
    return selected, len(selected)

# Example
universe = {1, 2, 3, 4, 5}
subsets = {
    'S1': {1, 2, 3},
    'S2': {2, 4},
    'S3': {3, 4, 5},
    'S4': {5}
}

covers, cost = greedy_set_cover(universe, subsets)
print(f"Selected subsets: {covers}")
print(f"Approximation ratio bound: O(log {len(universe)}) = O(log {len(universe)})")
```

**Hardness Result**: Set Cover cannot be approximated better than ln(n) unless P = NP (Dinur-Steurer, 2014).

### 3.3 Metric Traveling Salesman Problem (TSP)

**Problem**: Given a complete graph with edge weights satisfying the triangle inequality, find the shortest Hamiltonian cycle.

**2-Approximation Algorithm** (using Minimum Spanning Tree):

```python
import heapq

def mst_prim(vertices, edges):
    """
    Compute MST using Prim's algorithm.
    
    Args:
        vertices: List of vertices
        edges: Dict {(u, v): weight}
    
    Returns:
        List of edges in MST
    """
    if not vertices:
        return []
    
    in_mst = {vertices[0]}
    mst_edges = []
    pq = []
    
    # Initialize priority queue with edges from first vertex
    for v in vertices[1:]:
        w = edges.get((vertices[0], v), float('inf'))
        heapq.heappush(pq, (w, vertices[0], v))
    
    while pq and len(mst_edges) < len(vertices) - 1:
        weight, u, v = heapq.heappop(pq)
        
        if v in in_mst:
            continue
        
        in_mst.add(v)
        mst_edges.append((u, v, weight))
        
        # Add edges from new vertex
        for w in vertices:
            if w not in in_mst:
                edge_weight = edges.get((v, w), float('inf'))
                heapq.heappush(pq, (edge_weight, v, w))
    
    return mst_edges

def metric_tsp_approx(vertices, edges):
    """
    2-approximation for Metric TSP using MST doubling.
    
    Args:
        vertices: List of vertices
        edges: Dict {(u, v): weight} satisfying triangle inequality
    
    Returns:
        Tour and total cost
    """
    # Step 1: Compute MST
    mst = mst_prim(vertices, edges)
    
    # Step 2: Walk around MST (preorder traversal)
    # This gives a cycle visiting each vertex at least once
    visited = set()
    tour = []
    
    def dfs_visit(v):
        visited.add(v)
        tour.append(v)
        for u, w, edge in mst:
            if u == v and w not in visited:
                dfs_visit(w)
            elif w == v and u not in visited:
                dfs_visit(u)
    
    if vertices:
        dfs_visit(vertices[0])
    
    # Step 3: Shortcut repeated vertices (triangle inequality ensures this doesn't increase cost)
    final_tour = [tour[0]]
    for i in range(1, len(tour)):
        if tour[i] != final_tour[-1]:
            final_tour.append(tour[i])
    final_tour.append(final_tour[0])  # Return to start
    
    # Calculate cost
    total_cost = sum(edges.get((final_tour[i], final_tour[i+1]), 
                                edges.get((final_tour[i+1], final_tour[i]), float('inf'))) 
                     for i in range(len(final_tour) - 1))
    
    return final_tour, total_cost

# Example
vertices = ['A', 'B', 'C', 'D']
# Complete graph with triangle inequality
edges = {
    ('A', 'B'): 10, ('B', 'A'): 10,
    ('A', 'C'): 15, ('C', 'A'): 15,
    ('A', 'D'): 20, ('D', 'A'): 20,
    ('B', 'C'): 35, ('C', 'B'): 35,
    ('B', 'D'): 25, ('D', 'B'): 25,
    ('C', 'D'): 30, ('D', 'C'): 30
}

tour, cost = metric_tsp_approx(vertices, edges)
print(f"Approximate TSP tour: {tour}")
print(f"Cost: {cost}")
```

**Analysis**: The MST forms a spanning tree. A depth-first walk of the MST visits each vertex at least once. Using shortcuts (triangle inequality), we get a Hamiltonian cycle of cost at most 2 × OPT.

### 3.4 Bin Packing Problem

**Problem**: Pack items of given sizes into minimum number of bins of fixed capacity.

**First-Fit Decreasing Algorithm**:

```python
def first_fit_decreasing(items, capacity):
    """
    First-Fit Decreasing bin packing - achieves ~11/9 OPT ≈ 1.22 ratio
    asymptotically. First-Fit achieves ~1.7 ratio.
    
    Args:
        items: List of item sizes
        capacity: Bin capacity
    
    Returns:
        Number of bins used
    """
    items_sorted = sorted(items, reverse=True)
    bins = []
    
    for item in items_sorted:
        placed = False
        
        for bin_items in bins:
            if sum(bin_items) + item <= capacity:
                bin_items.append(item)
                placed = True
                break
        
        if not placed:
            bins.append([item])
    
    return len(bins)

# Example
items = [4, 3, 2, 5, 1, 3, 4, 2]
capacity = 6

num_bins = first_fit_decreasing(items, capacity)
print(f"Number of bins: {num_bins}")
```

**Important Clarification**: The First-Fit algorithm has an approximation ratio of approximately 1.7 (not exactly 2), while First-Fit Decreasing achieves approximately 1.22 asymptotically.

### 3.5 Knapsack Problem (FPTAS)

**Problem**: Given items with weights and values, maximize total value subject to weight capacity.

**Fully Polynomial-Time Approximation Scheme (FPTAS)**:

```python
def knapsack_fptas(items, capacity, epsilon):
    """
    FPTAS for 0/1 Knapsack.
    
    Runtime: O(n^3 / epsilon)
    Approximation: (1 + epsilon)-approximation
    
    Args:
        items: List of (weight, value) tuples
        capacity: Maximum weight
        epsilon: Error parameter (0 < epsilon <= 1)
    
    Returns:
        Maximum value achievable
    """
    n = len(items)
    if n == 0:
        return 0
    
    # Find maximum value
    max_value = max(v for w, v in items)
    
    # Scale values to reduce number of distinct values
    # Using K = (epsilon * max_value) / n
    K = (epsilon * max_value) / n
    
    scaled_values = [max(1, int(v / K)) for w, v in items]
    
    # Dynamic programming on scaled values
    # Number of possible scaled values is at most n/epsilon
    max_scaled = max(scaled_values)
    
    # DP table: dp[j] = minimum weight to achieve scaled value j
    dp = [float('inf')] * (max_scaled + 1)
    dp[0] = 0
    
    for i, (w, v) in enumerate(items):
        scaled_v = scaled_values[i]
        # Process in reverse to avoid using item multiple times
        for j in range(max_scaled, scaled_v - 1, -1):
            if dp[j - scaled_v] != float('inf'):
                dp[j] = min(dp[j], w + dp[j - scaled_v])
    
    # Find best achievable value
    best_scaled = 0
    for j in range(max_scaled + 1):
        if dp[j] <= capacity:
            best_scaled = j
    
    # Convert back to actual value
    # Actual value >= K * best_scaled - max_value * epsilon
    # But we return a conservative estimate
    actual_value = K * best_scaled
    
    return actual_value

# Example
items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
capacity = 50
epsilon = 0.1  # 10% error

result = knapsack_fptas(items, capacity, epsilon)
print(f"Approximate maximum value: {result}")
print(f"Approximation ratio: at most 1.1")
```

**Key Insight**: The FPTAS scales down the values to create a smaller DP table while guaranteeing (1+ε)-approximation.

---

## 4. Hardness of Approximation

Understanding which problems cannot be approximated well is crucial:

### PCP Theorem
The PCP (Probabilistically Checkable Proof) theorem states that NP = PCP(log n, O(1)), which implies that many optimization problems cannot be approximated arbitrarily well unless P = NP.

### Key Hardness Results

| Problem | Best Known Approximation | Lower Bound (unless P=NP) |
|---------|--------------------------|---------------------------|
| Vertex Cover | 2 | 2 - ε |
| Set Cover | ln n | (1 - o(1)) ln n |
| TSP (metric) | 1.5 (Christofides) | 1.0001 |
| Knapsack | FPTAS | No FPTAS if P≠NP (but we have it!) |
| Max-Cut | 0.878 (Goemans-Williamson) | 0.878 |

### Gap Preservation
Approximation hardness often comes from **gap-preserving reductions**: showing that distinguishing between solutions within a small factor gap is NP-hard.

---

## 5. Delhi University Syllabus Context

Based on the MSc CS syllabus for Advanced Algorithms (July 2025), this unit covers:

1. **Conceptual Foundation**: Need for approximation algorithms, polynomial-time approximation schemes (PTAS, FPTAS)
2. **Classical Algorithms**: Vertex Cover, Set Cover, Knapsack, Bin Packing, TSP
3. **Analysis Techniques**: Greedy methods, local search, linear programming rounding
4. **Hardness of Approximation**: Understanding the limits

**Recommended References**:
- Vazirani, V. V. — "Approximation Algorithms"
- Williamson & Shmoys — "The Design of Approximation Algorithms"
- Cormen et al. — "Introduction to Algorithms" (Chapter 35)

---

## 6. Challenging MCQs

### Multiple Choice Questions

1. **Consider the vertex cover approximation algorithm that returns twice the size of a maximal matching. What is the worst-case approximation ratio?**

   a) 1.5
   b) **2**
   c) log n
   d) n

2. **Which of the following statements about Set Cover is FALSE?**

   a) The greedy algorithm provides an O(log n) approximation
   b) Set Cover is APX-hard
   c) **Set Cover has a constant-factor approximation algorithm**
   d) It is hard to approximate better than ln n

3. **The metric TSP 2-approximation algorithm uses which of the following as a key structure?**

   a) **Minimum Spanning Tree**
   b) Maximum Matching
   c) Vertex Cover
   d) Independent Set

4. **For the Knapsack problem, which type of approximation scheme is known to exist?**

   a) PTAS only
   b) **FPTAS**
   c) Constant-factor approximation
   d) No approximation algorithm exists

5. **What is the asymptotic approximation ratio of First-Fit Decreasing for Bin Packing?**

   a) Exactly 2
   b) **Approximately 1.22 (11/9)**
   c) 1.5
   d) log n

6. **Which theorem provides the foundation for hardness of approximation results?**

   a) Cook-Levin Theorem
   b) **PCP Theorem**
   c) Kuratowski's Theorem
   d) Menger's Theorem

7. **In a maximization problem, an α-approximation algorithm guarantees:**

   a) Solution ≤ α × OPT
   b) **Solution ≥ (1/α) × OPT**
   c) Solution = OPT
   d) Solution ≥ α × OPT

8. **The FPTAS for Knapsack achieves what approximation ratio?**

   a) 2
   b) 1.5
   c) **1 + ε (for any ε > 0)**
   d) log n

---

## 7. Advanced Flashcards

### Flashcard 1
**Q:** Why is the greedy algorithm for Set Cover not a constant-factor approximation?

**A:** The greedy algorithm chooses the set covering the most uncovered elements at each step. This results in a logarithmic approximation ratio because the number of elements covered grows multiplicatively, leading to a logarithmic number of sets needed in the worst case. The lower bound of ln(n) has been proven, making O(log n) essentially optimal (unless P = NP).

### Flashcard 2
**Q:** Explain why the metric TSP can be approximated but general TSP cannot.

**A:** Metric TSP satisfies the triangle inequality (distances form a metric space), allowing us to use shortcuts without increasing total cost. The 2-approximation via MST works because we can always shortcut the depth-first walk. General TSP without the metric property has no polynomial-time approximation algorithm (ratio grows with n), as even distinguishing between tours of cost ≤ n and > (1+ε)n is NP-hard.

### Flashcard 3
**Q:** What is the key insight behind the FPTAS for Knapsack?

**A:** The knapsack problem has pseudo-polynomial dynamic programming (O(nW) where W is capacity). The FPTAS scales down the values using K = (ε × V_max) / n, reducing the number of distinct scaled values to O(n/ε). This makes the DP table size polynomial in both n and 1/ε while guaranteeing (1 + ε)-approximation.

### Flashcard 4
**Q:** Why does the 2-approximation for Vertex Cover via maximal matching guarantee a bound?

**A:** Let M be a maximal matching (no two edges can be added without sharing vertices). Any vertex cover must contain at least one endpoint of each edge in M, so |OPT| ≥ |M|. Our algorithm returns all vertices in M, giving |ALG| = 2|M| ≤ 2|OPT|.

### Flashcard 5
**Q:** Distinguish between PTAS and FPTAS.

**A:** Both guarantee (1 + ε)-approximation. The difference is runtime dependence on 1/ε:
- PTAS: Runtime polynomial in n for each fixed ε, but may be exponential in 1/ε
- FPTAS: Runtime polynomial in both n and 1/ε

FPTAS is stronger and exists for Knapsack. Not all PTAS problems admit FPTAS (this would imply fully polynomial-time solution even for exact case in some sense).

---

## 8. Key Takeaways

1. **Approximation algorithms** provide efficient near-optimal solutions to NP-hard problems with provable quality guarantees.

2. **Approximation ratios** express how close the algorithm's solution is to optimal:
   - Constant-factor (2-approximation, 1.5-approximation)
   - Asymptotic (for bin packing)
   - Polynomial-time approximation schemes (PTAS, FPTAS)

3. **Vertex Cover** has a simple 2-approximation using maximal matching; this is essentially tight (2 - ε approximation is NP-hard).

4. **Set Cover** can be approximated to within O(log n) using a greedy algorithm, and this is optimal unless P = NP.

5. **Metric TSP** admits a 2-approximation using MST; Christofides' algorithm improves this to 1.5.

6. **Knapsack** has an FPTAS achieving (1 + ε)-approximation in O(n³/ε) time.

7. **Bin Packing** achieves ~1.22 asymptotically with First-Fit Decreasing; First-Fit achieves ~1.7 (not 2 as commonly mistaken).

8. **2-opt is a local search heuristic**, not a guaranteed approximation algorithm — it may get stuck in local optima with unbounded ratio from OPT.

9. **Hardness of approximation** (via PCP theorem) shows that some problems cannot be approximated arbitrarily well, establishing fundamental limits.

10. **Approximation algorithms are essential** in practice for solving large-scale optimization problems where exact solutions are computationally infeasible.

---

*Prepared for MSc CS, Delhi University - Advanced Algorithms Course*
*Reference: Vazirani's Approximation Algorithms; Williamson & Shmoys*