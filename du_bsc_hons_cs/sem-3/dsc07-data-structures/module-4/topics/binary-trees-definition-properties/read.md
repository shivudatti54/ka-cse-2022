# Binary Trees: Definition and Properties

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Binary trees** are one of the most fundamental and widely used data structures in computer science. Unlike linear data structures (arrays, linked lists, stacks, queues), trees represent **hierarchical relationships** between data elements, making them essential for solving complex computational problems.

### Real-World Applications

- **File Systems**: Directory and folder structures are represented as trees, where each folder can contain subfolders
- **Database Indexing**: B-trees and B+ trees are used in databases and file systems for efficient data retrieval
- **Decision Making**: Decision trees in machine learning and AI for classification and prediction
- **Expression Parsing**: Arithmetic expressions are evaluated using expression trees
- **DOM Structure**: Web browsers use tree structures to represent HTML/XML documents
- **Network Routing**: Routing algorithms use tree structures for optimal path finding
- **Compiler Design**: Abstract Syntax Trees (AST) parse and represent program code

Understanding binary trees is crucial for the Delhi University BSc (Hons) Computer Science curriculum, as it forms the foundation for advanced data structures like AVL trees, Red-Black trees, Heaps, and Binary Search Trees.

---

## 2. Definition of Binary Tree

A **binary tree** is a hierarchical data structure consisting of **nodes**, where:

1. Each node contains a **value** (or data)
2. Each node has at most **two children**, referred to as the **left child** and **right child**
3. There is exactly **one root node** (the topmost node)
4. Every node (except the root) has exactly **one parent**
5. The tree has no cycles

### Formal Definition

A binary tree T is either:
- **Empty** (null/φ) — a tree with no nodes
- **Non-empty** — consists of a root node R and two disjoint binary trees T₁ (left subtree) and T₂ (right subtree)

```
        Binary Tree Structure
        
              [Root]
             /      \
         [Left]    [Right]
         /    \    /    \
       Nil   Nil Nil   Nil
```

---

## 3. Key Terminology

Understanding the terminology is essential for grasping binary tree properties:

| Term | Definition |
|------|------------|
| **Root** | The topmost node of the tree with no parent |
| **Parent** | A node that has one or more child nodes |
| **Child** | A node descended from a parent node |
| **Leaf Node** | A node with no children (also called external node) |
| **Internal Node** | A node with at least one child |
| **Sibling** | Nodes sharing the same parent |
| **Ancestor** | Any node on the path from the root to a given node |
| **Descendant** | Any node in the subtree rooted at a given node |
| **Subtree** | A tree consisting of a node and all its descendants |
| **Depth of a node** | The number of edges from the root to that node |
| **Level of a node** | The depth + 1 (root is at level 1) |
| **Height of a node** | The number of edges on the longest path from that node to a leaf |
| **Height of a tree** | The height of the root node |
| **Degree of a node** | Number of children a node has (0, 1, or 2 in binary trees) |

### Clarifying Depth vs. Level

A common source of confusion in binary trees is the difference between **depth** and **level**:

- **Depth**: Starts from **0**. The root node has depth 0. It represents the number of edges from the root.
- **Level**: Starts from **1**. The root node is at level 1. It represents the "generation" number.

```
                    Level 1: [A]          ← Depth 0
                   /        \
        Level 2: [B]        [C]           ← Depth 1
        /        \          /    \
    Level 3: [D]  [E]    [F]    [G]       ← Depth 2
```

---

## 4. Properties of Binary Trees

### 4.1 Fundamental Relationships

For a binary tree with `n` nodes, `e` edges, and height `h`:

1. **Maximum nodes**: A binary tree of height `h` can have at most **2^(h+1) - 1** nodes (when all levels are completely filled)

2. **Minimum nodes**: A binary tree of height `h` has at least **h + 1** nodes (when each level has only one node — essentially a linked list)

