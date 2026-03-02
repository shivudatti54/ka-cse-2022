# Nondeterministic Finite Automata

## Introduction

Finite Automata is a simple, yet powerful model of computation used to recognize patterns in strings. In the previous module, we studied Deterministic Finite Automata (DFA), which is a type of Finite Automata where every input symbol has a unique next state. However, in many cases, it is more convenient to design a Finite Automata where a single input symbol can have multiple next states. This type of Finite Automata is known as Nondeterministic Finite Automata (NFA).

NFA is a crucial concept in the Theory of Computation, as it provides a more flexible and expressive way of recognizing patterns in strings. Many real-world problems, such as text search, pattern matching, and compiler design, rely heavily on NFA.

## Key Concepts

### Definition of NFA

A Nondeterministic Finite Automata (NFA) is a 5-tuple (Q, Σ, δ, q0, F), where:

* Q is a finite set of states
* Σ is a finite set of input symbols (alphabet)
* δ is a transition function that maps each state and input symbol to a set of next states
* q0 is the initial state
* F is a set of accepting states

### Transition Function

The transition function δ is a crucial component of an NFA. It takes a state and an input symbol as input and returns a set of next states. This means that an NFA can have multiple possible next states for a given input symbol.

### Acceptance of a String

An NFA accepts a string if there exists a sequence of transitions from the initial state to an accepting state, such that the input string is consumed.

### Equivalence of NFA and DFA

Although NFA and DFA are different models of computation, they are equivalent in terms of their expressive power. This means that any language recognized by an NFA can also be recognized by a DFA, and vice versa.

## Examples

### Example 1: Designing an NFA to recognize the language {ab, abb, abbb, ...}

To design an NFA for this language, we need to create a transition function that maps each state and input symbol to a set of next states. The NFA can be designed as follows:

* Q = {q0, q1, q2}
* Σ = {a, b}
* δ(q0, a) = {q1}
* δ(q1, b) = {q2, q1}
* δ(q2, b) = {q2}
* q0 = q0
* F = {q2}

### Example 2: Converting an NFA to a DFA

To convert an NFA to a DFA, we need to create a new DFA that simulates the behavior of the NFA. This can be done by creating a new state in the DFA for each subset of states in the NFA.

## Exam Tips

1. Understand the definition of NFA and its components.
2. Be able to design an NFA to recognize a given language.
3. Understand the concept of equivalence between NFA and DFA.
4. Know how to convert an NFA to a DFA.
5. Be able to prove that a language is regular by showing that it can be recognized by an NFA.
6. Understand the limitations of NFA and how they can be overcome using more powerful models of computation.
7. Practice designing NFAs for different languages and converting them to DFAs.