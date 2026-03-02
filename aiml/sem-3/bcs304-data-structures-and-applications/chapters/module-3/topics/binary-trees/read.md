# Binary Trees and Applications

## Introduction to Binary Trees

A **binary tree** is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child. Unlike general trees, binary trees have a strict limitation on the number of children per node, which makes them particularly useful for many computational problems.

**Formal Definition**: A binary tree is either:
1. Empty (contains no nodes), or
2. Consists of a root node with exactly two subtrees: left subtree and right subtree, both of which are binary trees.

```
      A
     / \
    B   C
   / \   \
  D   E   F
```
*Figure 1: Example of a binary tree*

## Key Terminology

- **Root**: The topmost node in the tree (node A in Figure 1)
- **Parent**: A node that has one or more children
- **Child**: Nodes directly connected below a parent node
- **Leaf**: A node with no children (nodes D, E, F)
- **Internal node**: A node with at least one child (nodes A, B, C)
- **Depth**: The number of edges from the root to the node
- **Height**: The number of edges on the longest path from the node to a leaf
- **Level**: All nodes at the same depth (Level 0: A, Level 1: B, C, Level 2: D, E, F)

## Types of Binary Trees

### 1. Full Binary Tree
A binary tree in which every node has either 0 or 2 children.

```
      A
     / \
    B   C
   / \ 
  D   E
```
*Figure 2: Full binary tree*

### 2. Complete Binary Tree
A binary tree where all levels are completely filled except possibly the last level, which is filled from left to right.

```
      A
     / \
    B   C
   / \  /
  D   E F
```
*Figure 3: Complete binary tree*

### 3. Perfect Binary Tree
A binary tree where all internal nodes have exactly two children and all leaves are at the same level.

```
      A
     / \
    B   C
   / \ / \
  D  E F  G
```
*Figure 4: Perfect binary tree*

### 4. Degenerate (Pathological) Tree
A tree where each parent node has only one associated child node, effectively forming a linked list.

```
  A
   \
    B
     \
      C
       \
        D
```
*Figure 5: Degenerate binary tree*

### 5. Balanced Binary Tree
A tree where the height of the left and right subtrees of any node differ by at most 1.

```
      A
     / \
    B   C
   /   / \
  D   E   F
```
*Figure 6: Balanced binary tree*

## Properties of Binary Trees

| Property | Formula | Description |
|----------|---------|-------------|
| Maximum number of nodes at level i | 2^i | Level 0 has 1 node, level 1 has 2 nodes, etc. |
| Maximum number of nodes in a tree of height h | 2^(h+1)-1 | For height 2: 2^3-1 = 7 nodes |
| Minimum height for n nodes | ⌈log₂(n+1)⌉-1 | For 7 nodes: ⌈log₂8⌉-1 = 3-1 = 2 |
| Number of leaf nodes in a full binary tree | (n+1)/2 | For 7 nodes: (7+1)/2 = 4 leaves |
| Number of internal nodes in a full binary tree | (n-1)/2 | For 7 nodes: (7-1)/2 = 3 internal nodes |

## Binary Tree Traversals

Tree traversal refers to the process of visiting each node in the tree exactly once in a specific order.

### 1. Depth-First Traversals

**Pre-order (NLR)**:
1. Visit the root
2. Traverse the left subtree
3. Traverse the right subtree

Example (Figure 1): A, B, D, E, C, F

**In-order (LNR)**:
1. Traverse the left subtree
2. Visit the root
3. Traverse the right subtree

Example (Figure 1): D, B, E, A, C, F

**Post-order (LRN)**:
1. Traverse the left subtree
2. Traverse the right subtree
3. Visit the root

Example (Figure 1): D, E, B, F, C, A

### 2. Breadth-First Traversal (Level Order)

Visit nodes level by level from top to bottom and left to right.

Example (Figure 1): A, B, C, D, E, F

## Binary Search Trees (BST)

A **binary search tree** is a binary tree with the following properties:
1. The left subtree of a node contains only nodes with keys less than the node's key
2. The right subtree of a node contains only nodes with keys greater than the node's key
3. Both left and right subtrees must also be binary search trees

```
      8
     / \
    3   10
   / \    \
  1   6    14
     / \   /
    4   7 13
```
*Figure 7: Binary search tree*

**Operations on BST**:
- **Search**: O(h) time complexity, where h is the tree height
- **Insertion**: O(h) time complexity
- **Deletion**: O(h) time complexity (three cases: leaf node, node with one child, node with two children)

## Applications of Binary Trees

### 1. Expression Trees
Binary trees can represent arithmetic expressions where:
- Internal nodes are operators
- Leaf nodes are operands

```
      *
     / \
    +   -
   / \ / \
  A  B C  D
```
*Figure 8: Expression tree for (A+B)*(C-D)*

### 2. Huffman Coding
Used for lossless data compression by assigning variable-length codes to characters based on their frequencies.

### 3. Binary Space Partitioning
Used in computer graphics for efficiently rendering 3D scenes.

### 4. Decision Trees
Used in machine learning and artificial intelligence for classification problems.

### 5. Syntax Trees
Used in compilers to represent the structure of program code.

### 6. Heap Data Structure
A complete binary tree that satisfies the heap property (max-heap or min-heap).

```
      100
     /   \
    19    36
   / \    / \
  17  3  25  1
```
*Figure 9: Max-heap example*

## Implementation of Binary Trees

### Node Structure
```c
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
```

### Java Implementation
```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int val) {
        this.val = val;
        left = right = null;
    }
}
```

### Python Implementation
```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
```

## Complexity Analysis

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Search    | O(log n)     | O(n)       |
| Insertion | O(log n)     | O(n)       |
| Deletion  | O(log n)     | O(n)       |
| Traversal | O(n)         | O(n)       |

*Note: Worst case occurs when the tree becomes degenerate (linked list)*

## Exam Tips

1. **Remember traversal orders**: Use the acronyms NLR (Pre-order), LNR (In-order), LRN (Post-order)
2. **BST properties**: Always verify that left child < parent < right child for all nodes
3. **Height calculation**: For a complete binary tree with n nodes, height = ⌊log₂n⌋
4. **Tree vs Binary Tree**: All binary trees are trees, but not all trees are binary trees
5. **Practice drawing**: Be able to draw trees from traversal sequences
6. **Time complexity**: Remember that balanced trees have O(log n) operations while degenerate trees have O(n) operations
7. **Application questions**: Be prepared to explain real-world uses of binary trees with specific examples