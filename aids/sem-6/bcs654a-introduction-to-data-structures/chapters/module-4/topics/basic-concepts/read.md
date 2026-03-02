# Basic Concepts of Trees

## Introduction

Trees represent one of the most important non-linear data structures in computer science. Unlike linear data structures such as arrays, linked lists, stacks, and queues where elements are stored in a sequential manner, trees organize data in a hierarchical structure. This hierarchical organization makes trees exceptionally efficient for representing relationships that have a parent-child or hierarchical nature.

The concept of trees originates from the natural observation of hierarchical structures around us - organizational charts, family trees, file systems in computers, and XML/HTML document structures all exhibit tree-like properties. In computer science, trees are extensively used in file systems, database indexing (B-trees), compilers (parse trees), network routing algorithms, and game development (game trees).

For the University of Delhi Computer Science program, understanding tree data structures is fundamental as it forms the basis for more advanced topics like binary search trees, AVL trees, B-trees, and heap data structures. Trees provide efficient search operations with time complexities of O(log n) in balanced trees, making them superior to linear data structures for large datasets where search operations are frequent.

## Key Concepts

### Definition of a Tree

A tree is a finite set of nodes (also called vertices) that satisfies the following properties:
1. There is a specially designated node called the ROOT of the tree.
2. The remaining nodes are partitioned into n (≥ 0) disjoint sets T1, T2, ..., Tn, where each Ti is itself a tree.
3. The sets Ti are called the SUBTREES of the root.

In simpler terms, a tree is a collection of nodes where one node is designated as the root, and every other node is connected by an edge from exactly one parent node (except the root which has no parent). This creates a hierarchical structure with no cycles.

### Important Terminology

**Root**: The topmost node of the tree that has no parent. In any tree, there is exactly one root node.

**Parent Node**: A node that has one or more child nodes below it in the hierarchy.

**Child Node**: A node that has a parent node above it. A node can have zero or more children.

**Siblings**: Nodes that share the same parent are called siblings. For example, in a family tree, siblings are nodes at the same level with a common parent.

**Leaf Node (External Node)**: A node that has no children. It is also called a terminal node. In a tree representing a directory structure, files would be leaf nodes.

**Internal Node (Non-Leaf Node)**: A node that has at least one child. It is also called a branch node.

**Degree of a Node**: The number of children a node has. A leaf node has degree 0.

**Degree of a Tree**: The maximum degree of any node in the tree. For example, if a tree has nodes with degrees 2, 3, and 1, the degree of the tree is 3.

**Level or Depth**: The level of a node is defined as the number of edges on the path from the root to that node. The root is at level 0 (or level 1, depending on convention). In DU curriculum, we typically consider the root at level 1.

**Height of a Tree**: The maximum level of any node in the tree. A tree with only one node has height 1 (or 0). Height measures the longest path from root to a leaf.

**Depth of a Node**: The number of edges from the root to that node. This is synonymous with the level of a node.

**Path**: A sequence of nodes where each consecutive pair is connected by an edge. The path from node A to node B is the sequence of nodes starting at A and ending at B.

**Ancestors of a Node**: All nodes on the path from the root to that node, excluding the node itself but including the root. Ancestors are all nodes that come before a node in the hierarchical structure.

**Descendants of a Node**: All nodes that have this node as an ancestor. This includes all children, grandchildren, and so on.

**Subtree**: A tree formed by selecting a node and all its descendants. Every node in a tree (along with its descendants) forms a subtree.

**Forest**: A collection of disjoint trees. If we remove the root of a tree, the remaining subtrees form a forest.

### Properties of Trees

Trees satisfy several important mathematical properties that are essential for analysis:

1. If a tree has 'n' nodes, it must have exactly (n-1) edges. This is because every node except the root has exactly one edge connecting it to its parent.

2. A tree with 'n' nodes has exactly (n-1) links in the underlying graph structure.

3. The height of a tree with n nodes is at least log₂(n) (for a complete tree) and at most n (for a degenerate tree that essentially becomes a linked list).

4. For any node in a tree, there exists exactly one simple path from the root to that node.

### Types of Trees

**General Tree**: A tree where any node can have any number of children. This is the most general form of tree data structure.

