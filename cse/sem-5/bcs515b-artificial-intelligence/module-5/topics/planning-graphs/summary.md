# Planning Graphs - Summary

## Key Definitions and Concepts

- **Planning Graph**: A directed bipartite graph that alternates between proposition levels (states) and action levels, representing the progression of a planning problem.

- **Proposition Level (Pi)**: Contains literals that could be true after i actions, along with mutex links between incompatible propositions.

- **Action Level (Ai)**: Contains ground actions whose preconditions are satisfied at level Pi-1, with mutex links between mutually exclusive actions.

- **Mutex Links**: Mutual exclusion relationships indicating that two propositions or actions cannot be true/executed simultaneously.

- **GraphPlan Algorithm**: A planning algorithm that builds a planning graph incrementally and extracts solutions through backward search.

## Important Formulas and Theorems

- Two propositions are mutex if one is the negation of the other, or if all ways to achieve them involve mutex actions.

- Two actions are mutex if: (1) one deletes a precondition or addlist of the other, or (2) their preconditions are mutex at the previous level.

- GraphPlan terminates when: (1) goal appears in a proposition level without mutex, or (2) the graph stabilizes (no new propositions added between consecutive levels).

## Key Points

- Planning graphs provide a compact representation of the planning problem's search space.

- Mutex relationships enable efficient pruning by eliminating incompatible states and actions.

- GraphPlan works in two phases: expanding the graph forward and extracting solutions backward.

- The approach is complete for classical planning problems (deterministic, fully observable, static).

- Solution extraction uses backtracking to select non-mutex action sets achieving subgoals.

## Common Mistakes to Avoid

- Confusing proposition levels with action levels—remember they always alternate.

- Forgetting that mutex links exist at both proposition and action levels.

- Assuming mutex relationships are transitive—they are not.

- Not checking all goal propositions for mutex during solution extraction.

## Revision Tips

- Practice drawing planning graphs for simple problems like blocks world.

- Memorize the conditions for mutex between propositions and actions.

- Understand the backward extraction algorithm step by step.

- Compare GraphPlan with state-space search to understand its advantages.
