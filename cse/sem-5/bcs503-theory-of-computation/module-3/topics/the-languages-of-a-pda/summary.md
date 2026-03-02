# The Languages of a Pushdown Automaton - Summary

## Key Definitions and Concepts

- **Pushdown Automaton (PDA):** A 7-tuple M = (Q, Σ, Γ, δ, q₀, Z₀, F) where Q is states, Σ is input alphabet, Γ is stack alphabet, δ is transition function, q₀ is initial state, Z₀ is initial stack symbol, and F is set of final states.

- **Acceptance by Final State:** String w is accepted if (q₀, w, Z₀) ⊢* (p, ε, γ) for some p ∈ F and γ ∈ Γ*.

- **Acceptance by Empty Stack:** String w is accepted if (q₀, w, Z₀) ⊢\* (q, ε, ε) for some q ∈ Q.

- **Deterministic PDA (DPDA):** Has at most one move for each (q, a, X) combination.

- **Non-deterministic PDA (NPDA):** Can have multiple possible moves, enabling recognition of all CFLs.

## Important Formulas and Theorems

- **Equivalence Theorem:** L(F) = L(E), where L(F) is the family of languages accepted by final state and L(E) is the family of languages accepted by empty stack.

- **CFL = PDA:** A language is context-free if and only if some pushdown automaton accepts it.

- **DCFL ⊂ CFL:** Deterministic context-free languages are a proper subset of context-free languages.

## Key Points

- PDAs extend finite automata with stack memory, enabling recognition of non-regular languages like {ⁿⁿ | n ≥ 0}.

- The stack operates in LIFO (Last-In-First-Out) order, crucial for matching nested structures.

- Non-determinism is essential for recognizing certain CFLs; DPDAs cannot recognize all CFLs.

- Transition δ(q, a, X) = (p, γ) means: in state q, reading a, with X on stack, go to p and replace X with γ.

- ε-moves allow state changes without consuming input, useful for phase transitions in PDA design.

- The two acceptance modes (final state and empty stack) generate the same language family.

## Common Mistakes to Avoid

- Confusing the stack alphabet (Γ) with the input alphabet (Σ)—they are different sets.

- Forgetting that the initial stack symbol Z₀ remains in the stack unless explicitly popped.

- Assuming deterministic PDAs can recognize all CFLs—they can only recognize DCFLs.

- Not handling the empty string (ε) properly in PDA constructions where applicable.

## Revision Tips

- Practice tracing PDA computations for various inputs to understand acceptance behavior.

- Memorize the standard PDA constructions for palindromes, balanced parentheses, and wwʀ patterns.

- Remember: when converting acceptance by empty stack to final state, add a bottom marker to prevent premature stack emptying.

- Focus on understanding why non-determinism is needed for certain language recognitions.
