# **Trees: Insertion-Traversals-Searching-Copying a Tree, Binary Search Trees, Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

### Trees

- **Definition:** A tree is a non-linear data structure consisting of nodes where each node has a value and zero or more children.
- **Types of Trees:**
  - Binary Trees: Each node has at most two children (left and right).
  - N-ary Trees: Each node has at most n children.

### Binary Search Trees (BSTs)

- **Definition:** A binary search tree is a binary tree where each node's left child has a value less than its parent node, and each node's right child has a value greater than its parent node.
- **Properties:**
  - Each node has a unique value.
  - All values in the left subtree are less than the node's value.
  - All values in the right subtree are greater than the node's value.

### Insertion in BSTs

- **Step 1:** Insert the node with the new value into the tree.
- **Step 2:** Compare the new value with the parent node's value.
- **Step 3:** If the new value is less than the parent node's value, recur on the left subtree.
- **Step 4:** If the new value is greater than the parent node's value, recur on the right subtree.

### Searching in BSTs

- **Step 1:** Compare the target value with the root node's value.
- **Step 2:** If the target value is less than the root node's value, recur on the left subtree.
- **Step 3:** If the target value is greater than the root node's value, recur on the right subtree.
- **Step 4:** If the target value is equal to the root node's value, return the node.

### Finding Maximum and Minimum Values in BSTs

- **Finding Maximum Value:** Start at the root node and recur on the right subtree until a leaf node is reached. The maximum value is the node's value.
- **Finding Minimum Value:** Start at the root node and recur on the left subtree until a leaf node is reached. The minimum value is the node's value.

### Important Formulas and Definitions

- **Height of a Tree:** The number of edges on the longest path from the root node to a leaf node.
- **Depth of a Tree:** The number of edges on the shortest path from the root node to a leaf node.
- **Breadth-First Search (BFS):** A traversal algorithm that visits nodes level by level, starting from the root node.
- **Depth-First Search (DFS):** A traversal algorithm that visits nodes recursively, either by going left or right.

### Theorem

- **Binary Search Tree Theorem:** If a binary search tree is ordered by key, then the left child of a node contains values less than the node's key, and the right child of a node contains values greater than the node's key.
