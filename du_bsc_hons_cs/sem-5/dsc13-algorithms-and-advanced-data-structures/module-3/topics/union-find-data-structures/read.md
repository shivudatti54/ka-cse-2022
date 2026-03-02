# Union Find Data Structures

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Union Find** (also known as **Disjoint Set Union** or **DSU**) is a fundamental data structure in computer science that maintains a collection of disjoint (non-overlapping) sets. It supports two primary operations:

- **Find**: Determines which set a particular element belongs to
- **Union**: Merges two sets into a single set

This data structure is particularly useful for solving problems involving connectivity, clustering, and equivalence relations. The Union Find data structure is a critical component in many algorithmic solutions and is explicitly mentioned in the Delhi University BSc (Hons) Computer Science syllabus under the topic "Algorithms And Advanced Data Structures" (NEP 2024 UGCF).

The beauty of Union Find lies in its simplicity and efficiency. With proper optimizations (path compression and union by rank), it achieves almost constant time complexity for its operations, making it one of the most efficient data structures for dynamic connectivity problems.

---

## 2. Real-World Relevance and Applications

Understanding Union Find is essential because it appears in numerous practical applications:

### 2.1 Network Connectivity
- **Social Networks**: Determining if two users are connected through a network of friends
- **Computer Networks**: Checking connectivity between computers in a distributed system
- **Road Networks**: Determining if there's a path between two cities

### 2.2 Image Processing
- **Connected Component Labeling**: Identifying distinct objects in digital images
- **Pixel Clustering**: Grouping related pixels for image segmentation

### 2.3 Game Development
- **Kruskal's Algorithm**: Used in minimum spanning tree algorithms for generating game maps
- **Clustering**: Grouping game entities for efficient collision detection

### 2.4 Database Systems
- **Equivalence Queries**: Maintaining and querying equivalence relations in databases
- **Union of Tables**: Tracking merged database tables

### 2.5 Miscellaneous Applications
- **Dependency Resolution**: Managing package dependencies in software installation
- **Hypothesis Testing**: Used in statistical analysis for clustering observations
- **Maze Generation**: Creating and solving mazes using union operations

---

## 3. Basic Concepts

### 3.1 What is a Disjoint Set?

A **disjoint set** is a collection of sets where no element appears in more than one set. In other words, the sets are mutually exclusive and collectively exhaustive (every element belongs to exactly one set).

For example, if we have elements {1, 2, 3, 4, 5}, we could have:
- Set A = {1, 2, 3}
- Set B = {4, 5}

These are disjoint sets because no element appears in both sets.

### 3.2 The Union Find Data Structure

Union Find maintains a partition of elements into disjoint sets. It supports:

| Operation | Description | Time Complexity (Basic) |
|-----------|-------------|-------------------------|
| **MakeSet(x)** | Creates a new set containing only element x | O(1) |
| **Find(x)** | Returns the representative (root) of the set containing x | O(n) |
| **Union(x, y)** | Merges the sets containing elements x and y | O(n) |

### 3.3 Representative Element (Root)

Each set in Union Find has a **representative element** (also called the root or parent). This is typically the first element of the set, and we use it to identify which set an element belongs to. The Find operation returns this representative.

---

## 4. Data Structure Representation

Union Find can be implemented using:

### 4.1 Array-Based Representation

The most common and efficient implementation uses an array called `parent[]`:

- **parent[i]**: Stores the parent of element i
- If `parent[i] = i`, then i is the representative (root) of its set

```
Initial State (5 elements, each in its own set):
Index:     0   1   2   3   4
parent:  [ 0,  1,  2,  3,  4 ]
           ↓   ↓   ↓   ↓   ↓
Sets:    {0} {1} {2} {3} {4}
```

After Union(0, 1), Union(2, 3), Union(0, 2):
```
Index:     0   1   2   3   4
parent:  [ 1,  1,  3,  3,  4 ]
           ↓   ↓   ↓   ↓   ↓
Sets:    {0,1,2,3} {4}
```

---

## 5. Implementation Details

### 5.1 Basic Implementation (Without Optimizations)

This is the simplest form of Union Find, but it's inefficient for large datasets:

