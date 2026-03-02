# Binary Search Trees

## Introduction

A Binary Search Tree (BST) is a specialized binary tree data structure that maintains sorted data in a manner enabling efficient search, insertion, and deletion operations. Unlike general binary trees, BSTs enforce a critical property: for every node, all keys in the left subtree are less than the node's key, and all keys in the right subtree are greater than the node's key. This ordering property, first formalized by Windley (1960) and subsequently refined by Knuth (1971), is fundamental to the tree's efficiency in maintaining dynamic sets.

The BST represents a natural compromise between the rigid structure of sorted arrays (which offer O(log n) search but O(n) insertion/deletion) and linked lists (which offer O(1) insertion but O(n) search). Under ideal conditions of balance, BST operations execute in O(log n) time, making them indispensable in applications requiring frequent modifications to sorted collections. The data structure finds extensive application in database indexing, symbol table implementation, priority queue operations, and as the underlying mechanism for more advanced data structures including AVL trees, Red-Black trees, and B-trees.

This topic assumes knowledge of basic tree terminology including nodes, edges, root, parent, child, leaf, depth, and height. Students should be familiar with recursive problem-solving approaches and elementary algorithm analysis.

## Key Concepts

### Formal Definition

A Binary Search Tree T is a binary tree where each node stores a key (or key-value pair) satisfying the **BST Property**: For any node x, if y is in the left subtree of x, then key[y] ≤ key[x]; if y is in the right subtree of x, then key[y] ≥ key[x]. Most implementations enforce strict inequality (distinct keys) to simplify successor/predecessor operations, though the definition accommodates duplicate values through convention (typically placed in either left or right subtree consistently).

**Definition 1 (Tree Height)**: The height of a node x is the number of edges on the longest downward path from x to a leaf. The height of an empty tree is defined as -1, and the height of a single-node tree is 0.

**Definition 2 (Tree Depth)**: The depth of a node x is the number of edges from the root to x. The root has depth 0.

### Time Complexity Analysis

The efficiency of BST operations depends critically on tree height. Let n represent the number of nodes and h represent the tree height.

**Theorem 1**: For a BST with n nodes, the search, minimum, and maximum operations run in O(h) time.

_Proof_: Each recursive step descends one level, and the longest root-to-leaf path contains exactly h+1 nodes (h edges). Since we visit at most h+1 nodes, the time complexity is O(h). ∎

**Corollary 1**: In a balanced BST where h = Θ(log n), all basic operations run in Θ(log n) time.

**Corollary 2**: In the worst case (degenerate tree resembling a linked list), where h = n-1, operations degrade to Θ(n) time.

The average-case analysis, originally proven by Knuth, demonstrates that a randomly built BST with n distinct keys has expected height O(log n). Specifically, the expected height is approximately 4.311 ln(n) - O(1), which is proportional to ln(n) rather than n.

### Tree Traversals

BST traversals produce nodes in systematic orders, each serving distinct purposes:

**Inorder Traversal** (Left → Root → Right): Produces keys in sorted (ascending) order. This is the most frequently used traversal for BST validation and sorted output.

**Preorder Traversal** (Root → Left → Right): Useful for copying trees and prefix expression evaluation.

**Postorder Traversal** (Left → Right → Root): Useful for deleting trees and postfix expression evaluation.

**Theorem 2**: Inorder traversal of a BST yields keys in non-decreasing order.

_Proof_: By induction on tree height. Base case: empty tree (trivially sorted). Inductive step: Assume left subtree yields sorted sequence L, root key is k, right subtree yields sorted sequence R. Since all keys in L < k < all keys in R (by BST property), the concatenated sequence L ∪ {k} ∪ R is sorted. ∎

### Successor and Predecessor Operations

Given a node x, the **successor** is the smallest key greater than key[x]. If the right subtree of x is non-empty, the successor is the minimum node in the right subtree. Otherwise, the successor is the lowest ancestor of x whose left child is also an ancestor of x.

The predecessor operation is symmetric: if left subtree is non-empty, return maximum of left subtree; otherwise, return highest ancestor whose right child is an ancestor.

Both operations run in O(h) time, making them essential for in-order tree iteration.

## Examples

### Example 1: Constructing a BST from Sequence

Insert keys [7, 3, 9, 1, 5, 8, 10] sequentially:

```
Step 1: Insert 7     Step 2: Insert 3     Step 3: Insert 9
         7                  7                  7
                               \                / \
                               3              3   9

Step 4: Insert 1     Step 5: Insert 5     Step 6: Insert 8
         7                  7                  7
        / \               / \
       3   9 / \                            3   9              3   9
      /                 / \                / \   \
     1                 1   5              1   5   10
                           \
                            8
```

The final inorder traversal yields: 1, 3, 5, 7, 8, 9, 10 (sorted).

### Example 2: Search Operation Complexity

Consider searching for key k=5 in the tree above:

- Compare with 7: 5 < 7, go left (1 comparison)
- Compare with 3: 5 > 3, go right (2 comparisons)
- Compare with 5: 5 = 5, found (3 comparisons)

The path length equals tree height (h=2), demonstrating O(h) complexity.

### Example 3: Deletion Cases

Delete node 3 from the constructed tree:

1. Node 3 has only one child (1): Replace 3 with its child 1.

Result:

```
       7
      / \
     1   9
      \
       5
        \
         8
          \
           10
```

### Example 4: Complexity Analysis

Given n = 1,000,000 nodes:

- Balanced BST (h ≈ 20): Search requires ≤ 21 comparisons
- Degenerate BST (h = 999,999): Search requires ≤ 1,000,000 comparisons

This demonstrates why balance is critical: logarithmic vs. linear performance.

## Exam Tips

1. **Always verify BST property** when analyzing trees: left subtree keys < node key < right subtree keys. Common exam questions ask you to identify whether a given tree satisfies BST properties.

2. **Remember height definitions**: Some texts define height of single node as 1 (others as 0), and empty tree height as 0 (others as -1). Consistency matters in complexity analysis.

3. **Traversal relationships**: Inorder produces sorted output. If you need descending order, perform reverse inorder (right → root → left) or inorder with comparison reversal.

4. **Deletion is most complex**: Study all three cases (leaf node, one child, two children). The two-child case requires finding inorder successor and replacing.

5. **Worst-case occurs with sorted input**: Inserting sorted data (1,2,3,4...) creates a degenerate tree with O(n) operations. This is a common exam scenario testing understanding of balance importance.

6. **Balance factors matter**: AVL trees require balance factor ∈ {-1, 0, 1} at all nodes. Rotations (LL, RR, LR, RL) are the correction mechanisms.

7. **Space complexity**: O(n) for storing n keys, O(h) for recursion stack space during operations. Some questions ask for both time and space.
