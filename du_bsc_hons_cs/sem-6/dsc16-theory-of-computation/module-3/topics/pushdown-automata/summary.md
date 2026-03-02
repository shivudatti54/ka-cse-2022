# Pushdown Automata - Summary

## Key Definitions and Concepts

- **Pushdown Automaton (PDA)**: A computational model consisting of a finite control unit and an unbounded stack, formally defined as M = (Q, Σ, Γ, δ, q₀, Z₀, F) where Q is states, Σ is input alphabet, Γ is stack alphabet, δ is transition function, q₀ is initial state, Z₀ is initial stack symbol, and F is set of final states.

- **Configuration/Instantaneous Description**: A triple (q, w, γ) where q is current state, w is unread input, γ is stack contents (top on left).

- **Acceptance by Final State**: String w accepted if (q₀, w, Z₀) ⊢* (q, ε, γ) for some q ∈ F.

- **Acceptance by Empty Stack**: String w accepted if (q₀, w, Z₀) ⊢* (q, ε, ε).

- **Deterministic PDA (DPDA)**: Has at most one transition for each configuration; accepts deterministic CFLs.

- **Non-Deterministic PDA (NPDA)**: Has multiple possible transitions; accepts all context-free languages.

## Important Formulas and Theorems

- **Equivalence Theorem**: Languages accepted by PDAs with empty stack acceptance = Languages accepted by PDAs with final state acceptance.

- **Power Relationship**: Regular Languages ⊂ Deterministic CFL ⊂ CFL ⊂ Recursive Languages

- **Transition Function**: δ: Q × (Σ ∪ {ε}) × Γ → P(Q × Γ*)

## Key Points

- PDA extends finite automaton with unbounded stack memory
- Stack operations: push (X → aX), pop (X → ε), replace (X → aY)
- Every context-free grammar can be converted to an equivalent PDA
- Every PDA can be converted to an equivalent CFG
- DPDAs are strictly less powerful than NPDAs
- ε-transitions allow state changes without consuming input
- The initial stack symbol Z₀ acts as bottom-of-stack marker and enables acceptance checks
- Non-determinism is crucial for languages requiring "guessing" (like palindromes)

## Common Mistakes to Avoid

1. **Confusing stack representation**: Remember top of stack is on the LEFT in notation (γ = ZAX means Z is bottom, X is top).

2. **Forgetting initial stack symbol**: Every PDA must have Z₀ in the stack initially; acceptance by empty stack requires completely emptying this symbol.

3. **Treating DPDA and NPDA as equivalent**: DPDAs accept only deterministic CFLs, not all CFLs.

4. **Ignoring non-determinism**: Many CFLs (like palindromes) cannot be recognized by any DPDA.

5. **Mixing acceptance criteria**: Ensure you use the correct acceptance method when tracing or designing PDAs.

## Revision Tips

1. Practice writing formal 7-tuple definitions from memory
2. Trace at least 3-4 examples completely, writing each configuration
3. Remember the conversion between empty stack and final state acceptance
4. Focus on why DPDAs are weaker than NPDAs (determinism vs non-determinism)
5. Understand the connection between PDA and CFG — they accept the same class of languages