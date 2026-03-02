# Binary Search Trees (BST)

## Introduction
Binary Search Trees (BSTs) are hierarchical data structures that enable efficient searching, insertion, and deletion operations. A BST is a binary tree where each node has at most two children, and for every node, all elements in the left subtree are less than the node's value, while all elements in the right subtree are greater. This property enables O(h) time complexity for basic operations, where h is the tree height.

BSTs are fundamental in computer science due to their applications in database systems (indexing), filesystems (directory structures), and memory management. Their ordered nature makes them ideal for implementing ordered maps and sets. Modern applications include autocomplete features and decision tree algorithms in machine learning.

The balance between efficiency and implementation complexity makes BSTs a critical topic for MCA students. Understanding BST operations and their time/space tradeoffs is essential for designing optimized algorithms in technical interviews and real-world systems.

## Key Concepts
1. **Binary Tree Basics**
   - Root, parent, child, leaf nodes
   - Height vs depth: Height of tree = longest path from root to leaf
   - Complete vs perfect binary trees

2. **BST Properties**
   - Formal definition: For all nodes N, left_child(N) < N < right_child(N)
   - No duplicate values (unless modified implementation)
   - In-order traversal yields sorted sequence

3. **BST Operations**
   - **Search**: Recursive/iterative traversal using BST property
   - **Insertion**: Find correct position while maintaining BST property
   - **Deletion**:
     - Case 1: Node with no children (simple removal)
     - Case 2: Node with one child (bypass node)
     - Case 3: Node with two children (replace with in-order predecessor/successor)

4. **Traversal Methods**
   - In-order (LNR): Left, Node, Right → Sorted output
   - Pre-order (NLR): Node first → Copying tree structure
   - Post-order (LRN): Node last → Deleting trees
   - Level-order: Breadth-first using queues

5. **Balancing Techniques**
   - AVL Trees: Balance factor = height(left) - height(right) ∈ {-1,0,1}
   - Rotations: Left, Right, Left-Right, Right-Left rotations
   - Red-Black Trees: Color-based balancing (used in Java TreeMap)

## Examples
**Example 1: BST Construction**
Given sequence [8,3,10,1,6,14,4,7], construct BST step-by-step.

Solution:
1. Insert 8 as root
2. 3 < 8 → left child
3. 10 > 8 → right child
4. 1 < 3 → left of 3
5. 6 > 3 but <8 → right of 3
6. Continue until final structure:
```
        8
      /   \
     3    10
    / \     \
   1  6    14
     / \
    4   7
```

**Example 2: Node Deletion**
Delete node 3 from the above BST.

Solution:
1. Node 3 has two children (1 and 6)
2. Find in-order predecessor (max in left subtree = 1) or successor (min in right subtree = 4)
3. Choose successor: 4
4. Replace 3 with 4, then delete original 4 (now leaf node):
```
        8
      /   \
     4    10
    / \     \
   1  6    14
       \
        7
```

**Example 3: Validate BST**
Check if given tree is valid BST:
```
    5
   / \
  1   4
     / \
    3   6
```
Solution:
- Root 5: Left subtree (1 ≤5), Right subtree must be >5
- Node 4 violates as 4 <5 → Not a valid BST

## Exam Tips
1. Always verify BST property during insert/delete operations
2. For deletion with two children, clearly state whether using predecessor or successor
3. Practice drawing tree rotations for AVL balancing
4. Remember time complexities:
   - Balanced BST: O(log n) operations
   - Skewed BST: O(n) worst case
5. In-order traversal is key for sorted output and BST validation
6. Use iterative methods for traversal to avoid stack overflow in large trees
7. For diagram questions, label node values and clearly show left/right pointers