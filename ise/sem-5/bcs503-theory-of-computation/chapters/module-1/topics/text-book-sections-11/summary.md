# **Theory of Computation Revision Notes: Section 1.1**

### Definitions

- **Computer Model**: A mathematical representation of a computer's behavior.
- **Turing Machine**: A theoretical model for a computer that can perform computations.
- **State**: A set of symbols that define the machine's current status.
- **Transition Function**: A function that determines the next state and output symbol based on the current state and input symbol.

### Notations

- **Q**: The set of states.
- **Σ**: The input alphabet.
- **Γ**: The tape alphabet (including the blank symbol).
- **q0**: The initial state.
- **q**: The current state.
- **q'**: The next state.
- **a**: The input symbol.
- **b**: The output symbol.

### Turing Machine Formalism

- **Turing Machine Definition**: M = (Q, Σ, Γ, q0, δ, F) where:
  - Q is the set of states.
  - Σ is the input alphabet.
  - Γ is the tape alphabet.
  - q0 is the initial state.
  - δ is the transition function.
  - F is the set of final states.

### Key Theorems

- **Turing Machine Halting Problem**: A Turing machine will halt on all inputs if and only if it halts on a certain input.
- **Turing Machine Decidability**: A language is decidable if there exists a Turing machine that can determine whether a given string belongs to the language.

### Important Formulas

- **Turing Machine Transition Function**: δ(q, a) = (q', b) where q is the current state, a is the input symbol, q' is the next state, and b is the output symbol.

### Quick Revision Tips

- Understand the definitions of Turing machine states, transition function, and notations.
- Familiarize yourself with the formalism of a Turing machine.
- Review the key theorems and important formulas.