3. **Edge-Node Relationship**: In any tree with `n` nodes, there are exactly **n - 1** edges

4. **Relationship between nodes at different levels**:
   - At level `i`, maximum nodes = **2^(i-1)** (where i starts from 1)
   - Height `h` means the tree has `h + 1` levels (if root is at level 0)

### 4.2 Types of Binary Trees

#### Perfect Binary Tree

A binary tree in which **all levels are completely filled**.

```
           [1]           ← Level 1
         /    \
       [2]    [3]        ← Level 2
      /  \    /  \
    [4]  [5][6]  [7]     ← Level 3
```

**Properties of Perfect Binary Tree**:
- All leaf nodes are at the same level
- If height = h, then: **Number of nodes = 2^(h+1) - 1**
- If number of nodes = n, then: **Height h = log₂(n+1) - 1**
- Number of leaf nodes = **2^h**
- Total nodes = 2^(height+1) - 1 = 2^3 - 1 = 7 nodes ✓

#### Strict/Full Binary Tree

A binary tree in which **every node has either 0 or 2 children** (no node has exactly 1 child).

```
           [1]           
         /    \
       [2]    [3]        
      /  \    /  \
    [4]  [5][6]  [7]     
```

**Properties of Strict Binary Tree**:
- If there are `i` internal nodes, total nodes = **2i + 1**
- Number of leaf nodes = **i + 1**
- Relationship: Leaf nodes = Internal nodes + 1

#### Complete Binary Tree

A binary tree in which **all levels except possibly the last are completely filled, and nodes are as far left as possible**.

```
           [1]           
         /    \
       [2]    [3]        
      /  \    /
    [4]  [5][6]  
```

**Properties of Complete Binary Tree**:
- Can be efficiently stored in an **array** (used in Heaps)
- For node at index `i`:
  - Left child at index: **2i + 1**
  - Right child at index: **2i + 2**
  - Parent at index: **floor((i-1)/2)**
- Height = **⌊log₂(n)⌋**

### 4.3 Important Formula Clarification

> **CRITICAL CORRECTION**: The formula **n = 2^h - 1** only applies to **perfect binary trees**, not all binary trees!

For **any** binary tree:
- **Minimum nodes** with height h: **h + 1** (degenerate tree)
- **Maximum nodes** with height h: **2^(h+1) - 1** (perfect binary tree)

---

## 5. Binary Tree Representation

Binary trees can be represented in two primary ways:

### 5.1 Array Representation (Sequential)

Used mainly for **complete binary trees** to save space.

```c
// Array representation in C
// Index:    0   1   2   3   4   5   6
// Tree:     A   B   C   D   E   F   G

char tree[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};

// For node at index i:
// - Parent: (i-1)/2
// - Left Child: 2i + 1
// - Right Child: 2i + 2
```

**Advantages**: No pointer overhead, cache-friendly
**Disadvantages**: Wastes space for sparse trees, difficult to insert/delete

### 5.2 Linked Representation (Pointer-based)

Each node contains data and pointers to left and right children.

```c
// Node structure in C
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

struct Node* root = NULL;
```

```python
# Node class in Python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
```

---

## 6. Binary Tree Traversals

**Traversal** means visiting every node in the tree systematically. There are two main categories:

### 6.1 Depth-First Search (DFS) Traversals

#### Preorder (Root → Left → Right)
- Visit root first
- Then traverse left subtree
- Then traverse right subtree

```
Preorder: A, B, D, E, C, F, G
```

#### Inorder (Left → Root → Right)
- Traverse left subtree first
- Visit root
- Then traverse right subtree

```
Inorder: D, B, E, A, F, C, G
```

#### Postorder (Left → Right → Root)
- Traverse left subtree
- Then right subtree
- Visit root last

```
Postorder: D, E, B, F, G, C, A
```

### 6.2 Breadth-First Search (BFS) — Level Order

