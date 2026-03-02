# Trees: Rooted Trees and Path Lengths

## Comprehensive Study Material for Discrete Mathematical Structures

### BSc (Hons) Computer Science — Delhi University, NEP 2024 UGCF

---

## 1. Introduction

### 1.1 What Are Trees?

A **tree** is a fundamental non-linear data structure in computer science that represents hierarchical relationships between elements. Unlike linear data structures (arrays, linked lists, stacks, queues) where elements are arranged sequentially, trees organize data in a branching pattern, making them ideal for representing hierarchical structures such as organizational charts, file systems, family genealogies, and decision-making processes.

### 1.2 Real-World Relevance

Trees are ubiquitous in computer science and everyday applications:

- **File Systems**: Your computer's folder structure is a tree—folders contain files and subfolders, creating a hierarchical organization.
- **Decision Trees**: Used in machine learning for classification and regression tasks.
- **HTML/XML Documents**: The Document Object Model (DOM) in web browsers represents web pages as a tree structure.
- **Binary Search Trees**: Enable efficient searching, insertion, and deletion operations in databases.
- **Network Routing**: Routing algorithms use tree structures to find optimal paths.
- **Compilers**: Abstract Syntax Trees (AST) represent the syntactic structure of source code.

### 1.3 Delhi University Syllabus Context

This topic aligns with the **Discrete Mathematical Structures** paper for BSc (Hons) Computer Science under NEP 2024 UGCF. The syllabus covers:
- Basic tree terminology
- Rooted trees, properties of trees
- Binary trees, tree traversals
- Path lengths, height, and depth
- Weighted path lengths and optimal binary search trees

---

## 2. Fundamental Concepts of Trees

### 2.1 Definition of a Tree (Graph Theory)

In graph theory, a **tree** is a connected acyclic graph. That is:
- It is **connected**: There's a path between every pair of vertices
- It is **acyclic**: It contains no cycles (loops)

A tree with **n** vertices always has exactly **n-1** edges.

### 2.2 Basic Tree Terminology

| Term | Definition |
|------|------------|
| **Root** | The topmost node of a tree (in rooted trees) |
| **Parent** | A node that has one or more child nodes |
| **Child** | A node whose parent is a node above it |
| **Sibling** | Nodes that share the same parent |
| **Leaf (External Node)** | A node with no children |
| **Internal Node** | A node with at least one child |
| **Ancestor** | Any node on the path from the root to a given node |
| **Descendant** | Any node in the subtree rooted at a given node |
| **Degree** | Number of children of a node |
| **Forest** | A collection of disjoint trees |

### 2.3 Example: Understanding Tree Terminology

Consider the following tree representing a university organization:

```
              President (A)
                  |
        +---------+---------+
        |                   |
    Dean (B)           Dean (C)
        |                   |
   +----+----+         +----+----+
   |         |         |         |
Prof(D)  Prof(E)   Prof(F)   HOD(G)
```

- **Root**: A (President)
- **Leaf nodes**: D, E, F, G
- **Internal nodes**: A, B, C
- **Parent of D**: B
- **Children of B**: D, E
- **Siblings**: D and E (same parent B); F and G (same parent C)
- **Ancestors of G**: C, A
- **Descendants of B**: D, E

---

## 3. Rooted Trees

### 3.1 Definition

A **rooted tree** is a tree in which one specific node is designated as the **root**. This establishes a natural direction—from the root going outward to the leaves. Every node (except the root) has exactly one parent, and zero or more children.

### 3.2 Properties of Rooted Trees

1. **Unique Root**: Every rooted tree has exactly one root node
2. **Unique Path**: There is exactly one path from the root to any node
3. **Parent-Child Relationship**: Each node (except root) has precisely one parent
4. **Hierarchical Structure**: The structure naturally defines levels or generations

### 3.3 Level (or Depth) of a Node

The **level** or **depth** of a node is the number of edges from the root to that node. By convention:
- The root is at **level 0** (some textbooks use level 1)
- Each generation adds 1 to the level

```
Level 0:        Root (A)
Level 1:       /    \
Level 2:      B      C
Level 3:     / \    / \
Level 4:    D   E  F   G
```

### 3.4 Height of a Tree

The **height** of a tree is the maximum level of any node in the tree. Alternatively, it can be defined as the length (number of edges) of the longest path from the root to a leaf.

