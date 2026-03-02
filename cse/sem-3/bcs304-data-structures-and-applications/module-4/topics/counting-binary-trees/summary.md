# Counting Binary Trees - Summary

## Key Definitions and Concepts

- **Binary Tree**: A tree data structure where each node has at most two children (left and right)
- **Rooted Binary Tree**: A binary tree with a designated root node where left and right subtrees are distinguishable
- **Full (Strict) Binary Tree**: A binary tree where every node has either 0 or 2 children
- **Catalan Numbers**: The sequence of numbers that count binary trees, given by C(n) = (2n)! / [(n+1)! × n!]
- **Binary Search Tree (BST)**: A binary tree with ordering property where left < root < right

## Important Formulas and Theorems

- **Number of binary trees with n nodes**: C(n) = (2n)! / [(n+1)! × n!]
- **Recurrence relation**: T(0) = 1, T(n) = Σ(i=1 to n) T(i-1) × T(n-i)
- **Number of BSTs with n keys**: C(n) (same as binary trees)
- **Full binary trees with n internal nodes**: C(n)
- **Total nodes in full binary tree**: If internal nodes = n, then total nodes = 2n + 1

## Key Points

- Catalan numbers: 1, 1, 2, 5, 14, 42, 132, 429, ...
- The number of binary trees grows exponentially (approximately 4^n / (n^(3/2)√π))
- Both unlabeled binary trees and BSTs follow Catalan number sequence
- Full binary trees with n internal nodes have exactly n+1 leaf nodes
- The recurrence relation derives from choosing root and distributing remaining nodes to left and right subtrees

## Common Mistakes to Avoid

- Confusing between counting nodes vs internal nodes - they give different results
- Forgetting that BST counting assumes distinct/unique keys
- Not distinguishing between complete and full binary trees
- Using n! instead of Catalan numbers for counting tree structures

## Revision Tips

- Memorize the first 6-7 Catalan numbers as they appear frequently in problems
- Practice deriving tree counts for n = 1, 2, 3, 4, 5 using recurrence
- Remember that (2n)! / [(n+1)! × n!] is the key formula for exams
- Understand the recursive nature: T(n) depends on smaller subproblems
- Focus on the relationship between Catalan numbers and tree counting
