# 2-4 Trees and B-Trees

## Introduction

In the realm of computer science, efficient data organization and retrieval are paramount. While binary search trees provide excellent average-case performance, they can degrade to linear time complexity in worst-case scenarios, especially with sorted data. This limitation prompted the development of balanced multiway search trees, which maintain logarithmic time complexity regardless of input order.

**2-4 trees** (also known as 2-3-4 trees) represent a fundamental self-balancing search tree where each node can contain 2, 3, or 4 keys and have corresponding numbers of children. These trees guarantee height-balanced structure through node splitting operations during insertions, ensuring O(log n) worst-case performance for search, insertion, and deletion operations.

**B-Trees** generalize the concept of 2-4 trees and are extensively used in database systems and file systems. A B-tree of order m can have up to m-1 keys and m children per node, making it particularly efficient for disk-based storage systems where minimizing disk I/O is critical. The University of Delhi curriculum emphasizes understanding these trees because they form the backbone of modern storage systems and database indexing mechanisms.

## Key Concepts

### 2-4 Trees (2-3-4 Trees)

A 2-4 tree is a balanced search tree with the following properties:

1. **Node Types**: Each node can be a 2-node, 3-node, or 4-node:
   - **2-node**: Contains 1 key and has 2 children
   - **3-node**: Contains 2 keys and has 3 children
   - **4-node**: Contains 3 keys and has 4 children

2. **Balanced Height**: All leaf nodes must be at the same level (perfect balance)

3. **Search Property**: Keys within each node are sorted, and the tree maintains the binary search tree property extended for multiple keys

4. **Split Operation**: When a 4-node is full and insertion occurs, it splits into a 2-node and a 3-node, with the middle key promoted to the parent

### B-Trees

A B-Tree of order m (where m ≥ 3) satisfies:

1. **Node Capacity**: Each node can have at most m-1 keys and m children

