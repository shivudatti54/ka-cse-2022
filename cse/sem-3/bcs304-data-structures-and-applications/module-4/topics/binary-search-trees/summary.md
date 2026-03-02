# Binary Search Trees

## Overview

A Binary Search Tree (BST) is a data structure in which each node has at most two children and each node represents a value. BSTs are used in many applications, such as database indexing, file systems, webpage navigation, and compilers. They provide an efficient way to store and retrieve data, with an average time complexity of O(log n) for search, insert, and delete operations.

## Key Points

- A Binary Search Tree has the following properties: each node has a unique value, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value.
- BSTs support efficient search, insert, and delete operations with an average time complexity of O(log n).
- There are three types of BSTs: full, empty, and complete.
- BSTs can become unbalanced, leading to poor performance (worst-case time complexity of O(n)).
- BSTs require additional memory to store the tree structure.
- BSTs can be used to implement other data structures, such as heaps and priority queues.

## Important Definitions

- **Node**: A node in a BST represents a value and has at most two children (left child and right child).
- **Root Node**: The topmost node in a BST.
- **Leaf Node**: A node with no children.
- **Full Binary Search Tree**: A BST in which every node has two children.
- **Empty Binary Search Tree**: A BST with no nodes.
- **Complete Binary Search Tree**: A BST in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

## Key Formulas / Syntax

- `Node* createNode(int data)`: Creates a new node with the given data.
- `Node* insertNode(Node* root, int data)`: Inserts a new value into the BST.
- `Node* searchNode(Node* root, int data)`: Searches for a value in the BST.
- `Node* deleteNode(Node* root, int data)`: Deletes a value from the BST.

## Comparisons

| Data Structure     | Search   | Insert   | Delete   | Space Complexity |
| ------------------ | -------- | -------- | -------- | ---------------- |
| Binary Search Tree | O(log n) | O(log n) | O(log n) | O(n)             |
| Hash Table         | O(1)     | O(1)     | O(1)     | O(n)             |
| Linked List        | O(n)     | O(1)     | O(1)     | O(n)             |
| Array              | O(n)     | O(n)     | O(n)     | O(n)             |

## Exam Tips

- Understand the properties and operations of binary search trees.
- Know how to implement a binary search tree in code.
- Be able to analyze the time and space complexity of binary search tree operations.
- Understand the advantages and disadvantages of using binary search trees.
- Be able to compare binary search trees with other data structures.
