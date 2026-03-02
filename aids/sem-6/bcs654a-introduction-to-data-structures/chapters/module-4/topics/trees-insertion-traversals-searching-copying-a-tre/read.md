# **Trees: Insertion-Traversals-Searching-Copying a Tree, Binary Search Trees, Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

## **Introduction**

Trees are a fundamental data structure in computer science, used to store and manipulate large amounts of data efficiently. In this section, we will explore the basic concepts of trees, binary search trees, and operations performed on binary search trees.

### What is a Tree?

A tree is a non-linear data structure consisting of nodes, where each node has a value and zero or more child nodes. The root node is the topmost node, and the leaf nodes are the bottom-most nodes.

### Types of Trees

There are several types of trees, including:

- Binary Trees: A tree where each node has at most two child nodes.
- N-ary Trees: A tree where each node can have any number of child nodes.
- B-Tree: A self-balancing search tree that keeps data sorted and allows for efficient insertion, deletion, and search operations.

### Tree Operations

Trees support several operations, including:

- **Insertion**: Adding a new node to the tree.
- **Traversal**: Visiting each node in the tree in a specific order.
- **Searching**: Finding a specific node in the tree.
- **Copying**: Creating a copy of the tree.

### Binary Search Trees (BSTs)

A binary search tree is a specialized type of binary tree where each node has a value and two child nodes (left and right). The left child node has a value less than the parent node, and the right child node has a value greater than the parent node. This property allows for efficient search, insertion, and deletion operations.

### Properties of BSTs

- **Ordered**: Each node's value is less than or equal to its left child's value and greater than or equal to its right child's value.
- **Balanced**: The height of the left and right subtrees of every node differs by at most one.

### Operations on BSTs

- **Insertion**: Adding a new node to the tree while maintaining the BST property.
- **Searching**: Finding a specific node in the tree using the BST property.
- **Find Maximum and Min**: Finding the maximum and minimum values in the tree using the BST property.

### Example of a BST

```
    5
   / \
  3   8
 / \   \
1   4   9
```

In this example, the root node is 5, the left child node has a value less than 5 (3), and the right child node has a value greater than 5 (8).

### Insertion in a BST

Inserting a new node with value 2 into the tree would result in the following structure:

```
    5
   / \
  3   8
 / \   \
1   4   9
    /
   2
```

### Searching in a BST

Searching for the node with value 8 in the tree would result in the following structure:

```
    5
   / \
  3   8
 / \   \
1   4   9
```

### Find Maximum and Min in a BST

Finding the maximum value in the tree would result in 9, and finding the minimum value would result in 1.

### Example Code (Python)

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        if self.root is not None:
            return self._search(self.root, value)
        else:
            return False

    def _search(self, node, value):
        if value == node.value:
            return True
        elif value < node.value and node.left is not None:
            return self._search(node.left, value)
        elif value > node.value and node.right is not None:
            return self._search(node.right, value)
        else:
            return False

    def find_max(self):
        if self.root is not None:
            return self._find_max(self.root)
        else:
            return None

    def _find_max(self, node):
        if node.right is None:
            return node.value
        else:
            return self._find_max(node.right)

    def find_min(self):
        if self.root is not None:
            return self._find_min(self.root)
        else:
            return None

    def _find_min(self, node):
        if node.left is None:
            return node.value
        else:
            return self._find_min(node.left)
```

This code defines a basic binary search tree (BST) with insertion, search, find maximum, and find minimum operations.
