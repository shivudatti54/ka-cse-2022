# Balanced Search Trees

## Introduction

Balanced search trees represent one of the most important data structures in computer science, providing efficient mechanisms for storing and retrieving sorted data. While binary search trees (BST) offer O(log n) average-case time complexity for search, insert, and delete operations, their performance degrades severely to O(n) in the worst case when the tree becomes unbalanced. This limitation motivated the development of balanced search trees, which automatically maintain their height balance to guarantee logarithmic performance regardless of the input sequence.

In the context of the University of Delhi's Computer Science curriculum, balanced search trees are essential for understanding how real-world databases and file systems maintain efficient data access. The two most prominently studied balanced tree variants are AVL trees (named after inventors Adelson-Velsky and Landis) and Red-Black trees, each offering different trade-offs between implementation complexity and rotational operations. These structures find extensive applications in operating system memory management, compiler symbol tables, and associative arrays in programming languages like C++ STL (std::map, std::set) and Java (TreeMap, TreeSet).

This chapter explores the fundamental principles of tree balancing, the algorithmic mechanisms used to maintain balance, and the specific implementation details of AVL and Red-Black trees. Understanding these concepts is crucial for solving problems involving sorted data with guaranteed worst-case performance guarantees.

## Key Concepts

### The Need for Balancing

A binary search tree achieves O(log n) operations only when its height remains proportional to log n. When elements are inserted in sorted order (ascending or descending), the BST degenerates into a linked list, losing all its efficiency advantages. For instance, inserting 1, 2, 3, 4, 5, 6, 7 into a BST creates a right-skewed tree with height 7 instead of the balanced height of approximately 3. This worst-case scenario defeats the purpose of using a tree structure for search operations.

Balanced search trees solve this problem by enforcing mathematical constraints on tree height relative to the number of nodes. These constraints guarantee that the tree height never exceeds c × log(n) for some constant c, ensuring consistent O(log n) performance across all input sequences.

### AVL Trees

An AVL tree is a self-balancing binary search tree where the heights of the left and right subtrees of any node differ by at most one. This strict balance condition guarantees a maximum height of approximately 1.44 × log₂(n+2) - 0.328, ensuring excellent search performance.

**AVL Property:** For every node in the tree, the height of its left subtree and right subtree differ by at most 1. Each node stores an additional attribute called the balance factor, which equals height(right subtree) - height(left subtree). Valid balance factors are {-1, 0, 1}.

**Rotations in AVL Trees:** When an insertion or deletion violates the AVL property, specific rotational operations restore balance. A rotation is a local operation that changes the structure of the tree while preserving the binary search tree property.

- **Left Rotation (LL Case):** Applied when a node becomes right-heavy due to insertion in its right subtree's right child. The unbalanced node X moves down and to the left, its right child Y becomes the new root of this subtree.

- **Right Rotation (RR Case):** Applied when a node becomes left-heavy due to insertion in its left subtree's left child. The unbalanced node X moves down and to the right, its left child Y becomes the new root.

- **Left-Right Double Rotation (LR Case):** Applied when insertion occurs in the left subtree of the right child. First, a right rotation is performed on the left child, then a left rotation on the unbalanced node.

- **Right-Left Double Rotation (RL Case):** Applied when insertion occurs in the right subtree of the left child. First, a left rotation is performed on the right child, then a right rotation on the unbalanced node.

**Insertion in AVL Trees:** The insertion process first performs a standard BST insertion, then traverses back up the tree checking balance factors. If an imbalance is found at node X, appropriate rotation(s) are performed to restore balance. Only O(log n) nodes need checking since the height is bounded.

**Deletion in AVL Trees:** Deletion is more complex than insertion. After standard BST deletion, we must traverse back up to the root, checking and fixing imbalances at each level. Unlike insertion where at most one rotation suffices, deletion may require multiple rotations along the path to the root.

### Red-Black Trees

A Red-Black tree is a self-balancing binary search tree with an additional coloring property that ensures approximate balance. While less strictly balanced than AVL trees, Red-Black trees require fewer rotations during insertion and deletion, making them preferred in practice for implementations requiring frequent modifications.

**Red-Black Properties:**
1. Every node is either red or black.
2. The root is always black.
3. Every leaf (NIL node) is black.
4. If a node is red, then both its children must be black (no two consecutive red nodes).
5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes (black-height property).

**Black-Height:** The black-height of a node x, denoted bh(x), is the number of black nodes on any path from x to a leaf, not counting x itself. All paths from root to leaves have the same black-height due to property 5.

**Height Bound:** A Red-Black tree with n internal nodes has a height of at most 2 × log₂(n+1). This bound is slightly looser than AVL trees but still guarantees O(log n) operations.

**Rotations in Red-Black Trees:** Like AVL trees, Red-Black trees use left and right rotations for restructuring. However, the re-coloring strategy is more sophisticated, handling various cases based on the colors of the node, its parent, uncle, and sibling.

**Insertion in Red-Black Trees:** Insertion begins with a standard BST insertion, coloring the new node red (to avoid violating property 2 immediately). Then, cases are handled based on the colors of the new node's parent and uncle:

- **Case 1:** Uncle is red — re-color parent, uncle, and grandparent, then move focus to grandparent.
- **Case 2:** Uncle is black and new node is right child — left rotation on parent, then apply Case 3.
- **Case 3:** Uncle is black and new node is left child — right rotation on grandparent, re-color parent and grandparent.

