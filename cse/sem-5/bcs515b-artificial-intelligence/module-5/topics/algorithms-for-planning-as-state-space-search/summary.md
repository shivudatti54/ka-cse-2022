# Algorithms for Planning as State Space Search - Summary

## Key Definitions and Concepts

- **Planning Problem**: Tuple (P, A, I, G) where P=propositions, A=actions, I=initial state, G=goal state
- **State Space**: Graph where nodes are states and edges are action applications
- **Forward Search**: Progression from initial state toward goal using applicable actions
- **Backward Search**: Regression from goal state to find states that can lead to it
- **Partial-Order Planning**: Builds partially ordered action plans without committing to total order early

## Important Formulas and Theorems

- **Delete List Relaxation Heuristic**: Ignore negative effects, count unsatisfied goals
- **Additive Heuristic**: h(n) = Σ cost(goal_i) - may underestimate actual cost
- **Max Heuristic**: h(n) = max(cost(goal_i)) - always admissible
- **Planning Graph Levels**: S₀ → A₀ → S₁ → A₁ → S₂... alternating proposition and action levels

## Key Points

- State space search treats planning as graph traversal from initial to goal states
- Forward search is intuitive but may explore irrelevant states; backward search is more focused but has complex regression
- Heuristics are essential for efficient planning; delete list relaxation is the foundational approach
- Partial-order planning offers flexibility by not committing to action ordering prematurely
- Planning graphs provide leveled structure with mutex links indicating incompatibility
- Admissible heuristics (max, additive) are crucial for optimal search with A\*
- Graphplan uses planning graphs to efficiently extract solutions

## Common Mistakes to Confuse

- Confusing forward and backward search directions
- Forgetting that delete list relaxation ignores negative effects
- Mixing up admissible vs inadmissible heuristics
- Not understanding mutex links in planning graphs

## Revision Tips

1. Practice tracing forward and backward search on simple problems like blocks world
2. Memorize the planning problem tuple definition
3. Remember that heuristics estimate cost to goal, not actual cost
4. Focus on understanding when each algorithm type is appropriate
