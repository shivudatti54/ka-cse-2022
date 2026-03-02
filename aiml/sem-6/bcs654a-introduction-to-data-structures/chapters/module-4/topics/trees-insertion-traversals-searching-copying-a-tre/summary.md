# **Trees: Insertion-Traversals-Searching-Copying a Tree, Binary Search Trees, Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

## **Trees: Insertion-Traversals-Searching-Copying a Tree**

- **Insertion:** Insert a node into the tree by finding the appropriate location and updating the tree structure
- **Traversals:**
  - **Inorder Traversal:** Left-Root-Right
  - **Preorder Traversal:** Root-Left-Right
  - **Postorder Traversal:** Left-Right-Root
- **Copying a Tree:** Create a new tree by recursively copying each node

## **Binary Search Trees**

- **Definition:** A binary tree in which all elements in the left subtree are less than the root and all elements in the right subtree are greater than the root
- **Properties:**
  - **Ordered:** All elements in the left subtree are less than the root
  - **Sorted:** All elements in the right subtree are greater than the root
- **Types of Binary Search Trees:**
  - **AVL Tree:** Self-balancing binary search tree
  - **Red-Black Tree:** Self-balancing binary search tree

## **Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

- **Insertion:**
  - **Insert Node:** Insert a node with a given value into the tree by finding the appropriate location
  - **Insertion Time Complexity:** O(log n)
- **Searching:**
  - **Find Node:** Search for a node with a given value in the tree
  - **Searching Time Complexity:** O(log n)
- **Find Maximum and Min:**
  - **Find Maximum:** Find the maximum element in the tree by traversing the rightmost node
  - **Find Minimum:** Find the minimum element in the tree by traversing the leftmost node

**Important Formulas and Definitions:**

- **Height of a Tree:** The number of edges on the longest path from the root to a leaf
- **Depth of a Tree:** The number of edges on the shortest path from the root to a leaf
- **Node Value:** The value stored in a node
- **Parent Node:** The node that is the parent of a given node

**Theorem:** A binary search tree with n nodes has a height of at most log2(n) + 1.
