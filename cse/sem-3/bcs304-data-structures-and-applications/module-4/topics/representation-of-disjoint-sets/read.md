# Representation of Disjoint Sets

## 1. Introduction and Theoretical Foundation

A **disjoint-set data structure** (also known as **union-find** or **merge-find**) is a fundamental data structure in computer science that maintains a collection of disjoint (non-overlapping) sets. Formally, if we denote a universe of elements as $U$, a disjoint-set structure partitions $U$ into $n$ disjoint subsets $S_1, S_2, ..., S_n$ such that $S_i \cap S_j = \emptyset$ for all $i \neq j$, and $\bigcup_{i=1}^{n} S_i = U$.

This data structure supports two primary operations:

- **MakeSet(x)**: Creates a new set containing only element $x$
- **Find(x)**: Returns the representative (root) of the set containing element $x$
- **Union(x, y)**: Merges the sets containing elements $x$ and $y$

The theoretical importance of disjoint sets lies in their ability to solve equivalence relations efficiently. Two elements are said to be in the same equivalence class if they are connected through a chain of operations.

## 2. Array-Based Representation (Forest Representation)

The most efficient representation for disjoint sets uses a **forest** structure, where each set is represented as a tree. This approach, known as the **parent-pointer representation**, stores for each element a reference to its parent in the tree.

### 2.1 Data Structure Definition

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_ELEMENTS 100

// Disjoint set structure using parent array
typedef struct DisjointSet {
    int parent[MAX_ELEMENTS];
    int rank[MAX_ELEMENTS];  // For union by rank optimization
    int size;                // Number of elements
} DisjointSet;
```

### 2.2 MakeSet Operation

The **MakeSet** operation initializes each element as a singleton set with itself as the parent:

```c
// Initialize a new disjoint set with n elements
void makeSet(DisjointSet* ds, int n) {
    ds->size = n;
    for (int i = 0; i < n; i++) {
        ds->parent[i] = i;    // Each element is its own parent (root)
        ds->rank[i] = 0;      // Initial rank is 0
    }
}
```

**Theorem 1**: After calling MakeSet(x) for all elements $x \in U$, each element forms a separate set, and Find(x) returns $x$ for all $x$.

**Proof**: By initialization, we set parent[x] = x for each element x. The Find operation (defined below) returns the root by following parent pointers until a node points to itself. Since parent[x] = x initially, Find(x) returns x immediately. ∎

### 2.3 Find Operation with Path Compression

The **Find** operation returns the representative (root) of the set containing a given element. **Path compression** is an optimization that makes future operations faster by making each node point directly to the root:

```c
// Find operation with path compression
int find(DisjointSet* ds, int x) {
    if (ds->parent[x] != x) {
        // Path compression: make every node point directly to root
        ds->parent[x] = find(ds, ds->parent[x]);
    }
    return ds->parent[x];
}
```

### 2.4 Union Operation with Union by Rank

The **Union** operation merges two sets. **Union by rank** ensures that the smaller tree is attached to the root of the larger tree, keeping the tree height minimal:

```c
// Union operation with union by rank
void unionSets(DisjointSet* ds, int x, int y) {
    int rootX = find(ds, x);
    int rootY = find(ds, y);

    // Already in the same set
    if (rootX == rootY) {
        return;
    }

    // Union by rank: attach smaller tree under larger tree
    if (ds->rank[rootX] < ds->rank[rootY]) {
        ds->parent[rootX] = rootY;
    } else if (ds->rank[rootX] > ds->rank[rootY]) {
        ds->parent[rootY] = rootX;
    } else {
        // Same rank: choose one as root and increment its rank
        ds->parent[rootY] = rootX;
        ds->rank[rootX]++;
    }
}
```

## 3. Time Complexity Analysis

### 3.1 Amortized Analysis

**Theorem 2**: With both path compression and union by rank, any sequence of $m$ operations on $n$ elements takes $O(m \cdot \alpha(n))$ time, where $\alpha(n)$ is the inverse Ackermann function.

**Proof Sketch**: The inverse Ackermann function $\alpha(n)$ is the functional inverse of the Ackermann function $A(n)$. For all practical values of $n$, $\alpha(n) \leq 4$. The proof uses the **potential method** from amortized analysis:

- Define potential $\Phi = \sum_{i=1}^{n} \text{rank}(i) \cdot \log(n / \text{rank}(i))$
- Show that the amortized cost of Find with path compression is $O(\alpha(n))$
- Show that the amortized cost of Union with union by rank is $O(1)$
- Therefore, total amortized cost for $m$ operations is $O(m \cdot \alpha(n))$

**Corollary**: For practical purposes, the operations can be considered $O(1)$ (constant time) since $\alpha(10^{6}) = 2$ and $\alpha(10^{100}) = 3$.

### 3.2 Complexity Summary

| Operation | Without Optimization | With Path Compression | With Both Optimizations |
| --------- | -------------------- | --------------------- | ----------------------- |
| MakeSet   | O(n)                 | O(n)                  | O(n)                    |
| Find      | O(h)                 | O(log n) amortized    | O(α(n)) amortized       |
| Union     | O(h)                 | O(log n) amortized    | O(α(n)) amortized       |

_Note: h represents the height of the tree_

### 3.3 Space Complexity

The array-based representation requires:

- Parent array: O(n)
- Rank array: O(n)
- **Total Space**: O(n)

## 4. Linked List Representation

An alternative representation uses linked lists, where each set is a linked list with a head pointer:

```c
typedef struct ListNode {
    int data;
    struct ListNode* next;
} ListNode;

