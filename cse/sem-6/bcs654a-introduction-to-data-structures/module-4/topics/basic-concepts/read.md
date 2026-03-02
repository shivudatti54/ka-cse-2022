# Basic Concepts of Trees in Data Structures

## Introduction

A **tree** is a hierarchical, non-linear data structure that simulates parent-child relationships through nodes and edges. Unlike linear structures like arrays and linked lists, trees enable efficient representation of nested relationships found in real-world systems. This makes them indispensable for:

1. **File Systems**: Directory structures with folders (internal nodes) and files (leaf nodes)
2. **Database Indexing**: B-trees and B+ trees for fast data retrieval
3. **Compilers**: Abstract Syntax Trees (AST) for program parsing
4. **Machine Learning**: Decision trees for classification tasks
5. **Networking**: Routing tables and multicast trees

**Formal Definition**: A tree T is a finite set of nodes where:

1. There exists one designated node called the **root**
2. The remaining nodes form _n ≥ 0_ disjoint subsets _T₁, T₂,..., Tₙ_, each being a tree
3. No cycles exist in the structure

Key advantages over linear structures:

- **O(log n)** search operations in balanced trees
- **Dynamic size management** without memory reallocation
- **Hierarchical data preservation** crucial for semantic relationships

## Tree Terminology & Mathematical Foundations

### Core Components

```
 A (Root, Level 0)
 / \
 B C (Level 1)
 / \ \
 D E F (Level 2)
 /
 G (Level 3)
```

1. **Node**: Fundamental unit containing data (e.g., A, B, ..., G)
2. **Root**: Topmost node with no parent (A)
3. **Parent & Child**:

- B is parent of D and E
- D is child of B

4. **Leaf/Terminal Node**: Node with degree 0 (G, E, F)
5. **Internal Node**: Non-leaf node (A, B, C, D)
6. **Edge**: Connection between nodes (A-B, B-D, etc.)

### Quantitative Properties

1. **Degree of Node**: Number of children

- Degree(A) = 2, Degree(C) = 1, Degree(G) = 0

2. **Tree Degree**: Maximum degree among all nodes
3. **Level**: Root = 0, children of root = 1, etc.
4. **Depth**: Number of edges from root to node

- Depth(G) = 3 (Path: A→B→D→G)

5. **Height**: Number of edges on longest root-to-leaf path

- Height(Tree) = 3 (Path to G)

6. **Ancestor/Descendant**:

- Ancestors of G: D, B, A
- Descendants of B: D, E, G

**Key Formulas**:

- Total nodes in full binary tree: _2^(h+1) - 1_ (where h = height)
- Minimum height for _n_ nodes: _⌈log₂(n+1)⌉ - 1_
- Maximum nodes at level _l_: _2^l_ (for binary trees)

## Tree Types & Structural Variations

### 1. General Tree

- Nodes can have any number of children
- Applications: Organization charts, XML parsing

### 2. Binary Tree

- Max degree = 2 (left child & right child)
- Types: Strict/Full, Complete, Perfect
- Applications: Expression trees, Huffman coding

### 3. Binary Search Tree (BST)

- Left child < Parent < Right child
- Operations: O(h) search/insert/delete
- Applications: Database indexing, auto-completion

### 4. N-ary Tree

- Nodes can have up to _n_ children
- Applications: File systems, trie structures

## Examples

### Example 1: Node Property Calculation

Given tree:

```
 M
 / \
 B Q
 / \ \
 A C Z
```

Calculate for each node:

- Depth
- Height
- Degree
- Type (Leaf/Internal)

**Solution**:

| Node | Depth | Height | Degree | Type     |
| ---- | ----- | ------ | ------ | -------- |
| M    | 0     | 2      | 2      | Internal |
| B    | 1     | 1      | 2      | Internal |
| Q    | 1     | 1      | 1      | Internal |
| A    | 2     | 0      | 0      | Leaf     |
| C    | 2     | 0      | 0      | Leaf     |
| Z    | 2     | 0      | 0      | Leaf     |

### Example 2: Real-World Application

**Problem**: Represent this organizational hierarchy as a tree:

- CEO
- CTO
- Development Manager
- QA Manager
- CFO
- Accounting Head

**Solution**:

```
 CEO
 / \
 CTO CFO
 / \ \
 Dev QA Accounting
```

Properties:

- Height = 2 (Longest path: CEO→CTO→Dev)
- Degree(CTO) = 2
- Leaf nodes: Dev, QA, Accounting

## Exam Tips

1. **Terminology Precision**:

- Height vs Depth: Height is bottom-up (leaves=0), Depth is top-down (root=0)
- Degree counts immediate children only

2. **Binary Tree Properties**:

- Maximum nodes at level _l_: _2^l_
- Total nodes in perfect BT: _2^(h+1)-1_

3. **Cycle Detection**:

- Trees are **acyclic by definition**
- Any cycle makes it a graph, not a tree

4. **Edge Count**:

- For _n_ nodes, exactly _n-1_ edges
- Critical for MCQ questions

5. **Real-World Analogy**:

- File systems: Folders=internal nodes, Files=leaves
- DOM tree: HTML elements as nodes

6. **Height Calculation**:

- Height of leaf node = 0
- Height of tree = height of root

7. **BST Property**:

- Left subtree < Root < Right subtree
- In-order traversal gives sorted sequence
