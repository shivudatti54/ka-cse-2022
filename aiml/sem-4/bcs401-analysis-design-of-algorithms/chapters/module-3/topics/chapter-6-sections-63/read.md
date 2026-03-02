# **Chapter 6: Section 6.3 - Binary Search Trees**

## **Introduction**

In this section, we will discuss Binary Search Trees (BSTs), a fundamental data structure in computer science. BSTs are a type of tree-based data structure that allows for efficient searching, inserting, and deleting operations.

## **Definition**

A Binary Search Tree is a tree-like data structure in which each node has at most two children (i.e., left child and right child) and each node represents a key. The left subtree of a node contains only keys less than the node's key, while the right subtree of a node contains only keys greater than the node's key.

## **Properties**

- Each node in the tree has a unique key.
- All keys in the left subtree of a node are less than the node's key.
- All keys in the right subtree of a node are greater than the node's key.
- For any node, all keys in its left subtree and right subtree must also follow the above properties.

## **Types of Binary Search Trees**

- **AVL Tree**: An AVL tree is a self-balancing BST that ensures the height of the tree remains relatively small by rotating nodes when the balance factor exceeds a certain threshold.
- **Red-Black Tree**: A red-black tree is a self-balancing BST that uses colors (red and black) to maintain the tree's balance.

## **Operations on Binary Search Trees**

- **Insertion**: Inserting a new key into the tree while maintaining the BST property.
- **Deletion**: Deleting a key from the tree while maintaining the BST property.
- **Search**: Searching for a key in the tree and returning its location.
- **Traversal**: Traversing the tree in a specific order (e.g., inorder, preorder, postorder).

## **Example**

Suppose we want to create a binary search tree from the following list of keys:

```
[8, 3, 10, 1, 6, 14, 4, 7, 13]
```

We can create the following BST:

```
       8
     /   \
    3     10
   / \   /  \
  1   6 14   13
           / \
          4   7
```

## **Code Implementation**

Here is a Python implementation of a binary search tree using a node class:

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

# Example usage
bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

print(bst.search(10))  # Output: True
print(bst.search(15))  # Output: False
```

## **Conclusion**

In this section, we discussed binary search trees, a fundamental data structure in computer science. We covered the definition, properties, types, and operations on binary search trees, along with code implementation examples.
