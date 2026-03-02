# Game Playing: Minimax and Alpha-Beta Pruning

## Artificial Intelligence - Unit IV

---

## 1. Introduction

### 1.1 What is Game Playing in AI?

Game playing represents one of the most fascinating and historically significant areas of artificial intelligence research. At its core, game playing involves creating AI agents that can make optimal decisions in competitive environments where multiple players (typically two) have conflicting objectives. This field combines elements of search algorithms, decision theory, and heuristic evaluation to create intelligent game-playing systems.

The study of game playing in AI is not merely about creating computer opponents for chess, checkers, or tic-tac-toe. It encompasses a broader range of adversarial decision-making scenarios including strategic board games, card games, video games, and even real-world applications like automated negotiation systems, cybersecurity defense mechanisms, and economic market simulations.

### 1.2 Real-World Relevance

The techniques developed for game playing have far-reaching applications beyond traditional board games:

- **Robotics and Autonomous Systems**: Game theory and adversarial search help robots make decisions in competitive environments
- **Financial Trading**: Algorithmic trading uses similar concepts to predict market movements and make optimal trading decisions
- **Security and Cybersecurity**: Game-playing algorithms help in developing strategies for network defense against adversarial attacks
- **Resource Management**: Strategic decision-making in logistics, supply chain, and resource allocation
- **Multi-agent Systems**: Coordination and competition among multiple AI agents

For the Delhi University NEP 2024 UGCF syllabus, this unit forms a crucial component of the Artificial Intelligence paper, connecting theoretical concepts to practical applications that students will encounter in their professional careers.

---

## 2. Fundamentals of Game Playing

### 2.1 Game Taxonomy

Understanding the types of games is essential for selecting appropriate search algorithms:

#### Deterministic vs. Stochastic Games

| Type | Description | Examples | Search Approach |
|------|-------------|----------|------------------|
| **Deterministic** | No chance or random elements; perfect information | Chess, Checkers, Go | Minimax, Alpha-Beta |
| **Stochastic** | Involves probability and chance elements | Backgammon, Poker, Monopoly | Expectiminimax |

#### Information Availability

- **Perfect Information**: All players have complete knowledge of the game state (Chess, Checkers, Go)
- **Imperfect Information**: Some information is hidden (Poker, Bridge)

#### Zero-Sum vs. Non-Zero-Sum

- **Zero-Sum**: One player's gain is exactly another's loss (Chess, Checkers)
- **Non-Zero-Sum**: Outcomes can benefit or harm multiple players (Negotiation, Diplomacy)

### 2.2 The Game Tree

A game tree is a directed graph that represents all possible moves in a game from the initial state to terminal states. Each node in the tree represents a game state, and each edge represents a legal move.

```
                        [Initial State]
                            |
            +-------------+-------------+             
            |             |             |
          Move A       Move B        Move C
            |             |             |
        [State 1]    [State 2]    [State 3]
            |             |             |
          ...           ...           ...
```

**Key Terminology:**

- **Branching Factor (b)**: The average number of legal moves available at each state. For chess, approximately b ≈ 35; for checkers, b ≈ 10.
- **Depth (d)**: The maximum number of plies (half-moves) to reach a terminal state
- **Total Nodes**: Approximately b^d nodes in a complete game tree

The exponential growth of game trees (O(b^d)) makes exhaustive search impractical for complex games, necessitating heuristic evaluation and pruning techniques.

---

## 3. The Minimax Algorithm

### 3.1 Concept and Theory

The minimax algorithm, developed by John von Neumann and Oskar Morgenstern in 1944, is the fundamental algorithm for solving two-player zero-sum games with perfect information. The algorithm is named for its objective: one player (Maximizer) tries to maximize the score while the other (Minimizer) tries to minimize it.

The core principle is elegantly simple: assuming optimal play from both sides, the algorithm recursively evaluates all possible game states to determine the optimal move for the current player.

### 3.2 Algorithm Explanation

The minimax algorithm operates under these assumptions:
1. Both players play optimally
2. The game is deterministic with perfect information
3. The game is zero-sum (one player's gain is the other's loss)

The algorithm alternates between two perspectives:
- **Maximizer's Turn**: Chooses the move with the highest evaluated score
- **Minimizer's Turn**: Chooses the move with the lowest evaluated score (assuming it wants to minimize the Maximizer's outcome)

### 3.3 Pseudocode

