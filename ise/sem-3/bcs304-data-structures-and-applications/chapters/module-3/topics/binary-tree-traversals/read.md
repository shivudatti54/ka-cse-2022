# Binary Tree Traversals

## Introduction

Binary tree traversals represent one of the most fundamental operations in computer science, serving as the backbone for numerous algorithms and applications. A binary tree is a hierarchical data structure consisting of nodes, where each node has at most two children, referred to as the left child and the right child. Tree traversal refers to the process of visiting each node in the tree exactly once in a systematic manner, collecting the node information in a specific sequence.

The importance of binary tree traversals cannot be overstated in the context of data structures and algorithms. They form the foundation for expression tree evaluation, binary search tree operations, heap operations, and many tree-based algorithms. In expression trees, traversals allow us to convert between prefix, infix, and postfix notations. In binary search trees, traversals enable in-order traversal to retrieve elements in sorted order. Understanding traversals is essential for operations like searching, inserting, and deleting nodes in various tree structures.

This topic explores the four primary traversal methods: inorder, preorder, postorder, and level-order traversals. Each method has its unique characteristics and applications. The choice of traversal depends on the specific problem at hand. For instance, preorder traversal is useful for creating a copy of a tree or prefix expression generation, while inorder traversal produces sorted output for binary search trees.

## Key Concepts

### Tree Representation and Terminology

Before diving into traversals, it is crucial to understand tree terminology. The topmost node is called the ROOT. Nodes with no children are called LEAVES or terminal nodes. The HEIGHT of a node is the length of the longest path from that node to a leaf, while the HEIGHT OF TREE is the height of the root. The DEPTH of a node is the length of the path from the root to that node.

For a binary tree to be properly traversed, we need a suitable representation. The most common representation uses a structure with three fields: data, left pointer, and right pointer. Each node contains the actual data value and two pointers pointing to its left and right subtrees. A null pointer indicates the absence of a child.

### Inorder Traversal

Inorder traversal follows the LEFT-ROOT-RIGHT pattern. The algorithm recursively processes the left subtree, then visits the root node, and finally processes the right subtree. This traversal produces nodes in non-decreasing order when applied to a binary search tree, making it invaluable for sorted output operations.

The recursive implementation of inorder traversal is elegant and concise. The function first checks if the current node is null (base case), then recursively calls itself on the left subtree, processes the root by printing or storing its value, and finally recursively processes the right subtree. This systematic approach ensures every node is visited exactly once.

The iterative version of inorder traversal uses a stack to simulate the recursive call stack. We start from the root and keep pushing left children onto the stack until we reach a null node. Then we pop from the stack, process the node, and move to its right subtree. This approach is particularly useful in environments where recursion depth might be a concern.

### Preorder Traversal

Preorder traversal follows the ROOT-LEFT-RIGHT pattern. The root is visited first, followed by the entire left subtree, and then the entire right subtree. This traversal is particularly useful for creating a copy of the tree, generating prefix expressions from expression trees, and in tree serialization/deserialization operations.

The recursive implementation processes the root first, then recursively traverses the left subtree, and finally recursively traverses the right subtree. In expression tree contexts, preorder traversal produces prefix notation, which is useful in compilers for expression evaluation.

The iterative preorder traversal also utilizes a stack. We push the right child first (if it exists) and then the left child onto the stack, ensuring that the left child is processed before the right child since stacks follow LIFO order. This clever manipulation of stack operations produces the desired traversal order.

### Postorder Traversal

Postorder traversal follows the LEFT-RIGHT-ROOT pattern. Both subtrees are processed completely before visiting the root node. This traversal is essential for deleting or freeing nodes in a tree (post-order deletion ensures children are deleted before parents), evaluating expression trees to produce postfix notation, and computing directory sizes in file systems.

The recursive implementation processes the left subtree first, then the right subtree, and finally visits the root. This pattern ensures that child nodes are processed before their parent, which is critical for operations where we like tree deletion must free child nodes before their parent.

The iterative postorder traversal is more complex and typically requires either two stacks or a modified approach using a single stack with a "last visited" pointer. One common method involves using two stacks: the first stack stores nodes for processing, and the second stack is used to reverse the order, ultimately producing the correct postorder sequence.

### Level Order Traversal

Level order traversal visits nodes level by level, from left to right, starting at the root. This traversal is also known as BFS (Breadth-First Search) traversal, contrasting with the depth-first traversals (inorder, preorder, postorder). It uses a queue data structure rather than a stack.

The algorithm begins by enqueueing the root node. Then, we repeatedly dequeue a node, process it, and enqueue its left and right children (if they exist). This continues until the queue becomes empty, ensuring that nodes are visited in order of their depth from the root.

