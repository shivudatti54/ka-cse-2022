# Binary Trees

## Introduction

A binary tree is a hierarchical data structure consisting of nodes, where each node has at most two children, referred to as the left child and the right child. This fundamental data structure forms the basis for many advanced data structures and algorithms, including binary search trees, AVL trees, heap structures, and Huffman coding trees. The study of binary trees is essential for understanding efficient data storage and retrieval mechanisms in computer science.

The history of binary trees dates back to the 19th century when mathematician Karl Friedrich Gauss studied binary tree structures in relation to astronomical calculations. However, their formal study in computer science began with the development of file systems and data organization techniques in the 1950s and 1960s. Today, binary trees are ubiquitous in software engineering, powering everything from database indexing to compiler design.

## Definitions and Terminology

A **binary tree** T is a finite set of nodes such that either: (i) T is empty (null tree), or (ii) T consists of a distinguished node called the root, together with two disjoint binary trees called the left subtree and right subtree of the root.

**Key Terminology:**

- **Root**: The topmost node of the tree, having no parent
- **Parent**: A node that has one or more child nodes
- **Child**: A node descended from a parent node
- **Sibling**: Nodes sharing the same parent
- **Leaf Node**: A node with no children (also called external node)
- **Internal Node**: A node having at least one child
- **Depth**: The length of the path from the root to a node (root has depth 0)
- **Height**: The length of the longest path from a node to a leaf
- **Level**: All nodes at the same depth form a level
- **Degree**: Number of children a node has (max 2 in binary trees)

## Types of Binary Trees

### 1. Full Binary Tree

A binary tree in which every node has either 0 or 2 children. Also called a proper binary tree.

**Theorem**: In a full binary tree with $I$ internal nodes, there are $I + 1$ leaf nodes.

**Proof**: Let $n_1$ be the number of nodes with degree 1. Since it's a full binary tree, $n_1 = 0$. Total nodes $n = n_0 + n_2$ where $n_0$ is leaf nodes and $n_2$ is nodes with 2 children. For any tree: $n = n_1 + 2n_2 + 1$. Substituting $n_1 = 0$: $n_0 + n_2 = 2n_2 + 1$, which gives $n_0 = n_2 + 1$. Since internal nodes $I = n_2$, we have $n_0 = I + 1$. ∎

### 2. Complete Binary Tree

A binary tree in which all levels except possibly the last are completely filled, and all nodes are as far left as possible.

### 3. Perfect Binary Tree

A binary tree in which all internal nodes have exactly two children and all leaf nodes are at the same level.

### 4. Degenerate (Pathological) Binary Tree

A binary tree in which each parent node has only one child, creating a linked list-like structure.

### 5. Balanced Binary Tree

A binary tree in which the height difference between left and right subtrees of any node is at most 1.

## Properties of Binary Trees

**Property 1: Maximum Number of Nodes**
For a binary tree of height $h$ (height = number of edges on longest path):

- Maximum nodes = $2^{h+1} - 1$
- Maximum nodes at level $i$ = $2^i$

**Proof by Induction**: At level 0 (root), maximum nodes = $2^0 = 1$. Assuming level $i$ has at most $2^i$ nodes, each can have at most 2 children, so level $i+1$ has at most $2 \times 2^i = 2^{i+1}$ nodes. Summing geometric series: $\sum_{i=0}^{h} 2^i = 2^{h+1} - 1$. ∎

**Property 2: Relationship between Nodes and Height**
For a binary tree with $n$ nodes:

- Minimum height $h_{min} = \lfloor \log_2 n \rfloor$
- Maximum height $h_{max} = n - 1$

**Property 3: Node Count Bounds**
For a binary tree of height $h$:

- Minimum nodes $n_{min} = h + 1$ (degenerate tree)
- Maximum nodes $n_{max} = 2^{h+1} - 1$ (perfect tree)

## Representation of Binary Trees

### Linked Representation (Pointer-Based)

```c
struct Node {
    int data;
    struct Node *left;
    struct Node *right;
};
```

### Array Representation

For a complete binary tree stored in an array:

- Root at index 0
- Left child of node at index $i$: $2i + 1$
- Right child of node at index $i$: $2i + 2$
- Parent of node at index $i$: $\lfloor (i-1)/2 \rfloor$

## Time Complexity Analysis

| Operation | Array  | Linked |
| --------- | ------ | ------ |
| Search    | O(n)   | O(n)   |
| Insert    | O(n)   | O(n)   |
| Space     | O(2^h) | O(n)   |

## Examples

**Example 1**: Find the maximum number of nodes in a binary tree of height 4.

- Solution: Maximum nodes = $2^{4+1} - 1 = 2^5 - 1 = 31$

**Example 2**: In a full binary tree with 15 internal nodes, how many leaf nodes are there?

- Solution: By theorem, leaf nodes = $I + 1 = 15 + 1 = 16$

**Example 3**: A complete binary tree has 50 nodes. What is the height?

- Solution: Height = $\lfloor \log_2 50 \rfloor = \lfloor 5.64 \rfloor = 5$

## Exam Tips

1. Remember the key relationship: In a full binary tree, leaf nodes = internal nodes + 1
2. The height of a tree with $n$ nodes in worst case (degenerate) is $n-1$
3. A perfect binary tree of height $h$ has exactly $2^{h+1} - 1$ nodes
4. Array representation is efficient only for complete/perfect binary trees
5. The root is at level 0, not level 1 - this is a common source of errors
6. Be careful with definitions: height counts edges, while level counts nodes
7. When solving problems, first identify the type of binary tree given
