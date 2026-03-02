# Introduction to Trees

## Overview

A tree is a hierarchical, non-linear data structure consisting of nodes connected by edges, with one designated root node. It naturally represents hierarchical relationships and enables efficient O(log n) operations when balanced.

## Key Points

- **Hierarchical Structure**: One root node connected to child nodes forming parent-child relationships
- **Terminology**: Root (top node), leaf (no children), internal node (has children), siblings (same parent)
- **Path and Height**: Path is sequence of connected nodes, height is longest path from root to leaf
- **Binary Tree**: Each node has at most two children (left and right)
- **Node Structure**: Contains data, left pointer, and right pointer for binary trees
- **Tree Properties**: Max nodes at level L is 2^L, max nodes with height h is 2^(h+1) - 1
- **Applications**: File systems, databases (B-trees), compilers (syntax trees), AI (decision trees)

## Important Concepts

- Root has no parent, leaves have no children, all other nodes are internal
- Level indicates distance from root (root at level 0)
- Types include binary tree, BST, full, complete, perfect, balanced, AVL
- Full binary tree has nodes with 0 or 2 children only
- Complete binary tree fills all levels except possibly last (left to right)
- For n nodes, tree has exactly n-1 edges

## Notes

- Memorize all terminology and definitions for exams
- Practice drawing trees and calculating height, depth, levels
- Know tree properties and formulas for node counting
- Understand differences between full, complete, and perfect binary trees
- Remember applications in file systems, databases, and compilers
