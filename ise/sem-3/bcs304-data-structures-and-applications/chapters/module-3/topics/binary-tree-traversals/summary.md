# Binary Tree Traversals - Summary

## Key Definitions and Concepts

- BINARY TREE: A hierarchical data structure where each node has at most two children (left and right)
- TREE TRAVERSAL: Process of visiting each node exactly once in a systematic manner
- DEPTH-FIRST TRAVERSALS: Visit nodes by exploring one subtree completely before moving to another (inorder, preorder, postorder)
- BREADTH-FIRST TRAVERSAL: Visits nodes level by level (level-order)
- ROOT: The topmost node of the tree
- LEAF: A node with no children

## Important Formulas and Theorems

- TIME COMPLEXITY for all traversals: O(n) — each node visited exactly once
- SPACE COMPLEXITY (recursive): O(h) where h is tree height; O(log n) for balanced trees, O(n) for skewed trees
- SPACE COMPLEXITY (iterative): O(n) for queue/stack in worst case
- TRAVERSAL PATTERNS:
  - Inorder: LEFT → ROOT → RIGHT
  - Preorder: ROOT → LEFT → RIGHT
  - Postorder: LEFT → RIGHT → ROOT
  - Level-order: Level by level, left to right

## Key Points

- Inorder traversal on BST produces sorted (ascending) output
- Preorder traversal is useful for tree copying and prefix expression generation
- Postorder traversal is essential for postfix expression generation and tree deletion (process children before parent)
- Level-order traversal uses a QUEUE data structure; all other traversals use STACK
- Recursive implementations are simpler and more intuitive; iterative versions are important for avoiding stack overflow
- Expression trees: Inorder → infix, Preorder → prefix, Postorder → postfix
- The height of the tree directly impacts recursive space complexity

## Common Mistakes to Avoid

Confusing the order of operations in recursive traversals — the position of root processing (first, middle, or last) determines the traversal type.

Forgetting to handle the base case (null node) in recursive implementations, leading to infinite recursion or runtime errors.

Using STACK for level-order instead of QUEUE — this produces incorrect output order.

Assuming all traversals produce sorted output — only inorder on BST guarantees sorted sequence.

Mixing up prefix, infix, and postfix notations when applied to expression trees.

## Revision Tips

Practice drawing binary trees and manually tracing all four traversals until you can do them confidently without errors.

Memorize the traversal patterns using mnemonics: LNR (Inorder), NLR (Preorder), LRN (Postorder), where L=Left, R=Right, N=Node.

Solve previous year DU examination questions on tree traversals to understand the pattern and difficulty level.

Focus on iterative implementations as they are frequently asked in practical exams.

Understand the relationship between traversals and expression tree notations thoroughly.