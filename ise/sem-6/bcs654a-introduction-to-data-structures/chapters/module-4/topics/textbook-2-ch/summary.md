### Textbook 2: Ch - Introduction to Data Structures: Trees

#### Revision Notes

- **Definition:** A tree is a data structure consisting of nodes with a value and zero or more child nodes.
- **Types of Trees:**
  - Binary Tree: Each node has at most two child nodes.
  - N-ary Tree: Each node has more than two child nodes.

- **Properties:**
  - Connected: All nodes are reachable from each other.
  - Traversal: Can be traversed in various orders (e.g., inorder, preorder, postorder).

- **Binary Tree Representations:**
  - Inorder Traversal: Left-Root-Right
  - Preorder Traversal: Root-Left-Right
  - Postorder Traversal: Left-Right-Root

- **Operations on Binary Trees:**
  - **Insertion:**
    - Time complexity: O(h) in AVL trees, O(log n) in binary search trees.
  - **Deletion:**
    - Time complexity: O(h) in AVL trees, O(log n) in binary search trees.
  - **Search:**
    - Time complexity: O(h) in AVL trees, O(log n) in binary search trees.

- **Important Formulas:**
  - Height of a tree: h = log(n)
  - Number of nodes: n = 2^(h) - 1

- **Theorems:**
  - **Tree properties:** Every path from the root to a leaf has the same number of nodes.
  - **Balancing:** AVL trees and Red-Black trees are self-balancing binary search trees.
