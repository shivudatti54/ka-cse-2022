# Threaded Binary Trees - Summary

## Key Definitions and Concepts
- **Thread**: A null pointer replaced with a pointer to the inorder predecessor or successor of a node
- **Tag field (ltag/rtag)**: Boolean flag indicating whether the pointer is a child link (0) or a thread (1)
- **Right-threaded tree**: Only null right pointers are threaded to inorder successors
- **Double-threaded tree**: Both null left and right pointers are threaded for bidirectional traversal
- **Header node**: Dummy node simplifying traversal, with left pointing to first inorder node and right to last

## Important Formulas and Theorems
- **Null pointer count**: A binary tree with n nodes has exactly n+1 null pointers
- **Traversal complexity**: O(n) time, O(1) auxiliary space (vs O(h) space for recursive traversal)
- **Memory savings**: Threaded trees eliminate n+1 null pointers while adding n+1 threads

## Key Points
- Threaded binary trees solve the problem of wasted null pointers in standard binary trees
- The threading is defined with respect to a specific traversal order, typically inorder
- Each threaded pointer is accompanied by a tag field to distinguish it from child pointers
- Right-threaded trees enable forward inorder traversal without recursion or stacks
- Double-threaded trees enable both forward and backward traversal
- The header node ensures the traversal algorithm always has a starting point and termination condition

## Common Mistakes to Avoid
- Confusing threads with child pointers: Always check the tag field before following a pointer
- Forgetting that leaf nodes often have multiple threads since both children are null
- Not updating tag fields correctly when inserting or deleting nodes
- Assuming all threaded trees support bidirectional traversal: only double-threaded trees do

## Revision Tips
- Practice drawing the threaded version of a given binary tree
- Memorize the rule: null right → inorder successor, null left → inorder predecessor
- Remember that threaded trees trade off complexity in insertion/deletion for simpler traversal
- Review the relationship between the number of nodes and null pointers as it's frequently tested
- Compare space complexity: standard tree O(2n) pointers vs threaded tree O(2n + n+1 tag fields) but saves stack space during traversal