```
function MINIMAX(node, depth, maximizingPlayer):
    // Base case: terminal state or maximum depth reached
    if node is a terminal node or depth == 0:
        return the heuristic value of node
    
    if maximizingPlayer == true:
        maxEval = -∞
        for each child of node:
            eval = MINIMAX(child, depth - 1, false)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = +∞
        for each child of node:
            eval = MINIMAX(child, depth - 1, true)
            minEval = min(minEval, eval)
        return minEval

// To make a move:
function FIND_BEST_MOVE(game):
    bestMove = null
    bestValue = -∞
    for each legal move:
        result = MINIMAX(apply move, depth, false)
        if result > bestValue:
            bestValue = result
            bestMove = move
    return bestMove
```

### 3.4 Complete Worked Example

Let's illustrate minimax with a simple tic-tac-toe game truncated to 3 plies:

```
                    [Initial State]
                   X | . | .
                   . | O | .
                   . | . | .
                        |
                   (Maximizer's Turn - X to play)
                        
        +---------------+---------------+---------------+
        |               |               |
    [Position A]   [Position B]   [Position C]
    X | X | .       X | . | X       X | . | .
    . | O | .       . | O | .       . | O | .
    . | . | .       . | . | .       . | . | X
        |               |               |
    (Minimizer)     (Minimizer)     (Minimizer)
        |               |               |
   +----+----+    +----+----+    +----+----+
   |    |    |    |    |    |    |    |    |
  A1   A2   A3   B1   B2   B3   C1   C2   C3
 X|X|X|O|.   X|O|X|.   X|O.|.   X|O.|.
 X|O|O|.     X|O|O|X   X|O|O|X   X|O|X|.
 X|O|X|X     X|O|X|O   X|O|X|O   X|O|X|O

Terminal: Terminal: Terminal:
 X Wins    O Wins    Tie
 (+1)      (-1)      (0)
```

**Minimax Evaluation (Depth = 2):**

