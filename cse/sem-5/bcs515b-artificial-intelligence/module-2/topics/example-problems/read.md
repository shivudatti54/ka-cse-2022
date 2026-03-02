# Example Problems in Artificial Intelligence

## Introduction

The theoretical foundations of artificial intelligence provide the framework for understanding how autonomous agents can solve complex problems through systematic exploration of possible solutions. However, mere comprehension of search algorithms and optimization techniques remains insufficient for practical AI implementation. The formalization of real-world problems into computational representations constitutes a fundamental skill that bridges theoretical knowledge and practical application.

Classic example problems in AI serve as canonical benchmarks for evaluating algorithmic performance, demonstrating state space formalization techniques, and illustrating the characteristics that distinguish different problem types. These problems—including the 8-puzzle, 8-queens problem, water jug problem, missionary and cannibals problem, and traveling salesman problem—represent archetypal challenges that exhibit varying degrees of complexity in terms of branching factors, state space dimensionality, and constraint structures. Through systematic study of these canonical problems, students develop the analytical capabilities required to transform ambiguous problem descriptions into well-defined state representations amenable to algorithmic solution.

## Theoretical Foundations

### State Space Formalization

A search problem requires precise mathematical specification through its state space—the complete set of reachable configurations from the initial state through legal operations. Formally, a search problem P is defined as the quintuple (S, s₀, A, G, c), where:

- **S** denotes the finite or infinite set of all possible states
- **s₀ ∈ S** represents the initial state
- **A** represents the set of applicable actions or operators
- **G ⊆ S** defines the goal states
- **c: S × A → S** is the state transition function

The size and topological structure of the state space directly impact the selection of appropriate search strategies. Understanding whether the state space forms a tree or graph, whether it contains cycles, and whether goal states are reachable from the initial state are critical considerations in algorithm design.

### State Representation

The manner in which states are represented directly impacts both computational efficiency and algorithmic design. Common representation schemes include:

1. **Sequential Representation**: States encoded as ordered sequences (arrays, lists) where position matters
2. **Configuration Representation**: States represented as grids, graphs, or structural configurations
3. **Attribute-based Representation**: States described by tuples of attributes with specific domains

The choice of representation affects operator application efficiency and goal test complexity.

## Classic AI Problems

### The 8-Puzzle Problem

The 8-puzzle consists of a 3×3 grid containing eight numbered tiles (1-8) and one empty space. The objective is to transform an initial configuration into a goal configuration (typically the ordered arrangement with blank in bottom-right position) through sliding operations that move adjacent tiles into the empty space.

**State Representation**: Using a linear array of nine positions indexed 0-8, with 0 representing the blank tile, the goal state is: [1, 2, 3, 4, 5, 6, 7, 8, 0]

**Branching Factor Analysis**: The number of legal moves depends on blank position:

- Corner positions: 2 possible moves
- Edge positions: 3 possible moves
- Center position: 4 possible moves
- Average branching factor ≈ 3

**State Space Properties**: The 8-puzzle has 181,440 reachable states from any given initial configuration. A fundamental result in puzzle theory states that exactly half of all possible configurations are unsolvable—this parity property can be formally proven through analyzing permutation inversions.

**Theorem (Puzzle Solvability)**: A configuration is solvable if and only if the number of inversions (pairs of tiles i < j where tile i appears after tile j in the sequence) is even.

### The 8-Queens Problem

This constraint satisfaction problem requires placing eight queens on a standard 8×8 chessboard such that no two queens attack each other—meaning no two queens share the same row, column, or diagonal.

**Problem Formalization**: Find an assignment Q = {q₁, q₂, ..., q₈} where qᵢ = (rowᵢ, colᵢ) satisfying:

- rowᵢ ≠ rowⱼ for all i ≠ j (no same row)
- colᵢ ≠ colⱼ for all i ≠ j (no same column)
- |rowᵢ - rowⱼ| ≠ |colᵢ - colⱼ| for all i ≠ j (no same diagonal)

**State Space Analysis**: The total number of arrangements is C(64, 8) = 4,426,165,368. However, only 92 solutions exist after accounting for symmetry, yielding 12 fundamental solutions.

### Water Jug Problem

Two jugs with capacities A and B gallons must measure exactly Z gallons using operations: fill a jug from the water source, empty a jug completely, or pour water from one jug to another until either source is empty or destination is full.

**Formal State Model**: A state is represented as (x, y) where:

