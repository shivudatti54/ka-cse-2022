# Deterministic Finite Automata - Summary

## Key Definitions and Concepts

- **DFA (Deterministic Finite Automaton)**: A 5-tuple M = (Q, Σ, δ, q₀, F) where Q is states, Σ is alphabet, δ is transition function, q₀ is start state, and F is accepting states.

- **Transition Function (δ)**: Maps Q × Σ → Q, defining exactly one next state for each state-symbol pair.

- **Language of DFA**: L(M) = {w ∈ Σ\* | δ(q₀, w) ∈ F}—all strings that lead to accepting states.

- **Extended Transition Function (δ̂)**: Computes state after reading entire strings using recursion: δ̂(q, ε) = q and δ̂(q, wa) = δ(δ̂(q, w), a).

## Important Formulas and Theorems

- A DFA accepts string w if and only if δ̂(q₀, w) ∈ F
- A DFA rejects string w if and only if δ̂(q₀, w) ∉ F or transition is undefined
- Every NFA has an equivalent DFA (subset construction)
- DFAs can only accept regular languages

## Key Points

1. DFAs are deterministic: one transition per state-symbol pair
2. Start state q₀ must be in Q, accepting states F ⊆ Q
3. Transition function must be total (defined for all combinations) in complete DFAs
4. The empty string ε is accepted if q₀ ∈ F
5. DFAs can be represented as transition tables or transition diagrams
6. Finite automata have finite memory and cannot count unbounded
7. Languages like {0ⁿ1ⁿ | n ≥ 1} are not regular and cannot be accepted by any DFA

## Common Mistakes to Avoid

1. Forgetting to include the start state in the accepting state set when ε should be accepted
2. Leaving transitions undefined when a complete DFA is required
3. Confusing the alphabet symbols with states
4. Not checking all possible input combinations when designing transitions
5. Incorrectly determining the final state when processing strings

## Revision Tips

1. Practice drawing DFAs for simple languages: strings ending with 'a', strings containing 'ab', even-length strings
2. Always trace through example strings to verify your DFA design
3. Remember that the transition diagram helps visualize the automaton behavior
4. Focus on understanding the relationship between states and "memory" of what has been processed
5. Review the difference between DFA and NFA—DFA has exactly one path, NFA may have multiple paths