**Binary Tree**: A tree where each node can have at most two children. These children are typically referred to as the left child and the right child. Binary trees are extensively used in computer science.

**Binary Search Tree (BST)**: A binary tree where for each node, all nodes in its left subtree have values less than the node's value, and all nodes in its right subtree have values greater than the node's value.

**Balanced Binary Tree**: A binary tree where the height of the left and right subtrees of any node differ by at most 1. Examples include AVL trees and Red-Black trees.

**Full Binary Tree**: A binary tree where every node has either 0 or 2 children (no nodes with exactly one child).

**Complete Binary Tree**: A binary tree where all levels except possibly the last are completely filled, and all nodes are as far left as possible.

**Perfect Binary Tree**: A binary tree where all internal nodes have exactly two children and all leaf nodes are at the same level.

### Representation of Trees

Trees can be represented in computer memory using two primary methods:

**Linked Representation (Pointer-based)**: Each node contains a data field and pointers (or references) to its children. For a general tree where the number of children is variable, we can use:
- First child/next sibling representation
- Dynamic array of child pointers
- Linked list of children

For binary trees specifically, each node contains:
- Data element
- Pointer to left child
- Pointer to right child

**Array Representation**: For complete binary trees, an array can be used efficiently. For a node at index i:
- Left child is at index 2i
- Right child is at index 2i + 1
- Parent is at index floor(i/2)

This representation is memory-efficient for complete binary trees but wastes space for sparse trees.

## Examples

### Example 1: Identifying Tree Terminology

Consider the following tree structure:

```
           A (Root)
         / | \
        B  C  D
       / \   / \
      E   F G   H
         /
        I
```

Let's identify various components:
- Root: A
- Children of A: B, C, D (therefore B, C, D are siblings)
- Parent of E: B
- Leaf nodes: E, F, I, G, H (nodes with no children)
- Internal nodes: A, B, C, D (nodes with at least one child)
- Degree of node B: 2 (has children E and F)
- Degree of node D: 2 (has children G and H)
- Degree of tree: 3 (node A has 3 children)
- Height of tree: 3 (longest path A→B→F or A→D→H has 3 nodes)
- Ancestors of node I: A, C (path from root to I)
- Descendants of node C: G, H, I

### Example 2: Calculating Properties

A tree has 15 nodes. Answer the following:

(a) What is the minimum number of edges?
For any tree with n nodes, there are always exactly (n-1) edges. So minimum = maximum = 14 edges.

(b) What is the maximum possible height?
A tree with n nodes can have maximum height of (n-1) when it becomes degenerate (like a linked list). So maximum height = 15 - 1 = 14.

(c) What is the minimum possible height?
For minimum height, the tree should be as balanced as possible. For 15 nodes, a perfect binary tree has height log₂(15) + 1 ≈ 4. So minimum height = 4.

### Example 3: Array Representation

For a complete binary tree stored in an array:

Index:    1   2   3   4   5   6   7
Data:    A   B   C   D   E   F   G

Relationships:
- Root: A (at index 1)
- Left child of B (index 2): index 2×2 = 4 → D
- Right child of B: index 2×2+1 = 5 → E
- Left child of C (index 3): index 2×3 = 6 → F
- Right child of C: index 2×3+1 = 7 → G
- Parent of D (index 4): floor(4/2) = 2 → B
- Parent of G (index 7): floor(7/2) = 3 → C

## Exam Tips

1. Remember that a tree with n nodes always has exactly (n-1) edges. This is a fundamental property that frequently appears in exam questions.

2. The root node has no parent, and leaf nodes have no children. Internal nodes always have at least one child.

3. In the DU examination, clarify whether the root is at level 0 or level 1 from the question. Common convention in data structures is root at level 1, but some textbooks use level 0.

4. For binary trees, remember: if a node is at index i in array representation, its left child is at 2i and right child is at 2i+1.

5. Distinguish between height and degree: Height measures the maximum level (longest root-to-leaf path), while degree measures the number of children of a specific node.

6. A forest is formed when you remove the root of a tree - the remaining subtrees become disjoint trees.

7. In exam questions involving tree traversals or operations, always draw the tree first to visualize the structure before solving.

8. Remember that a full binary tree (every node has 0 or 2 children) with L leaf nodes has n = 2L - 1 total nodes.