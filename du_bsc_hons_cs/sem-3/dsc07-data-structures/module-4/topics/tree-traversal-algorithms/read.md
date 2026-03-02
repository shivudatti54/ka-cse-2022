# Tree Traversal Algorithms

## Introduction

Tree traversal is a fundamental operation in computer science that involves visiting all nodes of a tree data structure in a systematic manner. Trees are non-linear data structures unlike arrays or linked lists, which are linear. This non-linear nature necessitates special techniques to access all elements exactly once. Tree traversal algorithms form the backbone of numerous applications including expression tree evaluation, file system navigation, syntax tree parsing in compilers, and hierarchical data processing.

In the context of the University of Delhi's Data Structures curriculum, tree traversal algorithms are essential for understanding how to process hierarchical data efficiently. Whether you are implementing a binary search tree, building a game decision tree, or working with XML/HTML document object models, traversal algorithms provide the mechanism to "walk through" the tree structure. The ability to master these traversals demonstrates a student's understanding of recursion, algorithmic thinking, and data structure manipulation—skills essential for competitive placements and higher studies.

This topic covers two primary categories of tree traversal: Depth-First Search (DFS) traversals (including Preorder, Inorder, and Postorder) and Breadth-First Search (BFS) traversal (Level Order). Each traversal method has distinct characteristics, use cases, and implementation approaches that we will explore in detail.

## Key Concepts

### Binary Tree Fundamentals

Before diving into traversals, let us establish the fundamental structure of a binary tree. A binary tree consists of nodes where each node contains:
- **Data**: The value stored in the node
- **Left Child**: Pointer to the left subtree
- **Right Child**: Pointer to the right subtree

A node without children is called a **leaf node**. The topmost node is called the **root**. The **height** of a tree is the number of edges from the root to the deepest leaf. The **depth** of a node is the number of edges from the root to that node.

### Depth-First Search (DFS) Traversals

DFS traversals explore as deep as possible along each branch before backtracking. There are three variants, distinguished by when the root node is processed relative to its left and right subtrees.

**Preorder Traversal (Root-Left-Right)**
In preorder traversal, we visit the root node first, then recursively traverse the left subtree, followed by the right subtree. The order is: Node → Left → Right.

```
Algorithm Preorder(node):
    if node is null:
        return
    visit(node)              // Process root
    Preorder(node.left)      // Traverse left subtree
    Preorder(node.right)     // Traverse right subtree
```

**Inorder Traversal (Left-Root-Right)**
Inorder traversal processes the left subtree first, then the root, then the right subtree. For binary search trees, inorder traversal produces sorted output. The order is: Left → Node → Right.

```
Algorithm Inorder(node):
    if node is null:
        return
    Inorder(node.left)       // Traverse left subtree
    visit(node)              // Process root
    Inorder(node.right)      // Traverse right subtree
```

**Postorder Traversal (Left-Right-Root)**
Postorder traversal processes both subtrees before visiting the root node. This is useful for deleting trees (free memory from bottom-up) or evaluating expression trees. The order is: Left → Right → Node.

```
Algorithm Postorder(node):
    if node is null:
        return
    Postorder(node.left)     // Traverse left subtree
    Postorder(node.right)    // Traverse right subtree
    visit(node)              // Process root
```

### Breadth-First Search (BFS) - Level Order Traversal

Level order traversal visits nodes level by level, from left to right, starting from the root. This requires a queue data structure to maintain the nodes at each level. BFS is particularly useful for finding the shortest path in unweighted trees and level-wise processing.

```
Algorithm LevelOrder(root):
    if root is null:
        return
    create empty queue Q
    enqueue root into Q
    while Q is not empty:
        node = dequeue Q
        visit(node)
        if node.left is not null:
            enqueue node.left into Q
        if node.right is not null:
            enqueue node.right into Q
```

### Understanding Traversal Order Visually

Consider this binary tree:

```
           10
          /  \
         5    15
        / \     \
       3   7    20
```

