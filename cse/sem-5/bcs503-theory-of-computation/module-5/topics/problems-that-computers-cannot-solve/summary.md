# Problems That Computers Cannot Solve - Summary

## Key Definitions and Concepts

- **Decision Problem:** A problem requiring a yes/no answer depending on input
- **Decidable Problem:** A problem for which an algorithm exists that always halts with correct answer
- **Undecidable Problem:** A problem for which no such algorithm exists
- **Halting Problem:** Determines if a program halts on given input - proven undecidable by Turing
- **Reduction:** Technique to prove undecidability by transforming known undecidable problems
- **Rice's Theorem:** Every non-trivial property of languages recognized by TMs is undecidable
- **Post Correspondence Problem (PCP):** Classic undecidable problem used for reductions
- **Church-Turing Thesis:** All reasonable computation models are equivalent to Turing machines

## Important Formulas and Theorems

- **Turing's Halting Problem Proof:** Assumes H(P,I) exists → constructs contradictory program → H cannot exist
- **Rice's Theorem:** For property P of L(M), if P is non-trivial (not always true, not always false), then P is undecidable
- **Reduction Principle:** If A ≤ₘ B (A reduces to B) and B is undecidable, then A is undecidable

## Key Points

1. The Halting Problem is the fundamental undecidable problem - no algorithm can determine if any arbitrary program halts
2. Undecidability is proven via reduction from known undecidable problems (typically Halting Problem)
3. Rice's Theorem provides quick determination that language properties are undecidable
4. The Emptiness Problem (L(M) = ∅?) and Membership Problem (w ∈ L(M)?) are both undecidable
5. The Equivalence Problem (L(M₁) = L(M₂)?) for TMs is undecidable
6. PCP is undecidable and serves as a "master problem" for proving other problems undecidable
7. Undecidability means no algorithm exists for ALL inputs, not that individual instances are unsolvable

## Common Mistakes to Avoid

1. Confusing "undecidable" with "difficult" - undecidable means impossible for any algorithm
2. Applying Rice's Theorem to trivial properties (which are decidable) - always check if property is non-trivial
3. Attempting to prove undecidability by constructing an algorithm that sometimes fails - must prove NO algorithm exists
4. Confusing the general problem with specific instances - Halting Problem is undecidable but specific cases can be solved

## Revision Tips

1. Memorize the statement of Rice's Theorem and practice applying it to identify undecidable properties
2. Practice reduction proofs: start with Halting Problem instance, construct transformation, show contradiction
3. Understand that undecidability has practical implications - recognize when problems are theoretically unsolvable
4. Review the connection between decidability, semi-decidability, and co-semi-decidability
5. Remember: Turing machines define the limits - if TM cannot decide, no computer can
