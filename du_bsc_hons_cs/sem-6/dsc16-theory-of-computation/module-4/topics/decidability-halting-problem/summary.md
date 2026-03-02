# Decidability and the Halting Problem - Summary

## Key Definitions and Concepts

- **Decision Problem**: A problem requiring a yes/no answer
- **Decidable Problem**: A problem for which an algorithm exists that always halts with the correct answer
- **Recognizable (r.e.) Language**: A language for which a TM exists that accepts all strings in the language and rejects or loops on strings not in the language
- **Halting Problem**: Given M and w, determine if M halts on w
- **Reducibility**: Problem A reduces to problem B if we can transform A-instances to B-instances while preserving answers
- **Non-trivial Property**: A property that holds for some TMs but not for others

## Important Formulas and Theorems

- **Church-Turing Thesis**: Turing machines capture the notion of algorithm
- **Undecidability of Halting Problem**: No algorithm can decide if an arbitrary TM halts on arbitrary input
- **Rice's Theorem**: Any non-trivial property of a TM's language is undecidable
- **Decidability Relationships**: Decidable ⇒ Recognizable; Decidable = Recognizable ∩ Co-recognizable

## Key Points

- The Halting Problem is the canonical example of an undecidable problem
- Diagonalization proof shows the contradiction when assuming a Halting decider exists
- Rice's Theorem provides a quick way to prove many problems undecidable
- If A reduces to B and A is undecidable, then B must be undecidable
- Emptiness, finiteness, equivalence, and universality are all undecidable for TMs
- Practical consequences include limitations on program analysis, verification, and optimization
- Decidable problems exist for restricted models (DFAs, PDAs) but fail for TMs

## Common Mistakes to Avoid

- Confusing "recognizable" with "decidable"—a recognizer may loop forever on rejected inputs
- Incorrectly applying Rice's Theorem to trivial properties (which ARE decidable)
- Forgetting that the reduction direction matters: A ≤ B means solving B can solve A
- Assuming undecidability means "cannot be solved by any computer"—it means no algorithm exists

## Revision Tips

1. Practice writing out the Halting Problem proof step-by-step until you can reproduce it from memory
2. Create a table of common problems and their decidability status (DFA, PDA, TM cases)
3. For Rice's Theorem questions, identify whether the property is trivial—if trivial, it's decidable; otherwise, undecidable
4. Solve at least 3-4 reduction problems to master the technique
5. Remember: undecidable problems are not "hard to solve"—they are provably impossible to solve algorithmically