typedef struct SetHeader {
    ListNode* head;
    ListNode* tail;
    int size;  // Track size for union by size optimization
} SetHeader;
```

**Theorem 3**: In linked list representation with union by size, the time complexity of Union is O(1), but Find remains O(n).

**Proof**: The head and tail pointers allow constant-time insertion at the end. However, to find if two elements are in the same set, we must traverse from each element to find its set header, which in the worst case requires O(n) time. ∎

## 5. Comparative Analysis

| Criterion        | Array Representation          | Linked List Representation   |
| ---------------- | ----------------------------- | ---------------------------- |
| Space Complexity | O(n)                          | O(n) with higher constant    |
| Find Operation   | O(α(n)) amortized             | O(n) worst case              |
| Union Operation  | O(α(n)) amortized             | O(1) with tail pointer       |
| Cache Efficiency | Excellent (contiguous memory) | Poor (scattered allocations) |
| Implementation   | Simple                        | More complex                 |

## 6. Application: Kruskal's Minimum Spanning Tree Algorithm

Disjoint sets are essential in **Kruskal's algorithm** for finding the Minimum Spanning Tree (MST) of a weighted graph:

```c
// Kruskal's MST using disjoint sets
typedef struct Edge {
    int src, dest, weight;
} Edge;

int kruskalMST(Edge edges[], int E, int V) {
    // Sort edges by weight
    // ... (sorting code)

    DisjointSet ds;
    makeSet(&ds, V);

    int mstWeight = 0;
    int edgeCount = 0;

    for (int i = 0; i < E && edgeCount < V - 1; i++) {
        int rootSrc = find(&ds, edges[i].src);
        int rootDest = find(&ds, edges[i].dest);

        // If adding this edge doesn't form a cycle
        if (rootSrc != rootDest) {
            unionSets(&ds, rootSrc, rootDest);
            mstWeight += edges[i].weight;
            edgeCount++;
        }
    }
    return mstWeight;
}
```

**Theorem 4**: Kruskal's algorithm correctly produces a minimum spanning tree.

**Proof**: The correctness follows from the **cut property**: for any cut of the graph, the minimum-weight edge crossing the cut belongs to some MST. By processing edges in increasing order of weight and using Union-Find to avoid cycles, Kruskal's algorithm builds an MST. ∎

## 7. Additional Applications

1. **Network Connectivity**: Determining connected components in undirected graphs
2. **Image Segmentation**: Segmenting images based on pixel similarity
3. **Kruskal's MST**: Building minimum spanning trees
4. **Detecting Cycles**: In union-find based cycle detection for graphs
5. **Equivalence Relations**: Processing dependency queries

## 8. Practice Problems

### Problem 1: Trace the Union-Find Operations

Given elements {0, 1, 2, 3, 4, 5}, perform the following operations:

- Union(0, 1), Union(2, 3), Union(4, 5)
- Union(0, 2), Find(5)

Show the parent array after each operation with union by rank.

### Problem 2: Time Complexity Analysis

A sequence of n MakeSet operations followed by n-1 Union operations and m Find operations is performed. What is the worst-case and amortized time complexity?

### Problem 3: Cycle Detection

Given a graph with edges [(0,1), (1,2), (2,0)], show how Union-Find detects the cycle when processing edge (2,0).

---

**Key Takeaways**:

- Disjoint sets support MakeSet, Find, and Union operations in near-constant amortized time
- Path compression and union by rank are essential optimizations
- The inverse Ackermann function α(n) makes operations effectively constant-time
- Array-based representation with optimizations is preferred for practical applications
- Kruskal's MST algorithm is a primary application of disjoint sets
