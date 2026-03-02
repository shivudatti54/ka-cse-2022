# Backward Chaining - Summary

## Key Definitions and Concepts

- **Backward Chaining**: A goal-driven inference technique that starts with a hypothesis and works backwards through rules to find supporting facts
- **Top-Down Reasoning**: Another name for backward chaining, emphasizing the goal-to-facts direction
- **AND-OR Graph**: A tree structure representing the decomposition of goals, where AND nodes require all sub-goals and OR nodes allow any alternative
- **Sub-goal**: A smaller goal created when trying to prove the parent goal through rule antecedents

## Important Formulas and Theorems

The backward chaining algorithm follows this fundamental logic:

```
prove(goal):
    if goal is in facts: return TRUE
    find rules R where conclusion matches goal
    for each rule R:
        if prove(all antecedents of R): return TRUE
    return FALSE
```

This recursive structure ensures depth-first exploration of the rule space until primitive facts are reached.

## Key Points

- Backward chaining is goal-directed, starting from a hypothesis and working backwards to find supporting evidence
- It uses depth-first search strategy through the rule base
- Highly efficient when specific conclusions need to be verified rather than all possible conclusions
- Used extensively in diagnostic systems, troubleshooting applications, and Prolog programming
- AND nodes in the search graph require ALL conditions to be satisfied
- OR nodes require ONLY ONE alternative path to succeed
- Terminates with success (goal proven), failure (goal disproven), or unknown (insufficient information)

## Common Mistakes to Avoid

1. **Confusing direction**: Students often confuse backward chaining with forward chaining—remember backward goes goal-to-facts
2. **Ignoring AND conditions**: Failing to recognize that all conditions in an AND node must be satisfied
3. **Assuming exhaustive search**: Backward chaining doesn't explore all rules—only those relevant to the goal
4. **Forgetting termination**: Not considering all three termination conditions (success, failure, unknown)

## Revision Tips

1. **Practice tracing**: Solve at least 3-4 backward chaining examples by hand to understand the flow
2. **Draw AND-OR graphs**: Visualizing the goal decomposition helps understand the recursive structure
3. **Compare with forward chaining**: Study both techniques together to appreciate when each is appropriate
4. **Know the Prolog connection**: Understanding Prolog's inference mechanism reinforces backward chaining concepts
