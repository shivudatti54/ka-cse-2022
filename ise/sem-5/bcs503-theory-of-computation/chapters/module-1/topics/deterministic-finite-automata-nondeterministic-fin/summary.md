# Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA)

### Definitions

- **Deterministic Finite Automaton (DFA):**
  - A 5-tuple (Q, Σ, δ, q0, F) where:
    - Q is a finite set of states
    - Σ is a finite alphabet
    - δ is a transition function that maps (q, a) to q'
    - q0 is the initial state
    - F is the set of accepting states
- **Nondeterministic Finite Automaton (NFA):**
  - A 4-tuple (Q, Σ, δ, q0) where:
    - Q is a finite set of states
    - Σ is a finite alphabet
    - δ is a transition function that maps (q, a) to a set of states Q'
    - q0 is the initial state

### Transition Functions

- **DFA:**
  - δ(q, a) ∈ Q (q' is a single state)
- **NFA:**
  - δ(q, a) ⊆ Q (q' is a set of states)

### Epsilon-Transitions

- **Epsilon-Transitions:** δ(q, ε) = {q' | q' ∈ Q}
- **DFA:** No epsilon-transitions (ε ≠ a for all a ∈ Σ)
- **NFA:** Epsilon-transitions allowed

### Theorems

- **Myhill-Nerode Theorem:** Two NFAs are equivalent if and only if they have the same set of accepting states
- **Thompson's Construction:** Given a regular language, a DFA can be constructed in linear time

### An Application: Text Search

- **Text Search:** Given a text and a pattern, find all occurrences of the pattern
- **Using DFA/NFA:** Can be solved using a DFA/NFA with epsilon-transitions
- **Example:** Find all occurrences of "ab" in "ababab"

### Important Formulas

- **Regular Language:** A language recognized by a DFA/NFA
- **Regular Expression:** A way to describe a regular language using operators and symbols

## Revision Notes

- DFA and NFA are used to recognize regular languages
- Transition functions and epsilon-transitions are key concepts in the study of DFAs/NFA
- Thompson's Construction is a powerful tool for constructing DFAs from regular languages
- Text search can be solved using DFAs/NFA with epsilon-transitions
