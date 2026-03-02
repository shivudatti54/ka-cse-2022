# Threaded Binary Trees - Summary

## Key Definitions and Concepts

- **Threaded Binary Tree**: A binary tree where null pointers are replaced with "threads" that point to in-order predecessors or successors, enabling efficient traversal without recursion or stacks.

- **Thread**: A pointer that connects a node to its in-order predecessor (left thread) or successor (right thread), replacing what would otherwise be a null pointer.

- **LTHREAD/RTHREAD Flags**: Boolean indicators where TRUE (1) means the corresponding pointer is a thread, and FALSE (0) means it points to an actual child node.

- **Single Threaded**: Only one direction of threading (typically right threads for in-order successor).

- **Doubly Threaded**: Both left and right pointers are threaded to predecessor and successor respectively.

## Important Formulas and Theorems

- **Null Pointer Count**: A binary tree with n nodes has exactly n+1 null pointers, which can all be converted to threads.

- **Traversal Complexity**: O(n) time with O(1) auxiliary space (compared to O(n) space for recursive traversal).

- **Node Storage**: Single threaded requires n+2 fields per node; double threaded requires n+3 fields per node.

## Key Points

- Threaded binary trees solve the problem of wasted null pointers in regular binary trees.

- In-order threading is most common as it provides natural left-to-right ordering.

- The primary advantage is efficient O(1) space traversal without recursion or stacks.

- The main disadvantage is increased complexity in insertion and deletion operations.

- Thread flags must be carefully maintained during any structural modification.

- A dummy header node is often used to simplify boundary conditions in traversal.

- Both single and double threading preserve the original tree structure while adding navigation capability.

## Common Mistakes to Avoid

- Confusing thread pointers with child pointers; threads only replace null pointers, not existing child connections.

- Forgetting to update thread flags when marking pointers as threads or child pointers.

- Attempting traversal without first understanding whether the tree is single or doubly threaded.

- Assuming threads are bidirectional; single threaded trees only provide one-direction navigation.

## Revision Tips

1. Practice drawing threaded binary trees from regular binary trees, clearly distinguishing threads (dashed) from child pointers (solid).

2. Memorize the node structure and understand how LTHREAD and RTHREAD flags determine pointer interpretation.

3. Write out the in-order traversal algorithm for threaded trees step-by-step until it becomes automatic.

4. Review the tradeoff analysis: what we gain (efficient traversal) versus what we lose (complex insert/delete).

5. Solve previous year DU examination questions on this topic to understand the examination pattern and important concepts.