# **TREES: Introduction, Binary Trees, Binary Tree Traversals, Threaded Binary Trees**

## **Introduction**

A tree is a non-linear data structure consisting of nodes, where each node has a value and zero or more child nodes. Trees are used to represent hierarchical relationships between data entities. In this topic, we will explore the basics of trees, binary trees, binary tree traversals, and threaded binary trees.

## **Types of Trees**

- **Binary Tree**: A tree where each node has at most two child nodes (left and right).
- **N-ary Tree**: A tree where each node can have more than two child nodes.
- **Threaded Binary Tree**: A binary tree where each node has an additional thread (or pointer) to its leftmost child node.

## **Binary Trees**

A binary tree is a tree where each node has at most two child nodes. Binary trees are used to represent data in a hierarchical manner.

### Properties of Binary Trees

- **Root Node**: The topmost node of the tree.
- **Left Child**: The child node to the left of the root node.
- **Right Child**: The child node to the right of the root node.
- **Leaf Node**: A node with no child nodes.

### Types of Binary Trees

- **Full Binary Tree**: A binary tree where every node has either zero or two child nodes.
- **Empty Binary Tree**: A binary tree with no nodes.
- **Perfect Binary Tree**: A binary tree where all internal nodes have two child nodes and all leaf nodes have the same depth.

### Operations on Binary Trees

- **Insertion**: Adding a new node to the binary tree.
- **Deletion**: Removing a node from the binary tree.
- **Search**: Finding a node in the binary tree.

## **Binary Tree Traversals**

Binary tree traversals are used to visit each node in the binary tree.

### Types of Binary Tree Traversals

- **In-Order Traversal**: Left subtree, root node, right subtree.
- **Pre-Order Traversal**: Root node, left subtree, right subtree.
- **Post-Order Traversal**: Left subtree, right subtree, root node.

### Example of Binary Tree Traversals

```
    4
   / \
  2   6
 / \   \
1   3   5
```

- In-Order Traversal: 1, 2, 3, 4, 5, 6
- Pre-Order Traversal: 4, 2, 1, 3, 6, 5
- Post-Order Traversal: 1, 3, 2, 5, 6, 4

## **Threaded Binary Trees**

Threaded binary trees are binary trees with an additional thread (or pointer) to the leftmost child node.

### Properties of Threaded Binary Trees

- **Root Node**: The topmost node of the tree.
- **Left Child**: The child node to the left of the root node.
- **Right Child**: The child node to the right of the root node.
- **Leftmost Child Thread**: A thread pointing to the leftmost child node.

### Example of Threaded Binary Trees

```
    4
   / \
  2   6
 /   / \
1   3 5
```

- Root Node: 4
- Leftmost Child Thread: 1 (points to the leftmost child node)
- Left Child: 2
- Right Child: 6
- Leftmost Child Thread: 1 (points to the leftmost child node)

## Key Concepts

- **Tree**: A non-linear data structure consisting of nodes with values and child nodes.
- **Binary Tree**: A tree where each node has at most two child nodes.
- **Threaded Binary Tree**: A binary tree with an additional thread (or pointer) to the leftmost child node.
- **In-Order Traversal**: Left subtree, root node, right subtree.
- **Pre-Order Traversal**: Root node, left subtree, right subtree.
- **Post-Order Traversal**: Left subtree, right subtree, root node.

## Practice Questions

1.  What is a tree in data structures?
2.  What is a binary tree?
3.  What is the difference between a full binary tree and an empty binary tree?
4.  What is the purpose of binary tree traversals?
5.  What is the difference between in-order traversal, pre-order traversal, and post-order traversal?

## Answers

1.  A tree is a non-linear data structure consisting of nodes with values and child nodes.
2.  A binary tree is a tree where each node has at most two child nodes.
3.  A full binary tree is a binary tree where every node has either zero or two child nodes, while an empty binary tree has no nodes.
4.  Binary tree traversals are used to visit each node in the binary tree.
5.  In-order traversal visits the left subtree, root node, and then the right subtree, while pre-order traversal visits the root node first, followed by the left subtree, and then the right subtree. Post-order traversal visits the left subtree, then the right subtree, and finally the root node.
