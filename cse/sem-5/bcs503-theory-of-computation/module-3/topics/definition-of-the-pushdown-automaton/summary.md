# Definition of the Pushdown Automaton - Summary

## Key Definitions and Concepts

- **Pushdown Automaton (PDA)**: A finite automaton augmented with an unbounded stack memory that enables recognition of context-free languages.

- **Formal Definition**: PDA is a 7-tuple M = (Q, Σ, Γ, δ, q₀, Z₀, F) where:
  - Q = finite set of states
  - Σ = input alphabet
  - Γ = stack alphabet
  - δ = transition function
  - q₀ = start state
  - Z₀ = initial stack symbol
  - F = set of accepting states

- **Configuration**: Represented as (q, w, α) where q is current state, w is remaining input, and α is stack contents.

## Important Formulas

- **Transition Function (NPDA)**: δ: Q × (Σ ∪ {ε}) × Γ → P(Q × Γ\*)
- **Transition Function (DPDA)**: δ: Q × (Σ ∪ {ε}) × Γ → (Q × Γ\*) or empty

## Key Points

- A PDA extends a finite automaton by adding a LIFO stack memory
- The stack allows matching of nested structures (e.g., balanced parentheses)
- Every context-free language is recognized by some PDA
- ε-transitions allow state changes without consuming input
- Push operation adds to stack top; pop removes from stack top
- PDA can accept by final state or by empty stack (both equivalent)

## Common Mistakes to Avoid

1. Confusing stack alphabet (Γ) with input alphabet (Σ) – they serve different purposes
2. Forgetting that stack top is always the leftmost symbol in configuration notation
3. Not distinguishing between deterministic and non-deterministic PDAs
4. Incorrectly specifying whether acceptance is by final state or empty stack

## Revision Tips

1. Memorize the 7-tuple definition and what each component represents
2. Practice tracing PDA executions on simple inputs like 0011 or ()
3. Remember: NPDA can recognize all CFLs; DPDA only recognizes DCFLs
4. Review the equivalence between acceptance by final state and empty stack
5. Understand that ε-moves don't consume input but can modify state and stack
