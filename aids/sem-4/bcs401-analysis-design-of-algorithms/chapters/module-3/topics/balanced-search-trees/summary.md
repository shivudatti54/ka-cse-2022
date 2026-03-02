# Balanced Search Trees - Summary

## Key Definitions and Concepts

- **AVL Tree:** A self-balancing BST where the height difference between left and right subtrees of any node is at most 1. Balance factor = height(right) - height(left), must be ∈ {-1, 0, 1}.

- **Red-Black Tree:** A self-balancing BST with five properties: nodes are colored red/black, root is black, leaves (NIL) are black, red nodes have black children, and all paths from a node to leaves have equal black-height.

- **Rotation:** A local tree restructuring operation that maintains BST property while changing subtree heights. Types include left rotation, right rotation, and double rotations.

- **Black-Height:** The number of black nodes on any path from a node to a leaf, not counting the node itself. All paths from root to leaves must have equal black-height.

## Important Formulas and Theorems

- **AVL Height Bound:** h ≤ 1.44 × log₂(n + 2) for n nodes
- **Red-Black Height Bound:** h ≤ 2 × log₂(n + 1) for n nodes  
- **Operations Time Complexity:** O(log n) for search, insert, and delete in both AVL and Red-Black trees
- **Space Complexity:** O(n) for both tree types

## Key Points

- Unbalanced BSTs degrade to O(n) performance; balanced trees guarantee O(log n) worst-case.

- AVL trees have stricter balance, providing faster search but requiring more rotations during modification.

- Red-Black trees sacrifice some search efficiency for fewer rotations during insertion/deletion.

- Single rotations fix LL and RR cases; double rotations (LR, RL) fix cases where the imbalance is two levels deep.

- Red-Black trees use re-coloring as the primary mechanism, with rotations used only when necessary.

- The root of a Red-Black tree must always be BLACK; NIL nodes are always BLACK.

- In AVL deletion, multiple rotations may be needed along the path to the root.

## Common Mistakes to Avoid

1. Confusing rotation direction: LEFT rotation is applied when the tree is LEFT-HEAVY (not right-heavy as might be intuitive).

2. Forgetting that NIL nodes in Red-Black trees are BLACK and contribute to black-height.

3. Assuming deletion in AVL trees requires only one rotation like insertion.

4. Not updating parent pointers correctly after rotations.

5. Forgetting to re-color the root BLACK after rotations in Red-Black trees.

## Revision Tips

1. Practice drawing rotation cases on paper: LL, RR, LR, RL — understand visually how pointers change.

2. Memorize the five Red-Black properties and use them to verify whether a given tree is a valid Red-Black tree.

3. Remember the comparison: AVL for search-heavy workloads, Red-Black for modification-heavy workloads.

4. Solve at least 5 problems involving insertion sequence tracing for both tree types.

5. Focus on understanding why rotations work rather than memorizing cases — the underlying principle is restoring height balance.