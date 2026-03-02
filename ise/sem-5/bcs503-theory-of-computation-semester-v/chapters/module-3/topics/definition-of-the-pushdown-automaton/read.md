# Introduction to Pushdown Automaton

The Pushdown Automaton (PDA) is a type of automaton that uses a stack to store and retrieve symbols. It is a fundamental concept in the theory of computation, particularly in the context of context-free grammars and languages.

## Definition of Pushdown Automaton

A Pushdown Automaton is a 7-tuple (Q, Σ, Γ, δ, q0, Z0, F), where:

- Q is a finite set of states
- Σ is a finite set of input symbols
- Γ is a finite set of stack symbols
- δ is a transition function that maps a state, an input symbol, and a stack symbol to a new state and a new stack symbol
- q0 is the initial state
- Z0 is the initial stack symbol
- F is a set of final states

### Key Components of a PDA

The key components of a PDA are:

- **States (Q)**: A finite set of states that the PDA can be in.
- **Input Symbols (Σ)**: A finite set of input symbols that the PDA can read.
- **Stack Symbols (Γ)**: A finite set of stack symbols that the PDA can push and pop from the stack.
- **Transition Function (δ)**: A function that maps a state, an input symbol, and a stack symbol to a new state and a new stack symbol.
- **Initial State (q0)**: The initial state of the PDA.
- **Initial Stack Symbol (Z0)**: The initial symbol on the stack.
- **Final States (F)**: A set of final states that the PDA can be in to accept an input string.

## How a PDA Works

A PDA works by reading an input string one symbol at a time, and using the transition function to determine the next state and stack symbol. The PDA can push and pop symbols from the stack as needed.

### Example of a PDA

Consider a PDA that recognizes the language of all strings of the form {0^n 1^n | n ≥ 0}. The PDA can be defined as follows:

- Q = {q0, q1, q2}
- Σ = {0, 1}
- Γ = {Z0, 0}
- δ(q0, 0, Z0) = (q1, 0Z0)
- δ(q1, 0, 0) = (q1, 00)
- δ(q1, 1, 0) = (q2, ε)
- δ(q2, 1, 0) = (q2, ε)
- q0 = q0
- Z0 = Z0
- F = {q2}

### ASCII Diagram of the PDA

```
          +---------------+
          |               |
          |  q0           |
          |               |
          +---------------+
                  |
                  | 0
                  v
          +---------------+
          |               |
          |  q1           |
          |               |
          +---------------+
                  |
                  | 0
                  v
          +---------------+
          |               |
          |  q1           |
          |               |
          +---------------+
                  |
                  | 1
                  v
          +---------------+
          |               |
          |  q2           |
          |               |
          +---------------+
```

## Comparison of PDA and Other Automata

The following table compares the PDA with other types of automata:
| Automaton | Description | Example |
| --- | --- | --- |
| DFA | Deterministic Finite Automaton | Recognizes regular languages |
| NFA | Nondeterministic Finite Automaton | Recognizes regular languages |
| PDA | Pushdown Automaton | Recognizes context-free languages |
| TM | Turing Machine | Recognizes recursively enumerable languages |

## Exam Tips

- Make sure to understand the definition of a PDA and its key components.
- Practice drawing ASCII diagrams of PDAs to visualize how they work.
- Be able to explain how a PDA recognizes a given language.
- Be able to compare and contrast PDAs with other types of automata.
