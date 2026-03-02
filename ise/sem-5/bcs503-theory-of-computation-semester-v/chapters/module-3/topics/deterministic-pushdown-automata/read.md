# Deterministic Pushdown Automata

## Introduction

Deterministic Pushdown Automata (DPDA) is a type of automaton that uses a stack to recognize context-free languages. It is a deterministic version of the Pushdown Automaton (PDA), which means that for every input symbol and stack symbol, there is only one possible transition.

## Definition

A DPDA is a 6-tuple (Q, Σ, Γ, δ, q0, F), where:

- Q is the set of states
- Σ is the input alphabet
- Γ is the stack alphabet
- δ is the transition function
- q0 is the initial state
- F is the set of final states

## How DPDA Works

The DPDA works by reading the input string from left to right and using the stack to store and retrieve symbols. The transition function δ takes the current state, input symbol, and stack symbol as input and returns the next state and the symbol to be pushed or popped from the stack.

## Example

Consider a DPDA that recognizes the language {a^n b^n | n ≥ 0}. The DPDA can be defined as follows:

- Q = {q0, q1, q2}
- Σ = {a, b}
- Γ = {A}
- δ(q0, a, Z) = (q1, AZ)
- δ(q1, a, A) = (q1, AA)
- δ(q1, b, A) = (q2, Z)
- δ(q2, b, Z) = (q2, Z)
- q0 is the initial state
- F = {q2}

## ASCII Diagram

```
      +---------------+
      |  q0 (initial)  |
      +---------------+
           |
           | a, Z/AZ
           v
      +---------------+
      |  q1           |
      +---------------+
           | a, A/AA
           | b, A/Z
           v
      +---------------+
      |  q2 (final)   |
      +---------------+
           | b, Z/Z
```

## Comparison with Nondeterministic PDA

The main difference between DPDA and nondeterministic PDA is that DPDA has only one possible transition for every input symbol and stack symbol, whereas nondeterministic PDA can have multiple possible transitions.

|                     | DPDA                                            | Nondeterministic PDA                   |
| ------------------- | ----------------------------------------------- | -------------------------------------- |
| Transition function | δ(q, a, A) = (p, B)                             | δ(q, a, A) = {(p1, B1), (p2, B2), ...} |
| Recognition power   | Recognizes deterministic context-free languages | Recognizes context-free languages      |

## Exam Tips

- Make sure to understand the definition and working of DPDA.
- Practice drawing ASCII diagrams to visualize the DPDA.
- Be able to compare and contrast DPDA with nondeterministic PDA.
