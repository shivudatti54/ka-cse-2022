# Selection Trees


## Table of Contents

- [Selection Trees](#selection-trees)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Winner Trees (Min Selection Trees)](#winner-trees-min-selection-trees)
  - [Loser Trees (Max Selection Trees)](#loser-trees-max-selection-trees)
  - [Handling Non-Power-of-Two Leaf Counts](#handling-non-power-of-two-leaf-counts)
- [Examples](#examples)
  - [Example 1: Constructing a 4-way Winner Tree](#example-1-constructing-a-4-way-winner-tree)
  - [Example 2: Comparing Winner vs. Loser Tree Update Costs](#example-2-comparing-winner-vs-loser-tree-update-costs)
  - [Example 3: Non-Power-of-Two Leaves](#example-3-non-power-of-two-leaves)
- [Formal Pseudocode](#formal-pseudocode)
  - [Winner Tree Construction](#winner-tree-construction)
  - [Winner Tree Update](#winner-tree-update)
  - [Loser Tree Update](#loser-tree-update)
- [Complexity Analysis](#complexity-analysis)
- [Exam Tips](#exam-tips)

## Introduction

Selection Trees are specialized binary tree data structures designed to solve the problem of efficiently merging multiple sorted sequences. When dealing with k sorted lists that need to be combined into a single sorted sequence, naive approaches require significant comparisons. Selection trees provide an elegant solution by organizing the k initial elements in a tree structure, allowing us to identify the smallest (or largest) element among k candidates in O(1) time and update the structure in O(log k) time after each element is extracted.

The fundamental concept underlying selection trees is that we maintain a tree where each leaf node represents one element from one of the k sorted input sequences, and each internal node represents the "winner" (minimum or maximum) of its two children. This hierarchical comparison structure enables efficient merging operations critical in external sorting algorithms, where data may reside in slow storage devices and minimizing comparisons is paramount for performance.

Selection trees come in two primary variants: Winner Trees (also called Min Selection Trees) and Loser Trees (also called Max Selection Trees). Winner trees store the minimum element at the root, making them ideal for merging in ascending order, while loser trees store the maximum element at the root and are optimized for descending order merges. The loser tree variant offers a particular advantage: after extracting the winner, updating the tree requires only O(log k) comparisons rather than the O(k) comparisons needed in naive approaches.

## Key Concepts

### Winner Trees (Min Selection Trees)

A Winner Tree for k sorted sequences is a complete binary tree with k leaves and k-1 internal nodes. Each leaf node stores one element from one of the k sorted sequences, specifically the current element being processed from each sequence. Each internal node stores the smaller (winner) of its two children, and the root contains the overall minimum element among all k candidates.

**Construction**: The construction of a winner tree requires O(k) comparisons. Starting from the leaves, we compare pairs of elements and store the winner at their parent. This process continues level by level until the root is determined. The height of the tree is ⌈log₂k⌉, which determines the update complexity.

**Update Operation**: After removing the minimum element (the root) and replacing it with the next element from the same sorted sequence, we must update the tree. The update process starts at the leaf corresponding to the modified sequence and propagates upward, comparing the new element with its sibling and storing the winner at each level. This requires at most the height of the tree, which is O(log k) comparisons.

### Loser Trees (Max Selection Trees)

A Loser Tree inverts the winner tree logic: each internal node stores the larger (loser) of its two children, while an additional external array tracks the winners. This seemingly counterintuitive design provides a significant advantage during updates.

The key insight is that when we extract the winner from the root, we know the winner's identity but not the second-best candidate. In a winner tree, we would need to compare both children of the winner's path to find the next candidate. In a loser tree, each internal node already stores the loser from the comparison between its children—when we replace the winner with a new element, we only need to compare this new element with the stored loser at each level, which guarantees O(log k) comparisons without additional bookkeeping.

### Handling Non-Power-of-Two Leaf Counts

When k is not a power of two, the tree is not a perfect binary tree. We handle this by adding dummy (infinite) values to fill the leaf positions, ensuring a complete binary tree structure. The dummy values are set to positive infinity for min selection trees (so they never win) or negative infinity for max selection trees. This maintains the O(log k) update bound while simplifying the tree structure.

## Examples

### Example 1: Constructing a 4-way Winner Tree

Consider four sorted sequences: [3, 7, 9, 15], [1, 4, 8, 12], [2, 6, 10, 14], and [5, 11, 13, 16]. We wish to merge them using a winner tree.

**Step 1: Initialize leaves with first elements**
Leaf 0: 3, Leaf 1: 1, Leaf 2: 2, Leaf 3: 5

**Step 2: Build internal nodes level by level**

- Level 1: Compare (3, 1) → winner is 1, store at node 0
  Compare (2, 5) → winner is 2, store at node 1
- Level 2: Compare (1, 2) → winner is 1, store at root

The root contains 1 (the smallest element), which comes from Sequence 1. After extracting 1, we replace Leaf 1 with the next element from Sequence 1, which is 4. We then update the tree: at node 1, compare 4 with 2 → winner is 2; at root, compare 2 with 1 → winner is 1 (unchanged). Total comparisons: 3.

### Example 2: Comparing Winner vs. Loser Tree Update Costs

For k = 8 sequences, consider the update operation after extracting the current winner:

**Winner Tree Update**: After replacing the winner's leaf with the next element from its sequence, we must compare this new element with its sibling to determine the new winner at that node. However, we also need to compare this winner with the other child of each ancestor to determine if the path changed. This can require examining multiple nodes at each level.

**Loser Tree Update**: Each internal node already stores the loser from the previous comparison. When we insert a new element at a leaf, we simply compare it with the stored loser at each level. If the new element is smaller than the stored loser, it becomes the new winner and we continue upward. Otherwise, we replace the stored loser with the new element and stop. This guarantees exactly one comparison per level.

For 8 sequences (tree height = 3), loser tree update requires exactly 3 comparisons, while winner tree may require up to 6 comparisons in the worst case.

### Example 3: Non-Power-of-Two Leaves

Consider k = 5 sorted sequences. We need to add 3 dummy leaves with value +∞ to make it 8 leaves total:

Sequences: [2, 8], [1, 9], [5, 10], [3, 7], [4, 6]
Initial leaves: [2, 1, 5, 3, 4, ∞, ∞, ∞]

After building the tree with the standard comparison process, the root will contain 1 (from sequence 1). When we advance sequence 1 to element 9, the leaf becomes [2, 9, 5, 3, 4, ∞, ∞, ∞], and we update accordingly—the dummy infinity values ensure they never win, maintaining correct operation.

## Formal Pseudocode

### Winner Tree Construction

```
function buildWinnerTree(k, arrays):
    // Initialize leaves with first element from each array
    for i = 0 to k-1:
        tree[k + i] = arrays[i][0]
        arrayIndex[i] = 0  // Track current index in each array

    // Build internal nodes from bottom-up
    for i = k-1 down to 1:
        left = 2*i, right = 2*i + 1
        tree[i] = min(tree[left], tree[right])

    return tree
```

### Winner Tree Update

```
function updateWinnerTree(tree, k, modifiedLeaf, newValue):
    // Update the leaf
    pos = k + modifiedLeaf
    tree[pos] = newValue

    // Propagate upward
    while pos > 1:
        parent = pos / 2
        left = 2*parent, right = 2*parent + 1
        tree[parent] = min(tree[left], tree[right])
        pos = parent
```

### Loser Tree Update

```
function updateLoserTree(tree, k, modifiedLeaf, newValue):
    pos = k + modifiedLeaf
    tree[pos] = newValue

    // Compare with stored loser, not winner
    while pos > 1:
        parent = pos / 2
        sibling = 2*parent if (pos % 2 == 0) else 2*parent + 1

        // If new value is less than stored loser, swap
        if tree[pos] < tree[parent]:
            swap(tree[pos], tree[parent])

        pos = parent
```

## Complexity Analysis

**Construction Time**: Building a selection tree with k leaves requires comparing all k-1 internal nodes, each requiring one comparison. Therefore, construction time is Θ(k).

**Update Time**: After extracting the minimum element and replacing it with the next element from the corresponding sequence, we must update the path from that leaf to the root. The tree has height ⌈log₂k⌉, so update requires O(log k) comparisons in the worst case.

**Space Complexity**: The tree requires k leaves and k-1 internal nodes, totaling 2k-1 = Θ(k) space. This can be stored in a contiguous array of size 2k for simplicity.

**Proof of O(log k) Update Bound**: We prove by induction on tree height h that updating a selection tree requires at most h comparisons. For h = 0 (single node), no comparisons are needed. Assume the claim holds for trees of height h-1. When updating a tree of height h, we first update the leaf's sibling node (requiring 1 comparison to determine the new winner/loser), then recursively update the parent subtree of height h-1. By the induction hypothesis, this requires at most (h-1) comparisons. Total: 1 + (h-1) = h = ⌈log₂k⌉ comparisons. ∎

## Exam Tips

1. **Understand the fundamental difference**: Winner trees store the minimum at internal nodes and require comparing the new element with siblings at each level; loser trees store the maximum and compare with stored losers, guaranteeing exactly one comparison per level.

2. **Remember the height formula**: For k sorted sequences, the selection tree height is ⌈log₂k⌉, which directly determines the update complexity O(log k).

3. **Handle non-power-of-two cases**: When k is not a power of two, add dummy leaves with infinity values to complete the binary tree structure while preserving the O(log k) update bound.

4. **Compare with heap-based merging**: A binary heap requires O(k) time to build and O(log k) to extract minimum, but finding the minimum element requires O(1) access to root. Selection trees are specifically optimized for the repeated "find minimum and replace" pattern in k-way merging.

5. **Loser trees vs winner trees**: Remember that loser trees guarantee exactly one comparison per tree level during updates, while winner trees may require examining both children at each level.

6. **Space optimization**: Selection trees require exactly 2k-1 nodes for k sequences, stored efficiently in a complete binary tree array representation starting at index 1.

7. **Application context**: Selection trees are primarily used in external sorting where k sorted runs from tape or disk must be merged while minimizing expensive I/O operations.
   ===READ_MD===
