# Tree Definitions and Properties

## Introduction

A **tree** is a fundamental non-linear data structure in computer science that represents a hierarchical relationship between elements. Unlike linear data structures such as arrays, linked lists, stacks, and queues where elements are arranged sequentially, trees organize data in a branching structure that efficiently supports operations like searching, insertion, deletion, and traversal.

Trees are extensively used in various real-world applications: file systems use tree structures to organize directories and files, organizational charts represent reporting relationships as trees, the Document Object Model (DOM) in web development uses a tree structure to represent HTML documents, and decision trees are employed in machine learning for classification and regression tasks. In compiler design, parse trees represent the syntactic structure of source code, while binary search trees enable efficient O(log n) average-case searching.

For University of Delhi's Computer Science program, understanding tree definitions and properties forms the foundation for studying more advanced tree variants like Binary Search Trees, AVL Trees, B-Trees, and Heap data structures.

## Key Concepts

### Basic Tree Terminology

**Node**: Each element in a tree is called a node. A node contains data and may contain references (pointers) to its child nodes.

**Root**: The topmost node of a tree is called the root. It is the only node in the tree that has no parent. Every tree must have exactly one root.

**Edge (Link)**: A connection between two nodes is called an edge or link. If a node P is the parent of node C, there is an edge connecting P and C.

**Parent**: A node that has one or more child nodes is called a parent node.

**Child**: A node that has a parent node is called a child node.

**Sibling**: Nodes that share the same parent are called siblings.

**Leaf Node (External Node)**: A node that has no children is called a leaf node or terminal node.

**Internal Node (Non-Leaf Node)**: A node that has at least one child is called an internal node.

**Ancestor**: Any node on the path from the root to a given node is an ancestor of that node. The root is an ancestor of all nodes.

**Descendant**: Any node in the subtree rooted at a given node is a descendant of that node.

**Degree of a Node**: The number of children a node has is called its degree. A leaf node has degree 0.

**Degree of a Tree**: The maximum degree of any node in the tree is called the degree of the tree.

### Key Properties of Trees

**Level (Depth)**:
- The root node is at level 0 (or level 1, depending on convention).
- Each subsequent level contains nodes that are one edge away from the level above.
- If a node is at level L, its children are at level L+1.

**Height of a Node**: The height of a node is the number of edges on the longest path from that node to a leaf node. A leaf node has height 0.

**Depth of a Node**: The depth of a node is the number of edges from the root node to that node. The root has depth 0.

**Height of a Tree**: The height of a tree is the maximum level of any node in the tree. Equivalently, it is the length of the longest path from the root to a leaf.

**Subtree**: A subtree is a portion of a tree that itself forms a tree. If node R has children C1, C2, ..., Ck, then each node Ci and all its descendants form a subtree rooted at Ci.

### Important Tree Theorems

**Theorem 1**: A tree with n nodes has exactly (n-1) edges.

*Proof*: Every node except the root has exactly one edge connecting it to its parent. Since there are n-1 non-root nodes, there must be n-1 edges.

**Theorem 2**: If a tree has maximum degree d, then it has at least d+1 nodes.

*Proof*: This follows from the handshaking lemma in graph theory applied to trees.

**Theorem 3**: In a tree with n nodes, there is exactly one path between any two nodes.

*Proof*: Since trees are connected acyclic graphs, there cannot be multiple distinct paths between nodes.

### Types of Trees

**Empty Tree**: A tree with zero nodes (null tree).

**Binary Tree**: A tree where each node has at most two children. These children are typically referred to as the left child and right child.

**Full Binary Tree**: A binary tree where every node has either 0 or 2 children (no nodes with exactly 1 child).

**Complete Binary Tree**: A binary tree where all levels except possibly the last are completely filled, and all nodes are as far left as possible.

**Perfect Binary Tree**: A binary tree where all internal nodes have exactly 2 children and all leaf nodes are at the same level.

**Balanced Binary Tree**: A binary tree where the height difference between left and right subtrees of any node is at most 1.

**Binary Search Tree (BST)**: A binary tree where for each node, all nodes in its left subtree have values less than the node, and all nodes in its right subtree have values greater than the node.

## Examples

### Example 1: Identifying Tree Properties

Consider the following tree structure:

```
         A
        / \
       B   C
      / \   \
     D   E   F
        /
       G
```

