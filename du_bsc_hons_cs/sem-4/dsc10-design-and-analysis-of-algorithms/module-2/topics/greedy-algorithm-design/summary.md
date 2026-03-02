# Greedy Algorithm Design

## Introduction
Greedy Algorithm is a fundamental design technique in the Design and Analysis of Algorithms (DCA). It makes locally optimal choices at each step with the hope of finding a global optimum solution. This approach is particularly useful for optimization problems where greedy choices lead to optimal solutions.

---

## Key Concepts

### 1. Characteristics of Greedy Algorithms
- **Greedy Choice Property**: Global optimal solution can be reached by making locally optimal choices
- **Optimal Substructure**: An optimal solution contains optimal solutions to subproblems
- **Irrevocability**: Choices made are never reconsidered

### 2. Greedy vs Dynamic Programming
| Greedy | Dynamic Programming |
|--------|---------------------|
| Top-down approach | Bottom-up approach |
| Doesn't re-examine solutions | Examines all possibilities |
| Faster but not always optimal | Always finds optimal solution |
| Memory efficient | Requires more memory |

### 3. Standard Greedy Problems (Delhi University Syllabus)

**Activity Selection Problem**
- Select maximum number of non-conflicting activities
- Sort by finish time, select activities that don't overlap

**Fractional Knapsack Problem**
- Items can be taken partially (0-1 knapsack requires DP)
- Sort by value-to-weight ratio
- Time Complexity: O(n log n)

**Huffman Coding**
- Optimal prefix-free coding
- Uses priority queue (min-heap)
- Builds optimal binary tree for data compression

**Minimum Spanning Tree (MST)**
- **Kruskal's Algorithm**: Sort edges, use Union-Find
- **Prim's Algorithm**: Grow MST from a vertex

**Dijkstra's Algorithm**
- Single-source shortest path
- Works with non-negative weights
- Similar to Prim's MST algorithm

### 4. Algorithm Structure
```
GREEDY-ALGORITHM(problem):
    solution = ∅
    while problem not empty:
        SELECT = choose best candidate (greedy choice)
        if SELECT is feasible:
            solution = solution ∪ SELECT
            remove SELECT from problem
    return solution
```

### 5. Advantages & Limitations

**Advantages:**
- Simple to understand and implement
- Efficient time complexity (often O(n log n))
- Works optimally for certain problems

**Limitations:**
- Not applicable to all problems
- May not always produce optimal solution
- Proof of correctness can be challenging

---

## Conclusion
Greedy algorithms provide efficient solutions for optimization problems exhibiting greedy choice and optimal substructure properties. Mastery of standard problems like activity selection, fractional knapsack, MST, and Huffman coding is essential for the DCA paper under Delhi University NEP 2024 syllabus. Practice is key to identifying when greedy approach yields optimal results.

**Exam Tip**: Remember—greedy works when local optimal leads to global optimal!