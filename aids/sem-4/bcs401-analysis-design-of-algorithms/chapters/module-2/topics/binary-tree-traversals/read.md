# Binary Tree Traversals

## Introduction

Binary tree traversals represent one of the most fundamental operations in computer science, serving as the backbone for numerous algorithms and applications. A binary tree is a hierarchical data structure in which each node has at most two children, commonly referred to as the left child and the right child. Traversing a binary tree means visiting all nodes of the tree in a systematic manner, processing each node exactly once. This operation is essential for various tasks including printing tree elements, searching for specific values, evaluating expression trees, serializing tree structures, and implementing tree-based algorithms.

In the context of the University of Delhi Computer Science curriculum, understanding binary tree traversals is crucial because they form the foundation for more advanced tree operations and are frequently tested in internal assessments and end semester examinations. The concepts of pre-order, in-order, post-order, and level-order traversals appear repeatedly in algorithm design questions and form the basis for understanding recursive problem-solving approaches. Moreover, these traversal techniques are directly applicable in real-world scenarios such as file system navigation, decision tree implementations, and syntax tree parsing in compilers.

## Key Concepts

### Definition and Structure

A binary tree consists of nodes connected by edges, with each node containing data and pointers to its left and right children. The first node in the tree is called the root node. Nodes without children are called leaf nodes, while nodes with children are called internal nodes. The depth of a node refers to the number of edges from the root to that node, with the root at depth 0. The height of the tree is the maximum depth of any node in the tree.

### Types of Binary Tree Traversals

Binary tree traversals are classified based on the order in which the root node is visited relative to its left and right subtrees. There are three primary depth-first traversals:

**Pre-order Traversal (Root-Left-Right):** In this traversal, the root node is visited first, followed by the entire left subtree, and then the entire right subtree. The recursive algorithm can be expressed as: visit(root), pre-order(left-subtree), pre-order(right-subtree). This traversal is particularly useful for creating a copy of the tree, prefix expression evaluation in expression trees, and serializing tree data structures.

**In-order Traversal (Left-Root-Right):** This traversal visits the left subtree first, then the root node, and finally the right subtree. The recursive algorithm follows: in-order(left-subtree), visit(root), in-order(right-subtree). For binary search trees, in-order traversal produces nodes in sorted (ascending) order, making it essential for sorted output operations. This property makes in-order traversal extremely valuable in applications requiring sorted data retrieval.

**Post-order Traversal (Left-Right-Root):** Here, both subtrees are visited completely before the root node is processed. The algorithm follows: post-order(left-subtree), post-order(right-subtree), visit(root). This traversal is particularly useful for deleting or freeing tree nodes (to ensure children are processed before parents), evaluating postfix expressions, and computing directory sizes in file systems.

### Level-order Traversal

Level-order traversal, also known as breadth-first traversal, visits nodes level by level from top to bottom and left to right within each level. This traversal requires a queue data structure for implementation. Starting with the root node in the queue, we dequeue a node, visit it, and enqueue its left and right children (if they exist). This continues until the queue becomes empty. Level-order traversal is essential for finding the shortest path in an unweighted tree and for level-specific processing.

### Recursive vs Iterative Implementations

While recursive implementations of tree traversals are elegant and concise, understanding iterative versions is equally important for examination purposes. Recursive traversals naturally express the divide-and-conquer nature of tree processing but may cause stack overflow for very deep trees. Iterative implementations using explicit stacks or queues provide alternatives and demonstrate deeper understanding of traversal mechanics.

## Examples

### Example 1: Traversal on a Simple Binary Tree

Consider the following binary tree:

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

**Pre-order (Root-Left-Right):** A, B, D, E, C, F
Starting at root A, we visit A first, then recursively traverse the left subtree (B, D, E) completely before moving to the right subtree (C, F).

**In-order (Left-Root-Right):** D, B, E, A, C, F
We traverse the entire left subtree of A (which contains B, D, E), then visit A, then traverse the right subtree (C, F). Notice how this produces sorted output if this were a binary search tree.

**Post-order (Left-Right-Root):** D, E, B, F, C, A
We completely process both subtrees before visiting the root. This is useful when we need child results before processing parent nodes.

**Level-order:** A, B, C, D, E, F
We visit level by level: first A, then B and C, then D, E, and F.

### Example 2: Expression Tree Evaluation

Consider the expression tree for (3 + 4) * 2:

```
        *
       / \
      +   2
     / \
    3   4
```

Using post-order traversal for evaluation:
- First evaluate left subtree: 3 + 4 = 7
- Then evaluate right subtree: 2 = 2
- Finally apply root operation: 7 * 2 = 14

This demonstrates why post-order is useful for expression tree evaluation—the operands must be evaluated before the operator can be applied.

### Example 3: Iterative In-order Traversal

For the tree in Example 1, the iterative in-order traversal works as follows:

1. Start with an empty stack and current node = root (A)
2. Push all left nodes down to the leftmost: A, B, D (stack: [A, B, D])
3. Pop and visit D, move to its right (null)
4. Pop and visit B, move to its right (E)
5. Push E and its left (null): visit E
6. Pop and visit A, move to its right (C)
7. Push C and its left (null): visit C
8. Pop and visit F

Result: D, B, E, A, C, F

This iterative approach uses explicit stack management to simulate recursion, which is particularly useful for very deep trees where recursive calls might exceed stack limits.

## Exam Tips

For DU semester examinations, the following points are essential for success in binary tree traversal questions:

1. **Memorize the traversal orders precisely:** Pre-order is ROOT-LEFT-RIGHT, In-order is LEFT-ROOT-RIGHT, and Post-order is LEFT-RIGHT-ROOT. Many students confuse these during time-pressured exams.

2. **Practice drawing traversals from tree diagrams:** This is the most common examination question format. Given a binary tree diagram, students must write the sequence of nodes for each traversal type.

3. **Understand when each traversal is applicable:** Know that in-order gives sorted output for BSTs, post-order is used for deletion and expression evaluation, and pre-order for copying trees.

4. **Level-order requires a queue:** Remember that breadth-first traversal uses FIFO data structure, not the stack used in depth-first traversals.

5. **Iterative implementations may be tested:** Be prepared to write pseudo-code or explain the iterative version of any traversal, especially in-order.

6. **Time and space complexity:** All tree traversals have O(n) time complexity since each node is visited exactly once. Space complexity is O(h) for recursive traversals where h is tree height, and O(n) for worst-case (skewed tree).

7. **Connection to other topics:** Understand how traversals relate to divide-and-conquer strategy, as tree problems often involve processing subtrees recursively.