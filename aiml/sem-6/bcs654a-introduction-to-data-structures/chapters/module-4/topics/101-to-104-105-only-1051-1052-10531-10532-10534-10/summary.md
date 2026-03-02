# Revision Notes: 10.1 to 10.4, 10.5 (Selected), and 10.6.3

=====================================================

### Introduction to Trees (10.1-10.4)

- **Definition:** A tree is a non-linear data structure consisting of nodes with a value and zero or more child nodes.
- **Types of Trees:**
  - Binary Tree: Each node has at most two child nodes.
  - N-ary Tree: Each node can have more than two child nodes.
- **Representation of Binary Trees:**
  - In-order Traversal: Left-Root-Right
  - Pre-order Traversal: Root-Left-Right
  - Post-order Traversal: Left-Right-Root
- **Operations on Binary Trees:**
  - Insertion: Adding a new node to the tree while maintaining balance.
  - Deletion: Removing a node from the tree while maintaining balance.

### Binary Search Trees (10.5)

- **Definition:** A Binary Search Tree is a tree where each node's value is greater than the values in its left subtree and less than the values in its right subtree.
- **Properties:**
  - **Balance Factor:** The difference between the height of the left subtree and the height of the right subtree.
  - **Height:** The number of edges on the longest path from the root to a leaf node.
- **Insertion and Deletion:**
  - **Insertion:** Maintaining balance by rotating nodes.
  - **Deletion:** Maintaining balance by rotating nodes and updating heights.

### 10.5.1: Height of a Tree

- **Height of a Tree:** The maximum distance from the root to a leaf node.
- **Formulas:**
  - Height of a tree with n nodes: O(h) = O(log n)
  - Height of a binary tree with n leaves: O(log n)

### 10.5.2: Depth of a Tree

- **Depth of a Tree:** The minimum distance from the root to a leaf node.
- **Formulas:**
  - Depth of a tree with n nodes: O(d) = O(log n)

### 10.5.3.1: Properties of a Binary Search Tree

- **Properties:**
  - **Search:** Finding a node with a given value.
  - **Insertion:** Adding a new node to the tree while maintaining balance.
  - **Deletion:** Removing a node from the tree while maintaining balance.

### 10.5.3.2: Traversals of a Binary Search Tree

- **In-order Traversal:** Left-Root-Right
- **Pre-order Traversal:** Root-Left-Right
- **Post-order Traversal:** Left-Right-Root

### 10.5.3.4: Self-Balancing Binary Search Trees

- **Self-Balancing:** Maintaining balance after insertion or deletion.
- **Types:**
  - AVL Tree
  - Red-Black Tree

### 10.6.3: Operations on Binary Search Trees

- **Insertion and Deletion:** Maintaining balance and updating heights.
- **Search:** Finding a node with a given value.
- **Traversals:** In-order, pre-order, and post-order traversals.
