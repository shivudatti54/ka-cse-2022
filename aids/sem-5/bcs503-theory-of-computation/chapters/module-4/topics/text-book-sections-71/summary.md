# **Theory of Computation: Revision Notes - Section 7.1**

## **Definition of a Turing Machine**

- A Turing machine is a mathematical model for computation.
- It consists of:
  - A read/write head that can move left or right on an infinite tape.
  - An alphabet (σ) of input symbols.
  - An initial state (q0) and a set of final states (Qf).
  - A transition function δ(q, a) that specifies the next state and symbol on the tape.

## **Notations**

- q: state
- a: input symbol
- Σ: alphabet
- δ(q, a): transition function
- q0: initial state
- Qf: final states
- qt: current state
- α, β: input strings
- M: Turing machine

## **Types of Turing Machines**

- **Deterministic Turing Machine (DTM)**: every possible computation is uniquely determined by the initial state, input, and tape content.
- **Nondeterministic Turing Machine (NTM)**: may have multiple possible computations for the same initial state, input, and tape content.

## **Halting Problem**

- **Decision Problem**: given a Turing machine M and an input string α, determine whether M accepts α.
- **Halting Problem**: given a Turing machine M and an input string α, determine whether M will run forever or eventually halt.
- **Undecidability**: the halting problem is undecidable, meaning there is no algorithm that can solve it for all possible Turing machines and input strings.

## **Key Theorems**

- **Church-Turing Thesis**: every effectively calculable function can be computed by a Turing machine.
- **Turing's Incompleteness Theorem**: there cannot exist an algorithm that can solve the halting problem for all Turing machines.

## **Important Formulas**

- Turing's Halting Problem Formula: no algorithm can solve the halting problem for all Turing machines.
- Church's Thesis Formula: every effectively calculable function can be computed by a Turing machine.