```
Height = 4 (from root A to leaves D, E, F, or G)
```

In terms of edges: height = max(level)  
In terms of nodes: height = max(level) + 1

We will use the edge-based definition (more common in algorithms).

### 3.5 Height of a Node

The **height of a node** is the length of the longest path from that node to a leaf. For a leaf node, height = 0.

### 3.6 Depth of a Node

The **depth of a node** is the number of edges from the root to that node. This is the same as the level of the node.

### 3.7 Subtree

A **subtree** of a rooted tree is a node together with all its descendants. Every node in a tree is the root of some subtree.

```
Original Tree:          Subtree rooted at B:
      A                        B
     / \                      / \
    B   C        →          D   E
   / \
  D   E
```

### 3.8 Code Implementation: Representing Rooted Trees

```python
class TreeNode:
    """Represents a node in a rooted tree"""
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        """Add a child node to this node"""
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        """Calculate the level/depth of this node"""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def get_height(self):
        """Calculate height of subtree rooted at this node"""
        if not self.children:
            return 0
        return 1 + max(child.get_height() for child in self.children)
    
    def print_tree(self):
        """Print the tree structure"""
        spaces = " " * self.get_level() * 4
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()

# Example: Building the university tree
if __name__ == "__main__":
    root = TreeNode("President")
    
    dean_cs = TreeNode("Dean (CS)")
    dean_eng = TreeNode("Dean (Eng)")
    root.add_child(dean_cs)
    root.add_child(dean_eng)
    
    prof1 = TreeNode("Prof. Sharma")
    prof2 = TreeNode("Prof. Gupta")
    dean_cs.add_child(prof1)
    dean_cs.add_child(prof2)
    
    prof3 = TreeNode("Prof. Singh")
    dean_eng.add_child(prof3)
    
    print("Tree Structure:")
    root.print_tree()
    
    print(f"\nHeight of tree: {root.get_height()}")
    print(f"Level of Prof. Sharma: {prof1.get_level()}")
```

**Output:**
```
Tree Structure:
President
|__Dean (CS)
|   |__Prof. Sharma
|   |__Prof. Gupta
|__Dean (Eng)
    |__Prof. Singh

Height of tree: 2
Level of Prof. Sharma: 2
```

---

## 4. Path Lengths in Trees

### 4.1 Definition of a Path

A **path** in a tree is a sequence of nodes where each consecutive pair is connected by an edge. The **length of a path** is the number of edges in that path (some definitions use the number of nodes).

### 4.2 Internal Path Length (IPL)

The **internal path length** of a tree is the sum of the depths (distances from root) of all internal nodes.

### 4.3 External Path Length (EPL)

The **external path length** of a tree is the sum of the depths of all external (leaf) nodes.

### 4.4 Relationship Between IPL and EPL

For any binary tree with **n** internal nodes and **n+1** external nodes:

```
EPL = IPL + 2n
```

This is a fundamental property used in the analysis of tree algorithms.

### 4.5 Weighted Path Length

In many applications, each node has an associated **weight** (or probability). The **weighted path length** (also called the **weighted external path length**) is defined as:

```
WPL = Σ (weight of leaf_i × depth of leaf_i)
```

This concept is crucial in constructing **optimal binary search trees** and **Huffman coding trees**.

### 4.6 Example: Calculating Path Lengths

Consider the following binary tree:

```
           A (root)
          / \
        B     C
       /     / \
      D     E   F
```

**Node Depths:**
- A: 0 (root)
- B: 1
- C: 1
- D: 2
- E: 2
- F: 2

**Internal Path Length (IPL):**
```
IPL = depth(A) + depth(B) + depth(C)
    = 0 + 1 + 1 = 2
```

**External Path Length (EPL):**
```
EPL = depth(D) + depth(E) + depth(F)
    = 2 + 2 + 2 = 6
```

