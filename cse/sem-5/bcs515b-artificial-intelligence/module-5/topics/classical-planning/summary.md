# Classical Planning - Summary

## Key Definitions and Concepts

- **Classical Planning**: A planning paradigm assuming fully observable, deterministic, static environments with explicit state representations.
- **Planning Problem**: Tuple (S, A, I, G, γ) where S=states, A=actions, I=initial state, G=goal state, γ=transition function.
- **STRIPS**: Action representation with preconditions (required conditions), add list (effects that become true), and delete list (effects that become false).
- **Partial-Order Planning (POP)**: Planning approach maintaining unordered actions and resolving constraints incrementally.
- **Planning Graph**: Data structure with alternating proposition and action layers for efficient planning.
- **PDDL**: Planning Domain Definition Language - standard formalism for describing planning problems.

## Important Formulas and Theorems

- **Delete-list relaxation heuristic**: h₁(n) = minimum number of actions needed ignoring delete effects
- **Goal regression**: γ(s, a) is applicable if preconditions(a) ⊆ s; regress goal G through action a yields (G - add(a)) ∪ preconditions(a)

## Key Points

- Classical planning assumes deterministic, fully observable environments unlike real-world planning.
- Forward search (progression) starts from initial state; backward search (regression) starts from goal.
- STRIPS provides a simple yet powerful representation for actions with preconditions and effects.
- Partial-order planning is more flexible than total-order planning and handles independent subgoals naturally.
- Planning graphs provide polynomial-time heuristics and can detect unsolvable problems efficiently.
- Delete-list relaxation heuristic is admissible (never overestimates cost).
- PDDL separates domain definition from specific problem instances.

## Common Mistakes to Avoid

- Confusing preconditions with effects—they represent conditions before and after action execution.
- Forgetting that delete lists make planning harder due to action interactions.
- Not checking action applicability before applying actions in state-space search.
- Assuming classical planning handles uncertainty—it doesn't; that's for probabilistic planning.

## Revision Tips

- Practice writing STRIPS representations for simple actions like pickup, stack, unstack in blocks world.
- Work through at least one complete forward and backward search example manually.
- Remember the key advantage of POP: it considers only necessary orderings, finding more flexible solutions.
- Review planning graph structure—it alternates between proposition and action layers.
- Focus on understanding when forward vs backward search is more appropriate.
