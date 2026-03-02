## Textbook 2: Ch - Trees: Introduction, Basic Concepts, Representation of Binary Trees, Operations on Binary Trees

### Key Points

- **Definition of a Tree**
  - A tree is a non-linear data structure consisting of nodes with a value and zero or more child nodes.
  - Each node has a unique value and a set of child nodes.
- **Types of Trees**
  - Binary Trees
  - N-ary Trees
- **Binary Trees**
  - Definition: A tree in which each node has at most two children (left child and right child).
  - Examples: Binary Search Trees, AVL Trees, Red-Black Trees
- **Representation of Binary Trees**
  - Node: A node is an object that contains a value and a set of child nodes.
  - Node Structure:
    - Value (Node Value)
    - Left Child
    - Right Child
- **Operations on Binary Trees**
  - **Insertion**
    - Insert Node: Insert a new node with a given value into the binary tree.
    - Balance Factor: The difference between the height of the left subtree and the height of the right subtree.
  - **Deletion**
    - Delete Node: Delete a node with a given value from the binary tree.
    - After-Delete Balance: After deleting a node, the tree may become unbalanced. This is handled by rotating nodes to balance the tree.
  - **Traversal**
    - Pre-Order Traversal: Visit the current node, then the left subtree, and finally the right subtree.
    - In-Order Traversal: Visit the left subtree, then the current node, and finally the right subtree.
    - Post-Order Traversal: Visit the left subtree, then the right subtree, and finally the current node.

### Important Formulas, Definitions, and Theorems

- **Height of a Tree**: The height of a tree is the maximum depth of the tree, which is the number of edges on the longest path from the root to a leaf.
- **Balancing Factor**: The balancing factor of a binary tree is the difference between the height of the left subtree and the height of the right subtree.
- **In-Order Successor**: The in-order successor of a node is the smallest node in the right subtree of the node.
- **Properties of Binary Search Trees**
  - The left child of a node has a value less than the value of the node.
  - The right child of a node has a value greater than the value of the node.

### Key Concepts

- Node: A node is an object that contains a value and a set of child nodes.
- Edge: An edge is a connection between two nodes.
- Parent: The parent of a node is the node that connected to it.
- Leaf: A leaf is a node that has no children.