For Position A (Maximizer's move):
- A1: Terminal (+1) - Maximizer wins
- A2: Terminal (-1) - Minimizer wins  
- A3: Terminal (+1) - Maximizer wins
- **Best for Maximizer = +1** (chooses A1 or A3)

For Position B (Maximizer's move):
- B1: Terminal (0) - Tie
- B2: Terminal (0) - Tie
- B3: Terminal (0) - Tie
- **Best for Maximizer = 0**

For Position C (Maximizer's move):
- C1: Terminal (-1) - Minimizer wins
- C2: Terminal (+1) - Maximizer wins
- C3: Terminal (0) - Tie
- **Best for Maximizer = +1** (chooses C2)

**Root Decision:**
- Move A leads to +1
- Move B leads to 0
- Move C leads to +1

The Maximizer should choose either A or C (both lead to victory with optimal play from Minimizer).

---

## 4. Alpha-Beta Pruning

### 4.1 The Need for Pruning

The minimax algorithm, while theoretically sound, suffers from a critical practical limitation: it must explore the entire game tree to guarantee optimal results. For chess with a branching factor of approximately 35 and typical game depth of 80-100 plies, the search space contains roughly 10^120 positions—more than the estimated number of atoms in the observable universe.

Alpha-beta pruning dramatically reduces the search space without sacrificing optimality. It exploits the fact that once we find a clearly better or worse option, we can "prune" (ignore) entire branches of the search tree.

### 4.2 Alpha and Beta Definitions

- **Alpha (α)**: The best value that the Maximizer can guarantee at this point or above. Initially -∞.
  - Represents the lower bound of the Maximizer's assured score
  
- **Beta (β)**: The best value that the Minimizer can guarantee at this point or below. Initially +∞.
  - Represents the upper bound of the Minimizer's assured score

**Pruning Conditions:**
1. If β ≤ α: The Minimizer has found a move too good for the Maximizer; prune remaining siblings
2. If β > α: Continue searching

### 4.3 Pseudocode

```
function ALPHA_BETA(node, depth, alpha, beta, maximizingPlayer):
    // Base case
    if node is a terminal node or depth == 0:
        return heuristic value of node
    
    if maximizingPlayer == true:
        maxEval = -∞
        for each child of node:
            eval = ALPHA_BETA(child, depth - 1, alpha, beta, false)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  // Beta cutoff - prune remaining children
        return maxEval
    else:
        minEval = +∞
        for each child of node:
            eval = ALPHA_BETA(child, depth - 1, alpha, beta, true)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  // Alpha cutoff - prune remaining children
        return minEval
```

### 4.4 Complete Worked Example with Pruning

Consider this minimax tree with evaluation scores at terminal nodes:

```
                         [Root - Maximizer]
                              / | \
                            /   |   \
                          /     |     \
                       [A]    [B]    [C]
                       / \    / \    / \
                      /   \  /   \  /   \
                   3     12  5    10  2    15
                   
All terminal nodes evaluate to their labeled values
```

**Step-by-Step Alpha-Beta Execution:**

**Exploring Node A (Maximizer):**
- α = -∞, β = +∞
- Child A1: value = 3
  - α = max(-∞, 3) = 3
  - Continue (β > α)
- Child A2: value = 12
  - α = max(3, 12) = 12
  - Now β (+∞) ≤ α (12)? No, continue
- **A returns 12, α = 12**

**Back to Root (Minimizer's turn conceptually, but root is Maximizer):**
- We've found α = 12, β = +∞

**Exploring Node B:**
- α = 12 (from parent), β = +∞
- Child B1: value = 5
  - β = min(+∞, 5) = 5
  - Now β (5) ≤ α (12)? **YES! Prune B2 and B3**
  - B returns 5
- **No need to explore B2, B3** - they are pruned!

**Exploring Node C:**
- α = 12, β = +∞
- Child C1: value = 2
  - β = min(+∞, 2) = 2
  - Now β (2) ≤ α (12)? **YES! Prune C2 and C3**
  - C returns 2

**Root Decision:**
- A returns 12
- B returns 5 (pruned but evaluated first child)
- C returns 2

**Best move: A** (value = 12)

**Efficiency**: We pruned 3 terminal nodes (B2, B3, C2, C3) out of 6 total—50% reduction!

### 4.5 Implementation Example in Python

```python
import math

class GameNode:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children if children else []

def minimax(node, depth, is_maximizing):
    """Standard Minimax without alpha-beta pruning"""
    if depth == 0 or not node.children:
        return node.value
    
    if is_maximizing:
        max_eval = -math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = minimax(child, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

def alpha_beta(node, depth, alpha, beta, is_maximizing):
    """Minimax with Alpha-Beta pruning"""
    if depth == 0 or not node.children:
        return node.value
    
    if is_maximizing:
        max_eval = -math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                print(f"Pruning at maximizing node: beta={beta} <= alpha={alpha}")
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                print(f"Pruning at minimizing node: beta={beta} <= alpha={alpha}")
                break  # Alpha cutoff
        return min_eval

# Example: Building a sample game tree
# Tree structure:
#        Root (Max)
#       /   |   \
#      A    B    C
#     / \  / \  / \
#    3  12 5 10 2  15

def build_example_tree():
    # Leaf nodes
    a1 = GameNode(value=3)
    a2 = GameNode(value=12)
    b1 = GameNode(value=5)
    b2 = GameNode(value=10)
    c1 = GameNode(value=2)
    c2 = GameNode(value=15)
    
    # Intermediate nodes
    a = GameNode(children=[a1, a2])
    b = GameNode(children=[b1, b2])
    c = GameNode(children=[c1, c2])
    
    # Root
    root = GameNode(children=[a, b, c])
    
    return root

# Testing
if __name__ == "__main__":
    tree = build_example_tree()
    
    print("=== Standard Minimax ===")
    result = minimax(tree, 2, True)
    print(f"Minimax Result: {result}")
    
    print("\n=== Alpha-Beta Pruning ===")
    result = alpha_beta(tree, 2, -math.inf, math.inf, True)
    print(f"Alpha-Beta Result: {result}")
```

---

## 5. Evaluation Functions

### 5.1 Purpose and Need

Since searching to terminal states (checkmate, win/loss) is impractical for complex games, we use evaluation functions (also called heuristic functions) to estimate the desirability of non-terminal game states. The evaluation function assigns a numerical score to a board position indicating how favorable it is for the maximizing player.

### 5.2 Characteristics of Good Evaluation Functions

1. **Accuracy**: Should correlate strongly with actual winning probability
2. **Efficiency**: Must compute quickly (evaluated millions of times)
3. **Domain Knowledge**: Should capture important game-specific features

### 5.3 Example: Chess Evaluation Function

```python
def evaluate_chess_position(board, color):
    """
    Simple chess evaluation function
    Positive values favor white, negative favor black
    """
    # Piece values
    piece_values = {
        'pawn': 10,
        'knight': 30,
        'bishop': 30,
        'rook': 50,
        'queen': 90,
        'king': 900
    }
    
    # Position bonuses (center control)
    pawn_table = [
        [0,  0,  0,  0,  0,  0,  0,  0],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [5,  5, 10, 25, 25, 10,  5,  5],
        [0,  0,  0, 20, 20,  0,  0,  0],
        [5, -5,-10,  0,  0,-10, -5,  5],
        [5, 10, 10,-20,-20, 10, 10,  5],
        [0,  0,  0,  0,  0,  0,  0,  0]
    ]
    
    score = 0
    
    # Material evaluation
    for piece in board.pieces:
        value = piece_values[piece.type]
        if piece.color == color:
            score += value
        else:
            score -= value
    
    # Position bonus for pawns
    for pawn in board.get_pieces('pawn', color):
        row, col = pawn.position
        score += pawn_table[row][col]
    
    # Mobility bonus
    score += len(board.get_legal_moves(color)) * 0.1
    
    return score
```

### 5.4 Features of Evaluation Functions

| Feature | Description | Chess Example |
|---------|-------------|---------------|
| **Material** | Count of pieces | Queen = 9, Rook = 5 |
| **Position** | Control of center, development | Pawn chains, piece activity |
| **Mobility** | Number of legal moves | More moves = more options |
| **King Safety** | Protection of king | Castling, pawn shield |
| **Pawn Structure** | Doubled/isolated pawns | Weaknesses exploited |

---

## 6. Depth Limitation and Practical Considerations

### 6.1 Why Limit Depth?

Even with alpha-beta pruning, searching the full game tree is impossible for complex games. We must limit search depth and rely on evaluation functions at leaf nodes.

**Depth-4 search in chess**: ~10^6 positions
**Depth-8 search in chess**: ~10^9 positions

### 6.2 Quiescence Search

A problem with fixed-depth search: the evaluation may occur at a "noisy" position (e.g., just before a piece capture). Quiescence search extends the search for capture moves until a "quiet" position is reached.

```python
def quiescence(board, alpha, beta, depth):
    """Extend search for capture moves"""
    stand_pat = evaluate(board)
    
    if depth == 0:
        return stand_pat
    
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat
    
    # Search capture moves only
    for move in board.get_capture_moves():
        board.make_move(move)
        score = -quiescence(board, -beta, -alpha, depth - 1)
        board.undo_move(move)
        
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    
    return alpha
```

### 6.3 Iterative Deepening

A practical technique that combines the benefits of different search depths:

```python
def iterative_deepening(board, max_time):
    """Iteratively deepen search until time runs out"""
    depth = 1
    best_move = None
    
    while time_remaining():
        result = alpha_beta(board, depth, -math.inf, math.inf, True)
        if result != "timeout":
            best_move = result['move']
        depth += 1
    
    return best_move
```

**Advantages:**
- Always has a result available (useful for time control)
- Improves move ordering for better pruning
- Can abort gracefully when time runs out

### 6.4 Move Ordering for Better Pruning

The effectiveness of alpha-beta pruning depends heavily on move ordering:

- **Best-first**: Try best moves from previous iteration
- **Captures first**: Often lead to significant changes
- **Killer heuristic**: Moves that caused cutoffs in similar positions

---

## 7. Limitations and Extensions

### 7.1 Limitations of Minimax/Alpha-Beta

1. **Exponential complexity**: Still O(b^d) worst case
2. **Deterministic assumption**: Doesn't handle chance nodes
3. **Perfect information**: Limited for games with hidden information
4. **Evaluation function errors**: Garbage in, garbage out
5. **Horizon effect**: Missing tactics just beyond search depth

### 7.2 Advanced Extensions

| Technique | Description | Use Case |
|-----------|-------------|----------|
| **Expectiminimax** | Handles chance nodes | Backgammon, Poker |
| **Monte Carlo Tree Search** | Probabilistic exploration | Go, complex games |
| **Transposition Tables** | Cache evaluated positions | All games |
| **Principal Variation Search** | Optimized alpha-beta | High-performance engines |

---

## 8. Key Takeaways

1. **Game Playing in AI** involves creating intelligent agents that can make optimal decisions in competitive, adversarial environments with conflicting objectives.

2. **Minimax Algorithm** is the foundational algorithm for two-player zero-sum games with perfect information. It assumes optimal play from both sides and recursively evaluates all possible game states to determine the optimal move.

3. **Alpha-Beta Pruning** significantly improves efficiency without sacrificing optimality by eliminating branches that cannot influence the final decision. In best-case scenarios, it reduces complexity from O(b^d) to O(b^(d/2)).

4. **Evaluation Functions** estimate the desirability of non-terminal game states by combining multiple features like material advantage, positional strength, mobility, and king safety.

5. **Depth Limitation** is necessary for practical game-playing programs. Techniques like quiescence search and iterative deepening help manage the trade-off between search depth and computational efficiency.

6. **Move Ordering** is critical for effective alpha-beta pruning—examining the most promising moves first maximizes the number of pruned branches.

7. The branching factor of a game determines its computational complexity. Chess (~35) is significantly harder than checkers (~10), which is harder than tic-tac-toe (~4-9).

---

## 9. Multiple Choice Questions

**Question 1:** In the minimax algorithm, what is the role of the Maximizer?
- a) To minimize the score
- b) To maximize the score
- c) To prune the search tree
- d) To evaluate terminal states

