# Threaded Binary Trees

## Introduction

Binary trees, while fundamental to computer science, suffer from an inefficient utilization of memory due to the presence of null pointers. In a binary tree with n nodes, there are exactly n+1 null pointers (this can be proven by considering that each node has exactly two pointers, but only n-1 edges are used to connect nodes). These null pointers represent wasted memory space and missed opportunities for efficient traversal. Threaded binary trees, introduced by A.J. Perlis and C. Thornton in 1960, provide an elegant solution to this problem by replacing these null pointers with "threads" that point to predecessors or successors in some traversal order.

The primary motivation behind threaded binary trees is to enable efficient traversal without using recursion or stacks. In a standard binary tree, inorder traversal requires either recursion (which uses the call stack) or an explicit stack data structure. Both approaches consume additional memory proportional to the height of the tree, which can be O(n) in the worst case for skewed trees. Threaded binary trees eliminate this overhead by storing the traversal information directly in the tree structure itself, allowing for O(1) auxiliary space during traversals.

Threaded binary trees find practical applications in scenarios where memory is constrained and frequent traversals are required. They are particularly useful in implementing iterators for binary trees, database indexing structures, and embedded systems where stack space is limited. Understanding threaded binary trees also provides deeper insight into tree manipulations and pointer-based data structures, which is essential for any computer science student.

## Key Concepts

### The Problem with Standard Binary Trees

In a standard binary tree node structure, we typically have:
```
struct Node {
    DataType data;
    struct Node *left;
    struct Node *right;
};
```

Each node contains two pointer fields, but for leaf nodes and nodes with only one child, one or both pointers remain null. Consider a binary tree with n nodes: there are 2n pointer fields total. Since exactly n-1 edges connect the n nodes, exactly n-1 pointers are used to point to child nodes. This leaves 2n - (n-1) = n+1 null pointers. These null pointers represent wasted memory and missed connections.

### Threading Concept

Threaded binary trees replace null pointers with threads that connect nodes in a specific traversal order (most commonly inorder). A thread is essentially a pointer that, instead of pointing to a child node, points to the predecessor or successor of the current node in the desired traversal sequence.

To distinguish between regular child pointers and threads, we need additional flags or boolean fields in each node:
```
struct ThreadedNode {
    DataType data;
    struct ThreadedNode *left;
    struct ThreadedNode *right;
    int ltag;  // 0 = left points to child, 1 = left is a thread
    int rtag;  // 0 = right points to child, 1 = right is a thread
};
```

### Types of Threaded Binary Trees

Threaded binary trees can be classified based on which null pointers are threaded and the direction of threading:

**Single Threaded**: Only null right pointers (or null left pointers) are used for threading. This saves less memory but provides unidirectional traversal capability.

**Double Threaded**: Both null left pointers and null right pointers are used for threading. This allows traversal in both directions (forward and backward) and is the most common type.

**Left Threaded**: Only null left pointers are threaded to point to inorder predecessors.

**Right Threaded**: Only null right pointers are threaded to point to inorder successors.

Most textbooks and practical implementations focus on right-threaded binary trees (also called one-way threaded) and double-threaded binary trees (two-way threaded).

### Inorder Threading Rules

For a right-threaded binary tree (the most common variant), the threading rules are:

1. If the left child of a node is null, set the left pointer to point to its inorder predecessor.

2. If the right child of a node is null, set the right pointer to point to its inorder successor.

3. A special header node is often used to simplify traversal, where the left pointer of the header points to the first node in inorder traversal, and the right pointer points to the last node in inorder traversal.

### Traversing a Threaded Binary Tree

The key advantage of threaded binary trees is that they enable traversal without recursion or stacks. The algorithm for inorder traversal of a right-threaded binary tree works as follows:

1. Start from the root and always move to the left until reaching the leftmost node (this is the first node in inorder sequence).

2. Visit the current node.

3. If the right pointer is a thread (rtag = 1), follow the thread to the next node.

4. Otherwise (rtag = 0), move to the right child and repeat from step 2.

This process continues until we return to the header node, completing the traversal.

## Examples

### Example 1: Converting a Binary Tree to Right-Threaded Form

Consider the following binary tree:

```
        25
       /  \
      12   30
     /  \
    10  15
```

Step 1: Identify all null pointers and their traversal positions.

The inorder traversal of this tree is: 10, 12, 15, 25, 30

Step 2: Thread the null pointers according to inorder successor/predecessor:

- Node 10: Right child is null → thread to inorder successor (12)
- Node 15: Right child is null → thread to inorder successor (25)
- Node 25: Right child is null → thread to inorder successor (30)
- Node 30: Both children are null (no successor)
- Node 12: Both children exist, no threading needed
- Node 10: Left child is null, but its inorder predecessor doesn't exist in this tree

The resulting threaded tree structure:
```
        25
       /  \
      12   30 (thread to header)
     /  \
    10  15 (15's right threads to 25)
   /
  X    (10's left is null)
   \
    X  (10's right threads to 12)
```

### Example 2: Inorder Traversal of a Threaded Binary Tree

Given a right-threaded binary tree:

```
        H(Header)
       /  \
      25   /
     /  \
    12  30
   /   / \
  10  15  40
```

With threads: 10.right → 12, 15.right → 25, 30.right → 40, 40.right → header

Algorithm execution:

1. Start at root (25), move left to leftmost: 10
2. Visit 10 → print 10
3. 10.right is a thread → go to 12
4. Visit 12 → print 12
5. 12.right is a child (not thread) → go to 15
6. Visit 15 → print 15
7. 15.right is a thread → go to 25
8. Visit 25 → print 25
9. 25.right is a child → go to 30
10. Visit 30 → print 30
11. 30.right is a child → go to 40
12. Visit 40 → print 40
13. 40.right is a thread → go to header (traversal complete)

Output: 10, 12, 15, 25, 30, 40

### Example 3: Insertion in a Threaded Binary Tree

Inserting a new node in a threaded binary tree requires careful handling of threads. When inserting a node as the left child of a node X:

1. Set new node's left to X's left (which might be a thread to predecessor)
2. Set new node's right to X (since new node's inorder predecessor's successor is X)
3. Set X's left to new node
4. Update ltag flags appropriately

This maintains the threading property while inserting the new node in its correct inorder position.

## Exam Tips

1. **Remember the null pointer count**: There are exactly n+1 null pointers in a binary tree with n nodes. This is a fundamental property frequently tested in exams.

2. **Understand the difference between ltag and rtag**: Remember that ltag = 0 means left pointer points to a real child, while ltag = 1 means left pointer is a thread to the inorder predecessor.

3. **Threaded trees require no stack for traversal**: This is the primary advantage. In exams, when asked about the advantage of threaded binary trees, mention O(1) auxiliary space during traversal.

4. **Double threading vs single threading**: Double-threaded trees allow both forward (inorder successor) and backward (inorder predecessor) traversal, while single-threaded trees allow only one direction.

5. **The header node trick**: A dummy header node is often used to simplify traversal code. The header's left points to the first inorder node, and its right points to the last inorder node.

6. **Be prepared to draw threaded trees**: Questions often ask you to convert a regular binary tree into a threaded binary tree. Practice drawing both the tree structure and identifying which pointers become threads.

7. **Time and space complexity**: Remember that traversal of a threaded binary tree is O(n) time with O(1) space, compared to O(n) time and O(h) space for standard recursive traversal.