# Revision Notes: Trees - Introduction, Basic Concepts, Representation of Binary Trees, Operations on Binary Trees

=====================================================

### Introduction to Trees

- Definition: A tree is a non-linear data structure consisting of nodes, with each node having a value and zero or more child nodes.
- Types of Trees:
  - Binary Trees (BTs): Each node has at most two child nodes.
  - N-ary Trees: Each node has more than two child nodes.

### Basic Concepts

- **Node**: An element of a tree, represented as (value, left child, right child).
- **Root Node**: The topmost node of the tree.
- **Leaf Node**: A node with no child nodes.
- **Height**: The number of edges from the root node to the leaf node (h = log2(n) for a binary tree with n nodes).
- **Balanced Tree**: A tree with nodes at the same distance from the root node.

### Representation of Binary Trees

- **Inorder Traversal**: Left subtree, root node, right subtree.
- **Preorder Traversal**: Root node, left subtree, right subtree.
- **Postorder Traversal**: Left subtree, right subtree, root node.
- **Depth-First Search (DFS)**: Traverses the tree by visiting nodes at a given depth before moving to the next depth.

### Operations on Binary Trees

- **Insertion**:
  - Insert a node with value `x` into a binary tree `T`:
    - If `T` is empty, create a new node with value `x` as the root.
    - Otherwise, recursively insert `x` into the left or right subtree depending on whether `x` is less than or greater than the root node's value.
- **Deletion**:
  - Delete a node with value `x` from a binary tree `T`:
    - If `x` is the root node, replace it with the smallest (or largest) node in the right (or left) subtree.
    - Otherwise, recursively delete `x` from the left or right subtree depending on whether `x` is less than or greater than the root node's value.

### Important Formulas and Definitions

- **Height of a Binary Tree**: `h = log2(n)`, where `n` is the number of nodes.
- **Balanced Factor**: `B = h - log2(n)`, where `h` is the height and `n` is the number of nodes.

### Theorems

- **Height of a Binary Tree**: `h ≤ log2(n) + 1`.
- **Balanced Tree Properties**: If a tree is balanced, then its height is equal to `log2(n)`.

Note: This is a concise summary of the key points. For a detailed understanding, refer to the original textbook or online resources.
