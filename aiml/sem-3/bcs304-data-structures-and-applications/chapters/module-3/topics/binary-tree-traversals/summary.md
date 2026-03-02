# Binary Tree Traversals - Summary

## Key Definitions and Concepts
- TRAVERSAL: The process of visiting each node in a tree data structure exactly once in a systematic manner
- DEPTH-FIRST TRAVERSAL: Explores as far as possible along each branch before backtracking (includes pre-order, in-order, post-order)
- BREADTH-FIRST TRAVERSAL: Visits nodes level by level, also called level-order traversal
- THREADED BINARY TREE: A binary tree variant where null pointers store in-order predecessors/successors for efficient traversal

## Important Formulas and Algorithms
- PRE-ORDER (Root-Left-Right): Visit root, traverse left subtree, traverse right subtree
- IN-ORDER (Left-Root-Right): Traverse left subtree, visit root, traverse right subtree — produces sorted output for BST
- POST-ORDER (Left-Right-Root): Traverse left subtree, traverse right subtree, visit root — used for tree deletion
- LEVEL-ORDER: Use queue, process node then enqueue its children — produces nodes by distance from root

## Key Points
- ALL traversals have O(N) time complexity as each node is visited exactly once
- Recursive traversals use O(H) space where H is tree height; iterative stack versions also use O(H)
- Level-order traversal uses O(N) space in worst case (for wide/complete binary trees)
- IN-ORDER traversal of Binary Search Tree always produces sorted sequence
- POST-ORDER is essential for deleting trees — children must be processed before parent
- Pre-order produces PREFIX notation, post-order produces POSTFIX notation from expression trees
- Tree is uniquely determined by IN-ORDER + (PRE-ORDER OR POST-ORDER)
- Threaded binary trees eliminate stack/recursion overhead by storing traversal threads in null pointers

## Common Mistakes to Confuse
- Using stack for level-order traversal instead of queue — results in incorrect breadth-first order
- Forgetting that in-order of BST produces sorted output; this is a key property
- Mixing up traversal definitions — remember root position: pre (root first), in (root middle), post (root last)
- Assuming pre-order and post-order alone can reconstruct a unique tree — they cannot

## Revision Tips
- MEMORIZE the three positions of root in each depth-first traversal: PRE (root first), IN (root middle), POST (root last)
- PRACTICE drawing trees and manually tracing each traversal to build intuition
- REMEMBER: Level-order needs QUEUE, Depth-first uses STACK (explicit or recursive call stack)
- For expression trees, note that post-order is used by compilers because operands must be evaluated before applying operator
- Review time-space complexity trade-offs between recursive and iterative implementations