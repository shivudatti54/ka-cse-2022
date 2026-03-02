# Game Playing: Minimax & Alpha-Beta Pruning

## Introduction
Game playing represents a classic AI problem where agents make sequential decisions in competitive environments. The Minimax algorithm with Alpha-Beta pruning forms the foundation of adversarial search, essential for playing two-player zero-sum games like Chess, Checkers, and Tic-Tac-Toe. These algorithms are part of the Delhi University B.Sc. (Hons) Computer Science NEP 2024 syllabus under the Artificial Intelligence paper.

## Key Concepts

### Zero-Sum Games
- **Zero-sum game**: One player's gain equals the other's loss
- **Perfect information**: All game states visible to both players (no hidden information)
- **Deterministic**: No chance elements (no dice, cards)

### Minimax Algorithm
- **Purpose**: Find optimal move assuming optimal opponent
- **Two players**: MAX (maximizer) and MIN (minimizer)
- **Recursive approach**: Maximize at MAX nodes, minimize at MIN nodes
- **Utility values**: Terminal states evaluated for game outcome (+1, 0, -1)
- **Depth-first search**: Explores entire game tree to terminal states

### Alpha-Beta Pruning
- **Purpose**: Reduce nodes evaluated without affecting final decision
- **Alpha (α)**: Best value MAX can guarantee at MAX nodes
- **Beta (β)**: Best value MIN can guarantee at MIN nodes
- **Pruning conditions**:
  - Alpha cut-off: β ≤ α at MIN node
  - Beta cut-off: β > α at MAX node

### Evaluation Functions
- **Heuristic evaluation**: Estimate desirability of non-terminal states
- **Features**: Material count, piece positions, mobility, king safety
- **Depth limit**: Search only to fixed depth due to exponential complexity

### Complexity Analysis
| Aspect | Minimax | Alpha-Beta |
|--------|---------|------------|
| Time | O(b^d) | O(b^(d/2)) with perfect ordering |
| Space | O(bd) | O(bd) |

*(b = branching factor, d = depth)*

## Important Properties

- **Optimality**: Minimax is optimal against perfect opponent
- **Effectiveness**: Alpha-Beta provides same result as Minimax
- **Perfect ordering**: Best moves first → best pruning efficiency
- **Horizon effect**: Deeper search improves decision quality

## Limitations
- **Chess curse**: Brute-force limited in complex games
- **Evaluation accuracy**: Depends on heuristic quality
- **Combinatorial explosion**: Exponential search space

## Conclusion
Minimax with Alpha-Beta pruning revolutionized computer game playing. While Minimax guarantees optimal play in perfect information games, Alpha-Beta pruning makes real-time decisions feasible by eliminating irrelevant branches. Modern game-playing systems (like Chess engines) extend these principles with enhancements such as iterative deepening, transposition tables, and quiescence search. Understanding these algorithms is crucial for the Delhi University AI examination.