**Deletion in Red-Black Trees:** Deletion is considerably more complex due to the need to maintain all five properties. The algorithm handles various cases based on the colors of the sibling node and its children when a double-black situation arises (when a black node is removed from a black-height path).

### Comparison: AVL vs Red-Black Trees

| Aspect | AVL Trees | Red-Black Trees |
|--------|-----------|-----------------|
| Balance Factor | Strict: height difference ≤ 1 | Approximate: height ratio ≤ 2 |
| Search Performance | Better (tighter balance) | Slightly worse |
| Insertion/Deletion | More rotations | Fewer rotations |
| Applications | Databases (frequent lookups) | Language libraries (balanced modifications) |
| Memory Overhead | Balance factor per node | Color bit per node |

## Examples

### Example 1: AVL Tree Insertion

Insert keys 10, 20, 30, 40, 50, 25 into an AVL tree.

**Step-by-step solution:**

1. Insert 10: Tree: 10

2. Insert 20: 10 → 20 (right of 10)
   Tree: 10(right) → 20
   Balance factors are valid.

3. Insert 30: 10 → 20 → 30
   After insertion, 10 becomes left-heavy (balance factor = -1).
   Apply Left Rotation on node 10:
   
   Before:    10          After:     20
             \                      /  \
             20           →       10  30
              \
              30

4. Insert 40: 20 → 10, 30 → 40 (right of 30)
   Tree remains balanced.

5. Insert 50: Path: 20 → 30 → 40 → 50
   30 becomes right-heavy (balance factor = 2)
   Apply Left Rotation on node 30:
   
   Before:     20            After:     20
              /  \                     /  \
            10   30                  10   40
                \                    /  \
                40           →    30   50
                 \
                 50

6. Insert 25: Path: 20 → 10, then right to 30, then left to 25 (child of 30)
   30 becomes left-heavy (balance factor = -2, LR case)
   First, Left Rotation on child (25 and 40):
   Then, Right Rotation on 30:
   
   Final tree:
          20 (balanced)
         /  \
       10   40
           /  \
         30   50
        /
       25

### Example 2: Red-Black Tree Insertion

Insert keys 7, 3, 18, 10, 22, 8, 11 into a Red-Black tree.

**Step-by-step solution:**

1. Insert 7 (root): Color it BLACK (root must be black)
   Tree: 7(B)

2. Insert 3: Color RED
   Tree: 7(B) → 3(R)
   Valid (black 7 has red child 3, okay)

3. Insert 18: Color RED
   Tree: 7(B) → 3(R), 18(R)
   
4. Insert 10: Insert as red, then re-color
   Tree: 7(B) → 3(R), 18(R) → 10(R)
   
   Fix: 18 is red, 3 is red (consecutive reds). 7 is black, 3's uncle (18) is red.
   Apply Case 1: Recolor 3, 18 to BLACK, 7 to RED.
   
   Result: 7(R) → 3(B), 18(B) → 10(R)

5. Insert 22: Red child of 18.
   Tree balanced, no fix needed.

6. Insert 8: 10 is red, so 8 must be red. But 10's uncle (3) is black, and 8 is left child of 10 (LR case).
   Apply Case 2: Left rotation on 10, then Case 3.
   Result: 7(B) → 3(B), 18(B) → 10(R), 22(B) → 8(R), 11(R)

7. Insert 11: Node 10 is red, so 11 must be red. But 10's uncle (8) is red.
   Apply Case 1: Recolor 10, 8 to BLACK, 18 to RED.
   
   Final tree maintains all Red-Black properties.

### Example 3: Time Complexity Analysis

For a database containing 1 million records, compare the maximum number of comparisons needed for searching in:

(a) Unbalanced BST (worst case)
(b) AVL tree
(c) Red-Black tree

**Solution:**

(a) Unbalanced BST: In worst case, height = n = 1,000,000
   Maximum comparisons = 1,000,000

(b) AVL tree: Maximum height ≈ 1.44 × log₂(1,000,002) ≈ 1.44 × 20 ≈ 29
   Maximum comparisons ≈ 29

(c) Red-Black tree: Maximum height ≤ 2 × log₂(1,000,001) ≤ 2 × 20 = 40
   Maximum comparisons ≤ 40

This dramatic difference (from 1 million to under 40 comparisons) demonstrates why balanced search trees are essential for real-world applications.

## Exam Tips

1. **Remember AVL Balance Factor:** The balance factor is defined as height(right subtree) - height(left subtree), and valid values are {-1, 0, 1}.

2. **Rotation Naming Convention:** A LEFT rotation is performed when a node becomes LEFT-HEAVY (left subtree shorter), and RIGHT rotation when RIGHT-HEAVY. This counter-intuitive naming comes from the direction the root node moves.

3. **Red-Black Root Property:** Always remember that the root of a Red-Black tree must be BLACK. This is a common exam question.

4. **Black-Height Consistency:** All paths from any node to leaves must have the same black-height. Use this property to quickly verify if a given tree is a valid Red-Black tree.

5. **AVL vs Red-Black Choice:** For more searches than insertions/deletions, prefer AVL trees. For more insertions/deletions, prefer Red-Black trees (fewer rotations).

6. **Deletion is Harder:** In both tree types, deletion may require multiple rotations up to the root, while insertion requires at most one or two rotations.

7. **NIL Nodes in Red-Black:** Remember that NIL nodes (external null children) are always BLACK. They count toward black-height calculations.

8. **Space Complexity:** Both trees require O(n) space. AVL trees store balance factors (integers), while Red-Black trees store colors (1 bit), making them slightly more memory-efficient.