# Structural Representations - Summary

## Key Definitions

- **State Transition Diagram**: A directed graph representation of a finite automaton where vertices are states and labeled edges represent transitions
- **Transition Table**: A matrix representation of the transition function δ: Q × Σ → Q
- **5-Tuple Definition**: The formal specification M = (Q, Σ, δ, q₀, F) where Q is states, Σ is alphabet, δ is transition function, q₀ is initial state, and F is accepting states

## Important Formulas

- **Transition Function**: δ(q, a) = next state when in state q reading input symbol a
- **Acceptance Condition**: A string w is accepted if δ(q₀, w) ∈ F, where w is the concatenation of input symbols
- **Language of Automaton**: L(M) = {w ∈ Σ* : δ(q₀, w) ∈ F}

## Key Points

1. Finite automata have three equivalent structural representations: diagrams, tables, and formal definitions
2. State diagrams use circles for states, double circles for accepting states, and labeled directed edges for transitions
3. Transition tables are n × m matrices where n = |Q| and m = |Σ|, facilitating algorithmic processing
4. The formal 5-tuple (Q, Σ, δ, q₀, F) provides mathematical precision for proofs and rigorous reasoning
5. In deterministic finite automata, each state must have exactly one transition for every input symbol
6. The initial state q₀ must be specified exactly once in any representation
7. The set of accepting states F determines which final states cause string acceptance

## Common Mistakes

1. Forgetting to mark the initial state in diagrams or failing to specify it in formal definitions
2. Not including all required transitions, especially from accepting states back to non-accepting states
3. Confusing accepting states (in F) with the initial state—they are different concepts
4. In transition tables, incorrectly placing the transition target or using wrong state names