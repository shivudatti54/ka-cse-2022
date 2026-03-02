# Union Find Data Structures

## Introduction
Union Find (or Disjoint Set Union - DSU) is a fundamental data structure in computer science that tracks a set of elements partitioned into disjoint (non-overlapping) subsets. It efficiently supports two primary operations: **Find** (determines which subset an element belongs to) and **Union** (merges two subsets into one). This data structure is crucial for solving problems involving connectivity and grouping.

---

## Key Concepts

### Core Operations
- **MakeSet(x)**: Creates a new singleton set containing element x
- **Find(x)**: Returns the representative (root) of the set containing x
- **Union(x, y)**: Merges the sets containing elements x and y

### Representation
- Each element points to a parent pointer forming a **forest** (collection of trees)
- Each tree represents one disjoint set
- The root of each tree serves as the **representative** of that set
- Initially, each element is its own parent (self-loop)

### Optimization Techniques

**Path Compression** (for Find operation):
- During Find, compress the path by making every node point directly to the root
- Significantly improves performance for subsequent operations

**Union by Rank/Size**:
- Attach the smaller tree under the root of the larger tree
- **Rank**: Approximate tree height
- **Size**: Number of elements in the tree
- Balances the tree structure, preventing degeneration

---

## Time Complexity
| Operation | Without Optimization | With Both Optimizations |
|-----------|---------------------|------------------------|
| Find      | O(n)                | α(n) ≈ O(1) amortized  |
| Union     | O(n)                | α(n) ≈ O(1) amortized  |

*α(n) is the inverse Ackermann function, practically constant for all real inputs*

---

## Applications
- **Kruskal's Algorithm**: For finding Minimum Spanning Tree (MST)
- **Cycle Detection**: In undirected graphs
- **Image Processing**: Connected component labeling
- **Network Connectivity**: Social networks, peer-to-peer networks
- **Equivalence Relations**: Testing element connectivity
- **Quiz/Game Problems**: Grouping connected elements

---

## Conclusion
Union Find is an elegant and efficient data structure essential for handling dynamic connectivity problems. Its near-constant time operations (with path compression and union by rank) make it indispensable in graph algorithms, particularly in Kruskal's MST and cycle detection. Mastery of this topic is vital for the Delhi University syllabus covering graph theory and advanced data structures.

---

*Relevant for: Unit III - Graph Algorithms & Advanced Data Structures (UGCF NEP 2024)*