```python
class UnionFindBasic:
    def __init__(self, n):
        """Initialize n isolated sets."""
        self.parent = list(range(n))
    
    def find(self, x):
        """Find the representative of the set containing x."""
        if self.parent[x] != x:
            # Keep going until we find the root
            return self.find(self.parent[x])
        return x
    
    def union(self, x, y):
        """Unite the sets containing x and y."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Make one root point to the other
            self.parent[root_x] = root_y
    
    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)
```

**Problems with Basic Implementation:**
- Find operation can traverse a long chain of parents
- Creates unbalanced trees in worst case
- Time complexity degrades to O(n) per operation

---

### 5.2 Optimized Implementation (With Path Compression and Union by Rank)

This is the industry-standard implementation that achieves near-constant time complexity:

```python
class UnionFindOptimized:
    def __init__(self, n):
        """Initialize n isolated sets."""
        self.parent = list(range(n))
        self.rank = [0] * n  # Rank is used for union by rank
    
    def find(self, x):
        """Find with path compression."""
        if self.parent[x] != x:
            # Path compression: make every node point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Union by rank: attach smaller tree under larger tree
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                # Same rank: choose one as root and increment its rank
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
    
    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == root_y
```

### 5.3 Alternative: Union by Size

Instead of rank, we can use size to determine which tree to attach:

```python
class UnionFindBySize:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  # Track size of each tree
    
    def find(self, x):
        """Find with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        """Union by size."""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Attach smaller tree under larger tree
            if self.size[root_x] < self.size[root_y]:
                root_x, root_y = root_y, root_x  # Ensure root_x is larger
            
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
```

---

## 6. Understanding Path Compression

**Path Compression** is an optimization technique used in the Find operation. It flattens the tree structure by making every node on the find path point directly to the root.

### How It Works:

```
Before Path Compression (finding 3):
        0
       / \
      1   2
           \
            3

After Path Compression (finding 3):
        0
       /|\
      1 2 3
```

### Implementation:

```python
def find(self, x):
    """Find with path compression."""
    if self.parent[x] != x:
        # Recursive path compression
        self.parent[x] = self.find(self.parent[x])
    return self.parent[x]
```

The key line is: `self.parent[x] = self.find(self.parent[x])`

This line does two things:
1. Recursively finds the root
2. Updates the parent of x to point directly to the root

This significantly reduces the height of the tree, improving future Find operations.

---

## 7. Understanding Union by Rank

**Union by Rank** (or Union by Size) is an optimization technique for the Union operation. It ensures that we always attach the smaller tree under the larger tree, preventing the formation of skewed trees.

### How It Works:

1. Each root has a **rank** (approximate depth of the tree)
2. When merging two sets, attach the root with lower rank under the root with higher rank
3. If ranks are equal, choose one as root and increment its rank

```
Before Union by Rank:
    Set A (rank 2):        Set B (rank 1):
        0                     4
       / \                   |
      1   2                  5

After Union (attach smaller under larger):
        0
       /|\
      1 2 4
           |
           5
```

### Why It Works:

- Trees with higher rank have more nodes, so they're harder to reorganize
- Attaching smaller trees under larger ones keeps the overall height minimal
- Combined with path compression, this achieves near-constant time complexity

---

## 8. Detailed Time Complexity Analysis

### 8.1 Without Optimizations

| Operation | Time Complexity |
|-----------|-----------------|
| MakeSet | O(1) |
| Find | O(n) in worst case |
| Union | O(n) in worst case |
| Connected | O(n) in worst case |

The worst case occurs when we create a linear chain of elements.

### 8.2 With Path Compression Only

The time complexity becomes **O(log n)** on average, but worst case remains O(n).

### 8.3 With Union by Rank Only

The time complexity becomes **O(log n)** for both operations.

### 8.4 With Both Optimizations (The Optimal Case)

This is the magic of Union Find:

| Operation | Time Complexity |
|-----------|-----------------|
| Find | O(α(n)) amortized |
| Union | O(α(n)) amortized |
| Connected | O(α(n)) amortized |

Where **α(n)** is the **inverse Ackermann function**, which is:
- α(n) ≤ 4 for all practical values of n (n < 2^65536)
- Effectively constant time

**Amortized Analysis**: While a single operation might occasionally be slower, the average cost per operation over a sequence of operations is effectively constant.

### 8.5 Mathematical Proof Sketch

The inverse Ackermann function grows incredibly slowly:
- α(10^80) ≈ 4
- α(2^65536) ≈ 5

