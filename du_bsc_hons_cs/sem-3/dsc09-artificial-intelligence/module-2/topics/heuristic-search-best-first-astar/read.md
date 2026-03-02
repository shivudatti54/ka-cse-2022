# Heuristic Search: Best-First Search and A* Algorithm

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

### 1.1 What is Heuristic Search?

Heuristic Search is a fundamental concept in Artificial Intelligence that guides problem-solving by using "rules of thumb" or heuristic functions to estimate the cost or distance to the goal. Unlike uninformed search strategies (like BFS or DFS) that explore the search space blindly, heuristic search leverages domain-specific knowledge to make intelligent decisions about which path to explore next.

In the context of the Delhi University BSc (Hons) Computer Science syllabus (NEP 2024 UGCF), this topic falls under the **Artificial Intelligence** paper and is essential for understanding how AI systems make optimal decisions in large state spaces.

### 1.2 Real-World Relevance

Heuristic search algorithms power numerous real-world applications:

- **Navigation Systems**: Google Maps and GPS devices use A* algorithm to find optimal routes between locations
- **Game AI**: Pathfinding in video games (enemy characters finding the player)
- **Robotics**: Robot navigation and motion planning
- **Puzzle Solving**: Solving the 8-puzzle, 15-puzzle, and Rubik's cube
- **Network Routing**: Finding optimal paths in computer networks
- **Resource Allocation**: Scheduling and planning problems

---

## 2. Fundamentals of Heuristic Search

### 2.1 What is a Heuristic Function?

A **heuristic function** (denoted as **h(n)**) is an estimation function that calculates the approximate cost from a given node **n** to the goal node. It provides "domain knowledge" to the search algorithm.

**Key characteristics:**
- **h(n)** returns a numeric value representing estimated cost
- It is problem-specific (different problems require different heuristics)
- It must be efficient to compute (otherwise it defeats the purpose)

### 2.2 Heuristic Search vs Uninformed Search

| Aspect | Uninformed Search | Heuristic Search |
|--------|------------------|-------------------|
| **Knowledge Used** | None (blind) | Domain-specific (heuristic) |
| **Search Strategy** | Systematic exploration | Directed exploration |
| **Efficiency** | Generally slow | Generally faster |
| **Optimality** | BFS provides optimality | Depends on heuristic quality |
| **Memory Usage** | High for large spaces | Lower due to focused search |

---

## 3. Best-First Search

### 3.1 Concept and Motivation

**Best-First Search** is an informed search algorithm that explores the search space by selecting the most promising node based on a heuristic evaluation function. It combines the systematic nature of graph search with intelligent node selection.

### 3.2 Greedy Best-First Search

The **Greedy Best-First Search** algorithm always expands the node that appears to be closest to the goal based on the heuristic function **h(n)**.

**Algorithm Steps:**
```
1. Initialize: Insert start node into OPEN list
2. While OPEN is not empty:
   a. Remove the node with lowest h(n) value from OPEN
   b. If this node is the goal, return success
   c. Generate successors of this node
   d. For each successor:
      - If not visited before, add to OPEN
      - If visited, check if better path found
3. If goal not reached, return failure
```

**Advantages:**
- Fast and memory-efficient
- Often finds a solution quickly
- Simple to implement

**Disadvantages:**
- **Not guaranteed to be optimal** - may find a suboptimal path
- Can get stuck in loops if not careful
- Ignores the actual cost accumulated so far (**g(n)**)

### 3.3 Example: Greedy Best-First Search

Consider finding a route from City A to City E:

```
        B(4)
       /   \
      A(6)   D(3)
       \   /
        C(2)
         |
         E(0)
```
*(Numbers represent h(n) - estimated distance to goal E)*

**Greedy Best-First Search progression:**
1. Start at A: h(A)=6 → Add to OPEN
2. Expand A (lowest h): generates B(h=4), C(h=2)
3. Expand C (h=2): generates E(h=0)
4. **Goal reached! Path: A → C → E**

Note: This path may not be optimal in terms of actual distance traveled.

---

## 4. A* Algorithm: The Complete Explanation

### 4.1 Introduction to A*

**A* (A-Star)** is one of the most successful and widely-used heuristic search algorithms. It combines the benefits of both Dijkstra's algorithm (which finds shortest paths using actual cost) and Greedy Best-First Search (which uses heuristic guidance).

**Key Innovation**: A* uses **both** the cost accumulated so far **and** the estimated cost to the goal.

