# Introduction to Trees

## What is a Tree?

A **Tree** is a hierarchical, non-linear data structure consisting of nodes connected by edges. It is one of the most important data structures in computer science, used to represent hierarchical relationships.

**Definition:** A tree is a collection of nodes where:

- One node is designated as the root
- Every node (except root) is connected by exactly one edge from another node (its parent)
- There is exactly one path between root and any node

## Why Trees?

### Limitations of Linear Data Structures

1. **Fixed Access Pattern**: Arrays/Linked lists support sequential access
2. **Slow Operations**: Search can be O(n) in linear structures
3. **No Hierarchy**: Cannot naturally represent hierarchical data

### Advantages of Trees

1. **Hierarchical Structure**: Natural representation of hierarchical data
2. **Efficient Operations**: O(log n) for balanced trees
3. **Flexible**: Can represent various relationships
4. **Sorted Data**: BSTs maintain sorted order

## Basic Terminology

### Node and Relationships

```
 A (Root)
 / \\
 B C
 / \\ \\
 D E F
```

- **Node**: Each element (A, B, C, D, E, F)
- **Root**: Top node with no parent (A)
- **Parent**: Node with children (B is parent of D and E)
- **Child**: Node with a parent (B and C are children of A)
- **Siblings**: Nodes with same parent (B and C are siblings)
- **Leaf**: Node with no children (D, E, F)
- **Internal Node**: Node with at least one child (A, B, C)
- **Edge**: Connection between nodes

### Path and Level

- **Path**: Sequence of nodes connected by edges
- Path from A to E: A → B → E
- **Level**: Distance from root (root is at level 0)
- Level 0: A
- Level 1: B, C
- Level 2: D, E, F
- **Depth**: Number of edges from root to node
- **Height**: Number of edges in longest path from node to leaf
- Height of tree = Height of root

## Types of Trees

### 1. Binary Tree

Each node has at most 2 children (left and right).

### 2. Binary Search Tree (BST)

Binary tree where left < root < right for all nodes.

### 3. Full Binary Tree

Every node has 0 or 2 children.

### 4. Complete Binary Tree

All levels filled except possibly the last (filled left to right).

### 5. Perfect Binary Tree

All internal nodes have 2 children, all leaves at same level.

### 6. Balanced Binary Tree

Height difference of left and right subtrees ≤ 1 for all nodes.

### 7. AVL Tree

Self-balancing BST.

### 8. B-Tree

Multi-way search tree used in databases.

## Properties of Binary Trees

1. **Maximum nodes at level L**: 2^L
2. **Maximum nodes in tree of height h**: 2^(h+1) - 1
3. **Minimum height for n nodes**: ⌈log₂(n+1)⌉ - 1
4. **For n nodes, number of edges**: n - 1
5. **If leaf nodes = L, nodes with 2 children = T, then**: L = T + 1

## Node Structure

### Binary Tree Node

```c
struct Node {
 int data;
 struct Node* left;
 struct Node* right;
};
```

### Creating a Node

```c
struct Node* createNode(int data) {
 struct Node* newNode = malloc(sizeof(struct Node));
 newNode->data = data;
 newNode->left = NULL;
 newNode->right = NULL;
 return newNode;
}
```

## Applications of Trees

1. **File Systems**: Directory structure
2. **Databases**: B-trees for indexing
3. **Compilers**: Syntax trees
4. **XML/HTML**: DOM structure
5. **AI**: Decision trees
6. **Networks**: Routing algorithms
7. **Graphics**: Scene graphs
8. **Operating Systems**: Process trees

## Advantages and Disadvantages

### Advantages

- Hierarchical representation
- Efficient search (BST)
- Flexible size
- Natural recursion

### Disadvantages

- Complex implementation
- More memory for pointers
- Balancing overhead
- Sequential access slower than arrays

## Exam Tips

1. Memorize all terminology
2. Understand tree properties and formulas
3. Know all types of binary trees
4. Practice drawing trees
5. Calculate height, depth, levels
6. Remember node structure
7. Understand applications
8. Know time complexities
