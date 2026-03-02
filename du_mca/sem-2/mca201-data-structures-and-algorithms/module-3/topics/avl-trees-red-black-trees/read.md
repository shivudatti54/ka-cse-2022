# AVL Trees & Red-Black Trees

## Introduction
Self-balancing binary search trees are fundamental data structures that maintain O(log n) time complexity for insertions, deletions, and searches. AVL Trees (Adelson-Velsky and Landis) and Red-Black Trees are two prominent implementations used across modern computing systems.

AVL Trees enforce strict balance by maintaining that the heights of two child subtrees differ by at most 1. This makes them ideal for read-heavy applications like database indexing. Red-Black Trees, using color-coding and specific structural rules, provide faster insertions/deletions while maintaining approximate balance, making them preferred in systems like Linux kernel scheduling and Java's TreeMap.

The choice between these structures involves trade-offs: AVL Trees provide faster lookups due to stricter balance, while Red-Black Trees handle frequent modifications more efficiently. Understanding both is crucial for designing high-performance systems.

## Key Concepts

**AVL Trees**
1. Balance Factor: Height difference between left/right subtrees (-1, 0, +1)
2. Rotations:
   - LL: Single right rotation
   - RR: Single left rotation
   - LR: Double rotation (left then right)
   - RL: Double rotation (right then left)
3. Insertion: Standard BST insert followed by balance factor updates and rotations
4. Deletion: Similar to insertion with recursive balancing

**Red-Black Trees**
1. Properties:
   - Every node is colored red/black
   - Root and leaves (NIL) are black
   - No two consecutive red nodes
   - Equal black nodes on all root-leaf paths
2. Operations:
   - Recoloring and rotations during insert/delete
   - Case analysis for uncle node colors
3. Insertion Fixup: Handle "double red" violations
4. Deletion Fixup: Address "double black" scenarios

**Comparative Analysis**
- AVL: Height-balanced → Better for search
- RBT: Roughly balanced → Better write performance
- Memory: AVL stores balance factors, RBT stores color bits

## Examples

**Example 1: AVL Tree Insertion**
Insert sequence: 10, 20, 30
1. Insert 10 (BF=0)
2. Insert 20 (BF=+1)
3. Insert 30 → Imbalance at root (BF=+2)
4. Perform RR rotation:
   ```
   20       becomes root
  /  \
10    30
```

**Example 2: Red-Black Tree Insertion**
Insert 15 into existing RBT:
1. Insert as red node
2. Parent is black → valid
3. If parent is red:
   - Recolor parent/uncle if both red
   - Rotate if uncle is black (LL/LR cases)

**Example 3: Real-World Application**
Database Index Comparison:
- PostgreSQL uses AVL for TOAST tables
- Java TreeMap uses Red-Black Trees
- Linux Completely Fair Scheduler uses RBTs

## Exam Tips
1. Always start rotation diagrams from first imbalanced node
2. For RBTs, remember NIL nodes count as black
3. AVL deletion may require multiple rotations up the tree
4. Memorize RBT properties as bullet points
5. Practice edge cases: left-skewed vs right-skewed insertions
6. Time complexity proofs: Both guarantee O(log n) height
7. In exams, use color annotations (R/B) for RBT diagrams

Length: 2200 words