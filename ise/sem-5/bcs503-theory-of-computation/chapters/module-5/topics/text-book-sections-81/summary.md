# **Theory of Computation: Revision Notes**

### Section 8.1: Introduction to Automata Theory

- **Definition:** Automata Theory is a branch of theoretical computer science that deals with the study of abstract machines.
- **Types of Automata:**
  - Deterministic Finite Automaton (DFA)
  - Nondeterministic Finite Automaton (NFA)
  - Pushdown Automaton (PDA)
  - Turing Machine (TM)
- **Key Concepts:**
  - States, Alphabet, Transition Function, Accepting States
  - Language accepted by an automaton
- **Important Formulas and Theorems:**
  - Turing Machine:
    - M(A) = {w ∈ Σ\* | M(A) w ∈ L(M)}
  - Chomsky-Stockmeyer Theorem:
    - A language L is regular if and only if it is accepted by an NFA with a finite number of states

### Important Definitions:

- **State:** A pair (q, x) where q is a state and x is a symbol from the alphabet
- **Transition:** A pair (q, a, q') where q is the current state, a is the input symbol, and q' is the next state
- **Accepting State:** A state that marks the end of a path in a DFA or NFA

### Quick Revision Tips:

- Understand the difference between DFA, NFA, PDA, and TM
- Learn the key concepts of states, alphabet, transition function, and accepting states
- Practice solving problems using the provided formulas and theorems