This means for any dataset you can practically work with, the operations take constant time!

---

## 9. Concrete Examples

### Example 1: LeetCode Problem - Number of Connected Components

**Problem**: Given n nodes labeled from 0 to n-1 and a list of undirected edges, find the number of connected components.

```python
def count_components(n, edges):
    """
    Count the number of connected components in an undirected graph.
    
    Args:
        n: Number of nodes (0 to n-1)
        edges: List of [u, v] edges connecting nodes u and v
    
    Returns:
        Number of connected components
    """
    uf = UnionFindOptimized(n)
    
    # Process all edges
    for u, v in edges:
        uf.union(u, v)
    
    # Count unique roots
    roots = set()
    for i in range(n):
        roots.add(uf.find(i))
    
    return len(roots)


# Example usage
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(count_components(n, edges))  # Output: 2
```

**Explanation**:
- Initially, we have 5 separate sets: {0}, {1}, {2}, {3}, {4}
- Union(0, 1) merges {0} and {1} → {0, 1}
- Union(1, 2) merges {0, 1} and {2} → {0, 1, 2}
- Union(3, 4) merges {3} and {4} → {3, 4}
- Result: 2 connected components

---

### Example 2: Friend Circles Problem

**Problem**: Given a 2D grid is_friends where is_friends[i][j] = 1 if person i and j are friends, find the total number of friend circles.

```python
def find_circle_num(is_friends):
    """
    Find the number of friend circles.
    
    Args:
        is_friends: 2D list where is_friends[i][j] = 1 means 
                   person i and j are friends
    
    Returns:
        Number of friend circles
    """
    n = len(is_friends)
    uf = UnionFindOptimized(n)
    
    # Process all friendships
    for i in range(n):
        for j in range(i + 1, n):
            if is_friends[i][j] == 1:
                uf.union(i, j)
    
    # Count unique roots
    return len(set(uf.find(i) for i in range(n)))


# Example usage
is_friends = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
print(find_circle_num(is_friends))  # Output: 2
```

**Explanation**:
- Person 0 and 1 are friends → same circle
- Person 2 is only friends with themselves → separate circle
- Result: 2 friend circles

---

## 10. Delhi University Syllabus Context

This study material aligns with the **Delhi University BSc (Hons) Computer Science NEP 2024 UGCF** syllabus under:

**Paper: Algorithms And Advanced Data Structures**

Key topics covered from the syllabus:
- ✅ Disjoint Set Union (DSU) / Union Find data structure
- ✅ Basic operations: MakeSet, Find, Union
- ✅ Optimizations: Path Compression and Union by Rank
- ✅ Time and space complexity analysis
- ✅ Practical applications in graph algorithms
- ✅ Implementation in Python/C++

This content prepares students for both theoretical examinations and practical programming assignments.

---

## 11. Multiple Choice Questions (MCQs)

### Set 1: Basic Concepts

**Question 1:** What is another name for Union Find data structure?
- A) Stack
- B) Queue
- C) Disjoint Set Union
- D) Binary Search Tree

**Answer:** C) Disjoint Set Union

---

**Question 2:** Which operation in Union Find returns the representative of a set?
- A) Union
- B) MakeSet
- C) Find
- D) Connect

**Answer:** C) Find

---

**Question 3:** What does the Union operation do?
- A) Creates a new element
- B) Finds if two elements are connected
- C) Merges two sets
- D) Deletes an element

**Answer:** C) Merges two sets

---

**Question 4:** In the parent array representation, if parent[i] = i, then:
- A) i is not part of any set
- B) i is the representative of its set
- C) i has no children
- D) i is the smallest element

**Answer:** B) i is the representative of its set

---

### Set 2: Optimizations

**Question 5:** What is path compression used for?
- A) Speeding up Union operations
- B) Flattening the tree structure
- C) Balancing the tree
- D) Reducing memory usage

**Answer:** B) Flattening the tree structure

---

**Question 6:** In union by rank, which tree is attached under the other?
- A) Random tree
- Larger tree
- Smaller tree
- First tree

**Answer:** C) Smaller tree

---

**Question 7:** The inverse Ackermann function α(n) is approximately:
- A) n
- B) log n
- C) √n
- D) Constant for practical values

**Answer:** D) Constant for practical values

---

