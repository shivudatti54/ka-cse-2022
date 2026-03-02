# Threaded Binary Trees


## Table of Contents

- [Threaded Binary Trees](#threaded-binary-trees)
- [1. Motivation: The NULL Pointer Waste Problem](#1-motivation-the-null-pointer-waste-problem)
  - [1.1 Theoretical Foundation](#11-theoretical-foundation)
  - [1.2 The Threading Solution](#12-the-threading-solution)
  - [1.3 Inorder Traversal Reference](#13-inorder-traversal-reference)
- [2. Classification of Threaded Binary Trees](#2-classification-of-threaded-binary-trees)
  - [2.1 Right-Threaded Binary Tree (Single Threading)](#21-right-threaded-binary-tree-single-threading)
  - [2.2 Left-Threaded Binary Tree (Single Threading)](#22-left-threaded-binary-tree-single-threading)
  - [2.3 Fully Threaded Binary Tree (Double Threading)](#23-fully-threaded-binary-tree-double-threading)
- [3. Thread Flags: Distinguishing Threads from Child Pointers](#3-thread-flags-distinguishing-threads-from-child-pointers)
  - [3.1 The Flag Problem](#31-the-flag-problem)
  - [3.2 Node Structure](#32-node-structure)
- [4. The Header Node (Sentinel)](#4-the-header-node-sentinel)
  - [4.1 Purpose](#41-purpose)
  - [4.2 Header Node Properties](#42-header-node-properties)
  - [4.3 Threading Convention with Header](#43-threading-convention-with-header)
- [5. Detailed Threading Example](#5-detailed-threading-example)
  - [5.1 Original Binary Tree](#51-original-binary-tree)
  - [5.2 Threaded Representation (Fully Threaded with Header)](#52-threaded-representation-fully-threaded-with-header)
  - [5.3 Visual Representation](#53-visual-representation)
- [6. Inorder Traversal Using Threads](#6-inorder-traversal-using-threads)
  - [6.1 Algorithm for Right-Threaded Binary Tree](#61-algorithm-for-right-threaded-binary-tree)
  - [6.2 C Implementation for Fully Threaded Tree](#62-c-implementation-for-fully-threaded-tree)
  - [6.3 Complexity Analysis](#63-complexity-analysis)
- [7. Insertion in Threaded Binary Trees](#7-insertion-in-threaded-binary-trees)
  - [7.1 Insertion in Right-Threaded Tree](#71-insertion-in-right-threaded-tree)
  - [7.2 Algorithm for Right-Threaded Insertion](#72-algorithm-for-right-threaded-insertion)
  - [7.3 Complexity Analysis](#73-complexity-analysis)
- [8. Memory Optimization Analysis](#8-memory-optimization-analysis)
  - [8.1 Comparative Study](#81-comparative-study)
  - [8.2 Practical Example](#82-practical-example)
- [Summary](#summary)
- [Assessment Questions](#assessment-questions)
  - [MCQ 1: Thread Identification](#mcq-1-thread-identification)
  - [MCQ 2: NULL Pointer Count](#mcq-2-null-pointer-count)
  - [MCQ 3: Threaded Traversal Space Complexity](#mcq-3-threaded-traversal-space-complexity)
  - [MCQ 4: Header Node Configuration](#mcq-4-header-node-configuration)
  - [MCQ 5: Insertion Impact](#mcq-5-insertion-impact)

## 1. Motivation: The NULL Pointer Waste Problem

### 1.1 Theoretical Foundation

In a conventional binary tree representation using linked lists, each node contains two pointer fields—`left` and `right`—resulting in a total of **2n pointer fields** for a tree containing **n nodes**. However, these pointer fields are severely underutilized.

**Theorem 1.1**: In any binary tree with **n nodes** (n ≥ 1), exactly **n + 1** pointer fields are NULL.

_Proof_:

- Total pointer fields = 2n
- Each node except the root has exactly one incoming pointer from its parent
- Therefore, used pointers (edges) = n - 1 (the root has no parent)
- Unused (NULL) pointers = 2n - (n - 1) = n + 1 ∎

This means more than **50%** of allocated pointer memory is wasted. For a tree with 100 nodes, 101 out of 200 pointer fields are NULL.

### 1.2 The Threading Solution

The fundamental insight behind threaded binary trees is elegant: **replace NULL pointers with useful navigation information**. Specifically, we replace NULL left pointers with pointers to the **inorder predecessor** of the node, and NULL right pointers with pointers to the **inorder successor**.

**Definition**: A **thread** is a pointer that replaces a NULL child pointer, pointing to the inorder predecessor (for left threads) or inorder successor (for right threads) of a node.

### 1.3 Inorder Traversal Reference

For a sample binary tree:

```
        A
       / \
      B   C
     / \ / \
    D  E F  G
```

The inorder traversal yields: **D, B, E, A, C, F, G**

This ordering is critical because threading connects nodes in this exact sequence.

---

## 2. Classification of Threaded Binary Trees

### 2.1 Right-Threaded Binary Tree (Single Threading)

In a right-threaded binary tree:

- If a node's **right child is NULL**, replace the right pointer with a thread to its **inorder successor**.
- The left pointer remains a standard child pointer (or NULL if no left child exists).
- This enables forward traversal without recursion or stack.

### 2.2 Left-Threaded Binary Tree (Single Threading)

In a left-threaded binary tree:

- If a node's **left child is NULL**, replace the left pointer with a thread to its **inorder predecessor**.
- The right pointer remains a standard child pointer.
- This enables backward traversal.

### 2.3 Fully Threaded Binary Tree (Double Threading)

A fully (or symmetrically) threaded binary tree applies **both** threading rules:

- NULL left pointers → inorder predecessor threads
- NULL right pointers → inorder successor threads

This bidirectional threading allows both forward and backward inorder traversal without auxiliary data structures.

---

## 3. Thread Flags: Distinguishing Threads from Child Pointers

### 3.1 The Flag Problem

Since a pointer field can now store either:

- A valid child pointer, OR
- A thread to predecessor/successor

We require additional information to disambiguate. Two boolean flags solve this:

| Flag      | Value = 0                     | Value = 1                        |
| --------- | ----------------------------- | -------------------------------- |
| `lthread` | `left` points to left child   | `left` is a thread (predecessor) |
| `rthread` | `right` points to right child | `right` is a thread (successor)  |

### 3.2 Node Structure

```c
typedef struct ThreadedNode {
    int data;
    struct ThreadedNode *left;   // child pointer or predecessor thread
    struct ThreadedNode *right;  // child pointer or successor thread
    int lthread;                 // 1 = thread, 0 = child pointer
    int rthread;                 // 1 = thread, 0 = child pointer
} ThreadedNode;
```

**Memory Comparison**:

- Regular binary tree node: 3 fields (data, left, right) = 3 × 4 bytes = 12 bytes (typical)
- Threaded binary tree node: 5 fields = 5 × 4 bytes = 20 bytes

**Trade-off Analysis**: For n nodes:

- Regular tree: 2n pointers, n+1 NULL (wasted)
- Threaded tree: Saves n+1 pointer traversals during inorder traversal at cost of n additional boolean flags

---

## 4. The Header Node (Sentinel)

### 4.1 Purpose

Boundary nodes present challenges:

- The **leftmost** node has no inorder predecessor
- The **rightmost** node has no inorder successor

A **header node** (sentinel) resolves these edge cases without special-case handling during traversal.

### 4.2 Header Node Properties

| Property  | Value                                   |
| --------- | --------------------------------------- |
| `left`    | Points to the root of the tree          |
| `right`   | Points to itself (header)               |
| `lthread` | 0 (left is a real child pointer)        |
| `rthread` | 1 (right is a thread to rightmost node) |

### 4.3 Threading Convention with Header

- The **leftmost node's** left thread → header node
- The **rightmost node's** right thread → header node
- This creates a **circular inorder structure**: header → inorder first → ... → inorder last → header

---

## 5. Detailed Threading Example

### 5.1 Original Binary Tree

```
        A
       / \
      B   C
     / \ / \
    D  E F  G
```

**Inorder traversal**: D → B → E → A → C → F → G

### 5.2 Threaded Representation (Fully Threaded with Header)

| Node   | left       | lthread | right      | rthread | Reasoning                            |
| ------ | ---------- | ------- | ---------- | ------- | ------------------------------------ |
| Header | root(A)    | 0       | Header     | 1       | Sentinel configuration               |
| A      | B (child)  | 0       | C (child)  | 0       | Both children exist                  |
| B      | D (child)  | 0       | E (child)  | 0       | Both children exist                  |
| C      | A (thread) | 1       | F (child)  | 0       | No left child; pred = A              |
| D      | Header     | 1       | B (thread) | 1       | No children; pred = Header, succ = B |
| E      | B (thread) | 1       | A (thread) | 1       | No children; pred = B, succ = A      |
| F      | C (thread) | 1       | G (child)  | 0       | No left child; pred = C              |
| G      | F (thread) | 1       | Header     | 1       | No children; pred = F, succ = Header |

### 5.3 Visual Representation

```
        HEADER
           ^
           |
           | (left thread from leftmost)
           |
           v
           A <---------------------------+
          / \                            |
         B   C                           | (right thread from rightmost)
        / \ / \                          |
       D   E F   G ---------------------+
       ^   ^ ^   ^
       |   | |   |
       +---++----+
     (inorder predecessor/successor threads)
```

---

## 6. Inorder Traversal Using Threads

### 6.1 Algorithm for Right-Threaded Binary Tree

The primary advantage: **O(n) time, O(1) space** traversal without recursion or stack.

**Pseudocode**:

```
function InorderThreadedTraversal(header):
    // Step 1: Find the leftmost node (inorder first)
    current = header->left
    while current != header:
        while current->lthread == 0:
            current = current->left

        // Step 2: Visit current node
        visit(current)

        // Step 3: Follow threads to visit all successors
        while current->rthread == 1:
            current = current->right
            visit(current)

        // Step 4: Move to right subtree
        current = current->right
```

### 6.2 C Implementation for Fully Threaded Tree

```c
void inorder(ThreadedNode *header) {
    ThreadedNode *current = header->left;  // Start at root

    while (current != header) {
        // Move to leftmost node
        while (current->lthread == 0) {
            current = current->left;
        }

        // Visit current node
        printf("%d ", current->data);

        // Follow right threads while they exist
        while (current->rthread == 1) {
            current = current->right;
            printf("%d ", current->data);
        }

        // Move to right subtree
        current = current->right;
    }
}
```

### 6.3 Complexity Analysis

| Aspect                    | Value                 | Explanation                                |
| ------------------------- | --------------------- | ------------------------------------------ |
| **Time Complexity**       | O(n)                  | Each node visited exactly once             |
| **Space Complexity**      | O(1)                  | Only pointer variables; no stack/recursion |
| **Regular BST Traversal** | O(n) time, O(h) space | Stack or recursion required (h = height)   |

**Theorem 6.1**: Threaded binary tree traversal achieves optimal space complexity O(1) while maintaining O(n) time complexity.

_Proof_: Each edge is traversed at most twice (once going down, once going up via thread), giving O(n) operations. Only a constant number of pointers are used regardless of tree size, yielding O(1) space. ∎

---

## 7. Insertion in Threaded Binary Trees

### 7.1 Insertion in Right-Threaded Tree

**Case 1**: Insert as left child of a node whose left child is NULL

- The new node's right thread points to the parent
- The new node's left thread points to parent's inorder predecessor
- Parent's left thread becomes 0 (now points to new child)

**Case 2**: Insert as right child of a node whose right child is NULL

- The new node inherits parent's right thread (successor)
- Parent's right thread now points to new node
- New node's right thread flag = 1

### 7.2 Algorithm for Right-Threaded Insertion

```c
void insertRightThreaded(ThreadedNode *root, ThreadedNode *parent, int key) {
    ThreadedNode *newNode = createNode(key);

    // Find insertion position
    ThreadedNode *current = root;
    ThreadedNode *par = NULL;

    while (current != NULL) {
        par = current;
        if (key < current->data) {
            if (current->lthread == 0)
                current = current->left;
            else
                break;  // Found position
        } else {
            if (current->rthread == 0)
                current = current->right;
            else
                break;
        }
    }

    // Attach new node
    newNode->right = par->right;
    newNode->rthread = par->rthread;
    newNode->left = par;
    newNode->lthread = 1;

    par->right = newNode;
    par->rthread = 0;
}
```

### 7.3 Complexity Analysis

| Operation           | Time Complexity | Space Complexity |
| ------------------- | --------------- | ---------------- |
| Search for position | O(h)            | O(1)             |
| Thread update       | O(1)            | O(1)             |
| **Total**           | **O(h)**        | **O(1)**         |

Where h is the height of the tree (O(log n) for balanced, O(n) for skewed).

---

## 8. Memory Optimization Analysis

### 8.1 Comparative Study

For a tree with **n nodes**:

| Metric                  | Regular Binary Tree | Threaded Binary Tree |
| ----------------------- | ------------------- | -------------------- |
| Total pointer fields    | 2n                  | 2n                   |
| NULL (unused) pointers  | n + 1               | 0                    |
| Thread pointers         | 0                   | n + 1                |
| Additional flags        | 0                   | 2n booleans          |
| Space for pointers      | 2n × 4 = 8n bytes   | 2n × 4 = 8n bytes    |
| Space for flags         | 0                   | 2n × 1 ≈ 2n bytes    |
| **Net pointer "waste"** | n + 1               | 0                    |

### 8.2 Practical Example

For n = 1000 nodes:

- Regular tree: 1001 NULL pointers wasted
- Threaded tree: All pointers utilized; 2000 boolean flags added
- Memory overhead: ~2000 bytes for flags
- Savings: Eliminates need for traversal stack (saves ~1000 pointers in worst case)

---

## Summary

Threaded binary trees transform wasted NULL pointers into useful navigation threads, enabling efficient O(1) space inorder traversal. The key concepts include:

1. **Thread Flags**: Boolean fields distinguishing child pointers from threads
2. **Header Node**: Sentinel enabling circular traversal
3. **Traversal Advantage**: O(n) time, O(1) space without recursion
4. **Trade-off**: Slight node overhead (2 extra boolean flags) for significant traversal efficiency

---

## Assessment Questions

### MCQ 1: Thread Identification

In a fully threaded binary tree, a node has `lthread = 1` and `rthread = 0`. Which of the following is TRUE about this node?

(A) Both left and right pointers are threads  
(B) Both left and right pointers are child pointers  
(C) Left pointer is a thread to inorder predecessor; right pointer is child  
(D) Right pointer is a thread to inorder successor; left pointer is child

**Answer**: (C)  
**Explanation**: lthread = 1 indicates left pointer is a thread (inorder predecessor), while rthread = 0 indicates right pointer points to a real right child.

### MCQ 2: NULL Pointer Count

A binary tree has 15 nodes. How many NULL pointers exist in its standard (non-threaded) representation?

(A) 14  
(B) 15  
(C) 16  
(D) 30

**Answer**: (C)  
**Explanation**: Using formula NULL pointers = n + 1 = 15 + 1 = 16. Total pointer fields = 2n = 30, used pointers = n - 1 = 14, so NULL = 30 - 14 = 16.

### MCQ 3: Threaded Traversal Space Complexity

What is the space complexity of inorder traversal in a fully threaded binary tree?

(A) O(n)  
(B) O(log n)  
(C) O(1)  
(D) O(h)

**Answer**: (C)  
**Explanation**: Threaded binary trees use threads to navigate, requiring only a constant number of pointer variables. No stack or recursion is needed, giving O(1) space complexity.

### MCQ 4: Header Node Configuration

In a right-threaded binary tree with header node, what is the value of `header->rthread`?

(A) 0  
(B) 1  
(C) Depends on tree structure  
(D) Undefined

**Answer**: (B)  
**Explanation**: The header node's right pointer always points to the rightmost node (via thread), so rthread = 1. This creates the circular structure for traversal.

### MCQ 5: Insertion Impact

After inserting a new node as the right child of a leaf node in a right-threaded binary tree, what must be updated?

(A) Only the parent's rthread  
(B) Only the new node's threads  
(C) Both parent's and new node's thread information  
(D) No thread updates needed

**Answer**: (C)  
**Explanation**: The parent now has a real right child (rthread becomes 0), and the new node must inherit the thread information that the parent previously had (its right thread points to the parent's inorder successor).
