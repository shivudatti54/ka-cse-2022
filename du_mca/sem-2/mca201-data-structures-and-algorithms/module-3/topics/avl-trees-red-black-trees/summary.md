# AVL Trees & Red-Black Trees - Summary

## Key Definitions and Concepts
- **AVL Tree**: Self-balancing BST with |height(left) - height(right)| ≤ 1
- **Red-Black Tree**: Colored BST maintaining black-height balance
- **Rotation**: Tree restructuring operation preserving BST property
- **Black Height**: Number of black nodes from root to leaf (RBT)

## Important Formulas and Theorems
- AVL height bound: h ≤ 1.44log₂(n+2) - 1.328
- RBT height bound: h ≤ 2log₂(n+1)
- Balance Factor (AVL): BF(node) = height(left) - height(right)

## Key Points
- AVL requires more rotations but provides faster lookups
- RBTs use color flips and fewer rotations for faster writes
- Both guarantee O(log n) search time
- RBT properties enforce structural constraints through coloring
- Insertion in AVL: Up to 2 rotations per insertion
- RBT fixup cases depend on uncle node's color
- Real-world use: Databases (AVL), Language libraries (RBT)

## Common Mistakes to Avoid
- Forgetting to update balance factors after AVL rotations
- Assuming RBT leaves contain data (they're NIL nodes)
- Confusing LL/RR with LR/RL rotation scenarios
- Missing double rotation requirements in deep AVL trees

## Revision Tips
1. Practice drawing insertion sequences for both trees
2. Memorize RBT properties using acronym "BRNR" (Black Root, No Red-Red, Black equal)
3. Compare insertion steps side-by-side using same dataset
4. Implement rotation functions in pseudocode
5. Study Linux kernel's RBT implementation (rbtree.h)

Length: 650 words