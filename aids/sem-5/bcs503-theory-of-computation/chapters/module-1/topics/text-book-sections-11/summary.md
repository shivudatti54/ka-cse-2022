# **Theory of Computation Revision Notes - Section 1.1**

## **Definitions and Notations**

- **M** (Machine): a theoretical model of a computer
- **M'** (M'-program): a program written in a high-level language
- **Q** (Input): the input of the machine
- **q** (State): a state in the machine
- **T** (Tape): the tape used to store input and output
- **q_0** (Initial State): the initial state of the machine
- **q_f** (Final State): the final state of the machine

## **Theoretical Models of Computation**

- **Turing Machine (TM)**:
  - A simple model of computation
  - Reads and writes symbols on an infinite tape
  - Can move left or right and change symbols
- **Finite State Machine (FSM)**:
  - A simple model of computation
  - Reads and writes symbols on a finite tape
  - Can move left or right and change symbols
- **Pushdown Automaton (PDA)**:
  - A model of computation with a stack
  - Can push and pop symbols from the stack

## **Algorithms and Complexity**

- **Algorithm**:
  - A set of instructions for solving a problem
  - Can be represented by a Turing Machine
- **Time Complexity**:
  - The amount of time an algorithm takes to complete
  - Measured in Big O notation (e.g. O(n), O(n^2))
- **Space Complexity**:
  - The amount of memory an algorithm uses
  - Measured in Big O notation (e.g. O(n), O(n^2))

## **Important Formulas and Theorems**

- **Church-Turing Thesis**: any effectively calculable function can be computed by a Turing Machine
- **Turing Machine Acceptance**: a string is accepted if it is accepted by the Turing Machine
- **Halting Problem**: there is no general algorithm to determine whether a Turing Machine will halt on a given input string

## **Key Points**

- Theoretical models of computation (TM, FSM, PDA)
- Algorithms and complexity (time, space)
- Important formulas and theorems (Church-Turing Thesis, Turing Machine Acceptance, Halting Problem)
