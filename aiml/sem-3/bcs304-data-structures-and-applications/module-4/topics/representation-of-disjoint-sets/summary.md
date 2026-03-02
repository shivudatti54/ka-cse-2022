# Representation of Disjoint Sets - Summary

## Overview

The disjoint-set (union-find) data structure maintains a collection of disjoint sets supporting MakeSet, Find, and Union operations in near-constant amortized time.

## Key Concepts

### Array-Based Representation (Forest)

- Each element has a parent pointer; roots point to themselves
- **Find**: Returns the root with path compression optimization
- **Union**: Merges sets using union by rank heuristic
- **Space**: O(n) for parent and rank arrays

### Time Complexity

- Without optimization: O(h) where h is tree height
- With both optimizations: O(m × α(n)) where α(n) is the inverse Ackermann function
- For all practical n, α(n) ≤ 4, making operations effectively O(1)

### Comparison with Linked List

- Array representation: O(α(n)) amortized, better cache locality
- Linked list: O(1) union but O(n) find, poor cache performance

### Primary Application: Kruskal's MST

- Process edges in ascending weight order
- Use Union-Find to avoid adding edges that would create cycles
- Guarantees minimum spanning tree via cut property

## Essential Formulas

- **Amortized cost**: T(m,n) = O(m × α(n))
- **Space**: S(n) = O(n)
- **Inverse Ackermann**: α(n) ≤ 4 for all practical n