Visit nodes level by level, from left to right.

```
Level Order: A, B, C, D, E, F, G
```

---

## 7. Examples with Correct Calculations

### Example 1: Perfect Binary Tree

```
Height = 2
Number of nodes = 2^(2+1) - 1 = 2^3 - 1 = 8 - 1 = 7 ✓
Number of leaf nodes = 2^2 = 4 ✓
```

### Example 2: Strict Binary Tree

```
Internal nodes: 3 (A, B, C)
Total nodes = 2(3) + 1 = 7 ✓
Leaf nodes = 3 + 1 = 4 ✓
```

### Example 3: Complete Binary Tree

```
Tree has 5 nodes: A, B, C, D, E

Structure:
        A
       / \
      B   C
     / \
    D   E

Height = floor(log₂(5)) = floor(2.32) = 2 ✓
NOT 3 as previously incorrectly stated!
```

### Example 4: Finding Height from Nodes

```
Given: A perfect binary tree has 31 nodes
Find: Height h

Solution:
n = 2^(h+1) - 1
31 = 2^(h+1) - 1
32 = 2^(h+1)
2^5 = 2^(h+1)
h + 1 = 5
h = 4 ✓
```

---

## 8. Implementation Examples

### 8.1 Creating a Binary Tree in C

```c
#include <stdio.h>
#include <stdlib.h>

// Node structure
struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Preorder traversal
void preorder(struct Node* root) {
    if (root != NULL) {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// Inorder traversal
void inorder(struct Node* root) {
    if (root != NULL) {
        inorder(root->left);
        printf("%d ", root->data);
        inorder(root->right);
    }
}

// Count nodes
int countNodes(struct Node* root) {
    if (root == NULL) return 0;
    return 1 + countNodes(root->left) + countNodes(root->right);
}

// Calculate height
int height(struct Node* root) {
    if (root == NULL) return -1;  // Empty tree has height -1
    int leftHeight = height(root->left);
    int rightHeight = height(root->right);
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

int main() {
    // Creating the tree:
    //       1
    //      / \
    //     2   3
    //    / \   \
    //   4   5   6
    
    struct Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->right->right = createNode(6);
    
    printf("Preorder: ");
    preorder(root);  // Output: 1 2 4 5 3 6
    
    printf("\nInorder: ");
    inorder(root);   // Output: 4 2 5 1 3 6
    
    printf("\nTotal nodes: %d", countNodes(root));  // Output: 6
    printf("\nHeight: %d", height(root));  // Output: 2
    
    return 0;
}
```

### 8.2 Level Order Traversal in Python

```python
from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node.data)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Build tree:    1
#              / \
#             2   3
#            / \   \
#           4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print("Level Order:", levelOrder(root))
# Output: [1, 2, 3, 4, 5, 6]
```

---

## 9. Delhi University Syllabus Context

This content aligns with the **NEP 2024 UGCF** syllabus for BSc (Hons) Computer Science, Delhi University:

| Topic | Coverage in This Material |
|-------|---------------------------|
| Binary Tree Definition | ✓ Complete definition with formal notation |
| Properties (Nodes, Height, Leaves) | ✓ All properties with formulas |
| Types (Perfect, Strict, Complete) | ✓ Detailed explanation with examples |
| Representation (Array, Linked) | ✓ Both methods with code |
| Traversal Methods | ✓ Preorder, Inorder, Postorder, Level-order |
| Implementation | ✓ C and Python examples |
| Practical Applications | ✓ Real-world relevance |

---

## 10. Key Takeaways

1. **Binary trees** are hierarchical structures with each node having at most two children (left and right)

2. **Depth vs Level**: Depth starts from 0, level starts from 1. The root has depth 0 and level 1

3. **The formula n = 2^h - 1 only applies to perfect binary trees**, not all binary trees!

