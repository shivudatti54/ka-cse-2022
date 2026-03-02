# **Theory of Computation: Revision Notes - Section 8.1**

## **Defining Computation**

- A computation is a sequence of steps that transform one input into another.
- Computation can be represented using a Turing Machine, Finite Automata, Pushdown Automata, or a Recursive Function.

## **Key Concepts**

- **Turing Machine:**
  - A mathematical model for computation.
  - Consists of a tape, read/write head, and a set of states.
  - Can read and write symbols on the tape.
- **Finite Automata:**
  - A mathematical model for recognizing patterns.
  - Consists of a set of states, an alphabet, and transition functions.
  - Can recognize regular languages.
- **Pushdown Automata:**
  - A mathematical model for parsing expressions.
  - Consists of a stack, read/write head, and a set of states.
  - Can recognize context-free languages.

## **Important Formulas and Definitions**

- **Turing Machine:**
  - States: q, q'
  - Alphabet: Σ = {0, 1, B} (where B represents the blank symbol)
  - Tape: q0, q1, q2, ..., qn (where q0 is the initial state)
  - Transition Function: δ(q, a) = (q', a', B)
- **Finite Automata:**
  - States: q, q'
  - Alphabet: Σ = {0, 1}
  - Transition Functions: δ(q, a) = q'
- **Pushdown Automata:**
  - Stack: Σ = {A}
  - States: q, q'
  - Transition Functions: δ(q, a) = (q', a', A)

## **Important Theorems**

- **Turing Machine:**
  - The Church-Turing Thesis (1963): A computation can be represented by a Turing Machine.
  - The Halting Problem (1936): There cannot exist an algorithm that can determine whether a given Turing Machine will halt on a given input.
- **Finite Automata:**
  - The Pumping Lemma (1967): A regular language can be pumped up to increase its length by a factor of at least 2.

## **Revision Tips**

- Understand the key concepts and definitions of different computational models.
- Practice solving problems using Turing Machines, Finite Automata, and Pushdown Automata.
- Review the Church-Turing Thesis and the Halting Problem.
- Familiarize yourself with the Pumping Lemma for regular languages.
