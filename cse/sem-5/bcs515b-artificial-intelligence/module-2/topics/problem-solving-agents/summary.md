# Problem Solving Agents - Summary

## Key Definitions and Concepts

- **Problem Solving Agent**: An AI agent that uses search techniques to find a sequence of actions transforming an initial state to a goal state.
- **State Space**: The complete set of all reachable states from the initial state through legal operators.
- **Well-Defined Problem**: A problem with five components: initial state, goal state, operators, state space, and path cost.
- **Heuristic Function h(n)**: An estimate of the cost from state n to the nearest goal state.
- **Admissible Heuristic**: A heuristic that never overestimates the true cost (required for optimal A\*).

## Important Formulas and Theorems

- **BFS Complexity**: Time O(b^d), Space O(b^d) - Complete and optimal for unit costs
- **DFS Complexity**: Time O(b^m), Space O(bm) - Not complete for infinite spaces
- **A\* Evaluation**: f(n) = g(n) + h(n), where g(n) = path cost, h(n) = heuristic estimate
- **A\* Completeness**: Complete if branching factor is finite and all costs are positive
- **A\* Optimality**: Optimal if h(n) is admissible (never overestimates)

## Key Points

- Problem solving agents use explicit goal-directed search rather than simple reactive behavior.
- Uninformed searches (BFS, DFS, UCS) have no problem-specific knowledge; informed searches (Greedy, A\*) use heuristics.
- BFS always finds the shortest path when all operators have equal cost; A\* finds optimal path with admissible heuristics.
- The quality of heuristic directly determines informed search efficiency—better heuristics explore fewer nodes.
- Space complexity is often more limiting than time complexity in practical applications.
- A\* combines the advantages of uniform-cost search and greedy best-first search.

## Common Mistakes to Avoid

1. **Confusing BFS with DFS complexity**: Remember BFS is exponential in space while DFS is linear in space (but exponential in time).

2. **Using inadmissible heuristics with A\***: Non-admissible heuristics may lead to suboptimal solutions even though A\* still finds a solution.

3. **Ignoring branching factor**: The effectiveness of search algorithms depends heavily on the problem's branching factor.

4. **Forgetting that DFS can get stuck**: DFS is not complete for infinite state spaces and can loop infinitely without proper visited state tracking.

## Revision Tips

1. Practice formulating new problems by identifying states, operators, and goals—exam questions often test this skill.

2. Memorize the trade-offs between search algorithms: BFS for shortest path, DFS for memory-limited scenarios, A\* for optimal efficient search.

3. Work through the 8-puzzle example with both BFS and A\* to understand the practical difference heuristics make.

4. Remember that heuristics like Manhattan distance for sliding puzzles are admissible because they underestimate true moves needed.
