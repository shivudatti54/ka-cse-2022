# **INTRODUCTION TO DATA STRUCTURES**

# **Module: Trees: Introduction, Basic Concepts, Representation of Binary Trees, Operations on Binary Trees**

## **10.1: Introduction to Trees**

### Definition and Importance of Trees

A tree is a non-linear data structure consisting of nodes, where each node has a value and zero or more child nodes. Trees are used to represent hierarchical relationships between data elements, making them useful for organizing and searching large datasets efficiently.

### Types of Trees

- **Binary Trees**: A tree in which each node has at most two child nodes (left child and right child).
- **N-ary Trees**: A tree in which each node can have any number of child nodes.

### Properties of Trees

- **Connectedness**: A tree is connected if there is a path between every pair of nodes.
- **Root**: A node that is not a child of any other node.
- **Leaf**: A node with no child nodes.
- **Height**: The maximum distance from the root node to any leaf node.

### Example: A Simple Binary Tree

        1
       / \
      2   3
     / \
    4   5

In this example, the root node is 1, the left child of 1 is 2, and the right child of 1 is 3. The left child of 2 is 4, and the right child of 2 is 5.

## **10.2: Basic Concepts of Binary Trees**

### Node Representation

A node in a binary tree can be represented as a structure with the following elements:

- **Value**: The data stored in the node.
- **Left Child**: The node to the left of the current node.
- **Right Child**: The node to the right of the current node.
- **Parent**: The node that is the parent of the current node.

### Types of Nodes

- **Internal Node**: A node that has child nodes (left child and right child).
- **Leaf Node**: A node that does not have child nodes.

### Traversal of Binary Trees

---

There are three main types of traversal orders for binary trees:

- **In-Order Traversal**: Left subtree, root, right subtree.
- **Pre-Order Traversal**: Root, left subtree, right subtree.
- **Post-Order Traversal**: Left subtree, right subtree, root.

### Example: In-Order Traversal of a Binary Tree

        1
       / \
      2   3
     / \
    4   5

In-order traversal of this tree would visit the nodes in the following order:

1, 2, 4, 5, 3

## **10.3: Representation of Binary Trees**

### Representations of Binary Trees

There are two main ways to represent a binary tree:

- **Graphical Representation**: A visual representation of the tree using nodes and edges.
- **Array Representation**: A linear array of nodes, where each node is represented by an index.

### Example: Graphical Representation of a Binary Tree

The same binary tree as before:

        1
       / \
      2   3
     / \
    4   5

This tree can be represented graphically as:

1
/ \
 2 3
\ /
4 5

## **10.4: Operations on Binary Trees**

### Insertion Operation

The insertion operation is used to add a new node to the tree.

### Deletion Operation

The deletion operation is used to remove a node from the tree.

### Search Operation

The search operation is used to find a specific node in the tree.

## **10.5: Specific Operations on Binary Trees**

### 10.5.1: Traversal of Binary Trees

There are three main types of traversal orders for binary trees:

- **In-Order Traversal**: Left subtree, root, right subtree.
- **Pre-Order Traversal**: Root, left subtree, right subtree.
- **Post-Order Traversal**: Left subtree, right subtree, root.

### 10.5.2: Representation of Binary Trees

There are two main ways to represent a binary tree:

- **Graphical Representation**: A visual representation of the tree using nodes and edges.
- **Array Representation**: A linear array of nodes, where each node is represented by an index.

### 10.5.3: Specific Operations on Binary Trees

#### 10.5.3.1: In-Order Traversal of a Binary Tree

In-order traversal of the tree:

        1
       / \
      2   3
     / \
    4   5

In-order traversal would visit the nodes in the following order:

1, 2, 4, 5, 3

#### 10.5.3.2: Pre-Order Traversal of a Binary Tree

Pre-order traversal of the tree:

        1
       / \
      2   3
     / \
    4   5

Pre-order traversal would visit the nodes in the following order:

1, 2, 4, 5, 3

#### 10.5.3.4: Depth-First Search of a Binary Tree

Depth-first search of the tree:

        1
       / \
      2   3
     / \
    4   5

Depth-first search would visit the nodes in the following order:

1, 2, 4, 5, 3

## **10.6.3: Conclusion**

In this chapter, we have covered the basic concepts of binary trees, including node representation, types of nodes, traversal orders, and representations. We have also covered specific operations on binary trees, including insertion, deletion, and search operations. Understanding binary trees is essential for programming and solving many problems in computer science.