The traversals produce:
- **Preorder (Root-L-R)**: 10 → 5 → 3 → 7 → 15 → 20
- **Inorder (L-Root-R)**: 3 → 5 → 7 → 10 → 15 → 20
- **Postorder (L-R-Root)**: 3 → 7 → 5 → 20 → 15 → 10
- **Level Order**: 10 → 5 → 15 → 3 → 7 → 20

Notice how inorder produces sorted output—this is a crucial property of binary search trees.

### Iterative Implementations

While recursive implementations are elegant and concise, understanding iterative versions is important for technical interviews and understanding how recursion works under the hood. Iterative traversals use explicit stacks to simulate the recursion call stack.

**Iterative Inorder Traversal:**
```
Algorithm IterativeInorder(root):
    stack = empty stack
    current = root
    while current is not null OR stack is not empty:
        while current is not null:
            stack.push(current)
            current = current.left
        current = stack.pop()
        visit(current)
        current = current.right
```

## Examples

### Example 1: Expression Tree Evaluation

Expression trees represent arithmetic expressions where internal nodes are operators and leaves are operands. Consider the expression: (3 + 5) * (10 - 2)

```
           *
          / \
         +   -
        / \   \
       3   5   10  2
```

To evaluate this expression, we use **postorder traversal** (evaluate left, then right, then root/operator):

1. Evaluate left subtree: 3 + 5 = 8
2. Evaluate right subtree: 10 - 2 = 8
3. Apply root operator: 8 * 8 = 64

This is why postorder is essential for expression evaluation—the operands must be evaluated before the operator.

### Example 2: Binary Search Tree Search

Given a BST, to find if an element exists, we can use an approach similar to inorder traversal conceptually. For a BST with root = 50, and we want to find 75:

```
           50
          /  \
        30    70
        / \   / \
      20  40 60  80
```

Comparing 75 > 50, go right → Comparing 75 > 70, go right → Found 75 at node 80's left! This is essentially following the inorder path conceptually.

### Example 3: Serializing a Directory Structure

Consider representing a file system using a tree. Each node is either a file or directory. Using **preorder traversal**, we can serialize (save) and deserialize (restore) the structure:

- Preorder: Visit directory (node), then recursively process all children
- This is how the `tree` command in Linux displays directory structures

For a directory structure:
```
Root
├── Documents
│   ├── resume.pdf
│   └── notes.txt
└── Pictures
    └── photo.jpg
```

Preorder: Root → Documents → resume.pdf → notes.txt → Pictures → photo.jpg

## Exam Tips

For DU semester examinations, keep these crucial points in mind:

1. **Traversal Order Memorization**: Remember the mnemonic "Root Left Right" (Preorder), "Left Root Right" (Inorder), "Left Right Root" (Postorder). This is the most frequently tested concept.

2. **BST Property**: Inorder traversal of a Binary Search Tree always produces sorted (ascending) output—this is a theorem you must remember and can prove.

3. **Time and Space Complexity**: All tree traversals have O(n) time complexity where n is the number of nodes. Space complexity is O(h) where h is the height—O(log n) for balanced trees, O(n) for skewed trees.

4. **Recursive vs Iterative**: Understand that recursive traversals use the call stack (system stack), while iterative versions use an explicit user-defined stack.

5. **Level Order with Queue**: Remember that level order traversal is the only BFS traversal; all DFS traversals use a stack (explicit or implicit via recursion).

6. **Applications Knowledge**: Preorder is used for directory copying/serialization, Inorder for BST sorted output, Postorder for expression evaluation and tree deletion, Level Order for level-wise processing and shortest path.

7. **Drawing Trees**: Practice drawing trees from traversal sequences. Given inorder and preorder, you can uniquely reconstruct a binary tree—this is a common exam question.

8. **Stack and Queue Operations**: Be clear on which data structure each traversal uses—DFS uses stack (LIFO), BFS uses queue (FIFO).

9. **Base Case in Recursion**: Always include the null/base case check to prevent infinite recursion and stack overflow errors.

10. **Trace Algorithms**: Practice tracing through small trees (3-5 nodes) by hand to verify your understanding before implementing.