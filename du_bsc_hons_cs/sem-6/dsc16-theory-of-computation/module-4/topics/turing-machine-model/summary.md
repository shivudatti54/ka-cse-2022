# Turing Machine Model - Summary

## Key Definitions and Concepts

- **Turing Machine (TM)**: An abstract computational model consisting of an infinite tape, a read-write head, and a finite state control. Formalized as 7-tuple M = (Q, Σ, Γ, δ, q₀, q_accept, q_reject).

- **Transition Function**: δ: Q × Γ → Q × Γ × {L, R} defines the machine's behavior: (new state, symbol to write, direction to move).

- **Configuration**: An instantaneous description showing the current state, tape contents, and head position (e.g., XqY means state q with X to left of head and Y to right).

- **Turing-Recognizable Language**: A language L is recursively enumerable if some TM accepts every string in L (may loop on strings not in L).

- **Decidable Language**: A language L is recursive if some TM decides it—accepts all strings in L and rejects all strings not in L (halts on every input).

- **Church-Turing Thesis**: Every intuitively computable function can be computed by a Turing Machine.

## Important Formulas and Theorems

- **Undecidability of Halting Problem**: No algorithm exists that can determine, for arbitrary program P and input I, whether P(I) halts.

- **Rice's Theorem**: Any non-trivial property of the language recognized by a TM is undecidable.

- **TM Equivalence**: Multi-tape TMs, multi-head TMs, and other variants are computationally equivalent to standard TMs.

## Key Points

- The tape is infinite in both directions and can store any symbol from the tape alphabet Γ.

- Unlike finite automata, TMs can both read and write, and can move in both directions.

- A language is decidable if and only if it and its complement are both recursively enumerable.

- The universal Turing Machine can simulate any other Turing Machine given its description.

- Non-deterministic TMs (NTMs) and deterministic TMs (DTMs) accept the same class of languages (recursively enumerable).

- If a language is decidable, its complement is also decidable; if either is undecidable, both are undecidable.

## Common Mistakes to Avoid

1. Confusing "accept" with "decide" — a TM that accepts may loop forever on non-members.

2. Thinking Church-Turing Thesis is provable — it's a thesis/assertion supported by evidence.

3. Forgetting that the blank symbol ␣ is part of the tape alphabet but not the input alphabet.

4. Assuming the tape is finite — Turing Machines have unbounded tape capacity.

5. Believing all problems can be solved by algorithms — undecidable problems like Halting Problem prove otherwise.

## Revision Tips

1. Practice writing transition functions for simple language recognition problems.

2. Draw configuration diagrams to trace TM execution on sample inputs.

3. Memorize the formal 7-tuple definition and be able to write it from memory.

4. Understand why the halting problem is undecidable—focus on the diagonalization argument.

5. Review the equivalence proofs between TM variants to understand computational universality.