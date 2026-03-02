# Threaded Binary Trees

## Introduction

Binary trees are fundamental data structures in computer science, used extensively in applications ranging from expression parsing to symbol tables and database indexing. However, traditional binary tree implementations suffer from a significant inefficiency: many node pointers remain null, creating "wasted" memory space. In a binary tree with n nodes, there are exactly n+1 null pointers (a well-known result following from the property that a binary tree with n nodes has n+1 null links). This observation led to the development of threaded binary trees, an elegant solution that transforms these null pointers into useful navigation links called "threads."

Threaded binary trees were introduced by A.J. Perlis and C. Thornton in 1960 as a method to make tree traversals more efficient without using stacks or recursion. By replacing null pointers with threads that connect nodes in a specific traversal order, we can traverse the entire tree iteratively without auxiliary data structures. This optimization is particularly valuable in systems with limited memory or in real-time applications where stack usage must be minimized. Threaded binary trees represent a classic example of space-time tradeoff in data structure design, trading slightly increased complexity in insertion and deletion operations for more efficient traversal.

## Key Concepts

### The Threading Concept

In a standard binary tree node, we typically store three fields: LEFT child pointer, RIGHT child pointer, and DATA. In a threaded binary tree, we add two additional boolean flags (often called LTHREAD and RTHREAD) that indicate whether the left and right pointers are actual child links or threads. When LTHREAD is TRUE, the LEFT pointer points to the in-order predecessor of the node. When RTHREAD is TRUE, the RIGHT pointer points to the in-order successor of the node.

For example, consider a binary tree where the in-order traversal produces: D, B, E, A, C, F. In a right-threaded binary tree, node A's RIGHT pointer (which would be null in a traditional tree) points to C (its in-order successor), and node C's RIGHT pointer points to F. This allows us to traverse the tree in O(n) time without recursion or stacks.

### Types of Threaded Binary Trees

Threaded binary trees can be classified based on two criteria: the type of threading and the traversal order used.

**Single Threaded vs Double Threaded**: In a single threaded tree, only one direction of threading is used, typically the RIGHT pointers for in-order traversal. This means null RIGHT pointers are replaced with threads to in-order successors. A double threaded tree threads both LEFT null pointers (to in-order predecessors) and RIGHT null pointers (to in-order successors). Double threading provides more flexibility but requires additional LTHREAD flags.

**Traversal Order Based**: The most common is in-order threading, where threads connect nodes in in-order sequence. Pre-order threading and post-order threading are also possible, each connecting nodes according to their respective traversal orders. In-order threading is the most widely used because it produces a natural left-to-right ordering of nodes.

### Node Structure

The typical node structure for a doubly threaded binary tree (supporting both predecessor and successor threads) includes:

```
typedef struct threaded_node {
    int data;
    struct threaded_node *left;
    struct threaded_node *right;
    int lthread;  // 1 if left is thread, 0 if left is child
    int rthread;  // 1 if right is thread, 0 if right is child
} THREADED;
```

For a singly threaded tree, we only need one flag. The header node (dummy node) technique is often used where a dummy header node points to the root and helps handle edge cases like finding the first and last nodes in traversal.

### Traversals in Threaded Binary Trees

The primary advantage of threaded binary trees becomes evident during traversal. To perform an in-order traversal without recursion or stack:

1. Start by finding the leftmost node (first node in in-order)
2. Visit each node
3. If the node has a right thread, follow it to the successor
4. Otherwise, go to the right child and find its leftmost descendant
5. Repeat until we reach the header/dummy node

This algorithm efficiently traverses the entire tree using only the thread links, achieving O(n) time complexity while using O(1) auxiliary space.

### Insertion in Threaded Binary Trees

Insertion in a threaded binary tree requires careful handling to maintain the threading property. When inserting a new node as a left or right child, we must update the threads of the affected nodes. The general procedure involves:

1. Find the appropriate position in the tree (like regular BST insertion)
2. Attach the new node
3. Update the thread of the new node's parent
4. Update the thread of the new node's in-order successor (for double threading)

Deletion is more complex and requires restoring the threading property by carefully reconnecting threads after removing a node.

## Examples

### Example 1: Converting a Binary Tree to Threaded Form

Consider the following binary tree:

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

The in-order traversal is: D, B, E, A, C, F

To create a right-threaded binary tree:
- Node D: RIGHT thread points to B (its in-order successor)
- Node E: RIGHT thread points to A
- Node B: RIGHT thread points to E (but E is actual child, so no thread needed here - E is already connected via B's right child)
- Node A: RIGHT child is C (actual child)
- Node C: RIGHT thread points to F
- Node F: RIGHT thread points to NULL (or header)

After threading, node D's RIGHT pointer now points to B, node E's RIGHT pointer points to A, and node C's RIGHT pointer points to F.

### Example 2: In-order Traversal of Threaded Tree

Given a threaded binary tree, perform in-order traversal:

Starting at the leftmost node, visit it. Check if RIGHT is a thread or child. If thread, follow it to the next node. If child, go to right child and find its leftmost descendant.

For the tree in Example 1, traversal would be:
- Start at D (leftmost)
- Visit D, follow RIGHT thread to B
- Visit B, go to right child E
- Visit E, follow RIGHT thread to A
- Visit A, go to right child C
- Visit C, follow RIGHT thread to F
- Visit F, traversal complete

This traversal uses only the thread links after the initial descent.

### Example 3: Node Structure Representation

For a doubly threaded tree storing integers:

```
       15
      /  \
     10   25
    /  \
   5   12
```

Node 5: LEFT points to NULL (thread to header), LTHREAD=1; RIGHT points to 10, RTHREAD=0
Node 10: LEFT points to 5 (child), LTHREAD=0; RIGHT points to 12 (child), RTHREAD=0
Node 12: LEFT points to 10 (thread), LTHREAD=1; RIGHT points to 15 (thread), RTHREAD=1
Node 15: LEFT points to 10 (thread), LTHREAD=1; RIGHT points to 25 (child), RTHREAD=0
Node 25: LEFT points to 15 (thread), LTHREAD=1; RIGHT points to NULL (thread to header), RTHREAD=1

## Exam Tips

1. Remember the formula for null pointers: A binary tree with n nodes has exactly n+1 null pointers, making threading always possible.

2. In singly threaded trees, we only need one additional flag; in doubly threaded trees, we need two flags (LTHREAD and RTHREAD).

3. The time complexity for traversal in threaded binary trees is O(n) with O(1) space, compared to O(n) space for recursive/stack-based approaches.

4. Threaded binary trees sacrifice the ability to easily perform insertion and deletion compared to regular binary trees, as these operations require careful thread maintenance.

5. For exam questions on drawing threaded trees, clearly mark threads with dashed lines and indicate which nodes are connected via threads versus child pointers.

6. The in-order successor of the rightmost node and in-order predecessor of the leftmost node typically point to a dummy header node.

7. Be prepared to differentiate between single threading (only successor threads) and double threading (both predecessor and successor threads) in exam questions.

8. Remember that threads replace null pointers, not actual child pointers. Actual child connections remain unchanged during threading.

9. For interview-style questions: Threaded binary trees eliminate the need for stacks during traversal but require additional memory for thread flags.

10. Practice converting between binary tree representations and threaded representations, as this is a common examination problem.