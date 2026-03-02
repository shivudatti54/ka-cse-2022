# **Trees: Introduction, Basic Concepts, Representation of Binary Trees, Operations on Binary Trees**

### 10.1 to 10.4

- **Definition of a Tree**: A tree is a non-linear data structure consisting of nodes, where each node has a value and zero or more child nodes.
- **Types of Trees**:
  - Binary Tree: A tree in which each node has at most two child nodes.
  - N-ary Tree: A tree in which each node has more than two child nodes.
- **Tree Traversal**:
  - Inorder Traversal: Left root right
  - Preorder Traversal: root left right
  - Postorder Traversal: left right root
- **Tree Representation**:
  - Adjacency List Representation
  - Matrix Representation

### 10.5

- **Binary Search Trees (BSTs)**:
  - Definition: A binary tree where for each node, all elements in the left subtree are less than the node, and all elements in the right subtree are greater than the node.
- **Properties of BSTs**:
  - BST is a tree
  - All elements in the left subtree of a node are less than the node
  - All elements in the right subtree of a node are greater than the node
  - For every node, all elements in the left subtree and right subtree must also form a BST
- **Operations on BSTs**:
  - Insertion
  - Deletion
  - Search

### 10.6.3

- **Height of a Tree**:
  - Definition: The maximum number of edges in a path from the root to the farthest leaf node in a tree.
  - Formula: h = log(n) for a complete binary tree, where n is the number of nodes.
  - Theorem: The height of a balanced binary search tree is log(n), where n is the number of nodes.
