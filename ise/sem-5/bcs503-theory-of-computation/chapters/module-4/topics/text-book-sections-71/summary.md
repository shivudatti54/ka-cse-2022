# **Theory of Computation: Revision Notes - Section 7.1**

### Definitions

- **Turing Machine**: A mathematical model for computation that can read and write symbols on an infinite tape.
- **State**: A set of symbols that the machine can be in.
- **Transition Function**: A function that specifies the next state and symbol to write, given the current state and input symbol.
- **Accepting State**: A state that indicates the machine has accepted the input.
- **Halting Problem**: The problem of determining, given an arbitrary program and input, whether the program will run forever or eventually halt.

### Notations

- **M = (Q, Σ, Γ, δ, q0, F)**: A 7-tuple defining a Turing Machine, where:
  - Q: Set of states
  - Σ: Set of input symbols
  - Γ: Set of tape symbols
  - δ: Transition function
  - q0: Initial state
  - F: Set of accepting states

### Theorems

- **Turing Machine Theorem**: Any effectively calculable function can be computed by a Turing Machine.
- **Church-Turing Thesis**: Any effectively calculable function can be computed by a Turing Machine, and all Turing Machines are equivalent in computational power.

### Important Formulas

- **Turing Machine Algorithm**:
  1.  Initialize the tape with the input string.
  2.  Read the current symbol and determine the next state.
  3.  Write the new symbol on the tape.
  4.  Repeat steps 2-3 until a halting state is reached.
- **Halting Function**:
  1.  Define a function that takes a program and input as input.
  2.  Run the program on the input until it halts or runs forever.

### Important Concepts

- **Computational Complexity**: The resources required (time and space) to solve a problem.
- **Decidable Language**: A language that can be decided by a Turing Machine, i.e., a language for which there exists an algorithm that can determine whether a given string is in the language or not.
