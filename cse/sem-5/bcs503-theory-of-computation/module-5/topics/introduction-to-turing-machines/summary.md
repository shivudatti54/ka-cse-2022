# Introduction to Turing Machines - Summary

## Key Definitions and Concepts

- **Turing Machine**: An abstract computational model consisting of an infinite tape, a read-write head, a control unit, and state register, defined as a 7-tuple M = (Q, Σ, Γ, δ, q₀, q_accept, q_reject).

- **Tape**: Infinite sequence of cells that stores both input and working memory; uses a blank symbol (B) to fill unused cells.

- **Transition Function**: δ: Q × Γ → Q × Γ × {L, R} — determines next state, symbol to write, and head direction.

- **Turing-recognizable Language**: A language L is recursively enumerable if some TM accepts all strings in L (may loop on others).

- **Decidable Language**: A language L is recursive if some TM accepts all strings in L and rejects all strings not in L (halts on all inputs).

## Important Formulas and Theorems

- **Church-Turing Thesis**: Any intuitively computable function can be computed by a Turing Machine. This establishes TM as the standard model of computation.

- **Equivalence of Variants**: Multi-tape TMs, Non-deterministic TMs, and other computational models are all computationally equivalent to the basic single-tape deterministic TM.

## Key Points

- Turing Machines are more powerful than Finite Automata and Pushdown Automata—they can recognize recursively enumerable languages (the broadest class in Chomsky hierarchy).

- The TM has infinite tape (unbounded memory) and can move the head in both directions, unlike finite automata with finite memory.

- A TM halts when entering q_accept (accepts) or q_reject (rejects); if it never enters either, it loops forever.

- Every finite automaton is a special case of TM where the head only reads without moving or writing.

- The Entscheidungsproblem (decision problem) was proven unsolvable using Turing Machines by Turing and Church independently.

- Turing Machines provide the theoretical foundation for studying computational complexity (P vs NP) and computability (decidability).

## Common Mistakes to Avoid

- Confusing "reject" with "loop forever"—a TM can reject by halting in q_reject, but looping means it's still running.

- Believing that more tape or faster computation changes what can be computed—only the algorithm (TM description) matters for computability.

- Forgetting that the blank symbol B is part of the tape alphabet Γ but not the input alphabet Σ.

- Assuming non-deterministic TMs can compute more than deterministic TMs—they have the same computing power, though potentially different time complexity.

## Revision Tips

- Practice writing the formal 7-tuple definition from memory—it frequently appears in exams.

- Trace through simple TM examples (like 0ⁿ1ⁿ recognition) multiple times to understand the configuration notation.

- Remember: Church-Turing Thesis is a thesis (accepted without proof), not a theorem—don't try to prove it formally.

- Focus on understanding the conceptual differences between automata models rather than memorizing every transition.
