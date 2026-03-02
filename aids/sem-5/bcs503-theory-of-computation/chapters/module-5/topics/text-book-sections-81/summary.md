# **Theory of Computation Revision Notes**

**Topic: Sections 8.1**

- **Definition of a Turing Machine:**
  - A 6-tuple (Q, Σ, Γ, δ, q0, F) where:
    - Q: set of states
    - Σ: input alphabet
    - Γ: tape alphabet
    - δ: transition function
    - q0: initial state
    - F: set of final states

- **States and Transitions:**
  - States: q, q', ..., qn
  - Transitions: δ(q, a) = (q', b, L/R)
    - q' is the next state
    - b is the symbol to write on the tape
    - L/R indicates direction of movement (left/right)

- **Formal Definition:**
  - A Turing Machine M = (Q, Σ, Γ, δ, q0, F) is a computation if:
    - Initially, the tape is in state q0 and contains a string w
    - After each transition, the machine is in a valid state and the tape contains a string
    - The machine halts in a final state

- **Key Theorems:**
  - **Church-Turing Thesis:** Any effectively calculable function can be computed by a Turing Machine
  - **Halting Problem:** There is no general algorithm to determine whether a given Turing Machine will halt on a given input

- **Important Formulas:**
  - Turing Machine acceptance condition: M accepts w if w is in F
  - Turing Machine computation: M(w) = (q, w', s) where q is the final state and w' is the final string

- **Concepts:**
  - **Tape:** infinite sequence of cells, each containing a symbol from Σ or ∅
  - **Read/Write Head:** moves along the tape, reads/supplies symbols
