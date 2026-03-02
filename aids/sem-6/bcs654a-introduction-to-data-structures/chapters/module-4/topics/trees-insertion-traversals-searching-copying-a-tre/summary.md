# **Trees: Insertion-Traversals-Searching-Copying a Tree, Binary Search Trees, Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

## **Insertion**

- **Insertion in a Tree**: Insert a node with a given key into the tree while maintaining the binary search property.
- **Insertion Algorithm**:
  - If the tree is empty, create a new node with the given key and return the tree with one node.
  - Otherwise, recursively find the correct position for the new node based on the given key.

## **Traversals**

- **Inorder Traversal**: Left subtree -> Root -> Right subtree
- **Preorder Traversal**: Root -> Left subtree -> Right subtree
- **Postorder Traversal**: Left subtree -> Right subtree -> Root

## **Searching**

- **Searching in a Tree**: Find a node with a given key in the tree.
- **Searching Algorithm**:
  - Start at the root node and compare the given key with the key of the current node.
  - If the keys match, return the current node.
  - Otherwise, recursively search the left or right subtree depending on the comparison result.

## **Copying a Tree**

- **Copying a Tree Algorithm**: Create a new tree and recursively copy each node from the original tree.
- **Copying Formula**:
  - Create a new node with the same key as the current node.
  - Recursively copy the left and right subtrees.

## **Binary Search Trees (BSTs)**

- **Definition**: A BST is a binary tree where each node's key is greater than its left child's key and less than its right child's key.
- **Properties**:
  - BSTs maintain the binary search property.
  - All elements in the left subtree of a node are less than the node's key.
  - All elements in the right subtree of a node are greater than the node's key.

## **Operations on BSTs**

- **Insertion in a BST**: Insert a node with a given key into the BST while maintaining the binary search property.
- **Searching in a BST**: Find a node with a given key in the BST.
- **Find Maximum and Min**: Find the maximum and minimum keys in the BST.

## **Formulas and Theorems**

- **Balanced Binary Search Tree**: A BST with a height of O(log n) is balanced.
- **AVL Tree**: A balanced BST with a balance factor of -1 or 1 is an AVL tree.
- **Heights of BSTs**: The height of a BST with n nodes is O(log n).