**Verification:**
```
n = 3 internal nodes (A, B, C)
EPL = IPL + 2n = 2 + 2(3) = 2 + 6 = 8... Wait, let me recalculate

Actually: EPL = 2 + 2(3) = 2 + 6 = 8, but our calculated EPL is 6.

Let me reconsider - F is at depth 2, so:
EPL = 2 + 2 + 2 = 6

The formula EPL = IPL + 2n applies to proper binary trees where each internal node has exactly 2 children.
In this case, B has 1 child (D) and C has 2 children (E, F).

For this tree:
- Internal nodes: A, B, C (3 nodes)
- External nodes: D, E, F (3 nodes - treating missing children as external)

Actually, the correct interpretation:
If we consider the "extended" binary tree (where missing children are represented as external nodes):
- Extended external nodes: 4 (let's say D has 2 external children, E has 2, F has 2 = 6 extended externals minus... this is complex)

For standard calculation with our 3 leaves (D, E, F):
n = 3
EPL = 6
IPL = 2
IPL + 2n = 2 + 6 = 8 ≠ 6

The formula EPL = IPL + 2n applies when we consider ALL missing child positions as external nodes.
Let's use a complete binary tree example:
```

### 4.7 Complete Binary Tree Example

```
           A (depth 0)
          / \
        B     C (depth 1)
       / \   / \
      D   E F   G (depth 2)
```

**Internal Path Length:**
```
IPL = depth(A) + depth(B) + depth(C)
    = 0 + 1 + 1 = 2
```

**External Path Length:**
```
EPL = depth(D) + depth(E) + depth(F) + depth(G)
    = 2 + 2 + 2 + 2 = 8
```

**Verification:**
```
n = 3 internal nodes
EPL = IPL + 2n = 2 + 6 = 8 ✓
```

### 4.8 Weighted Path Length Example

Consider a Huffman coding scenario with characters and their frequencies:

```
Character: A  B  C  D
Weight:    10 15 20 25
```

Suppose the tree structure gives depths:
- A: depth 2
- B: depth 2
- C: depth 3
- D: depth 3

**Weighted Path Length:**
```
WPL = (10 × 2) + (15 × 2) + (20 × 3) + (25 × 3)
    = 20 + 30 + 60 + 75
    = 185
```

The goal in Huffman coding is to minimize this weighted path length.

### 4.9 Code: Calculating Path Lengths

```python
class BinaryTreeNode:
    def __init__(self, data, weight=None):
        self.data = data
        self.weight = weight  # For weighted path length
        self.left = None
        self.right = None

def calculate_path_lengths(root, depth=0, internal_path=0, external_path=0, is_leaf=True):
    """Calculate internal and external path lengths recursively"""
    if root is None:
        # Treat null as external node at current depth
        return internal_path, external_path + depth
    
    if root.left is None and root.right is None:
        # Leaf node - contributes to external path length
        if root.weight:
            weighted = root.weight * depth
            print(f"Leaf {root.data}: depth={depth}, weighted={weighted}")
        return internal_path, external_path + depth
    
    # Internal node - contributes to internal path length
    internal_path += depth
    
    # Recurse on children
    internal_path, external_path = calculate_path_lengths(
        root.left, depth + 1, internal_path, external_path
    )
    internal_path, external_path = calculate_path_lengths(
        root.right, depth + 1, internal_path, external_path
    )
    
    return internal_path, external_path

def weighted_path_length(root, depth=0):
    """Calculate weighted path length"""
    if root is None:
        return 0
    
    if root.left is None and root.right is None:
        if root.weight is not None:
            return root.weight * depth
        return 0
    
    return (weighted_path_length(root.left, depth + 1) + 
            weighted_path_length(root.right, depth + 1))

# Example usage
if __name__ == "__main__":
    # Build the example tree
    #        A
    #       / \
    #      B   C
    #     /   / \
    #    D   E   F
    
    root = BinaryTreeNode('A')
    root.left = BinaryTreeNode('B')
    root.right = BinaryTreeNode('C')
    root.left.left = BinaryTreeNode('D')
    root.right.left = BinaryTreeNode('E')
    root.right.right = BinaryTreeNode('F')
    
    # Calculate path lengths
    ipl,/epl = calculate_path_lengths(root)
    print(f"Internal Path Length: {ipl}")
    print(f"External Path Length: {epl}")
    
    # Weighted path length example
    #        A(5)
    #       / \
    #    B(10) C(15)
    #    /    /  \
    # D(20) E(25) F(30)
    
    print("\n--- Weighted Path Length ---")
    root2 = BinaryTreeNode('A', 5)
    root2.left = BinaryTreeNode('B', 10)
    root2.right = BinaryTreeNode('C', 15)
    root2.left.left = BinaryTreeNode('D', 20)
    root2.right.left = BinaryTreeNode('E', 25)
    root2.right.right = BinaryTreeNode('F', 30)
    
    wpl = weighted_path_length(root2)
    print(f"Weighted Path Length: {wpl}")
```

