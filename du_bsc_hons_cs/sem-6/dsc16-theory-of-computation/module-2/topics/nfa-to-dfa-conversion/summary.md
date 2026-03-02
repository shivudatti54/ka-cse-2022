# NFA to DFA Conversion - Summary

## Key Definitions and Concepts

- **Power Set Construction**: The fundamental algorithm that converts an NFA to a DFA by treating each subset of NFA states as a single DFA state.
- **ε-closure**: The set of all states reachable from a given state by following zero or more ε-transitions.
- **Subset Construction**: Another name for the power set construction method.
- **Dead State**: A non-accepting DFA state that transitions to itself on all inputs (represents ∅ in the power set).

## Important Formulas and Theorems

- **Maximum DFA States**: If an NFA has n states, the equivalent DFA can have up to 2^n states
- **Start State of DFA**: ε-closure(start state of NFA)
- **Accept State of DFA**: Any DFA state that contains at least one NFA accept state
- **Transition Function**: δ_D({q₁,q₂,...}, a) = ε-closure(δ_N(q₁,a) ∪ δ_N(q₂,a) ∪ ...)

## Key Points

- NFAs and DFAs are equivalent in computational power—both recognize the same class of languages (regular languages)
- The subset construction provides a constructive proof of NFA-DFA equivalence
- Each DFA state represents a set of possible NFA states
- ε-transitions require computing ε-closure before processing other inputs
- The converted DFA may have fewer states than the theoretical maximum (2^n)
- DFAs are easier to implement but harder to design; NFAs are easier to design but harder to implement
- The conversion algorithm runs in O(n² × |Σ|) time

## Common Mistakes to Avoid

1. **Forgetting ε-closures**: Always compute ε-closure of the result set, not just the union of transitions
2. **Missing the dead state**: Include ∅ as a valid DFA state when it appears during construction
3. **Incorrect accept state identification**: A DFA state is accepting if it contains ANY NFA accept state (not ALL)
4. **Not including start state properly**: The DFA start state must be the ε-closure of the NFA start state

## Revision Tips

1. Practice at least 3 conversion problems of varying difficulty before the exam
2. Always draw the transition table step-by-step—it shows your work and earns partial credit
3. Remember: ε-closure({q₀}) includes q₀ itself plus all states reachable via ε-transitions
4. The dead state trap is important: if all transitions go to ∅, include ∅ in your diagram
5. Understand that while the conversion can theoretically produce 2^n states, most practical conversions yield much smaller DFAs