2. **Root Constraint**: Root has at least 2 children (unless it's a leaf)

3. **Minimum Occupancy**: All non-leaf nodes (except root) have at least ⌈m/2⌉ children

4. **Leaf Level**: All leaf nodes appear at the same level

5. **Key Distribution**: Keys in each node are sorted, with k keys indicating k+1 children

**Relationship between 2-4 Trees and B-Trees**: A 2-4 tree is essentially a B-tree of order 4 (since maximum children = 4). This relationship helps in understanding both structures through a unified perspective.

### Operations on 2-4 Trees

**Search Operation**:
- Start at root
- Compare target key with keys in current node
- If found, return the value
- Otherwise, determine the appropriate child subtree and continue recursively

**Insertion Algorithm**:
1. Find the appropriate leaf node for insertion
2. If leaf is not a 4-node, simply insert the key in sorted order
3. If leaf is a 4-node (full), perform split operation:
   - Create new node by moving middle key up
   - Distribute remaining keys to left and right nodes
   - If parent is also full, propagate split upward
4. Handle root splitting separately (if root becomes full)

**Deletion Algorithm** (Simplified):
1. Find the target key
2. If in leaf, simply remove it
3. If in internal node, replace with predecessor or successor, then delete from leaf
4. Handle underflow (when node has fewer than required keys) by borrowing from siblings or merging

### B-Tree Operations

**Search Complexity**: O(log n) - with base approximately m/2 (the minimum degree)

**Insertion**:
- Find appropriate leaf position
- Insert key while maintaining sorted order
- If node overflows (exceeds m-1 keys), split the node and promote middle key
- Continue propagating splits upward as necessary

**Deletion**:
- More complex than insertion
- May require borrowing from siblings (rotation) or merging nodes
- Must maintain minimum key constraint of ⌈m/2⌉ - 1

### Practical Applications

**2-4 Trees**: Used in in-memory data structures, Java's TreeMap implementation (via red-black trees, which are mathematically equivalent), and educational purposes to understand balancing.

**B-Trees**: Ubiquitous in database systems (MySQL InnoDB, Oracle, PostgreSQL), file systems (NTFS, HFS+), and key-value stores due to their excellent disk I/O characteristics.

## Examples

### Example 1: Inserting into a 2-4 Tree

**Problem**: Insert keys 10, 20, 30, 40, 50, 60, 70 into an empty 2-4 tree.

**Solution**:

**Step 1**: Insert 10
- Create root node with key 10

**Step 2**: Insert 20
- Root has space, add 20 to get [10, 20]

**Step 3**: Insert 30
- Root becomes full [10, 20, 30], needs split
- Split: Middle key 20 moves up, 10 and 30 become children
- Tree: Root [20], Left child [10], Right child [30]

**Step 4**: Insert 40
- Find leaf for 40 (right subtree of 30)
- Insert into [30] → [30, 40]

**Step 5**: Insert 50
- Insert into [30, 40] → [30, 40, 50] (full)
- Split [30, 40, 50]: 40 moves up
- Merge with root: Root becomes [20, 40]
- Left: [10, 20], Middle: [30], Right: [50]
- Wait, this needs rebalancing...
- Final tree: Root [40], Left child [20], Right child [60], with [10, 20, 30] and [50, 60, 70] as leaves

**Final Result**: A balanced 2-4 tree with height 1 containing all keys.

### Example 2: B-Tree Search Operation

**Problem**: Given a B-tree of order 5 (minimum degree t=2, meaning 2-4 keys per node), search for key 45.

**Solution**:

**B-tree structure**: Assume root contains keys [20, 40], with children:
- Child 1: [10, 15] (leaf)
- Child 2: [25, 30, 35] (leaf)
- Child 3: [45, 50] (leaf)

**Search Process**:
1. Start at root [20, 40]
2. Compare 45:
   - 45 > 20 and 45 > 40, so go to Child 3
3. At Child 3 [45, 50]:
   - 45 == 45, found!
   - Return the associated value

**Time Complexity**: O(log n) - in this case, 2 comparisons at root + 1 at leaf = 3 operations for n=7 keys.

### Example 3: B-Tree Insertion with Split

**Problem**: Insert keys 10, 20, 30, 40, 50 into a B-tree of order 5.

**Solution**:

**Initial insertions**:
- Insert 10 → [10]
- Insert 20 → [10, 20]
- Insert 30 → [10, 20, 30]
- Insert 40 → [10, 20, 30, 40] (full, 4 keys = m-1)

**Insert 50** (causes overflow):
1. Insert 50 into full node → [10, 20, 30, 40, 50]
2. Split at position 2 (0-indexed):
   - Left: [10, 20]
   - Middle: 30 (promoted)
   - Right: [40, 50]
3. Since this is root, create new root with 30
4. Final tree: Root [30], Left child [10, 20], Right child [40, 50]

**Note**: For a B-tree of order 5, maximum keys = 4, so splitting occurs at 5 keys.

## Exam Tips

1. **Understand the Relationship**: Remember that a 2-4 tree is equivalent to a B-tree of order 4. This connection frequently appears in exam questions.

2. **Minimum Keys Rule**: For B-trees with minimum degree t, non-root nodes must have at least t-1 keys. Remember this constraint for deletion questions.

3. **Time Complexity**: Always remember O(log n) for search, insert, and delete operations in both 2-4 trees and B-trees.

4. **Height Calculation**: The height of a B-tree with n keys and minimum degree t is at most logₜ((n+1)/2). This formula is essential for theoretical questions.

5. **Split vs Merge**: During insertion, nodes split when they overflow (more than m-1 keys). During deletion, nodes merge when they underflow (fewer than t-1 keys).

6. **Order vs Degree**: Don't confuse order (m) with minimum degree (t). Relationship: t = ⌈m/2⌉. A B-tree of order 5 has minimum degree 2.

7. **Disk Access Advantage**: B-trees are designed for disk-based storage with large node sizes (typically matching disk block size), minimizing I/O operations. This is a common exam question.

8. **Leaf Node Property**: In both 2-4 trees and B-trees, all leaf nodes are at the same level. This guarantees balanced height.

9. **Red-Black Tree Equivalence**: A red-black tree can be represented as a 2-4 tree (via a color-flipping transformation). This conceptual link helps understand why red-black trees are self-balancing.

10. **Practice Drawing**: For exams, practice drawing both trees step-by-step for various insertion sequences to ensure accuracy.