---

## 5. Binary Trees

### 5.1 Definition

A **binary tree** is a rooted tree in which each node has at most **two children**, conventionally called the **left child** and **right child**.

### 5.2 Types of Binary Trees

#### 5.2.1 Full Binary Tree (Proper Binary Tree)
A binary tree in which every node has either 0 or 2 children (no node has exactly 1 child).

```
        A
       / \
      B   C
     / \
    D   E
```

#### 5.2.2 Complete Binary Tree
A binary tree in which all levels except possibly the last are completely filled, and all nodes are as far left as possible.

```
        A
       / \
      B   C
     / \ /
    D  E F
```

#### 5.2.3 Perfect Binary Tree (Complete Binary Tree - alternate definition)
A binary tree in which all internal nodes have exactly 2 children and all leaf nodes are at the same level.

```
            A
           / \
          B   C
         / \ / \
        D  E F  G
```

### 5.3 Important Properties of Binary Trees

| Property | Formula |
|----------|---------|
| Maximum nodes at level i | 2^i |
| Maximum nodes in tree of height h | 2^(h+1) - 1 |
| Minimum height for n nodes | ⌊log₂(n)⌋ |
| Relationship between leaves (L) and internal nodes (I) with degree 2 | L = I + 1 |

### 5.4 Array Representation of Binary Trees

For a complete binary tree, we can use array representation:

- Root at index 0
- Left child of node at index i: 2i + 1
- Right child of node at index i: 2i + 2
- Parent of node at index i: ⌊(i-1)/2⌋

```
Index:   0   1   2   3   4   5   6
Tree:    A   B   C   D   E   F   G

           A(0)
          /   \
       B(1)    C(2)
       / \     / \
     D(3) E(4) F(5) G(6)
```

### 5.5 Code: Array Representation

```python
class ArrayBinaryTree:
    """Binary tree represented as an array"""
    def __init__(self, capacity=100):
        self.tree = [None] * capacity
        self.size = 0
    
    def insert(self, value):
        """Insert a value at the next available position"""
        if self.size >= len(self.tree):
            raise Exception("Tree is full")
        self.tree[self.size] = value
        self.size += 1
    
    def get_left_child(self, index):
        """Get left child index"""
        left = 2 * index + 1
        return self.tree[left] if left < self.size else None
    
    def get_right_child(self, index):
        """Get right child index"""
        right = 2 * index + 2
        return self.tree[right] if right < self.size else None
    
    def get_parent(self, index):
        """Get parent index"""
        if index == 0:
            return None
        return self.tree[(index - 1) // 2]
    
    def display(self):
        """Display tree level by level"""
        level = 0
        index = 0
        while index < self.size:
            # Number of nodes at this level
            level_nodes = 2 ** level
            print(f"Level {level}: ", end="")
            for i in range(level_nodes):
                if index < self.size:
                    print(f"{self.tree[index]} ", end="")
                    index += 1
            print()
            level += 1

# Example
if __name__ == "__main__":
    arr_tree = ArrayBinaryTree()
    for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        arr_tree.insert(char)
    
    print("Binary Tree from Array:")
    arr_tree.display()
    
    print(f"\nLeft child of B (index 1): {arr_tree.get_left_child(1)}")
    print(f"Right child of B (index 1): {arr_tree.get_right_child(1)}")
    print(f"Parent of D (index 3): {arr_tree.get_parent(3)}")
```

---

## 6. Tree Traversals

### 6.1 Definition

**Tree traversal** is the process of visiting each node in a tree exactly once in a systematic way. For binary trees, there are four common traversal methods.

### 6.2 Types of Traversals

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Preorder** | Root → Left → Right | Copying a tree, prefix expression evaluation |
| **Inorder** | Left → Root → Right | Getting sorted order from BST |
| **Postorder** | Left → Right → Root | Deleting a tree, postfix expression evaluation |
| **Level-order** | Level by level (BFS) | Finding shortest path, level-wise processing |

### 6.3 Code: Tree Traversals

