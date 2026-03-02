# **Theory of Computation Revision Notes: Section 5.1**

### Overview

This section covers the basics of Computability Theory, including the definition of a Turing Machine and the halting problem.

### Important Concepts

- **Turing Machine**:
  - A theoretical model for a computer
  - Consists of a tape, a read/write head, and an infinite number of symbols (0 and 1)
  - Can be in one of four states (q0, q1, q2, q3)
  - Can move the read/write head left or right, and change its state
- **Computational Complexity**:
  - Measures the amount of time or space required to solve a problem
  - Examples: Time complexity, Space complexity
- **Halting Problem**:
  - Decidability problem: Given a program and input, determine whether the program will halt or run forever
  - Undecidable problem: There is no general algorithm to solve the halting problem

### Important Formulas and Definitions

- **Turing Machine's Transition Function**:
  - Δ: Σ × {L, R} × Q → Σ × Q (delta function)
  - δ(q, a, b) = (q', L/R, σ)
- **Turing Machine's State**:
  - q: a set of states (q0, q1, q2, q3)
- **Turing Machine's Tape**:
  - Σ: set of input symbols (0, 1)
  - a: input symbol on the tape

### Important Theorems

- **Turing Machine's Halting Theorem**:
  - If a Turing machine halts on a given input, then it will halt on all inputs that can be reduced to that input.
- **Halting Problem's Undecidability**:
  - There is no general algorithm to determine whether a Turing machine will halt on a given input.

### Key Points for Revision

- Turing Machine basics
- Computational complexity and decidability
- Halting problem and its undecidability
- Turing Machine's transition function and state
- Turing Machine's tape and input symbols
