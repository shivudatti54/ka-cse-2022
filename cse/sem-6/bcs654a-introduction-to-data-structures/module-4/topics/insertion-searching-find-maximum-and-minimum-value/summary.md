# Insertion, Searching, Finding Maximum and Minimum Values

## Overview

Fundamental BST operations include inserting new values while maintaining order, searching for specific values efficiently, and finding minimum/maximum values by traversing leftmost/rightmost paths respectively.

## Key Points

- **Insertion Algorithm**: Compare with root, recurse left or right, insert at NULL position
- **Searching Algorithm**: Compare target with current node, follow left/right branch based on comparison
- **Find Minimum**: Traverse leftmost path until reaching leftmost leaf node
- **Find Maximum**: Traverse rightmost path until reaching rightmost leaf node
- **Time Complexity**: All operations O(h) where h is height of tree
- **Recursive Implementation**: Natural for tree operations following subtree structure
- **Iterative Alternative**: Uses loop instead of recursion, more space efficient

## Important Concepts

- Insertion maintains BST property by placing value at correct leaf position
- Search efficiency depends on tree balance, best O(log n), worst O(n)
- Minimum always in leftmost position due to BST ordering
- Maximum always in rightmost position due to BST ordering
- Both recursive and iterative versions achieve same results
- Duplicate values handled by convention (left, right, or rejection)

## Notes

- Practice writing code for both recursive and iterative versions
- Understand how BST property guides all operations
- Trace operations on sample trees showing comparison paths
- Know that finding min/max is O(h) not O(log n) for skewed trees
- Remember insertion always creates new leaf node
