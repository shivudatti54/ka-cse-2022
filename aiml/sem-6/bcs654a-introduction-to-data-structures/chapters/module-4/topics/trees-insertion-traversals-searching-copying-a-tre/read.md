# **Trees: Insertion-Traversals-Searching-Copying a Tree, Binary Search Trees, Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

## **Introduction**

A tree is a non-linear data structure consisting of nodes, where each node has a value and zero or more child nodes. Trees are used to represent hierarchical relationships between data elements. In this topic, we will explore the following concepts:

- Insertion into a tree
- Traversals of a tree (Inorder, Preorder, Postorder)
- Searching in a tree
- Copying a tree
- Introduction to Binary Search Trees (BSTs)
- Operations on BSTs (Insertion, Searching, Find Maximum and Min)

## **Insertion into a Tree**

Insertion into a tree involves adding a new node to the existing tree. There are two types of insertion:

- **Balanced Insertion**: When a new node is inserted into a balanced tree, the tree remains balanced after insertion. This ensures that the tree remains roughly balanced and search operations are efficient.
- **Unbalanced Insertion**: When a new node is inserted into an unbalanced tree, the tree becomes unbalanced after insertion. This can lead to inefficient search operations.

## **Traversals of a Tree**

Traversals of a tree involve visiting each node in the tree in a specific order. There are three types of traversals:

- **Inorder Traversal**: Inorder traversal visits the left subtree, the current node, and then the right subtree. This traversal order ensures that the nodes are visited in ascending order.
- **Preorder Traversal**: Preorder traversal visits the current node, the left subtree, and then the right subtree. This traversal order is useful for creating a copy of the tree.
- **Postorder Traversal**: Postorder traversal visits the left subtree, the right subtree, and then the current node. This traversal order is useful for deleting a tree.

## **Searching in a Tree**

Searching in a tree involves finding a specific node in the tree. There are two types of searching:

- **Exact Search**: Exact search involves finding an exact match for the searched value.
- **Range Search**: Range search involves finding all nodes within a specified range.

## **Copying a Tree**

Copying a tree involves creating a new tree that is identical to the original tree. This can be done using preorder traversal.

## **Binary Search Trees (BSTs)**

A Binary Search Tree is a specific type of tree where each node has a unique value and the left child node has a value less than the parent node, while the right child node has a value greater than the parent node. BSTs are used to store data in a way that allows for efficient searching, insertion, and deletion.

## **Operations on Binary Search Trees**

### Insertion

Insertion into a BST involves adding a new node with a value greater than the parent node's value. The new node is inserted into the left or right subtree depending on whether the value is greater or lesser than the parent node's value.

### Searching

Searching in a BST involves finding a specific node with a given value. The search is performed by traversing the tree from the root node until the value is found or the leaf nodes are reached.

### Find Maximum and Min

Finding the maximum and minimum values in a BST involves traversing the tree from the root node until the maximum or minimum value is found.

## **Example Use Cases**

- **Database Indexing**: BSTs can be used to index large datasets, allowing for efficient searching and retrieval of data.
- **File System Organization**: BSTs can be used to organize files in a file system, allowing for efficient searching and retrieval of files.
- **Compilers**: BSTs can be used in compilers to represent the parse tree of a program, allowing for efficient traversals and analysis.

## **Code Example**

Here is an example implementation of a BST in Python:

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
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, node):
        if node.right is None:
            return node.value
        else:
            return self._find_max(node.right)

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if node.left is None:
            return node.value
        else:
            return self._find_min(node.left)
```

This implementation provides basic operations for inserting, searching, and finding the maximum and minimum values in a BST.