4. **Three important types**:
   - **Perfect**: All levels completely filled
   - **Strict/Full**: Every node has 0 or 2 children
   - **Complete**: All levels filled except possibly last, nodes are left-aligned

5. **Four traversal methods**:
   - Preorder (Root → Left → Right)
   - Inorder (Left → Root → Right)
   - Postorder (Left → Right → Root)
   - Level-order (Breadth-first)

6. **Array representation** works best for complete binary trees; **linked representation** is more flexible

7. **Height of tree** with n nodes: Minimum = ⌈log₂(n+1)⌉ - 1 (for complete), Maximum = n - 1 (for degenerate)

---

## 11. Assessment

### Multiple Choice Questions

**Easy Level**

1. In a binary tree, each node can have at most how many children?
   - (a) 1
   - (b) 2 ✓
   - (c) 3
   - (d) Unlimited

2. What is the maximum number of nodes in a binary tree of height h (height = number of edges)?
   - (a) 2h
   - (b) 2^h
   - (c) 2^(h+1) - 1 ✓
   - (d) h²

3. Which traversal visits the root node first?
   - (a) Inorder
   - (b) Postorder
   - (c) Preorder ✓
   - (d) Level-order

**Medium Level**

4. In a perfect binary tree of height 2, how many leaf nodes are there?
   - (a) 2
   - (b) 3
   - (c) 4 ✓
   - (d) 7

5. In a strict (full) binary tree with 10 internal nodes, how many total nodes are there?
   - (a) 10
   - (b) 19
   - (c) 20
   - (d) 21 ✓

6. For a complete binary tree stored in an array, what is the index of the right child of the node at index i?
   - (a) 2i
   - (b) 2i + 1
   - (c) 2i + 2 ✓
   - (d) i + 1

**Hard Level**

7. A binary tree has 15 nodes. The maximum possible height is:
   - (a) 3
   - (b) 4
   - (c) 14 ✓
   - (d) 15

8. In a binary tree, if the root is at level 1, what is the depth of a node at level 5?
   - (a) 4 ✓
   - (b) 5
   - (c) 6
   - (d) 3

9. Which property is TRUE for a strict binary tree?
   - (a) All leaf nodes are at the same level
   - (b) Number of leaf nodes = Number of internal nodes + 1 ✓
   - (c) It is always complete
   - (d) Height = log₂(n)

10. The inorder traversal of a binary search tree always gives:
    - (a) Sorted order ✓
    - (b) Reverse sorted order
    - (c) Random order
    - (d) Level by level order

### Fill in the Blanks

1. A binary tree with height 0 has exactly **1** node.
2. In a binary tree with n nodes, there are exactly **n-1** edges.
3. A binary tree where each node has exactly one child is called a **degenerate** (or skewed) tree.
4. The process of visiting all nodes in a tree is called **traversal**.
5. A binary tree with all levels completely filled is called a **perfect** binary tree.

---

## 12. Flashcards

| # | Question | Answer |
|---|----------|--------|
| 1 | What is the maximum number of nodes in a binary tree of height h? | 2^(h+1) - 1 (for perfect binary tree) |
| 2 | How many children can a node have in a binary tree? | At most 2 (left and right) |
| 3 | What type of binary tree has all leaf nodes at the same level? | Perfect binary tree |
| 4 | What is the traversal order: Left → Root → Right? | Inorder traversal |
| 5 | In array representation, what is the index of the left child of node at index i? | 2i + 1 |
| 6 | What type of binary tree has nodes as far left as possible in the last level? | Complete binary tree |
| 7 | How many leaf nodes does a perfect binary tree of height h have? | 2^h |
| 8 | What is the height of an empty tree? | -1 |
| 9 | In a strict binary tree with i internal nodes, how many total nodes? | 2i + 1 |
| 10 | What traversal gives sorted output for a BST? | Inorder traversal |

---

*Study Material prepared for Delhi University BSc (Hons) Computer Science — NEP 2024 UGCF*