Calculate the following:
1. Number of nodes
2. Number of edges
3. Height of the tree
4. Height of node B
5. Depth of node G
6. Degree of node A
7. Number of leaf nodes

**Solution**:

1. **Number of nodes**: 7 (A, B, C, D, E, F, G)

2. **Number of edges**: 6 (n-1 = 7-1 = 6)
   - Edges: A-B, A-C, B-D, B-E, C-F, E-G

3. **Height of the tree**: 3
   - Path from root A to deepest leaf: A → B → E → G (3 edges)

4. **Height of node B**: 2
   - Longest path from B to leaf: B → E → G (2 edges)

5. **Depth of node G**: 3
   - Path from root A to G: A → B → E → G (3 edges)

6. **Degree of node A**: 2 (has children B and C)

7. **Number of leaf nodes**: 3 (D, F, G are nodes with no children)

### Example 2: Verifying Tree Properties

Given a tree with 10 nodes:
- How many edges does it have?
- What is the maximum possible height?
- What is the minimum possible height?

**Solution**:

1. **Number of edges**: By Theorem 1, a tree with n nodes has exactly n-1 edges.
   - Therefore: 10 - 1 = **9 edges**

2. **Maximum possible height**: A tree can be skewed (like a linked list) where each node has exactly one child.
   - Height = n - 1 = 10 - 1 = **9** (root at level 0, last node at level 9)

3. **Minimum possible height**: Achieved by a complete or perfectly balanced tree.
   - For 10 nodes, a perfectly balanced tree would have height approximately log₂(10) ≈ 3.something
   - Minimum height = **3** (root at level 0, deepest leaves at level 3)

### Example 3: Complete Binary Tree Verification

Is the following tree a complete binary tree?

```
         1
        / \
       2   3
      / \ /
     4  5 6
```

**Solution**:

For a complete binary tree:
- All levels except possibly the last are completely filled
- The last level has all nodes as far left as possible

**Analysis**:
- Level 0: Node 1 (completely filled)
- Level 1: Nodes 2, 3 (completely filled)
- Level 2: Nodes 4, 5, 6 (last level)

Node 6 is the leftmost node at level 2, which satisfies the condition. Node 5 has a child, and node 4 has no children—however, in a complete binary tree, the nodes at the last level need not all be leaves; they just need to be as far left as possible.

**Verdict**: This is **NOT** a complete binary tree because node 3 at level 1 has a child (node 6), but node 4 at level 2 exists to its left without children. The violation is that not all nodes at level 1 (except possibly level 1) are filled.

A correct complete binary tree with 6 nodes would be:

```
         1
        / \
       2   3
      / \ /
     4  5 6
```

Wait—this is actually correct. Let me reconsider: In this tree, node 6 is the leftmost available position at level 2, and there are no gaps. This **IS** a complete binary tree.

## Exam Tips

1. **Remember the fundamental property**: A tree with n nodes always has exactly n-1 edges. This is frequently tested in exams.

2. **Distinguish between height and depth**: Height is measured from a node going downward to leaves; depth is measured from the root going upward to the node.

3. **Binary tree array representation**: For a complete binary tree with n nodes stored in an array indexed from 1:
   - Parent of node at index i: floor(i/2)
   - Left child of node at index i: 2i
   - Right child of node at index i: 2i+1
   This is essential for heap implementations.

4. **Maximum nodes at level L**: A binary tree can have at most 2^L nodes at level L (if root is at level 0).

5. **Maximum nodes in tree of height H**: A binary tree of height H can have at most 2^(H+1) - 1 nodes (perfect binary tree case).

6. **Leaf vs internal node count**: In any binary tree, the number of leaf nodes = number of nodes with degree 2 + 1 (for non-empty trees). This is derived from the property: L = I + 1 where L = leaf nodes and I = internal nodes with 2 children.

7. **Don't confuse tree types**: A full binary tree has nodes with 0 or 2 children; a complete binary tree allows 1 child only at the last level and must be left-justified.

8. **Practice identifying properties**: Given a tree diagram, be prepared to identify root, parent-child relationships, siblings, ancestors, descendants, leaf nodes, height, and depth.

9. **Remember the recursive definition**: A tree is either empty or consists of a root and zero or more subtrees (which are themselves trees).

10. **Space-time tradeoff**: Tree structures provide O(log n) average-case operations but require extra memory for storing child pointers.