**Question 2:** Alpha-beta pruning guarantees:
- a) Finding a solution faster but possibly suboptimal
- b) Finding the optimal solution with less computation
- c) Finding a solution for games with chance nodes
- d) Eliminating all unnecessary nodes

**Question 3:** What happens when beta ≤ alpha in alpha-beta pruning?
- a) Continue searching all children
- b) Prune the remaining siblings
- c) Return alpha value immediately
- d) Change the maximizing player to minimizing

**Question 4:** Which of the following is NOT a characteristic of a good evaluation function?
- a) Accuracy
- b) Efficiency
- c) Complexity
- d) Domain knowledge

**Question 5:** In chess, what is the approximate branching factor?
- a) 2-5
- b) 10-15
- c) 30-35
- d) 100-120

**Question 6:** What is the primary purpose of the quiescence search?
- a) To speed up the algorithm
- b) To avoid the horizon effect
- c) To improve move ordering
- d) To handle time constraints

**Question 7:** Which algorithm is used for games with chance nodes?
- a) Minimax
- b) Alpha-Beta
- c) Expectiminimax
- d) A* Search

**Question 8:** The complexity of alpha-beta pruning in the worst case is:
- a) O(b^d)
- b) O(b^(d/2))
- c) O(d)
- d) O(n)