### 4.2 The A* Evaluation Function: f(n) = g(n) + h(n)

The A* algorithm uses a comprehensive evaluation function:

```
f(n) = g(n) + h(n)
```

Where:
- **g(n)**: The actual cost from the start node to node n (the path cost so far)
- **h(n)**: The heuristic estimate from node n to the goal
- **f(n)**: The estimated total cost of the path through node n to the goal

**Intuitive Understanding:**
- **g(n)** tells us: "How much have we spent so far?"
- **h(n)** tells us: "How much more will we need?"
- **f(n)** tells us: "What's the estimated total cost?"

A* always selects the node with the **lowest f(n)** value to expand next.

### 4.3 A* Algorithm Pseudocode

```python
def a_star_search(start, goal, neighbors, h):
    """
    A* Search Algorithm
    
    Parameters:
    - start: Starting node
    - goal: Goal node
    - neighbors: Function that returns (neighbor, cost) pairs
    - h: Heuristic function estimating cost to goal
    
    Returns:
    - Path from start to goal (if found)
    """
    
    # Priority queue ordered by f(n) = g(n) + h(n)
    open_set = PriorityQueue()
    open_set.put((f(start), start))
    
    # Track the path
    came_from = {}
    
    # g(n): Cost from start to node n
    g_score = {start: 0}
    
    # f(n): g(n) + h(n)
    f_score = {start: h(start)}
    
    while not open_set.empty():
        # Get node with lowest f_score
        current = open_set.get()[1]
        
        # Goal check
        if current == goal:
            return reconstruct_path(came_from, current)
        
        # Explore neighbors
        for neighbor, move_cost in neighbors(current):
            # Tentative g score
            tentative_g = g_score[current] + move_cost
            
            # If this path is better than any previous one
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                # Update tracking
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h(neighbor)
                open_set.put((f_score[neighbor], neighbor))
    
    return None  # No path found


def reconstruct_path(came_from, current):
    """Reconstruct path from goal to start"""
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  # Reverse to get start-to-goal
```

### 4.4 A* Algorithm - Step by Step Example

Consider this graph (find path from S to G):

```
        A(3) --- 1 --- B(2)
       /                  \
    S(6)                   G(0)
       \                  /
        D(2) --- 2 --- E(3)
```
*(Node labels: Node(cost to goal))*

**h(n) values**: S=6, A=3, B=2, D=2, E=3, G=0

**Step-by-step execution:**

| Step | Node Expanded | g(n) | h(n) | f(n)=g+h | OPEN Queue (sorted by f) |
|------|--------------|------|------|----------|-------------------------|
| 1 | S | 0 | 6 | 6 | A(3+1=4), D(2+2=4), E(3+2=5) |
| 2 | A | 1 | 3 | 4 | B(2+1=3), D(2+2=4), E(3+2=5) |
| 3 | B | 2 | 2 | 4 | G(0+3=3), D(2+2=4), E(3+2=5) |
| 4 | G | 3 | 0 | 3 | **GOAL FOUND!** |

**Optimal Path**: S → A → B → G (cost = 3)

### 4.5 Properties of A*

#### Optimality with Admissible Heuristics

**A* is optimal (finds the shortest path) if h(n) is admissible.**

An **admissible heuristic** never overestimates the true cost to reach the goal:
```
h(n) ≤ h*(n) for all nodes n
```
Where h*(n) is the actual minimum cost from n to goal.

**Proof intuition**: If h is admissible, A* never overestimates the cost of any solution through any node. Therefore, when it finds a solution, it must be optimal.

#### Completeness

A* is **complete** - it will find a solution if one exists (assuming finite state space and costs > 0).

#### Time and Space Complexity

- **Time Complexity**: O(b^d) where b is branching factor, d is depth of optimal solution
- **Space Complexity**: O(b^d) - stores all explored nodes in memory

---

## 5. Admissible vs Consistent (Monotonic) Heuristics

### 5.1 Admissible Heuristics

A heuristic **h(n)** is **admissible** if:
```
h(n) ≤ h*(n) for all nodes n
```
It **never overestimates** the true cost to the goal.

**Example**: Straight-line distance is admissible for pathfinding because straight lines are the shortest possible path.

### 5.2 Consistent (Monotonic) Heuristics

A heuristic **h(n)** is **consistent (or monotone)** if for every node n and every successor n':
```
h(n) ≤ cost(n, n') + h(n')
```
This is a stronger condition than admissibility.