**Question 8:** What is the amortized time complexity of Find with both optimizations?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(α(n))

**Answer:** D) O(α(n))

---

### Set 3: Applications

**Question 9:** Which algorithm uses Union Find to find minimum spanning tree?
- A) Dijkstra's Algorithm
- B) Kruskal's Algorithm
- C) Prim's Algorithm
- D) Bellman-Ford Algorithm

**Answer:** B) Kruskal's Algorithm

---

**Question 10:** Union Find is used to solve which type of problems?
- A) Sorting problems
- B) Searching problems
- C) Dynamic connectivity problems
- D) String matching problems

**Answer:** C) Dynamic connectivity problems

---

## 12. Flashcard Set

### Flashcard 1: Definition
**Front:** Union Find / Disjoint Set Union
**Back:** A data structure that tracks a collection of disjoint sets, supporting Find (determine set membership) and Union (merge sets) operations efficiently.

---

### Flashcard 2: Primary Operations
**Front:** What are the two main operations in Union Find?
**Back:** 
1. **Find(x)**: Returns the representative/root of the set containing x
2. **Union(x, y)**: Merges the sets containing elements x and y

---

### Flashcard 3: Path Compression
**Front:** What is Path Compression?
**Back:** An optimization technique in the Find operation that makes every node on the find path point directly to the root, flattening the tree structure.

---

### Flashcard 4: Union by Rank
**Front:** What is Union by Rank?
**Back:** An optimization in the Union operation that attaches the smaller tree (lower rank) under the larger tree (higher rank), preventing formation of skewed trees.

---

### Flashcard 5: Time Complexity (Optimized)
**Front:** What is the time complexity of Find/Union with both optimizations?
**Back:** O(α(n)) amortized, where α(n) is the inverse Ackermann function. For all practical purposes, this is constant time O(1).

---

### Flashcard 6: Applications
**Front:** Name three real-world applications of Union Find.
**Back:** 
1. Network connectivity (social networks, computer networks)
2. Kruskal's algorithm for Minimum Spanning Tree
3. Image processing (connected component labeling)

---

### Flashcard 7: Inverse Ackermann
**Front:** Why is α(n) considered effectively constant?
**Back:** The inverse Ackermann function grows extremely slowly. α(n) ≤ 4 for any n < 2^65536, which covers all practically computable values.

---

### Flashcard 8: MakeSet
**Front:** What does MakeSet operation do?
**Back:** Creates a new set containing only a single element x, with x as its own parent/representative. Takes O(1) time.

---

## 13. Key Takeaways

### Summary

1. **Union Find** (Disjoint Set Union) is a data structure for managing disjoint sets with two main operations: Find and Union.

2. **Basic Implementation**: Uses a parent array where each element points to its parent. Without optimizations, operations take O(n) time.

3. **Path Compression**: An optimization that flattens the tree by making nodes point directly to the root during Find operations.

4. **Union by Rank**: An optimization that attaches the smaller tree under the larger tree during Union, preventing unbalanced structures.

5. **Combined Optimizations**: When both techniques are used, the amortized time complexity becomes O(α(n)), which is effectively constant for all practical purposes.

6. **Applications**: Union Find is crucial for solving connectivity problems, Kruskal's MST algorithm, image processing, network analysis, and more.

7. **Implementation**: Can be easily implemented using arrays in O(n) space.

### Important Formulas

| Metric | Without Optimizations | With Optimizations |
|--------|----------------------|-------------------|
| Find | O(n) | O(α(n)) |
| Union | O(n) | O(α(n)) |
| Space | O(n) | O(n) |

### For the Exam

- Remember that α(n) ≤ 4 for all practical n
- Know how to trace through Find and Union operations
- Understand why combining both optimizations gives the best performance
- Be able to implement Union Find from scratch

---

## 14. References and Further Reading

1. **Textbooks**:
   - "Introduction to Algorithms" by Cormen, Leiserson, Rivest, Stein (CLRS) - Chapter 21
   - "Algorithms" by Robert Sedgewick

2. **Online Resources**:
   - GeeksforGeeks: Union Find (Disjoint Set Data Structures)
   - LeetCode: Union Find problems

3. **Practice Problems**:
   - LeetCode 200: Number of Islands
   - LeetCode 547: Number of Provinces
   - LeetCode 130: Surrounded Regions

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*