# BST Insert, Delete, and Search - Quick Revision

## Introduction
A Binary Search Tree (BST) is a hierarchical data structure where each node has at most two children. The left child contains values smaller than the parent, while the right child contains larger values. This property enables efficient searching, insertion, and deletion operations with average O(log n) time complexity.

## Key Concepts

### Properties
- Each node stores a key and has left and right pointers
- **Left subtree keys < parent key**
- **Right subtree keys > parent key**
- In-order traversal yields sorted sequence
- No duplicate keys (standard implementation)

### Search Operation
- **Algorithm**: Begin at root, compare target value
  - If equal → return node (found)
  - If smaller → traverse left subtree
  - If larger → traverse right subtree
- **Base case**: Reach null (not found)
- **Time Complexity**: O(h) where h = height of tree

### Insert Operation
- **Algorithm**:
  - Start from root, compare with each node
  - If smaller, go left; if larger, go right
  - Insert when null position is found
- **New node always inserted as leaf**
- Follows same path as search operation
- **Time Complexity**: O(h) — O(log n) for balanced tree

### Delete Operation
Three cases based on node type:

1. **Leaf Node**: Simply remove (no children)

2. **Single Child**: Replace node with its child

3. **Two Children**:
   - Find **in-order successor** (smallest in right subtree) OR **in-order predecessor** (largest in left subtree)
   - Copy successor/predecessor value to current node
   - Delete successor/predecessor node recursively

- **Time Complexity**: O(h)

### Complexity Summary

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Search    | O(log n)     | O(n)       |
| Insert    | O(log n)     | O(n)       |
| Delete    | O(log n)     | O(n)       |

### Exam Tips (Delhi University Syllabus)

- Remember: In-order predecessor = maximum in left subtree
- Remember: In-order successor = minimum in right subtree
- Worst case occurs when tree becomes skewed (like linked list)
- Balanced BST (AVL/Red-Black) guarantees O(log n) in all cases
- Applications: symbol tables, database indexing, expression trees

---

*Revision complete. Practice recursive implementations for search, insert, and delete operations.*