**Question 9:** Iterative deepening provides all the following advantages EXCEPT:
- a) Always has a result available
- b) Improves move ordering
- c) Guarantees optimal solution
- d) Graceful time management

**Question 10:** What does a higher branching factor indicate?
- a) Easier game to solve
- b) More complex search space
- c) Better pruning efficiency
- d) Simpler evaluation function

---

**Answers:**
1. (b) 2. (b) 3. (b) 4. (c) 5. (c) 6. (b) 7. (c) 8. (a) 9. (c) 10. (b)

---

## 10. Flashcards for Quick Review

| Term | Definition |
|------|------------|
| **Minimax** | A recursive algorithm for solving two-player zero-sum games assuming optimal play |
| **Alpha (α)** | The best value the Maximizer can guarantee; lower bound |
| **Beta (β)** | The best value the Minimizer can guarantee; upper bound |
| **Pruning** | Eliminating branches of the search tree that cannot influence the final decision |
| **Evaluation Function** | Heuristic that estimates the desirability of a non-terminal game state |
| **Branching Factor** | Average number of legal moves available at each game state |
| **Horizon Effect** | Problem where the search misses important events just beyond the search depth |
| **Quiescence Search** | Extended search that continues through capture moves to reach "quiet" positions |
| **Iterative Deepening** | Technique of repeatedly deepening search with increasing depth limits |
| **Zero-Sum Game** | A game where one player's gain equals the other's loss |
| **Perfect Information** | Game state where all players have complete knowledge of the game |
| **Killer Heuristic** | Optimization that remembers moves that caused cutoffs |
| **Transposition Table** | Cache storing previously evaluated positions to avoid recomputation |
| **Principal Variation** | The line of play that the search determines to be optimal |

---

## References for Further Study

1. Russell, S. & Norvig, P. - "Artificial Intelligence: A Modern Approach" (Chapter 5)
2. Knuth, D.E. & Moore, R.W. - "An Analysis of Alpha-Beta Pruning"
3. Delhi University B.Sc. (Hons) Computer Science NEP 2024 UGCF Syllabus

---

*This study material is prepared for Delhi University B.Sc. (Hons) Computer Science students under NEP 2024 UGCF curriculum.*