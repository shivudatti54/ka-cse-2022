# Leftist Trees


## Table of Contents

- [Leftist Trees](#leftist-trees)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Null Path Length (NPL)](#null-path-length-npl)
  - [Leftist Property](#leftist-property)
  - [Structure of a Leftist Tree Node](#structure-of-a-leftist-tree-node)
- [Merge Operation](#merge-operation)
- [Insert Operation](#insert-operation)
- [Delete-Min Operation](#delete-min-operation)
- [Build-Heap Operation](#build-heap-operation)
- [Time Complexity Summary](#time-complexity-summary)
- [Exam Tips](#exam-tips)

## Introduction

Leftist trees represent an elegant solution to the problem of efficiently merging priority queues. Introduced by Crane in 1972, these specialized binary trees combine the heap property with a structural property that guarantees logarithmic time complexity for the merge operation. Unlike binary heaps which require O(n) time to merge two heaps, leftist trees achieve merge in O(log n) time, making them particularly valuable in applications requiring frequent merging of priority queues such as in scheduling algorithms, Huffman coding, and the implementation of meldable priority queues.

A leftist tree is a variant of a binary tree that maintains the heap property (each node's key is no greater than its children's keys for a min-heap, or no smaller for a max-heap) while also satisfying the leftist property. The fundamental insight behind leftist trees is that by maintaining additional information about the "weight" or "rank" of each subtree, we can always merge two trees by working primarily on their right spines, thereby limiting the depth of traversal and achieving logarithmic complexity.

The concept of leftist trees becomes particularly powerful when considering its applications in scenarios involving dynamic sets where operations like merge, insert, and delete-min must be performed efficiently. The ability to merge two priority queues in O(log n) time, rather than the O(n) time required by conventional binary heaps, provides significant performance advantages in algorithms that manipulate multiple priority queues simultaneously.

## Key Concepts

### Null Path Length (NPL)

The null path length of a node in a binary tree is defined as the length of the shortest path from that node to a null pointer (a null child) in its subtree. Formally, for any node x in a leftist tree:

```
NPL(x) = 0 if x is a leaf or has null children
NPL(x) = 1 + min(NPL(left_child), NPL(right_child)) otherwise
```

This definition leads to a crucial property: the right spine of a leftist tree contains at most log(n+1) nodes. This property is essential because all merge operations in a leftist tree are performed along the right spine, ensuring logarithmic time complexity.

The NPL value for each node can be computed recursively using this definition, and it serves as the "weight" or "rank" information that guides the merge operation. Intuitively, a node with a smaller NPL value indicates a heavier (more unbalanced) right subtree, which is precisely the condition that allows us to bound the height of the tree.

### Leftist Property

A binary tree is said to satisfy the leftist property if for every node in the tree, the null path length of its left child is greater than or equal to the null path length of its right child. Mathematically:

```
NPL(left_child) ≥ NPL(right_child) for every node
```

This asymmetry in the tree structure is the source of the name "leftist" trees—the left children tend to have longer paths to null nodes, meaning the tree grows more densely to the left. The leftist property guarantees that the right spine of the tree contains the minimum number of nodes possible for a tree of a given size, which directly translates to efficient merge operations.

It is important to distinguish between the heap property and the leftist property. The heap property ensures that the minimum (or maximum) element is at the root, while the leftist property ensures efficient merging capability. A valid leftist tree must satisfy both properties simultaneously.

### Structure of a Leftist Tree Node

Each node in a leftist tree contains the following components:

- **key**: The priority value stored at the node
- **left**: Pointer to the left child
- **right**: Pointer to the right child
- **npl**: The null path length of the node

This node structure allows us to maintain both the heap ordering and the leftist property while performing tree operations efficiently.

## Merge Operation

The merge operation forms the foundation of all other operations in leftist trees. Given two leftist trees T1 and T2, the merge operation combines them into a single leftist tree while preserving both the heap property and the leftist property. The algorithm proceeds recursively along the right spines of the trees.

**Algorithm Merge(T1, T2):**

1. If T1 is null, return T2. If T2 is null, return T1.
2. Ensure that the root of T1 has the smaller key (swap if necessary).
3. Merge T1's right subtree with T2 using the recursive call: T1.right = Merge(T1.right, T2).
4. After merging, if NPL(T1.left) < NPL(T1.right), swap T1.left and T1.right to restore the leftist property.
5. Update T1.npl = NPL(T1.right) + 1.
6. Return T1.

**Proof of O(log n) Merge Complexity:**

Let n be the total number of nodes in both trees. Consider the right spine of the resulting tree. At each recursive step, we merge the right subtree of one tree with the entire other tree. The key observation is that after each merge, the right child of the root has an NPL value that is at most one less than the NPL of the original root. Since the NPL of any node is bounded by log(n+1), the depth of the right spine—and therefore the number of recursive calls—is O(log n). Each recursive call performs constant-time work (comparisons and pointer updates), giving us O(log n) total time complexity.

## Insert Operation

The insert operation in a leftist tree is straightforward given the merge operation. To insert a new element with key k:

1. Create a new single-node leftist tree Tnew containing only the node with key k.
2. Return Merge(T, Tnew).

Since creating a single-node tree takes O(1) time and merge takes O(log n) time, the insert operation runs in O(log n) time.

## Delete-Min Operation

The delete-min operation removes and returns the minimum element from the priority queue:

1. Let root = T, and let min = root.key.
2. Let T' = Merge(root.left, root.right) to combine the two subtrees after removing the root.
3. Free the memory for root.
4. Return min and T'.

The delete-min operation also runs in O(log n) time because both the access to the root and the merge operation are O(1) and O(log n) respectively.

## Build-Heap Operation

Given an array of n keys, we can construct a leftist tree in O(n) time by:

1. Creating n single-node trees.
2. Processing the trees in a queue, merging pairs of trees until only one tree remains.

This bottom-up construction achieves linear time, similar to heap construction, because the merge operations on smaller trees are balanced across the construction process.

## Time Complexity Summary

| Operation  | Time Complexity |
| ---------- | --------------- |
| Merge      | O(log n)        |
| Insert     | O(log n)        |
| Delete-Min | O(log n)        |
| Find-Min   | O(1)            |
| Build      | O(n)            |

## Exam Tips

1. Remember that leftist trees optimize for merge operations, not for random access. Unlike binary heaps, leftist trees do not support efficient decrease-key operations.

2. The NPL value of a node is always one more than the minimum NPL of its children. Use this recursive relationship to compute NPL values for any node in a leftist tree.

3. When merging two leftist trees, always compare the root keys first and recursively merge into the right subtree of the tree with the smaller root.

4. After any merge operation, always check and if necessary swap the left and right children to restore the leftist property (NPL(left) ≥ NPL(right)).

5. The right spine of a leftist tree containing n nodes has at most log₂(n+1) nodes. This is the key to achieving logarithmic merge complexity.

6. Understand the difference between the heap property (key ordering) and the leftist property (structural property). Both must hold for a valid leftist tree.

7. The insert operation is just a special case of merge—insert by merging with a single-node tree. This conceptual simplicity is a powerful aid in understanding the data structure.

8. For exam problems involving tracing operations, always maintain the NPL values at each node after every operation to ensure the leftist property is preserved.