Level order traversal finds applications in finding the width of a tree, level-wise printing, finding the minimum depth of a tree, and in algorithms like level-order successor in binary trees. The time complexity for level order traversal is O(n), and the space complexity is O(w) where w represents the maximum width of the tree.

## Examples

### Example 1: Inorder Traversal of a Binary Search Tree

Consider the following binary tree:

```
        15
       /  \
      6    20
     / \   /
    3   8 17
```

Step-by-step inorder traversal:

Starting at root (15), we first go to the left subtree rooted at 6.
At node 6, we go to its left child 3.
At node 3, both children are null, so we visit 3 (output: 3).
We return to node 6, visit it (output: 3, 6).
We go to right child 8 of node 6.
At node 8, both children are null, so we visit 8 (output: 3, 6, 8).
We return to root 15, visit it (output: 3, 6, 8, 15).
We go to right subtree rooted at 20.
At node 20, we go to left child 17.
At node 17, both children are null, so we visit 17 (output: 3, 6, 8, 15, 17).
We return to node 20, visit it (output: 3, 6, 8, 15, 17, 20).

Final inorder traversal output: 3, 6, 8, 15, 17, 20

Notice how the output is sorted in ascending order, which is the key property of inorder traversal on binary search trees.

### Example 2: Preorder Traversal for Expression Evaluation

Consider an expression tree for the arithmetic expression: (3 + 4) * 2

```
        *
       / \
      +   2
     / \
    3   4
```

Step-by-step preorder traversal:

Starting at root (*), visit root first (output: *)
Go to left subtree rooted at +
Visit node + (output: *, +)
Go to left child 3, visit it (output: *, +, 3)
Return to node +, go to right child 4, visit it (output: *, +, 3, 4)
Return to root *, go to right child 2, visit it (output: *, +, 3, 4, 2)

Final preorder traversal output: * + 3 4 2

This produces the PREFIX NOTATION for the expression, which can be evaluated using a stack without parentheses.

### Example 3: Level Order Traversal for Finding Tree Width

Consider the same tree from Example 1:

```
        15
       /  \
      6    20
     / \   /
    3   8 17
```

Step-by-step level order traversal using a queue:

Initialize queue with root: [15]
Dequeue 15, process it, enqueue children: Output: 15, Queue: [6, 20]
Dequeue 6, process it, enqueue children: Output: 15 6, Queue: [20, 3, 8]
Dequeue 20, process it, enqueue children: Output: 15 6 20, Queue: [3, 8, 17]
Dequeue 3, no children: Output: 15 6 20 3, Queue: [8, 17]
Dequeue 8, no children: Output: 15 6 20 3 8, Queue: [17]
Dequeue 17, no children: Output: 15 6 20 3 8 17, Queue: []

Final level order output: 15, 6, 20, 3, 8, 17

The maximum width of this tree is 3 (at level 2 with nodes 6, 20, or 3, 8, 17).

## Exam Tips

Understanding binary tree traversals is crucial for DU semester examinations. Here are essential points to remember:

TIME AND SPACE COMPLEXITY remains consistent across all traversal methods. Each traversal visits every node exactly once, giving O(n) time complexity. Recursive implementations use O(h) stack space where h is the height of the tree (O(log n) for balanced trees, O(n) for skewed trees), while iterative implementations use O(n) or O(h) space depending on the approach.

THE RECURSIVE APPROACH is generally preferred in algorithm design due to its simplicity and readability. The base case is crucial: when the node is null, simply return without processing. Understanding the recursive call stack helps in debugging traversal-related problems.

CHOOSING THE RIGHT TRAVERSAL depends on the problem requirements. Use INORDER for binary search trees when sorted output is needed. Use PREORDER for tree copying, prefix expression generation, or serialization. Use POSTORDER for postfix expression generation, tree deletion, or when children must be processed before parents. Use LEVEL ORDER for finding minimum depth, tree width, or level-wise processing.

ITERATIVE VERSIONS are often asked in practical examinations. Remember to use a STACK for depth-first traversals and a QUEUE for level-order traversal. The key is maintaining the correct order of node processing while simulating the recursive behavior.

TRAVERSALS ON EXPRESSION TREES demonstrate practical applications. Inorder traversal produces infix notation (with parentheses for clarity), preorder produces prefix notation, and postorder produces postfix notation. This is extensively tested in DU examinations.

TRACE TRAVERSALS MANUALLY by following the systematic rules. Write down the recursive calls and their execution order. For a tree with n nodes, ensure you understand how each node is visited exactly once and in what sequence.

THE HEIGHT-BALANCED PROPERTY affects recursive space complexity. In the worst case (completely skewed tree), the height is n, leading to O(n) stack space. This is particularly important to remember when analyzing algorithm complexity.

APPLICATIONS OF TRAVERSALS are frequently asked. Binary search tree operations, expression tree evaluation, file system directory calculations, and tree serialization all rely on understanding traversals thoroughly.