# Balanced Search Trees

## Table of Contents

- [Balanced Search Trees](#balanced-search-trees)
- [Introduction](#introduction)
- [1. AVL Trees](#1-avl-trees)
  - [1.1 Definition and Properties](#11-definition-and-properties)
  - [1.2 Height Analysis and Proof of Logarithmic Bound](#12-height-analysis-and-proof-of-logarithmic-bound)
  - [1.3 Rotations in AVL Trees](#13-rotations-in-avl-trees)
  - [1.4 Insertion Algorithm](#14-insertion-algorithm)
  - [1.5 Deletion Algorithm](#15-deletion-algorithm)
- [2. Red-Black Trees](#2-red-black-trees)
  - [2.1 Definition and Properties](#21-definition-and-properties)
  - [2.2 Height Analysis](#22-height-analysis)
  - [2.3 Insertion with Fixup](#23-insertion-with-fixup)
  - [2.4 Deletion with Fixup](#24-deletion-with-fixup)
- [3. B-Trees](#3-b-trees)
  - [3.1 Definition and Properties](#31-definition-and-properties)
  - [3.2 Height Analysis](#32-height-analysis)
  - [3.3 Operations](#33-operations)
- [4. Comparative Analysis](#4-comparative-analysis)
- [5. Practical Applications](#5-practical-applications)
- [Summary](#summary)
- [Assessment Questions](#assessment-questions)
  - [Question 1 (Application)](#question-1-application)
  - [Question 2 (Analysis)](#question-2-analysis)
  - [Question 3 (Computation)](#question-3-computation)
  - [Question 4 (Proof)](#question-4-proof)

## Introduction

Balanced search trees constitute a fundamental class of data structures in computer science that maintain sorted data while guaranteeing efficient search, insertion, and deletion operations in O(log n) time complexity. The primary limitation of basic binary search trees (BST) is their susceptibility to becoming unbalanced during insertions and deletions, which can degrade performance to O(n) in the worst case. This occurs when the input data arrives in sorted or nearly sorted order, causing the BST to degenerate into a linked list.

Balanced search trees address this fundamental problem by enforcing specific structural constraints that bound the tree's height to O(log n), regardless of the sequence of operations performed. The key insight is that by maintaining these balance conditions, we can guarantee logarithmic time complexity for all fundamental operations.

In this comprehensive module, we examine three major categories of balanced search trees: AVL Trees, Red-Black Trees, and B-Trees. Each represents a distinct approach to achieving balance, with different trade-offs between implementation complexity, height bounds, and operational efficiency. These data structures form the backbone of numerous critical systems, including database management systems, file systems, compiler implementations, and language runtime libraries. The Java Collections Framework (TreeMap, TreeSet), C++ Standard Template Library (std::map, std::set), and Python's sorted containers all employ balanced tree implementations to deliver predictable performance guarantees.

## 1. AVL Trees

### 1.1 Definition and Properties

An AVL tree, named after inventors G.M. Adelson-Velsky and E.M. Landis who introduced the concept in 1962, represents the earliest practical solution to the self-balancing binary search tree problem. AVL trees maintain balance through strict constraints on the height differential between subtrees.

**Formal Definition:**

An AVL tree is a binary search tree T such that for every node x ∈ T, the balance factor BF(x) satisfies:

```
BF(x) = height(left(x)) - height(right(x)) ∈ {-1, 0, +1}
```

where height(null) = -1 by convention.

**Key Properties:**

1. **Binary Search Tree Property:** For every node x, all keys in left(x) are less than key(x), and all keys in right(x) are greater than key(x).

2. **Balance Factor Constraint:** The absolute difference between heights of left and right subtrees is at most 1 for every node.

3. **Recursive Balance:** Every subtree of an AVL tree is itself an AVL tree.

### 1.2 Height Analysis and Proof of Logarithmic Bound

The critical theorem establishing AVL trees' efficiency guarantee is:

**Theorem:** The height h of an AVL tree with n nodes satisfies h < 1.44 log₂(n+2) - 0.328.

_Proof by Induction:_

Let N(h) represent the minimum number of nodes in an AVL tree of height h. We establish the recurrence:

- N(0) = 1 (single node)
- N(1) = 2 (root plus one child)
- For h ≥ 2, an AVL tree must have one subtree of height h-1 and the other of height at least h-2 (due to balance constraint)

Thus: N(h) = 1 + N(h-1) + N(h-2)

This recurrence generates the Fibonacci-like sequence: 1, 2, 3, 4, 7, 12, 20, 33, 54, 88, ...

We can prove by induction that N(h) > F(h+3) where F(k) is the k-th Fibonacci number. Since F(k) ≈ φ^k/√5 (where φ ≈ 1.618), we have:

n ≥ N(h) > φ^(h+3)/√5

Taking logarithms: h < log_φ(n) - 3 ≈ 1.44 log₂(n) - 3

Therefore, operations on AVL trees run in O(log n) time. ∎

### 1.3 Rotations in AVL Trees

When insertion or deletion violates the balance factor constraint, we perform structural modifications called rotations to restore balance without violating the BST property.

**Left Rotation (LL Case):**

```
 y x
 / \ / \
 x T3 ===> T1 y
 / \ / \
 T1 T2 T2 T3
```

The right-heavy node y with balance factor -2 triggers rotation. Node x becomes the new root, y becomes its right child, and T2 becomes y's left child.

**Right Rotation (RR Case):** Symmetric to left rotation, applied when balance factor is +2 with right child having balance factor ≥ 0.

**Left-Right Rotation (LR Case):**

```
 z z y
 / \ / \ / \
 y T4 ===> x T4 ===> x z
 / \ / \ / \ / \
 T1 x y T3 T1 T2 T3 T4
 / \ / \
 T2 T3 T1 T2
```

First, perform right rotation on left child y, then left rotation on z.

**Right-Left Rotation (RL Case):** Symmetric to LR case.

### 1.4 Insertion Algorithm

```
AVL-INSERT(T, z):
 y = NULL
 x = T.root
 while x ≠ NIL:
 y = x
 if z.key < x.key:
 x = x.left
 else:
 x = x.right
 z.parent = y
 if y == NULL:
 T.root = z
 else if z.key < y.key:
 y.left = z
 else:
 y.right = z
 z.left = NIL
 z.right = NIL
 z.color = RED // for RB trees
 // Update heights and fix AVL balance
 while y ≠ NULL:
 update height(y)
 if BF(y) = +2:
 if BF(y.left) = +1:
 RIGHT-ROTATE(y)
 else:
 LEFT-RIGHT-ROTATE(y)
 else if BF(y) = -2:
 if BF(y.right) = -1:
 LEFT-ROTATE(y)
 else:
 RIGHT-LEFT-ROTATE(y)
 y = y.parent
```

**Time Complexity:** O(log n) - we traverse O(log n) nodes to find insertion point, and rotations are constant-time operations affecting only O(log n) ancestors.

### 1.5 Deletion Algorithm

Deletion in AVL trees follows the standard BST deletion procedure followed by rebalancing along the path to the root. The algorithm must handle three cases: node has no children (simple removal), one child (splice out), or two children (replace with inorder successor and remove successor). After removal, we traverse upward, updating heights and performing necessary rotations.

## 2. Red-Black Trees

### 2.1 Definition and Properties

A Red-Black tree is a self-balancing binary search tree that achieves balance through color attributes and structural properties. Introduced by Guibas and Sedgewick in 1979, Red-Black trees require less restructuring than AVL trees but provide slightly weaker balance guarantees.

**Formal Definition:**

A Red-Black tree is a binary search tree where each node stores an extra bit representing its color (red or black), satisfying the following properties:

1. **Node Color:** Every node is either red or black.

2. **Root Property:** The root is always black.

3. **Leaf Property (NIL):** All leaf nodes (external NIL pointers) are black. In implementation, a single sentinel NIL node is often used.

4. **Red Property:** If a node is red, then both its children are black. Equivalently, no two red nodes can be adjacent on any root-to-leaf path.

5. **Black-Height Property:** For each node x, all paths from x to descendant leaves contain the same number of black nodes, denoted bh(x).

### 2.2 Height Analysis

**Lemma:** A Red-Black tree with n internal nodes has height h ≤ 2 log₂(n+1).

_Proof:_

Consider a node x with black-height bh(x). The subtree rooted at x contains at least 2^bh(x) - 1 internal nodes (can be proven by induction on bh).

Since the root has black-height at least h/2 (at least half the nodes on any path are black by the Red Property), we have:

n ≥ 2^(h/2) - 1

Therefore: h ≤ 2 log₂(n+1)

This guarantees O(log n) height, ensuring logarithmic time complexity for all operations. ∎

### 2.3 Insertion with Fixup

```
RB-INSERT-FIXUP(T, z):
 while z.parent.color = RED:
 if z.parent = z.parent.parent.left:
 y = z.parent.parent.right // uncle
 if y.color = RED:
 z.parent.color = BLACK
 y.color = BLACK
 z.parent.parent.color = RED
 z = z.parent.parent
 else:
 if z = z.parent.right:
 z = z.parent
 LEFT-ROTATE(T, z)
 z.parent.color = BLACK
 z.parent.parent.color = RED
 RIGHT-ROTATE(T, z.parent.parent)
 else: // symmetric case
 (swap left/right in above)
 T.root.color = BLACK
```

The fixup algorithm handles three cases based on uncle's color and triangle/line configuration, ensuring O(1) amortized rotations.

### 2.4 Deletion with Fixup

Deletion in Red-Black trees is more complex due to the need to maintain the Black-Height property when removing a black node. The fixup algorithm handles cases where the double-black problem arises, moving the imbalance upward through rotations and recoloring.

## 3. B-Trees

### 3.1 Definition and Properties

B-Trees, introduced by Bayer and McCreight in 1972, are balanced trees optimized for disk access. Unlike binary trees, B-Trees are multi-way search trees where nodes can contain multiple keys and have multiple children, minimizing disk I/O operations.

**Definition of B-Tree of order m:**

A B-Tree of minimum degree t (where m = 2t or 2t-1) satisfies:

1. **Node Capacity:** Every node can have at most m children and m-1 keys.

2. **Minimum Fill:** Except root, every node has at least ⌈m/2⌉ children.

3. **Root Property:** Root has at least 2 children if non-leaf.

4. **Level Property:** All leaves appear at the same level (external nodes contain no children).

5. **Key Ordering:** Keys within a node are sorted; keys in children fall between parent keys.

### 3.2 Height Analysis

**Theorem:** A B-Tree of order m with n keys has height h (number of edges from root to leaf) satisfying:

```
h ≤ log_⌈m/2⌉((n+1)/2) + 1
```

_Proof:_

At root: at least 2 children (if non-leaf)
At level 1: at least 2⌈m/2⌉ children
At level 2: at least 2⌈m/2⌉² children
...
At level h-1: at least 2⌈m/2⌉^(h-1) leaf nodes

Since leaves contain keys: n + 1 ≥ 2⌈m/2⌉^(h-1)

Taking logarithms: h - 1 ≤ log\_⌈m/2⌉((n+1)/2)

Therefore: h ≤ log\_⌈m/2⌉((n+1)/2) + 1 = O(log_m n)

Since disk block size determines m (typically m = 2^10 to 2^12), the height remains very small even for millions of keys.

### 3.3 Operations

**Search:** O(log_m n) - compare target with keys in current node, navigate to appropriate child.

**Insertion:** Find appropriate leaf; if leaf has room, insert key in sorted position; if full, split into two nodes, promote middle key to parent, recursively handle overflow.

**Deletion:** Complex cases include borrowing from siblings (when sibling has extra keys) and merging with sibling (when both have minimum keys), potentially propagating changes upward.

## 4. Comparative Analysis

| Aspect                   | AVL Trees           | Red-Black Trees                 | B-Trees               |
| ------------------------ | ------------------- | ------------------------------- | --------------------- |
| **Balance Criterion**    | Height diff ≤ 1     | Color properties + black-height | Node fill constraints |
| **Max Height**           | ~1.44 log₂n         | ~2 log₂n                        | ~log\_⌈m/2⌉(n)        |
| **Search Efficiency**    | Optimal             | Slightly less optimal           | Excellent for disk    |
| **Insertion Cost**       | More rotations      | Fewer rotations                 | Node splits           |
| **Memory Overhead**      | 1 integer (height)  | 1 bit (color)                   | Higher per node       |
| **Typical Applications** | In-memory databases | Language libraries              | File systems, DBs     |

**Theorem:** AVL trees provide faster lookups than Red-Black trees because they are more strictly balanced. However, Red-Black trees provide faster insertions and deletions on average.

_Proof Sketch:_ AVL trees may require O(log n) rotations per insertion, while Red-Black trees guarantee O(1) amortized rotations. The height difference (approximately 1.44 log n vs 2 log n) translates to roughly 10-15% more comparisons in AVL tree searches.

## 5. Practical Applications

1. **Database Systems:** B-Trees and B+Trees (variant) provide indexing for virtually all relational databases. The logarithmic height ensures minimal disk accesses.

2. **Language Runtime Libraries:** Java's TreeMap/TreeSet, C++ std::map/set, and Python's sortedcontainers use Red-Black trees for ordered associative containers.

3. **File Systems:** Modern file systems (NTFS, ext4, HFS+) use B-Trees for directory indexing and extent mapping.

4. **Compilers:** Symbol tables often implemented using balanced trees for efficient lookup during parsing.

## Summary

Balanced search trees solve the fundamental problem of worst-case degradation in binary search trees. AVL trees enforce strict height balance for optimal search, Red-Black trees provide relaxed balance with efficient updates, and B-Trees optimize for multi-way branching critical in disk-based storage. Understanding these structures and their underlying invariants is essential for designing efficient algorithms and selecting appropriate data structures for real-world applications.

---

## Assessment Questions

### Question 1 (Application)

Consider inserting the following keys sequentially into an initially empty AVL tree: 10, 20, 30, 40, 50, 25. After inserting 50, the tree becomes unbalanced. Draw the tree state before insertion of 50 and identify the specific rotation(s) needed to restore balance. Show the tree state after each rotation.

### Question 2 (Analysis)

Given a Red-Black tree property that no path from root to leaf is more than twice as long as any other, explain why this property holds. Provide a formal argument using the black-height property and explain how this relates to the O(log n) worst-case operation time.

### Question 3 (Computation)

For a B-Tree of order m = 7 (maximum 6 keys per node, minimum 3 children), calculate: (a) the maximum number of keys in a tree of height 3, (b) the minimum number of keys in a tree of height 3, and (c) the number of disk accesses required to search for a key in the worst case.

### Question 4 (Proof)

Prove that in an AVL tree of height h, the number of nodes N(h) satisfies N(h) ≥ F(h+3) - 1, where F(k) is the k-th Fibonacci number (F(0)=0, F(1)=1, F(k)=F(k-1)+F(k-2)). Use this to derive the bound h < 1.44 log₂ n.
