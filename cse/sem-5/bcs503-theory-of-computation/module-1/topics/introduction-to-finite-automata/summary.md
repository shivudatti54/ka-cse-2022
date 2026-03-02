# Introduction to Finite Automata - Summary

## Key Definitions and Concepts

- **Finite Automaton (FA):** A 5-tuple M = (Q, Σ, δ, q₀, F) where Q is the finite set of states, Σ is the input alphabet, δ is the transition function, q₀ is the start state, and F is the set of final states.

- **Deterministic FA (DFA):** For each state and input symbol, there is exactly one next state. The transition function δ: Q × Σ → Q is a total function.

- **Non-Deterministic FA (NFA):** For each state and input symbol, there can be zero, one, or multiple next states. The transition function δ: Q × Σ → P(Q), where P(Q) is the power set of Q.

- **Extended Transition Function (δ\*):** Defines transitions for entire strings, defined recursively as δ*(q, ε) = q and δ*(q, wa) = δ(δ\*(q, w), a).

- **Language of FA:** L(M) = {w ∈ Σ* | δ*(q₀, w) ∈ F}

## Important Formulas and Theorems

- **DFA Transition:** δ: Q × Σ → Q
- **NFA Transition:** δ: Q × Σ → P(Q) (power set)
- **Equivalence Theorem:** For every NFA, there exists an equivalent DFA recognizing the same language.

## Key Points

1. Finite automata have finite memory (states) and can recognize regular languages only.

2. In a DFA, the transition function must be defined for all state-symbol combinations (totality).

3. The start state is marked with an incoming arrow, and final states are marked with double circles in transition graphs.

4. A string is accepted if the automaton reaches a final state after processing the entire input.

5. NFA provides more flexibility in design but has the same computational power as DFA.

6. The empty string ε is handled by the extended transition function δ\*.

7. Dead or trap states are useful when rejecting certain patterns in DFA design.

8. The subset construction algorithm converts NFA to equivalent DFA.

## Common Mistakes to Avoid

1. **Forgetting to make δ total in DFA:** Every state-symbol pair must have a defined transition; use a dead/trap state if needed.

2. **Confusing NFA with DFA:** Remember NFA can have multiple transitions for the same input from a state.

3. **Not checking the entire input:** A string is accepted only if processing the complete string ends in a final state.

4. **Incorrect state identification:** Carefully identify what information each state must remember about the input processed so far.

## Revision Tips

1. Practice drawing both transition tables and transition graphs for various language recognition problems.

2. Memorize the formal definition of DFA and NFA as 5-tuples - this is frequently asked in exams.

3. Solve at least 5-6 DFA design problems covering different patterns (ending with, containing, divisible by, etc.).

4. Understand the proof of NFA to DFA equivalence conceptually before attempting conversion problems.

5. Use the "trace method" to verify your designed automata with test strings.