- x = current water in jug 1 (0 ≤ x ≤ A)
- y = current water in jug 2 (0 ≤ y ≤ B)

**State Transition Function**:

- Fill jug 1: (x, y) → (A, y)
- Fill jug 2: (x, y) → (x, B)
- Empty jug 1: (x, y) → (0, y)
- Empty jug 2: (x, y) → (x, 0)
- Pour jug 1 to jug 2: (x, y) → (max(0, x - (B - y)), min(B, x + y))

This exemplifies problems with discrete state transitions and arithmetic constraints.

### Missionaries and Cannibals Problem

Three missionaries and three cannibals must cross a river using a boat that holds at most two people. The constraint requires that cannibals must never outnumber missionaries on either bank.

**State Representation**: A state is defined as (M, C, B) where:

- M = number of missionaries on the starting bank (0-3)
- C = number of cannibals on the starting bank (0-3)
- B = boat position (0 = starting side, 1 = destination side)

Initial state: (3, 3, 0), Goal state: (0, 0, 1)

**Constraint Satisfaction**: At each state, both banks must satisfy: if M > 0, then M ≥ C

### Traveling Salesman Problem (TSP)

Given n cities with pairwise distances, find the shortest tour visiting each city exactly once and returning to the starting city. This NP-hard combinatorial optimization problem has a state space of (n-1)!/2 unique tours for symmetric distance matrices.

## Worked Examples

### Example 1: 8-Puzzle Analysis Using BFS

**Problem**: Given initial state [1, 2, 3, 4, 5, 6, 7, 0, 8] and goal state [1, 2, 3, 4, 5, 6, 7, 8, 0], find the solution sequence.

**Solution**:

1. Initial state S₀: Position index 8 contains 0 (blank)
2. Legal moves from S₀: slide tile 8 left into blank position (other moves possible based on blank location)
3. Resulting state S₁: [1, 2, 3, 4, 5, 6, 7, 8, 0]
4. BFS explores level by level: depth 1 yields 2-4 successors, depth 2 yields 9-16 successors, depth 3 yields 24-36 successors

**Complexity Analysis**: For this configuration, the optimal solution requires 26 moves. BFS guarantees the shortest path but may explore 100,000-500,000 nodes for moderately difficult configurations, demonstrating the trade-off between completeness and computational cost.

### Example 2: Water Jug Problem (5-gallon and 3-gallon jugs)

**Problem**: Measure exactly 4 gallons using a 5-gallon jug and a 3-gallon jug.

**Solution Sequence**:

1. Fill 5-gallon jug: (5, 0)
2. Pour from 5 into 3: (2, 3)
3. Empty 3-gallon jug: (2, 0)
4. Pour from 5 into 3: (0, 2)
5. Fill 5-gallon jug: (5, 2)
6. Pour from 5 into 3 until 3 is full: (4, 3)

**Goal achieved**: 4 gallons in the 5-gallon jug.

### Example 3: 8-Queens Problem Using Backtracking

**Problem**: Place 8 queens on the chessboard with no attacks.

**Solution Process**:

- Column 1: Place queen at row 1 → [1, -, -, -, -, -, -, -]
- Column 2: Rows 1, 2 conflict; try row 3 → [1, 3, -, -, -, -, -, -]
- Column 3: Try row 5 → [1, 3, 5, -, -, -, -, -]
- Continue systematically until all 8 queens placed

**One Valid Solution**: [1, 5, 8, 6, 3, 7, 2, 4]

## Algorithm Analysis

### Search Complexity Considerations

Understanding the relationship between problem characteristics and algorithmic performance is essential:

| Metric           | Definition                            | Relevance                          |
| ---------------- | ------------------------------------- | ---------------------------------- |
| Time Complexity  | Number of nodes generated             | Affects runtime                    |
| Space Complexity | Maximum frontier size                 | Affects memory requirements        |
| Completeness     | Guarantees solution if one exists     | Required for infinite state spaces |
| Optimality       | Guarantees shortest/cheapest solution | Required for optimization problems |

**Key Insight**: BFS guarantees completeness and optimality for unweighted graphs but requires O(b^d) space, where b is branching factor and d is solution depth. DFS requires O(bm) space (m = maximum depth) but sacrifices optimality and may explore irrelevant branches.

The selection between search strategies depends on problem characteristics: state space size, solution depth requirements, memory constraints, and whether the problem requires optimal solutions.