**Interpretation**: The estimated cost to goal from n is no greater than the cost to reach n' plus the estimated cost from n' to goal.

### 5.3 Comparison Table

| Property | Admissible Heuristic | Consistent Heuristic |
|----------|---------------------|---------------------|
| **Definition** | h(n) ≤ h*(n) | h(n) ≤ cost + h(n') |
| **Overestimates** | Never | Never |
| **Triangle Inequality** | Not required | Required |
| **Optimality in A*** | Guarantees optimal solution | Guarantees optimal solution + efficiency |
| **Path Performance** | First solution optimal | First solution always optimal |
| **Example** | Manhattan distance | Euclidean distance (for certain problems) |

### 5.4 Why Consistency Matters

When h is **consistent**:
1. The f(n) values along any path are **non-decreasing**
2. When A* expands a node, it has found the **optimal path** to that node
3. No node needs to be re-expanded (saves computation)

**Example comparison** for 8-puzzle:
- **h1 = Number of misplaced tiles** (admissible, not consistent)
- **h2 = Sum of Manhattan distances** (admissible AND consistent)

---

## 6. Practical Implementation: 8-Puzzle Problem

The 8-puzzle is a classic problem for demonstrating A*.

### 6.1 Problem Definition

```
Initial State:              Goal State:
[1, 2, 3]                   [1, 2, 3]
[4, 5, 6]                   [4, 5, 6]
[7, 8, 0]                   [7, 8, 0]
```

The tile with '0' represents the blank space.

### 6.2 Implementation with A*

```python
import heapq
from typing import List, Tuple, Set, Optional

class EightPuzzle:
    def __init__(self, initial: List[List[int]], goal: List[List[int]]):
        self.initial = tuple(tuple(row) for row in initial)
        self.goal = tuple(tuple(row) for row in goal)
    
    def is_goal(self, state: Tuple[Tuple[int, ...], ...]) -> bool:
        return state == self.goal
    
    def get_blank_position(self, state: Tuple[Tuple[int, ...], ...]) -> Tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return (-1, -1)
    
    def get_neighbors(self, state: Tuple[Tuple[int, ...], ...]) -> List[Tuple[Tuple[int, ...], ...], int]]:
        """Generate all valid moves and their costs (cost = 1 for each move)"""
        neighbors = []
        row, col = self.get_blank_position(state)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
        
        for dr, dc in moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                # Swap blank with tile
                new_state = [list(r) for r in state]
                new_state[row][col], new_state[new_row][new_col] = \
                    new_state[new_row][new_col], new_state[row][col]
                neighbors.append((tuple(tuple(r) for r in new_state), 1))
        
        return neighbors
    
    def h_misplaced(self, state: Tuple[Tuple[int, ...], ...]) -> int:
        """Heuristic 1: Count misplaced tiles (excluding blank)"""
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != self.goal[i][j]:
                    count += 1
        return count
    
    def h_manhattan(self, state: Tuple[Tuple[int, ...], ...]) -> int:
        """Heuristic 2: Sum of Manhattan distances"""
        distance = 0
        for i in range(3):
            for j in range(3):
                tile = state[i][j]
                if tile != 0:
                    # Find goal position of this tile
                    for gi in range(3):
                        for gj in range(3):
                            if self.goal[gi][gj] == tile:
                                distance += abs(i - gi) + abs(j - gj)
        return distance
    
    def a_star_search(self, use_manhattan: bool = True) -> Optional[List[Tuple[Tuple[int, ...], ...]]]:
        """A* search implementation"""
        h = self.h_manhattan if use_manhattan else self.h_misplaced
        
        # Priority queue: (f(n), g(n), state, path)
        open_set = [(h(self.initial), 0, self.initial, [self.initial])]
        heapq.heapify(open_set)
        
        # Track visited states and their best g scores
        visited = {self.initial: 0}
        
        while open_set:
            f, g, current, path = heapq.heappop(open_set)
            
            if self.is_goal(current):
                return path
            
            # Skip if we've found a better path to this state
            if g > visited.get(current, float('inf')):
                continue
            
            for neighbor, cost in self.get_neighbors(current):
                new_g = g + cost
                if new_g < visited.get(neighbor, float('inf')):
                    visited[neighbor] = new_g
                    new_f = new_g + h(neighbor)
                    heapq.heappush(open_set, (new_f, new_g, neighbor, path + [neighbor]))
        
        return None


# Example usage
if __name__ == "__main__":
    initial = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]
    
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    puzzle = EightPuzzle(initial, goal)
    
    print("Using Manhattan Distance Heuristic:")
    path = puzzle.a_star_search(use_manhattan=True)
    if path:
        print(f"Solution found in {len(path) - 1} moves")
    
    print("\nUsing Misplaced Tiles Heuristic:")
    path = puzzle.a_star_search(use_manhattan=False)
    if path:
        print(f"Solution found in {len(path) - 1} moves")
```

### 6.3 Sample Output

```
Using Manhattan Distance Heuristic:
Solution found in 3 moves

Using Misplaced Tiles Heuristic:
Solution found in 5 moves
```

**Note**: Manhattan distance is a stronger heuristic (more accurate), resulting in fewer node expansions and faster solution.

---

## 7. Dijkstra's Algorithm as Special Case of A*

When the heuristic function **h(n) = 0** for all nodes, A* degenerates to **Dijkstra's Algorithm**:

```
f(n) = g(n) + 0 = g(n)
```

This means Dijkstra's algorithm explores nodes in order of actual cost from start, with no heuristic guidance. It finds the shortest path but explores more nodes than A* with a good heuristic.

---

## 8. Key Takeaways

1. **Heuristic Search** uses domain knowledge (heuristic function h(n)) to efficiently explore the search space, balancing between actual cost and estimated cost.

2. **Greedy Best-First Search** expands nodes based solely on h(n), making it fast but not guaranteed to find optimal solutions.

3. **A* Algorithm** combines g(n) (actual cost from start) and h(n) (estimated cost to goal) using f(n) = g(n) + h(n), providing both optimality and efficiency.

4. **Admissible Heuristics** never overestimate the true cost and guarantee optimal solutions with A*.

5. **Consistent (Monotonic) Heuristics** satisfy the triangle inequality, ensuring A* never needs to re-expand nodes and finds optimal solutions more efficiently.

6. **Heuristic Dominance**: If h1(n) ≥ h2(n) for all nodes (and both are admissible), then h1 dominates h2 and will expand fewer nodes.

7. **For Delhi University Exam**: Remember that A* is complete, optimal (with admissible h), and optimally efficient given the same heuristic constraints.

---

## 9. Practice Questions (MCQs)

### Multiple Choice Questions

**Q1. In A* algorithm, the evaluation function f(n) = g(n) + h(n), where:**
- (a) g(n) is heuristic estimate to goal
- (b) h(n) is cost from start to n
- (c) g(n) is cost from start to n
- (d) h(n) is always greater than actual cost

**Q2. A* algorithm is guaranteed to find optimal solution if:**
- (a) h(n) is always positive
- (b) h(n) is admissible
- (c) h(n) is consistent
- (d) h(n) = 0 for all nodes

**Q3. Which heuristic is admissible for the 8-puzzle?**
- (a) Number of tiles in correct position
- (b) Sum of Manhattan distances
- (c) Number of inversions
- (d) None of the above

**Q4. Greedy Best-First Search is:**
- (a) Complete and optimal
- (b) Complete but not optimal
- (c) Not complete but optimal
- (d) Neither complete nor optimal

**Q5. If heuristic h is consistent, then:**
- (a) It is also admissible
- (b) A* never re-expands nodes
- (c) f(n) is non-decreasing along any path
- (d) All of the above

**Answers**: 1-(c), 2-(b), 3-(b), 4-(b), 5-(d)

---

## 10. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **Heuristic Function h(n)** | Estimates the cost from node n to the goal |
| **g(n)** | Actual cost from start node to node n |
| **f(n)** | Estimated total cost = g(n) + h(n) |
| **Admissible Heuristic** | Never overestimates: h(n) ≤ h*(n) |
| **Consistent Heuristic** | Satisfies triangle inequality: h(n) ≤ cost + h(n') |
| **Optimality** | Property of finding the shortest path solution |
| **Completeness** | Property of finding a solution if one exists |
| **Branching Factor** | Average number of successors per node |

---

## 11. References

1. Russell, S. & Norvig, P. - "Artificial Intelligence: A Modern Approach" (Chapter 3)
2. Delhi University BSc (Hons) Computer Science Syllabus - NEP 2024 UGCF
3. Primary Notes: Informed Search - Heuristic Search Strategies

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum.*