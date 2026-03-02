# Module 4: Core Operations on Data Structures (Insertion, Search, Min/Max, Count)

## Introduction

After constructing fundamental data structures like linked lists and trees, the next logical step is to perform meaningful operations on them. This module covers four essential operations that form the backbone of many complex algorithms: inserting new data, searching for existing data, finding the extreme values (minimum and maximum), and counting the number of nodes. Mastering these operations is crucial for efficiently managing and manipulating data within your programs.

## Core Concepts and Explanations

These operations are most commonly demonstrated using a **Binary Search Tree (BST)** due to its sorted property, which allows for efficient implementations. However, the concepts apply broadly to other structures like linked lists.

### 1. Insertion

Insertion involves adding a new node with a given key/value into the data structure while preserving its properties.

- **In a BST:** The key property is that for any node, all values in its left subtree are smaller, and all in its right subtree are larger. The insertion algorithm leverages this:

1.  Start at the root.
2.  Compare the new key with the current node's key.
3.  If the new key is **less**, go to the left child. If the left child is `NULL`, insert the new node here.
4.  If the new key is **greater**, go to the right child. If the right child is `NULL`, insert the new node here.
5.  Repeat the process until the node is inserted.

- **Example (BST):** Insert `15` into the BST `[20, 10, 30, 5, 25]`.
- Compare 15 with root (20): 15 < 20 → go left.
- Compare 15 with left child (10): 15 > 10 → go right.
- The right child of `10` is `NULL` → Insert `15` as the right child of `10`.

### 2. Searching

Searching checks whether a node with a specific key exists within the structure.

- **In a BST:** The process is similar to insertion but only traverses the tree without modifying it.

1.  Start at the root.
2.  If the current node is `NULL`, return "Not Found".
3.  If the search key is **equal** to the current node's key, return "Found".
4.  If the search key is **less**, recursively search the left subtree.
5.  If the search key is **greater**, recursively search the right subtree.

- **Example (BST):** Search for `25` in the same tree.
- Compare 25 with root (20): 25 > 20 → go right.
- Compare 25 with right child (30): 25 < 30 → go left.
- Compare 25 with left child (25): Match found! Return success.

### 3. Finding Maximum and Minimum Value

These operations find the node with the largest or smallest key.

- **In a BST:** The sorted property makes this extremely efficient.
- **Minimum Value:** The smallest key is located by starting at the root and repeatedly moving to the **left child** until a node with no left child is found. This node contains the minimum value.
- **Maximum Value:** The largest key is located by starting at the root and repeatedly moving to the **right child** until a node with no right child is found. This node contains the maximum value.

- **Example (BST):** Find Min and Max in `[20, 10, 30, 5, 25]`.
- **Min:** Start at 20 → left to 10 → left to 5 (no left child). **Min = 5**.
- **Max:** Start at 20 → right to 30 (no right child). **Max = 30**.

### 4. Counting Nodes

This operation calculates the total number of nodes in the entire structure or a subtree. It's a fundamental operation for determining the size of the data structure.

The most straightforward approach is a **recursive traversal** (like Inorder, Preorder, or Postorder):

1. If the tree/subtree is empty (root is `NULL`), the count is `0`.
2. Otherwise, the total count is:
   `1 (for the current root node) + Count of nodes in left subtree + Count of nodes in right subtree`.

- **Example (BST):** Count nodes in the tree with root `20`.
- Count = 1 (root=20) + count(left subtree rooted at 10) + count(right subtree rooted at 30).
- Count(left subtree @10): `1 + count(left@5) + count(right@15)` = 1 + 1 + 1 = **3**.
- Count(right subtree @30): `1 + count(left@25) + count(right@NULL)` = 1 + 1 + 0 = **2**.
- **Total Count:** 1 + 3 + 2 = **6 nodes**.

## Key Points & Summary

| Operation        | Key Idea (for BST)                                                                                            | Time Complexity | Space Complexity (Recursive) |
| :--------------- | :------------------------------------------------------------------------------------------------------------ | :-------------- | :--------------------------- |
| **Insertion**    | Traverse by comparing keys; insert at the first `NULL` position found while maintaining the BST property.     | O(h) \*         | O(h) \*                      |
| **Searching**    | Traverse by comparing keys; follow the left/right path until a match is found or a `NULL` pointer is reached. | O(h) \*         | O(h) \*                      |
| **Find Min/Max** | For Min: go left until you can't. For Max: go right until you can't.                                          | O(h) \*         | O(1) (Iterative)             |
| **Count Nodes**  | Recursively count: `1 + count(left) + count(right)`.                                                          | O(n)            | O(h) \*                      |

\*\*_h = height of the tree. For a balanced tree, h = log₂(n), making operations efficient (O(log n)). For a skewed tree (like a linked list), h = n, making operations less efficient (O(n))._

- These operations are **fundamental building blocks** for more complex algorithms like deletion, balancing, and traversal optimizations.
- While BSTs are used for examples, the logic for **counting nodes** applies identically to any binary tree. Insertion and search logic would be different for structures like heaps or hash tables.
- Understanding the recursive approach for counting and searching is critical, as recursion is a natural fit for tree-based structures.
- Always consider the **time and space complexity** to choose the right data structure for your application.
