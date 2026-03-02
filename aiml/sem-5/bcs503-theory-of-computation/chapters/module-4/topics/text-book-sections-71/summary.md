# Revision Notes: Theory of Computation - Section 7.1

==============================

### Definitions

- **Turing Machine**: A mathematical model for computation that consists of a tape divided into cells, each of which can hold a symbol from a finite alphabet.
- **Turing Machine State**: A set of symbols that the machine can read from the current cell.
- **Turing Machine Transition Function**: A function that maps each state and symbol to the next state and symbol.

### Key Concepts

- **Turing Machine Languages**: A set of strings that can be accepted by a Turing machine.
- **Decidable Language**: A language that can be determined to be non-empty or empty by a Turing machine in finite time.
- **Undecidable Language**: A language for which no Turing machine can determine whether a given string is in the language or not.

### Theorem: Turing's Halting Theorem

- **Statement**: There cannot exist an algorithm that can determine, given an arbitrary program and input, whether the program will run forever or eventually halt.
- **Proof**: Assume there is an algorithm that can determine whether a program will halt. Apply the algorithm to the program and input. If the algorithm halts, then the program halts. If the algorithm runs forever, then the program will run forever.

### Important Formulas

- **Church-Turing Thesis**: Any effectively calculable function can be computed by a Turing machine.
- **Turing Machine Acceptance Criterion**: A string is accepted by a Turing machine if it is in the language accepted by the machine.

### Key Formulas

- **Turing Machine State Transition Function**: Δ = (Q, Σ, Γ, δ)
- **Turing Machine Language**: L(M) = {w | M accepts w}

Note: This summary provides a concise overview of the key concepts, definitions, and theorems in Section 7.1 of the theory of computation. It is intended to serve as a quick revision guide before exams.
