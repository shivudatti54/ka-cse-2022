# **Deterministic Finite Automata, Nondeterministic Finite Automata, An Application: Text Search, Finite Automata with Epsilon-Transitions**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Deterministic Finite Automata (DFA)](#deterministic-finite-automata-dfa)
   - [Definition](#definition)
   - [Properties](#properties)
   - [Construction](#construction)
   - [Decidability](#decidability)
   - [Examples](#examples)
4. [Nondeterministic Finite Automata (NFA)](#nondeterministic-finite-automata-nfa)
   - [Definition](#definition)
   - [Properties](#properties)
   - [Construction](#construction)
   - [Decidability](#decidability)
   - [Examples](#examples)
5. [Text Search using Finite Automata](#text-search-using-finite-automata)
   - [Problem Statement](#problem-statement)
   - [Solution](#solution)
   - [Efficiency](#efficiency)
6. [Finite Automata with Epsilon-Transitions](#finite-automata-with-epsilon-transitions)
   - [Definition](#definition)
   - [Properties](#properties)
   - [Construction](#construction)
   - [Examples](#examples)
7. [Conclusion](#conclusion)
8. [Further Reading](#further-reading)

## **Introduction**

Finite Automata is a fundamental concept in computer science, used to model and analyze the behavior of formal languages. In this module, we will explore two types of Finite Automata: Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA). We will also delve into the application of Finite Automata in text search and the extension to Finite Automata with Epsilon-transitions.

## **Historical Context**

The concept of Finite Automata dates back to the 1930s, when the mathematician Emil Post introduced the idea of a "post machine" to study the limits of computation. In the 1950s and 1960s, finite automata were used to model the behavior of formal languages, and the concept gained popularity in the development of compiler design and parsing algorithms.

## **Deterministic Finite Automata (DFA)**

### Definition

A DFA is a 5-tuple:

M = (Q, Σ, δ, q0, F)

where:

- Q: a finite set of states
- Σ: a finite set of input symbols
- δ: a transition function that maps each state and input symbol to a new state
- q0: the initial state
- F: a finite set of accepting states

### Properties

- **Decidability**: A DFA is decidable if there exists an algorithm that can determine whether a given input string is accepted or not.
- **Determinism**: A DFA is deterministic if, for each state and input symbol, there is only one possible next state.
- **Acceptance**: A DFA accepts an input string if it ends in an accepting state.

### Construction

A DFA can be constructed from a regular expression using the following steps:

1. Start with an empty set of states Q = ∅
2. For each character c in Σ, add a new state q to Q
3. Define the transition function δ as follows:
   - δ(q, c) = q' for some q' in Q
4. Choose an initial state q0 in Q
5. Choose an accepting state F in F

### Decidability

A DFA is decidable if there exists an algorithm that can determine whether a given input string is accepted or not. This can be done by constructing a DFA from the regular expression and then using a decision algorithm such as the "longest prefix" algorithm.

### Examples

- A DFA that accepts all strings consisting of only 0s and 1s:
  - Q = {q0, q1}
  - Σ = {0, 1}
  - δ(q0, 0) = q0, δ(q0, 1) = q1
  - δ(q1, 0) = q0, δ(q1, 1) = q1
  - q0, q1 are the initial and accepting states
- A DFA that accepts all strings consisting of only 1s:
  - Q = {q0}
  - Σ = {0, 1}
  - δ(q0, 0) = ∅, δ(q0, 1) = q0
  - q0 is the initial and accepting state

## **Nondeterministic Finite Automata (NFA)**

### Definition

An NFA is a 5-tuple:

M = (Q, Σ, δ, q0, F)

where:

- Q: a finite set of states
- Σ: a finite set of input symbols
- δ: a transition function that maps each state and input symbol to a set of new states
- q0: the initial state
- F: a finite set of accepting states

### Properties

- **Nondeterminism**: An NFA is nondeterministic if, for each state and input symbol, there is more than one possible next state.
- **Decidability**: An NFA is decidable if there exists an algorithm that can determine whether a given input string is accepted or not.
- **Acceptance**: An NFA accepts an input string if any of its final states are reachable from the initial state.

### Construction

An NFA can be constructed from a regular expression using the following steps:

1. Start with an empty set of states Q = ∅
2. For each character c in Σ, add a new state q to Q
3. Define the transition function δ as follows:
   - δ(q, c) = {q' for q' in Q}
4. Choose an initial state q0 in Q
5. Choose an accepting state F in F

### Decidability

An NFA is decidable if there exists an algorithm that can determine whether a given input string is accepted or not. This can be done by constructing an equivalent DFA and then using a decision algorithm such as the "longest prefix" algorithm.

### Examples

- An NFA that accepts all strings consisting of only 0s and 1s:
  - Q = {q0, q1}
  - Σ = {0, 1}
  - δ(q0, 0) = {q0}, δ(q0, 1) = {q1}
  - δ(q1, 0) = {q0}, δ(q1, 1) = {q1}
  - q0 is the initial state, q1 is the accepting state
- An NFA that accepts all strings consisting of only 1s:
  - Q = {q0}
  - Σ = {0, 1}
  - δ(q0, 0) = ∅, δ(q0, 1) = {q0}
  - q0 is the initial and accepting state

## **Text Search using Finite Automata**

### Problem Statement

Given a text string and a pattern string, determine whether the pattern string is present in the text string.

### Solution

A DFA can be constructed to solve this problem. The DFA has the following states:

- q0: the initial state
- q1: a state that represents the presence of the pattern string
- q2: a state that represents the absence of the pattern string

The transition function δ is defined as follows:

- δ(q0, c) = q0 for all c in Σ
- δ(q0, \*) = q1
- δ(q1, c) = q1 for all c in Σ
- δ(q1, \*) = q2

The initial state is q0, and the accepting state is q1.

### Efficiency

The time complexity of this algorithm is O(n \* m), where n is the length of the text string and m is the length of the pattern string. This is because the DFA has to explore all possible paths in the transition graph.

## **Finite Automata with Epsilon-Transitions**

### Definition

A Finite Automaton with Epsilon-transitions is a 5-tuple:

M = (Q, Σ, δ, q0, F)

where:

- Q: a finite set of states
- Σ: a finite set of input symbols
- δ: a transition function that maps each state to a set of new states, including the possibility of ε-transitions (empty strings)
- q0: the initial state
- F: a finite set of accepting states

### Properties

- **Epsilon-transitions**: A Finite Automaton with Epsilon-transitions allows for the possibility of ε-transitions, which are transitions that do not consume any input symbols.
- **Decidability**: A Finite Automaton with Epsilon-transitions is decidable if there exists an algorithm that can determine whether a given input string is accepted or not.
- **Acceptance**: A Finite Automaton with Epsilon-transitions accepts an input string if any of its final states are reachable from the initial state.

### Construction

A Finite Automaton with Epsilon-transitions can be constructed from a regular expression using the following steps:

1. Start with an empty set of states Q = ∅
2. For each character c in Σ, add a new state q to Q
3. Define the transition function δ as follows:
   - δ(q, ε) = q
   - δ(q, c) = {q' for q' in Q}
4. Choose an initial state q0 in Q
5. Choose an accepting state F in F

### Examples

- A Finite Automaton with Epsilon-transitions that accepts all strings consisting of only 0s and 1s:
  - Q = {q0, q1}
  - Σ = {0, 1}
  - δ(q0, ε) = q0, δ(q0, 0) = {q0}, δ(q0, 1) = {q1}
  - δ(q1, ε) = q0, δ(q1, 0) = {q0}, δ(q1, 1) = {q1}
  - q0 is the initial state, q1 is the accepting state
- A Finite Automaton with Epsilon-transitions that accepts all strings consisting of only 1s:
  - Q = {q0}
  - Σ = {0, 1}
  - δ(q0, ε) = q0, δ(q0, 0) = ∅, δ(q0, 1) = {q0}
  - q0 is the initial and accepting state

## **Conclusion**

In this module, we have explored the concepts of Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA), and their application in text search. We have also introduced the concept of Finite Automata with Epsilon-transitions, which allows for the possibility of ε-transitions. We have provided examples and case studies to illustrate the concepts, and have discussed the time complexity of the algorithms used to solve the problems.

## **Further Reading**

- "Introduction to the Theory of Computation" by Michael Sipser
- "Automata Theory, Languages, and Computation" by John E. Hopcroft, Jeffrey D. Ullman, and Jeffrey S. Vitter
- "Finite Automata and Formal Language Theory" by Peter Linz
- "Epsilon-Automata and Transduction" by G. P. van Leeuwen