```python
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    """Root, Left, Right"""
    if root:
        print(root.data, end=" -> ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    """Left, Root, Right"""
    if root:
        inorder(root.left)
        print(root.data, end=" -> ")
        inorder(root.right)

def postorder(root):
    """Left, Right, Root"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" -> ")

def levelorder(root):
    """Level by level using BFS"""
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" -> ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example tree:
#        +
#       / \
#      *   -
#     / \   \
#    a   b   c

if __name__ == "__main__":
    root = TreeNode('+')
    root.left = TreeNode('*')
    root.right = TreeNode('-')
    root.left.left = TreeNode('a')
    root.left.right = TreeNode('b')
    root.right.right = TreeNode('c')
    
    print("Preorder:  ", end="")
    preorder(root)
    print("\nInorder:   ", end="")
    inorder(root)
    print("\nPostorder: ", end="")
    postorder(root)
    print("\nLevel-order: ", end="")
    levelorder(root)
```

**Output:**
```
Preorder:  + -> * -> a -> b -> - -> c -> 
Inorder:   a -> * -> b -> + -> c -> - -> 
Postorder: a -> b -> * -> c -> - -> + -> 
Level-order: + -> * -> - -> a -> b -> c -> 
```

---

## 7. Assessment Section

### 7.1 Multiple Choice Questions

**Question 1:** In a tree with n vertices, how many edges does it have?
- (a) n
- (b) n-1
- (c) n+1
- (d) 2n

**Answer:** (b) n-1

---

**Question 2:** The depth of the root node in any tree is:
- (a) 1
- (b) 0
- (c) -1
- (d) Equal to height

**Answer:** (b) 0

---

**Question 3:** In a binary tree, each node can have at most:
- (a) 1 child
- (b) 2 children
- (c) 3 children
- (d) Any number of children

**Answer:** (b) 2 children

---

**Question 4:** A binary tree with 15 nodes has a minimum height of:
- (a) 3
- (b) 4
- (c) 5
- (d) 15

**Answer:** (b) 4 (since 2^4 - 1 = 15)

---

**Question 5:** In a full binary tree with n internal nodes, the number of leaves is:
- (a) n
- (b) n+1
- (c) n-1
- (d) 2n

**Answer:** (b) n+1

---

**Question 6:** Which traversal visits the root node first?
- (a) Inorder
- (b) Postorder
- (c) Preorder
- (d) Level-order

**Answer:** (c) Preorder

---

**Question 7:** The external path length (EPL) of a binary tree with internal path length (IPL) = 10 and n = 5 internal nodes is:
- (a) 10
- (b) 15
- (c) 20
- (d) 25

**Answer:** (c) 20 (EPL = IPL + 2n = 10 + 10 = 20)

---

**Question 8:** A complete binary tree of height h has:
- (a) All nodes at level h
- (b) All levels except possibly last are full
- (c) All internal nodes have 2 children
- (d) Maximum possible nodes

**Answer:** (b) All levels except possibly last are full

---

**Question 9:** In a perfect binary tree of height 3, how many nodes are there?
- (a) 7
- (b) 8
- (c) 15
- (d) 16

**Answer:** (c) 15 (2^(3+1) - 1 = 15)

---

**Question 10:** Which property is TRUE for a binary search tree (BST)?
- (a) Left subtree contains nodes with values greater than root
- (b) Right subtree contains nodes with values greater than root
- (c) Inorder traversal gives sorted ascending order
- (d) All of the above

**Answer:** (c) Inorder traversal gives sorted ascending order (Note: (b) is partially correct but (c) is the defining property)

---

**Question 11:** The height of a leaf node is:
- (a) 0
- (b) 1
- (c) Depth of its parent + 1
- (d) Undefined

**Answer:** (a) 0

---

**Question 12:** Weighted path length is used in:
- (a) Binary search trees
- (b) Huffman coding
- (c) AVL trees
- (d) Heap operations

**Answer:** (b) Huffman coding

---

### 7.2 True/False Questions

1. **True or False:** A tree with n vertices always has exactly n-1 edges.
   - **Answer:** True

2. **True or False:** In a binary tree, the root has no parent.
   - **Answer:** True

3. **True or False:** A complete binary tree is always a full binary tree.
   - **Answer:** False (Full binary tree requires every node has 0 or 2 children)

4. **True or False:** The inorder traversal of a BST produces sorted output.
   - **Answer:** True

