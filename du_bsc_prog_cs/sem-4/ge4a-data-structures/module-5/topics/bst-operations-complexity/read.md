# Binary Search Tree Operations and Complexity Analysis

## Introduction

A Binary Search Tree (BST) is one of the most fundamental data structures in computer science, serving as the backbone for many efficient searching, insertion, and deletion operations. In the context of the University of Delhi's Computer Science curriculum, understanding BST operations and their time complexity is essential for both theoretical knowledge and practical application.

A BST is a binary tree where each node has at most two children, with the key property that all nodes in the left subtree contain values less than the root's key, and all nodes in the right subtree contain values greater than the root's key. This ordering property enables efficient search operations, reducing the average search space by half at each level.

In real-world applications, BSTs are used extensively in database systems for indexing, in compiler symbol tables, in file systems, and in implementing associative arrays (like Python's dict or C++'s map). Understanding the complexity of BST operations helps in making informed decisions about when to use this data structure versus alternatives like arrays, linked lists, or hash tables.

## Key Concepts

### 1. Structure of a BST Node

Each node in a BST contains:
- **Key/Value**: The data being stored
- **Left Pointer**: Reference to the left child (values less than current)
- **Right Pointer**: Reference to the right child (values greater than current)

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

### 2. Search Operation

The search operation in a BST exploits the ordering property. Starting from the root, we compare the target value with the current node's key:
- If equal, we found the element
- If target is less, we go to the left subtree
- If target is greater, we go to the right subtree
- If we reach None, the element is not present

**Time Complexity Analysis**:
- **Best Case**: O(1) - when the searched element is at the root
- **Average Case**: O(log n) - when the tree is balanced
- **Worst Case**: O(n) - when the tree becomes degenerate (like a linked list)

### 3. Insertion Operation

Insertion follows the same path as search until we find an empty position. We never replace existing values; we always insert as a leaf node.

**Time Complexity Analysis**:
- **Best Case**: O(1) - inserting at root
- **Average Case**: O(log n) - balanced tree
- **Worst Case**: O(n) - degenerate tree

**Important**: Insertion order affects the tree shape. Inserting sorted data creates a degenerate tree!

### 4. Deletion Operation

Deletion is the most complex BST operation with three cases:

**Case 1: Node is a leaf** - Simply remove the node
**Case 2: Node has one child** - Replace node with its child
**Case 3: Node has two children** - Find in-order successor (smallest in right subtree) or in-order predecessor (largest in left subtree), replace the node's value with it, and delete that successor/predecessor

**Time Complexity**: O(h) where h is height, which is O(log n) average, O(n) worst case

### 5. Tree Traversal Methods

- **In-order**: Left → Root → Right (gives sorted order)
- **Pre-order**: Root → Left → Right (used for copying/serializing)
- **Post-order**: Left → Right → Root (used for deleting trees)

### 6. Height and Balance

The height of a node is the number of edges from that node to the deepest leaf. The height of the tree is the height of the root.

**Balance Factor**: For each node, balance factor = height(left subtree) - height(right subtree)

A BST is considered balanced if the height difference is at most 1 for all nodes. This ensures O(log n) operations.

### 7. Why Complexity Matters

The difference between O(n) and O(log n) is dramatic:
- For n = 1,000,000: log₂(1,000,000) ≈ 20
- For n = 1,000,000,000: log₂(1,000,000,000) ≈ 30

This is why balanced BSTs (like AVL, Red-Black trees) are crucial for real-world applications.

## Examples

### Example 1: Searching in a BST

Consider the following BST and search for key = 45:

```
        30
       /  \
     20    40
    /  \     \
   10  25    50
              \
               60
```

**Step-by-step search for 45**:
1. Start at root (30). Is 45 == 30? No. Is 45 > 30? Yes → Go right to 40
2. At node 40. Is 45 == 40? No. Is 45 > 40? Yes → Go right to 50
3. At node 50. Is 45 == 50? No. Is 45 > 50? No → Go left to None
4. Reached None: Element not found

**Complexity**: We visited 3 nodes (30, 40, 50). In a balanced tree with 7 nodes, this is O(log n) = O(3).

### Example 2: Insertion Operation

Insert keys: 50, 30, 70, 20, 40, 60, 80

**Step-by-step**:
1. Insert 50 as root
2. Insert 30: 30 < 50 → left of 50
3. Insert 70: 70 > 50 → right of 50
4. Insert 20: 20 < 50 → left to 30 → 20 < 30 → left of 30
5. Insert 40: 40 < 50 → left to 30 → 40 > 30 → right of 30
6. Insert 60: 60 > 50 → right to 70 → 60 < 70 → left of 70
7. Insert 80: 80 > 50 → right to 70 → 80 > 70 → right of 70

Final tree (balanced):
```
        50
       /  \
     30    70
    /  \   /  \
   20  40 60  80
```

**Complexity**: Each insertion takes O(h) time. For n insertions, total time is O(nh). For balanced tree, this is O(n log n).

### Example 3: Deletion with Two Children

Delete node 50 from:

```
        50
       /  \
     30    70
    /  \   /  \
   20  40 60  80
```

**Solution**:
1. Find in-order successor of 50 (smallest in right subtree): 60
2. Replace 50's value with 60
3. Delete the original 60 node (which is a leaf)

Result:
```
        60
       /  \
     30    70
    /  \     \
   20  40    80
```

**Complexity**: Finding successor takes O(h), deletion takes O(1). Total: O(h).

## Exam Tips

1. **Remember the recurrence relation**: For BST operations, the time complexity follows T(n) = T(n/2) + O(1), which solves to O(log n) in the average case.

2. **Draw trees for deletion**: For exam questions, always draw the BST when solving deletion problems. It helps visualize the in-order successor/predecessor selection.

3. **Distinguish between worst and average case**: The key differentiator is whether the tree is balanced. Be prepared to explain what "balanced" means.

4. **Insertion order matters**: Remember that inserting sorted data (1,2,3,4,5) creates a degenerate tree with O(n) operations. This is a common exam trick.

5. **In-order traversal gives sorted output**: This is a fundamental property of BSTs and is frequently tested.

6. **Space complexity is O(n)**: For all operations including traversal, the auxiliary space is O(n) in worst case (for skewed recursion), O(h) for balanced trees, and O(log n) average.

7. **Know when to use BST over hash tables**: BSTs maintain sorted order, support range queries, and provide O(log n) worst-case for ordered operations.