# Extensions to the Basic Turing Machine - Summary

## Key Definitions and Concepts

- **Multi-tape Turing Machine:** Extended TM with k tapes, each having independent read-write heads. Transition function: δ: Q × Γ^k → Q × Γ^k × {L,R}^k
- **Non-deterministic Turing Machine:** TM where transition function returns a set of possible actions. δ: Q × Γ → P(Q × Γ × {L,R})
- **Universal Turing Machine:** A TM that can simulate any other TM given its description and input
- **Linear Bounded Automaton:** Restricted TM using only O(n) space where n is input length; corresponds to context-sensitive languages

## Important Formulas and Theorems

- **Equivalence Theorem:** Multi-tape TM ≡ Single-tape TM (computational power)
- **NDTM ≡ DTM:** Every NDTM can be simulated by DTM using breadth-first search
- **Church-Turing Thesis:** Turing-computable functions = λ-definable functions = Intuitive notion of computability
- **Single-tape simulation of k-tape TM:** O(n²) time complexity

## Key Points

- Extensions don't increase computational power but provide convenience and potentially better time complexity
- Multi-tape TMs can simulate single-tape TMs trivially; reverse simulation uses encoding with O(n²) overhead
- NDTMs explore all computation branches; DTM simulation uses BFS, potentially exponential time
- Universal Turing Machine forms theoretical basis for modern stored-program computers
- LBAs are restricted TMs that cannot move beyond input boundaries; recognize CSL
- Church-Turing Thesis establishes Turing Machine as the standard model of computation

## Common Mistakes to Avoid

- Confusing "equivalence in power" with "equal efficiency"—simulation often has overhead
- Thinking NDTM is more powerful than DTM—they accept the same languages, just potentially faster
- Forgetting that LBA space is bounded by input length plus end markers
- Assuming Church-Turing Thesis is proven—it remains a thesis accepted by consensus

## Revision Tips

- Focus on understanding formal definitions and transition functions for each extension
- Memorize the key equivalence theorems—they frequently appear in exams
- Practice tracing through simple examples of each machine type
- Review undecidability proofs and the Halting Problem—classic exam questions
- Know the relationship between machine types and language classes (Regular → CFL → CSL → Recursive)
