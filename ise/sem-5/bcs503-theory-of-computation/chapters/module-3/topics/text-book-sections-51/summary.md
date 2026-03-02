# **Theory of Computation Revision Notes**

**Section 5.1: Introduction to Automata Theory**

### Key Concepts

- **Automata**: A mathematical model used to describe the behavior of a system that can perform a set of operations.
- **Deterministic Finite Automaton (DFA)**: A type of automaton that can only be in one of a finite number of states at any given time.
- **Non-Deterministic Finite Automaton (NFA)**: A type of automaton that can be in one of multiple states at any given time.
- **Pushdown Automaton (PDA)**: A type of automaton that can remember information on a stack.

### Important Formulas and Definitions

- **Regular Expression**: A string of characters that can be used to describe a set of strings.
  - Definition: A set of strings that can be formed using a finite number of operations, including union, concatenation, and Kleene star.
- **Thompson's Construction**: A method for converting a regular expression into a DFA.
- **Myhill-Nerode Theorem**: A theorem that states that two NFAs are equivalent if and only if they have the same set of accepting states.

### Important Theorems

- ** pumping lemma for regular languages**: A theorem that states that for any regular language, there exists a string that can be pumped to prove that the language is context-free.
- **Chomsky hierarchy**: A hierarchy that categorizes context-free languages based on their regularity.

### Important Concepts for Quick Revision

- **States**: The set of possible positions in an automaton.
- **Transitions**: The set of rules that determine how an automaton moves from one state to another.
- **Accepting states**: The set of states that an automaton is in when it accepts a string.
- **Language**: The set of strings that an automaton accepts.
