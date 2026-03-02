# **TREES: Introduction, Binary Trees, Binary Tree Traversals, Threaded Binary Trees**

### Introduction to Trees

- A tree is a data structure that consists of nodes or vertices connected by edges.
- Each node has a value and zero or more child nodes.
- Trees can be used to represent hierarchical data.

### Binary Trees

- A binary tree is a tree in which each node has at most two child nodes.
- Binary trees can be used to represent balanced and unbalanced data.
- Types of binary trees:
  - **Full binary tree**: every node has either 0 or 2 children.
  - **Empty binary tree**: no nodes.
  - **Perfect binary tree**: every node has two children and the height of the left and right subtrees of every node differ by at most one.

### Binary Tree Traversals

- A traversal of a binary tree visits each node exactly once.
- Types of traversals:
  - **Inorder traversal**: left subtree, root, right subtree
  - **Preorder traversal**: root, left subtree, right subtree
  - **Postorder traversal**: left subtree, right subtree, root

### Threaded Binary Trees

- A threaded binary tree is a binary tree where each node has a thread pointing to its leftmost child.
- Types of threaded binary trees:
  - **Threaded binary search tree (T-BST)**: maintains the BST property.
  - **Threaded binary tree (T-BT)**: does not necessarily maintain the BST property.

### Important Formulas and Definitions

- **Height of a tree**: the number of edges on the longest path from the root to a leaf node.
- **Depth of a tree**: the number of edges on the shortest path from the root to a leaf node.
- **Order statistic**: the kth smallest element in a set of n elements.
- **Inorder, preorder, postorder traversal formulas**:
  - Inorder: L(x), x, R(x)
  - Preorder: x, L(x), R(x)
  - Postorder: L(x), R(x), x

### Important Theorems

- **Binary search tree (BST) property**: for any node x, all elements in the left subtree of x are less than x, and all elements in the right subtree of x are greater than x.
- **Threaded binary search tree (T-BST) property**: for any node x, all elements in the left subtree of x are less than x, and all elements in the right subtree of x are greater than x.
