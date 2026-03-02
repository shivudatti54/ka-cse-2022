# Basic Concepts of Trees - Summary

## Key Definitions and Concepts

- **Root**: Topmost node with no parent
- **Parent**: Direct predecessor node in hierarchy
- **Child**: Direct successor node in hierarchy
- **Leaf Node**: Node with 0 children (degree 0)
- **Internal Node**: Non-leaf node with ≥1 child
- **Subtree**: Tree consisting of a node and its descendants
- **Depth**: Number of edges from root to node
- **Height**: Number of edges on longest path from node to leaf
- **Degree**: Number of children a node has
- **Level**: Depth + 1 (root is level 1)
- **Sibling**: Nodes sharing the same parent

## Important Formulas and Theorems

1. **Height of Node**:
   ```c
   height(node) = 1 + max(height(child1), height(child2), ...)
   ```
2. **Depth Calculation**:
   ```c
   depth(node) = depth(parent) + 1
   ```
3. **Maximum Nodes at Level L** (Binary Tree):
   ```math
   2^{L-1}
   ```
4. **Height vs Nodes Relationship**:
   ```math
   Minimum height = ⌈log₂(n+1)⌉ - 1
   Maximum height = n-1 (for skewed tree)
   ```

## Key Points

1. Trees enable O(log n) operations in balanced structures vs O(n) in linear structures
2. Fundamental properties:
   - Exactly one root node
   - No cycles allowed
   - N nodes ⇒ N-1 edges
3. Binary Tree Special Case:
   - Max degree = 2
   - Strict/Full: 0 or 2 children
   - Complete: All levels filled except last
4. Tree traversal types:
   - Pre-order (Root-Left-Right)
   - In-order (Left-Root-Right)
   - Post-order (Left-Right-Root)
5. Height of tree = Height of root node
6. Applications:
   - File systems (directory structure)
   - Database indexing (B-trees)
   - Compiler parse trees
   - Decision trees in ML
7. Binary Search Tree property:
   ```c
   left_child < parent < right_child
   ```

## Common Mistakes to Avoid

1. **Depth vs Height Confusion**:
   - Depth: Path from root **to** node
   - Height: Path from node **to deepest leaf**

2. **Root Node Properties**:
   - Depth = 0 (not 1)
   - Level = 1 (not 0)

3. **Binary Tree Assumptions**:
   - Not all trees are binary
   - Binary trees ≠ Binary Search Trees

4. **Leaf Node Misconception**:
   - Leaf nodes can exist at different levels
   - Root can be leaf (in single-node tree)

## Revision Tips

1. **Diagram Practice**:
   - Draw trees from given traversals
   - Calculate depth/height for each node

2. **Formula Drill**:
   - Memorize `2^{L-1}` nodes per level
   - Practice height/depth calculations

3. **Terminology Flashcards**:
   - Create cards for root, leaf, degree, etc.
   - Compare sibling vs cousin nodes

4. **Real-world Connections**:
   - Map directory structures to tree concepts
   - Compare family trees with data structure trees

**Exam Focus**: Expect 2-3 marker questions on terminology, 5-mark problems on tree properties/calculations, and application-based questions connecting to BSTs/expression trees.
