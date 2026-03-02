# Nondeterministic Finite Automata (NFA) - Summary

## Key Definitions and Concepts

- **NFA Definition**: A 5-tuple M = (Q, Σ, δ, q₀, F) where δ: Q × (Σ ∪ {ε}) → P(Q) maps to power sets of states
- **Nondeterminism**: Multiple possible transitions from a state for the same input; acceptance requires at least one accepting computation path
- **ε-Closure**: The set of all states reachable from a given state using zero or more ε-transitions
- **Extended Transition Function (δ*)**: Computes the set of all states reachable after processing an input string

## Important Formulas and Theorems

- **Language of NFA**: L(M) = {w ∈ Σ* | δ*(q₀, w) ∩ F ≠ ∅}
- **Subset Construction**: Convert NFA to DFA by representing each DFA state as a set of NFA states
- **NFA-DFA Equivalence**: For every NFA, there exists an equivalent DFA accepting the same language; both recognize exactly the regular languages

## Key Points

1. NFAs provide a more intuitive design framework compared to DFAs for complex language patterns
2. The transition function of an NFA returns a set of possible next states (including empty set)
3. ε-transitions allow state changes without consuming input symbols
4. A string is accepted if there exists at least one path from start to an accepting state
5. The subset construction may result in up to 2^n states from an n-state NFA
6. Nondeterminism does not increase computational power—NFAs and DFAs are equivalent
7. Dead states (empty set) may be needed in DFA conversion for complete transitions

## Common Mistakes to Avoid

1. Confusing "all paths must accept" with "at least one path accepts" (the latter is correct for NFA)
2. Forgetting to compute ε-closures before processing input symbols with ε-transitions
3. Not including the original state in its own ε-closure
4. Missing states in the power set during subset construction
5. Treating empty set (∅) transitions incorrectly in DFA conversion

## Revision Tips

1. Practice tracing NFA computations step-by-step with different input strings
2. Master ε-closure computation as it's fundamental to handling ε-transitions
3. Work through multiple NFA to DFA conversions to understand the subset construction
4. Compare NFA and DFA designs for the same language to appreciate the design convenience of NFA
5. Review the equivalence proof between NFAs and DFAs from the Theory of Computation curriculum