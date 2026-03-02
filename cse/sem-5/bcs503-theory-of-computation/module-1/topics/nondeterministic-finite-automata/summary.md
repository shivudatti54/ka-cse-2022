# Non-Deterministic Finite Automata (NFA) - Summary

## Key Definitions and Concepts

- **NFA Definition**: A 5-tuple M = (Q, Σ, δ, q₀, F) where Q is states, Σ is alphabet, δ: Q × (Σ ∪ {ε}) → P(Q) is transition function, q₀ is start state, and F is set of final states.

- **Non-determinism**: From any state, multiple transitions possible for the same input, including zero transitions (ε-transitions).

- **Acceptance**: A string w is accepted if at least one path from start state to a final state consumes w.

- **ε-Closure**: Set of all states reachable from a given state via zero or more ε-transitions.

## Important Formulas and Theorems

- **Equivalence Theorem**: Every NFA has an equivalent DFA (subset/powerset construction).

- **Subset Construction**: DFA state = set of NFA states reachable simultaneously.

- **Transition in DFA**: δ_DFA(S, a) = ε\*(∪(δ(p, a) for all p in S))

## Key Points

- NFA transition function returns a set of states, not a single state.
- ε-transitions allow state changes without consuming input.
- NFA provides multiple computation paths; acceptance requires at least one successful path.
- NFAs are often easier to construct for complex language patterns.
- Subset construction may produce 2^n states from n-state NFA.
- NFA and DFA recognize exactly the same class of languages (Regular Languages).

## Common Mistakes to Avoid

- Forgetting that NFA accepts if ANY path leads to acceptance (not requiring ALL paths).
- Neglecting ε-closure when computing transitions in ε-NFA.
- Treating empty set (∅) as a valid DFA state during subset construction.
- Confusing the start state with final states - they can be the same state.

## Revision Tips

- Practice drawing NFAs for various language patterns (strings starting/ending with specific symbols, containing substrings).
- Memorize the subset construction algorithm steps with an example.
- Remember: non-determinism does not increase computing power, only provides convenience.
- Review examples of converting NFA to DFA to understand the state explosion phenomenon.
