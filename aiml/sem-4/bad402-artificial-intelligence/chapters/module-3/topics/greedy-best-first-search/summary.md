# Greedy Best First Search

### Definition

Greedy Best First Search (GBFS) is a heuristic search algorithm used to find the shortest path or a good solution in optimization problems. It is a variant of Best First Search (BFS) that uses a heuristic function to guide the search.

### Key Points

- **Heuristic Function**: A function that estimates the cost to reach the goal from a given state.
- **Greedy Choice**: The algorithm chooses the next state by selecting the one with the lowest estimated cost.
- **No Backtracking**: The algorithm does not revisit previously explored states.
- **Guaranteed to Find a Solution**: If the heuristic function is admissible (never overestimates the cost) and consistent (the estimated cost to reach the goal from a given state is less than or equal to the true cost), then GBFS is guaranteed to find a solution.

### Important Formulas and Definitions

- **Admissible Heuristic**: A heuristic function that never overestimates the cost to reach the goal.
- **Consistent Heuristic**: A heuristic function that always estimates the cost to reach the goal from a given state as less than or equal to the true cost.
- **Estimated Total Cost**: The sum of the costs to reach the current state and the estimated cost to reach the goal from the current state.

### Theorem

- **Greedy Best First Search Theorem**: If the heuristic function is admissible and consistent, then GBFS is guaranteed to find a solution.

### Important Theorems and Results

- **A\* (A-Star) Algorithm**: A variant of GBFS that uses an admissible heuristic function to guide the search.
