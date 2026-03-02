# Tree Definitions and Traversals

## Introduction

Trees represent one of the most important non-linear data structures in computer science, forming the backbone of many algorithms and applications. Unlike linear data structures such as arrays and linked lists, trees store data in a hierarchical manner with parent-child relationships. This hierarchical organization makes trees ideal for representing file systems, organizational hierarchies, XML/HTML document structure, and decision-making processes.

In the context of the University of Delhi's Computer Science curriculum, understanding trees is fundamental to mastering advanced topics like binary search trees, AVL trees, B-trees, heaps, and graph algorithms. Trees provide efficient search operations (O(log n) in balanced trees), making them indispensable for database indexing and symbol table implementations. The study of tree traversals is particularly crucial as it forms the basis for many tree-related algorithms and helps solve problems like expression evaluation, serialization, and tree printing.

This topic introduces the fundamental concepts of trees, including terminology, properties, and various traversal techniques. Mastery of these concepts is essential for solving competitive programming problems and implementing efficient software systems.

## Key Concepts

### Basic Tree Terminology

A **tree** is a finite set of nodes that either contains a distinguished node called the **root**, or is empty. The remaining nodes (excluding the root) are partitioned into n ≥ 0 disjoint subsets, each of which is itself a tree called a **subtree** of the root.

**Root**: The topmost node of a tree, having no parent. In a tree with only one node, that node is the root.

**Node**: Each element in a tree is called a node. It contains data and may have zero or more child nodes.

**Parent**: A node that has one or more child nodes is called a parent node.

**Child**: A node directly connected to another node (below it) in the tree hierarchy.

**Sibling**: Nodes that share the same parent are called siblings.

**Leaf Node (Terminal Node)**: A node that has no children is called a leaf node or external node.

**Internal Node**: A node that has at least one child (non-leaf node).

**Ancestor**: Any node on the path from the root to a given node is an ancestor of that node.

**Descendant**: Any node in a subtree rooted at a given node is a descendant of that node.

**Level (Depth)**: The level of a node is the number of edges from the root to that node. The root is at level 0.

**Height**: The maximum level of any node in the tree. A tree with only one node has height 0.

**Degree**: The degree of a node is the number of children it has.

**Forest**: A collection of disjoint trees.

### Binary Trees

A **binary tree** is a special type of tree in which each node has at most two children, commonly referred to as the **left child** and **right child**.

**Strict Binary Tree**: A binary tree in which every node has either 0 or 2 children (no node has exactly one child).

**Complete Binary Tree**: A binary tree in which all levels except possibly the last are completely filled, and all nodes are as far left as possible.

**Perfect Binary Tree**: A binary tree in which all internal nodes have exactly two children and all leaf nodes are at the same level.

**Full Binary Tree**: Another name for a strict binary tree.

### Properties of Binary Trees

1. **Maximum Nodes**: A binary tree of height h can have at most 2^(h+1) - 1 nodes.
2. **Leaf Nodes**: A binary tree with n nodes has at most n/2 leaf nodes (if n > 1).
3. **Relationship between nodes**: For any non-empty binary tree with n0 leaf nodes and n2 nodes of degree 2, we have: n0 = n2 + 1.

### Tree Representations

**Linked Representation**: Each node contains data, left child pointer, and right child pointer.

```c
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};
```

**Array Representation**: For complete binary trees, nodes can be stored in an array where:
- Parent of node at index i is at index (i-1)/2
- Left child of node at index i is at index 2i + 1
- Right child of node at index i is at index 2i + 2

### Tree Traversals

Tree traversal refers to the process of visiting each node in a tree exactly once in a systematic way. There are three fundamental depth-first traversal methods:

**1. Preorder Traversal (Root-Left-Right)**
- Visit the root node first
- Traverse the left subtree
- Traverse the right subtree
- Useful for: creating copy of tree, prefix expression evaluation

**2. Inorder Traversal (Left-Root-Right)**
- Traverse the left subtree
- Visit the root node
- Traverse the right subtree
- For BST: gives sorted order, useful for inorder successor/predecessor

**3. Postorder Traversal (Left-Right-Root)**
- Traverse the left subtree
- Traverse the right subtree
- Visit the root node last
- Useful for: deleting tree, evaluating postfix expressions

**4. Level Order Traversal (Breadth-First)**
- Visit nodes level by level, from left to right
- Uses a queue data structure
- Useful for: finding shortest path in unweighted tree, level-wise operations

## Examples

### Example 1: Tree Construction and Traversals

Consider the following binary tree:

```
         A
        / \
       B   C
      / \   \
     D   E   F
```

**Preorder (Root-Left-Right)**: A → B → D → E → C → F

Step-by-step:
1. Visit A (root)
2. Go left to B, visit B
3. Go left to D, visit D
4. D has no children, backtrack to B
5. Go right to E, visit E
6. E has no children, backtrack to A
7. Go right to C, visit C
8. C has no left child, go right to F, visit F

**Inorder (Left-Root-Right)**: D → B → E → A → C → F

**Postorder (Left-Right-Root)**: D → E → B → F → C → A

**Level Order**: A → B → C → D → E → F

### Example 2: Expression Tree Evaluation

Build an expression tree for the infix expression: (3 + 4) * (5 - 2)

```
        *
       / \
      +   -
     / \   \
    3   4   5
           /
          2
```

Inorder traversal gives: 3 + 4 * 5 - 2 (with parentheses for clarity)
Postorder traversal gives: 3 4 + 5 2 - * (postfix expression)

To evaluate using postorder (postfix):
- Push 3, Push 4 → Stack: [3, 4]
- Encounter '+', pop 4 and 3, compute 3+4=7, push 7 → Stack: [7]
- Push 5, Push 2 → Stack: [7, 5, 2]
- Encounter '-', pop 2 and 5, compute 5-2=3, push 3 → Stack: [7, 3]
- Encounter '*', pop 3 and 7, compute 7*3=21 → Result: 21

### Example 3: Counting Nodes in a Tree

Write a C function to count the total number of nodes in a binary tree:

```c
int countNodes(struct Node* root) {
    if (root == NULL)
        return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}
```

For the tree in Example 1:
- countNodes(A) = 1 + countNodes(B) + countNodes(C)
- countNodes(B) = 1 + countNodes(D) + countNodes(E) = 1 + 0 + 0 = 1
- countNodes(C) = 1 + countNodes(NULL) + countNodes(F) = 1 + 0 + 0 = 1
- Total = 1 + 1 + 1 + 1 + 1 + 1 = 6 nodes

## Exam Tips

1. **Remember traversal order**: For preorder, think "Root First"; for inorder, think "Root in middle"; for postorder, think "Root Last".

2. **Tree formulas are important**: Remember n0 = n2 + 1 relationship and maximum nodes formula 2^(h+1) - 1 for binary trees.

3. **Recursive nature**: Tree traversals are naturally recursive. Understand the base case (empty tree returns) and recursive case.

4. **Level order uses queue**: Remember that level order traversal requires a queue, not recursion.

5. **Binary Search Tree property**: Inorder traversal of a BST always gives sorted output - this is a frequently tested concept.

6. **Time and Space Complexity**: All tree traversals have O(n) time complexity. Recursive traversals have O(h) space complexity (where h is height), level order has O(w) where w is maximum width.

7. **DU Exam Pattern**: Be prepared to draw trees from traversals and vice-versa. Questions like "If preorder is ABDCE and inorder is DBACE, construct the tree" are common.

8. **Applications matter**: Know when to use each traversal - prefix/infix/postfix expressions, tree copying (preorder), deleting trees (postorder), BST operations (inorder).