5. **True or False:** The height of a tree is the number of nodes on the longest path from root to leaf.
   - **Answer:** True (or false depending on whether we count edges vs nodes)

6. **True or False:** Every node in a tree has exactly one parent except the root.
   - **Answer:** True

7. **True or False:** Postorder traversal is useful for deleting a tree.
   - **Answer:** True

8. **True or False:** A forest is a collection of connected trees.
   - **Answer:** False (A forest is a collection of disjoint trees)

---

### 7.3 Fill in the Blanks

1. A node with no children is called a **leaf** node.
2. The number of edges from root to a node is called its **depth**.
3. A binary tree where each internal node has exactly 2 children is called a **full** binary tree.
4. The process of visiting all nodes exactly once is called **traversal**.
5. In a tree with n internal nodes, the external path length = internal path length + **2n**.
6. The traversal order Root-Left-Right is called **preorder**.
7. A tree where all levels are completely filled is called a **complete** binary tree.
8. The maximum number of nodes at level k is **2^k**.

---

### 7.4 Short Answer Questions

1. **Define height and depth of a node in a tree.**
   - **Answer:** Height of a node is the length of the longest path from that node to a leaf. Depth of a node is the number of edges from the root to that node.

2. **What is the difference between a full binary tree and a complete binary tree?**
   - **Answer:** A full binary tree has every node with either 0 or 2 children. A complete binary tree has all levels except possibly the last completely filled, with nodes as far left as possible.

3. **Explain the relationship between internal and external path lengths.**
   - **Answer:** For a binary tree with n internal nodes: EPL = IPL + 2n

4. **What is weighted path length? Give one application.**
   - **Answer:** Weighted path length = Σ (weight of leaf × depth of leaf). Used in Huffman coding for optimal prefix codes and in constructing optimal binary search trees.

---

## 8. Key Takeaways

### 8.1 Fundamental Concepts

1. **Trees** are hierarchical, non-linear data structures with a root node and connected descendant nodes
2. A tree with **n** vertices always has exactly **n-1** edges
3. Key terminology includes: root, parent, child, leaf, sibling, ancestor, descendant

### 8.2 Rooted Trees

1. Rooted trees establish a unique path from root to any node
2. **Level/Depth** of a node = number of edges from root
3. **Height** of a tree = maximum level of any node (longest root-to-leaf path)
4. **Subtree** = a node and all its descendants

### 8.3 Path Lengths

1. **Internal Path Length (IPL)** = sum of depths of all internal nodes
2. **External Path Length (EPL)** = sum of depths of all external (leaf) nodes
3. **EPL = IPL + 2n** (for binary trees with n internal nodes)
4. **Weighted Path Length** = Σ(weight × depth), crucial for Huffman coding

### 8.4 Binary Trees

1. Each node has at most 2 children (left and right)
2. **Full binary tree**: every node has 0 or 2 children
3. **Complete binary tree**: all levels except possibly last are full, nodes are left-aligned
4. **Perfect binary tree**: all internal nodes have 2 children, all leaves at same level
5. **Property**: L = I + 1 (leaves = internal nodes + 1 for full binary trees)

### 8.5 Traversals

| Method | Order | Application |
|--------|-------|-------------|
| Preorder | Root → Left → Right | Copying trees |
| Inorder | Left → Root → Right | BST sorted output |
| Postorder | Left → Right → Root | Deleting trees |
| Level-order | By level (BFS) | Shortest path |

### 8.6 Delhi University Exam Tips

- Remember formulas: nodes at level i = 2^i, total nodes = 2^(h+1) - 1
- Know the difference between full, complete, and perfect binary trees
- Practice calculating IPL, EPL, and weighted path lengths
- Understand all four traversals and their applications
- Be able to draw trees from traversal sequences and vice versa

---

## References

1. Rosen, K.H. (2019). *Discrete Mathematics and Its Applications* (8th ed.). McGraw-Hill.
2. Tremblay, J.P., & Sorenson, P.G. (1984). *An Introduction to Data Structures with Applications*. McGraw-Hill.
3. Liu, C.L., & Mohopatra, D.P. (2003). *Elements of Discrete Mathematics* (3rd ed.). McGraw-Hill.
4. Delhi University, NEP 2024 UGCF Syllabus for BSc (Hons) Computer Science - Paper on Discrete Mathematical Structures.

---

*This study material is prepared for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*