# Deterministic Pushdown Automata - Summary

## Key Definitions and Concepts

- **DPDA**: A 7-tuple M = (Q, Σ, Γ, δ, q₀, Z₀, F) where δ: Q × (Σ ∪ {ε}) × Γ → Q × Γ\* is the transition function
- **Configuration**: A triple (q, w, γ) representing current state, remaining input, and stack content
- **Deterministic Context-Free Language (DCFL)**: Languages accepted by DPDAs

## Important Formulas and Theorems

- Transition notation: (q, aw, Xγ) ⊢ (p, w, αγ) means moving from state q to p, consuming 'a', replacing X with α
- For determinism: |δ(q, a, X)| ≤ 1 for all q ∈ Q, a ∈ Σ ∪ {ε}, X ∈ Γ
- If ε-transition exists: δ(q, ε, X) defined implies δ(q, a, X) undefined for all a ∈ Σ

## Key Points

- DPDAs recognize deterministic context-free languages, a proper subset of context-free languages
- At most one transition for any (state, input, stack-top) combination
- Acceptance by final state ≠ Acceptance by empty stack for DPDAs
- DCFLs are closed under complementation but not under union
- Used in LL(k) and LR(k) parsing in compilers
- Stack enables "counting" and "matching" capabilities beyond finite automata
- ε-transitions allow moves without consuming input symbols

## Common Mistakes to Avoid

1. Confusing PDA with DPDA - not all PDAs are deterministic
2. Assuming ε-transitions can coexist with input transitions from same state-stack combination
3. Treating acceptance by empty stack and final state as equivalent (they're not for DPDAs)
4. Forgetting the initial stack symbol Z₀ is always present at the start

## Revision Tips

1. Practice writing formal DPDA definitions with all 7 components
2. Trace several examples step-by-step to understand computation
3. Remember the determinism constraints before designing DPDAs
4. Focus on the closure properties - DCFLs are closed under complement but not union
5. Relate DPDAs to compiler parsing (LL/LR parsers) for practical understanding
