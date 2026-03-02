# Recursive and Recursively Enumerable Languages - Summary

## Key Definitions and Concepts

- **Recursively Enumerable (RE) Language:** A language L is RE if there exists a Turing machine that accepts every string in L and may either reject or loop forever on strings not in L
- **Recursive (Decidable) Language:** A language L is recursive if there exists a Turing machine that always halts—accepting strings in L and rejecting strings not in L
- **Turing-Recognizable:** Another term for RE languages
- **Semi-Decidable:** Another term for RE languages
- **Mapping Reducibility:** A ≤ₘ B means a computable function f reduces problem A to problem B

## Important Formulas and Theorems

- **Relationship:** Recursive ⊂ Recursively Enumerable
- **Complement Closure:** If L is recursive, then L̅ is recursive; If L is RE, L̅ may not be RE
- **Characterization:** L is recursive if and only if both L and L̅ are RE
- **Rice's Theorem:** Any non-trivial property of the language recognized by a TM is undecidable

## Key Points

- Every regular language is recursive; every recursive language is RE
- The Halting Problem is the canonical undecidable problem
- RE languages are closed under union, intersection, concatenation, and Kleene star
- Recursive languages are closed under union, intersection, complementation, concatenation, and Kleene star
- The emptiness problem for TMs is undecidable, but decidable for DFAs and CFGs
- A language is RE if and only if some Turing machine can enumerate its strings
- Undecidability is proven by reducing a known undecidable problem to the target problem

## Common Mistakes to Avoid

- Confusing RE with recursive—remember that RE may not halt on rejected inputs
- Forgetting that RE languages are not closed under complementation
- Assuming all problems have decision procedures—many fundamental problems are undecidable
- Incorrectly applying Rice's Theorem to trivial properties (always true or always false)

## Revision Tips

1. Practice constructing TMs that recognize RE languages and decide recursive languages
2. Memorize the closure properties table for both classes
3. Review proofs of undecidability for standard problems (Halting Problem, Empty, EQ)
4. Understand the diagonalization argument for proving existence of undecidable problems
5. Solve previous year DU exam questions on this topic to understand the exam pattern