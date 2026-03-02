# **Trees: Insertion-Traversals-Searching-Copying a Tree, Binary Search Trees, Operations on Binary Search Trees: Insertion-Searching-Find Maximum and Min**

## **Introduction**

Trees are a fundamental data structure in computer science, used for storing and organizing large amounts of data. In this module, we will explore the basics of trees, including insertion, traversals, searching, copying, and operations on binary search trees.

## **Basic Concepts**

- **Tree**: A tree is a data structure consisting of nodes, where each node has a value and zero or more child nodes.
- **Node**: A node is an element in the tree, consisting of a value and zero or more child nodes.
- **Root**: The root of a tree is the topmost node, which has no parent node.
- **Leaf**: A leaf is a node with no child nodes.
- **Parent**: A parent is a node that has a child node.
- **Child**: A child is a node that has a parent node.

## **Representation of Binary Trees**

A binary tree is a tree in which each node has at most two child nodes: a left child and a right child.

## **Types of Binary Trees**

- **Full Binary Tree**: A full binary tree is a binary tree in which every node has two child nodes.
- **Empty Binary Tree**: An empty binary tree is a binary tree with no nodes.

## **Operations on Binary Trees**

### Insertion

Insertion is the process of adding a new node to the binary tree.

- **Left Child Insertion**: To insert a new node as the left child of a node, we create a new node with the given value and make it the left child of the existing node.
- **Right Child Insertion**: To insert a new node as the right child of a node, we create a new node with the given value and make it the right child of the existing node.

### Searching

Searching is the process of finding a node with a given value in the binary tree.

- **Path-Based Search**: To search for a node using path-based search, we start at the root node and traverse the tree by following the child nodes until we find the desired node.
- **Recursive Search**: To search for a node using recursive search, we define a recursive function that takes a node and a value as input and returns the node if it is found, or `null` otherwise.

### Copying a Tree

Copying a tree is the process of creating a new tree that is a copy of the original tree.

- **Deep Copy**: To create a deep copy of a tree, we create a new tree and recursively copy each node in the original tree to the corresponding node in the new tree.

## **Binary Search Trees**

A binary search tree is a type of binary tree in which each node has a value and its left child node has a value less than the node's value, while its right child node has a value greater than the node's value.

## **Properties of Binary Search Trees**

- **Ordered**: A binary search tree is ordered because the values in the left subtree of a node are less than the node's value, and the values in the right subtree of a node are greater than the node's value.
- **Balanced**: A binary search tree is balanced if the height of the left and right subtrees of every node differs by at most one.

## **Operations on Binary Search Trees**

### Insertion

Insertion in a binary search tree is similar to insertion in a binary tree, but we also need to ensure that the values in the left and right subtrees remain ordered.

- **Left Child Insertion**: To insert a new node as the left child of a node, we create a new node with the given value and make it the left child of the existing node, ensuring that the values in the left subtree remain ordered.
- **Right Child Insertion**: To insert a new node as the right child of a node, we create a new node with the given value and make it the right child of the existing node, ensuring that the values in the right subtree remain ordered.

### Searching

Searching in a binary search tree is similar to searching in a binary tree, but we also need to ensure that the values in the left and right subtrees remain ordered.

- **Path-Based Search**: To search for a node using path-based search, we start at the root node and traverse the tree by following the child nodes until we find the desired node, ensuring that the values in the left and right subtrees remain ordered.
- **Recursive Search**: To search for a node using recursive search, we define a recursive function that takes a node and a value as input and returns the node if it is found, or `null` otherwise.

### Find Maximum and Min

Finding the maximum and minimum values in a binary search tree is similar to finding the maximum and minimum values in a binary tree, but we also need to ensure that the values in the left and right subtrees remain ordered.

- **Find Maximum**: To find the maximum value in a binary search tree, we start at the root node and traverse the tree by following the right child nodes until we reach a leaf node, which contains the maximum value.
- **Find Minimum**: To find the minimum value in a binary search tree, we start at the root node and traverse the tree by following the left child nodes until we reach a leaf node, which contains the minimum value.

## **Example**

Suppose we have a binary search tree with the following structure:

        4
       / \
      2   6
     / \   \
    1   3   7

We can perform the following operations:

- Insertion: Inserting a new node with value 5 as the right child of node 3.

      4

  / \
   2 6
  / \ \
  1 3 7
  /
  5

- Searching: Searching for node 2. We start at the root node and traverse the tree by following the left child nodes until we find node 2.

      4

  / \
   2 6
  / \ \
  1 3 7

We can also find the maximum and minimum values in the tree:

- Find Maximum: The maximum value in the tree is 7.
- Find Minimum: The minimum value in the tree is 1.

## **Code Snippets**

Here are some code snippets in Python that demonstrate the insertion, searching, copying, and finding maximum and minimum values in binary search trees:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
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
            return None
        if value < node.value:
            return self._search(node.left, value)
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return node

    def copy(self):
        return BinarySearchTree()
        # implement copying algorithm here

    def find_max(self):
        if self.root is None:
            return None
        max_value = self.root.value
        node = self.root
        while node.right is not None:
            max_value = node.right.value
            node = node.right
        return max_value

    def find_min(self):
        if self.root is None:
            return None
        min_value = self.root.value
        node = self.root
        while node.left is not None:
            min_value = node.left.value
            node = node.left
        return min_value
```

Note that this is a simplified implementation and may not cover all edge cases.
