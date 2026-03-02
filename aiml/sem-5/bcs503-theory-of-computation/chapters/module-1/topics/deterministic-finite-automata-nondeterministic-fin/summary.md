# **Deterministic Finite Automata (DFA), Nondeterministic Finite Automata (NFA), Text Search, and Finite Automata with Epsilon-Transitions**

## **I. Deterministic Finite Automata (DFA)**

- **Definition:** A DFA is a 5-tuple (Q, Σ, δ, q0, F) where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps each state and symbol to a next state
  - q0 is the initial state
  - F is the set of final states
- **Key Properties:**
  - Deterministic: For each state and symbol, there is exactly one next state
  - Finite: The automaton has a finite number of states
- **Important Formulas:**
  - ε-automaton: A DFA with an empty ε-transition set
  - ε-loop: A state that has an ε-transition to itself

## **II. Nondeterministic Finite Automata (NFA)**

- **Definition:** An NFA is a 4-tuple (Q, Σ, δ, q0) where:
  - Q is a finite set of states
  - Σ is a finite set of input symbols
  - δ is a transition function that maps each state and symbol to a set of next states
  - q0 is the initial state
- **Key Properties:**
  - Nondeterministic: For each state and symbol, there may be multiple next states
  - Finite: The automaton has a finite number of states
- **Important Formulas:**
  - ε-transition: A transition from a state to itself with an empty input

## **III. Text Search Application**

- **Problem:** Given a text and a pattern, determine if the pattern exists in the text
- **Approach:**
  - Convert the text to a DFA (or NFA)
  - Use the DFA (or NFA) to search for the pattern in the text
- **Key Concepts:**
  - Regular expressions: A way to describe patterns using automata
  - Word boundaries: A way to handle cases where the pattern is not a contiguous sequence of characters

## **IV. Finite Automata with Epsilon-Transitions**

- **Definition:** A finite automaton with ε-transitions is an automaton that can move from a state to itself with an empty input
- **Key Properties:**
  - ε-transitions: Allow the automaton to move from a state to itself without consuming an input symbol
  - May have multiple final states
- **Important Formulas:**
  - ε-loop: A state that has an ε-transition to itself

**Theorems:**

- **Myhill-Nerode Theorem:** States in a DFA are equivalent if and only if they have the same language
- **Kleene's Theorem:** A language is regular if and only if it can be accepted by a finite automaton with ε-transitions
