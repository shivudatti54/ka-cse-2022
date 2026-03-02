# 2-4 Trees and B-Trees - Summary

## Key Definitions and Concepts

- **2-4 Tree**: A self-balancing search tree where each node contains 1, 2, or 3 keys (making it a 2-node, 3-node, or 4-node respectively) with corresponding children

- **B-Tree**: A generalized balanced search tree of order m where each node can have at most m-1 keys and m children; all leaf nodes are at the same level

- **Minimum Degree (t)**: For a B-tree of order m, t = ⌈m/2⌉; each non-root node must have at least t-1 keys

- **Node Split**: When inserting into a full node, the middle key moves up and the remaining keys form separate nodes

- **Node Merge**: When deletion causes underflow (fewer than t-1 keys), adjacent siblings may be merged

## Important Formulas and Theorems

- **B-Tree Height**: h ≤ logₜ((n+1)/2) where n = number of keys, t = minimum degree
- **Maximum keys per node**: m-1 = 2t-2
- **Minimum keys per node** (non-root): t-1
- **Search/Insert/Delete Complexity**: O(log n) for all operations
- **2-4 Tree as B-Tree**: A 2-4 tree is equivalent to a B-tree of order 4

## Key Points

1. Both 2-4 trees and B-trees maintain perfect balance—all leaf nodes are at the same level

2. B-trees minimize disk I/O by storing multiple keys per node, making them ideal for database systems

3. Insertion in B-trees always starts at a leaf node and may cause cascading splits upward

4. Deletion in B-trees is complex and may involve borrowing from siblings or merging nodes

5. The minimum degree t determines the minimum occupancy of internal nodes (at least t children)

6. 2-4 trees can be directly mapped to red-black trees through color transformations

7. For a B-tree of order m, each node has between ⌈m/2⌉ and m children (except root)

## Common Mistakes to Avoid

- Confusing "order" with "minimum degree" in B-trees—remember t = ⌈m/2⌉

- Forgetting that root has different constraints (can have fewer than t children)

- Assuming B-trees are binary—they are multiway trees with variable branching factor

- Incorrectly calculating when splitting occurs (at m keys, not m-1)

## Revision Tips

1. Practice drawing 2-4 trees and B-trees step-by-step for sequences of insertions

2. Memorize the relationship between order m and minimum degree t

3. Remember the height formula and be able to derive bounds for different values

4. Focus on understanding the split and merge operations as these are frequently tested

5. Review the disk access advantage of B-trees as this connects theory to practical applications