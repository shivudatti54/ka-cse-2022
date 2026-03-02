# **Theory of Computation: Deterministic Finite Automata, Nondeterministic Finite Automata, and Text Search**

**Module:** Theory of Computation
**Topic:** Deterministic Finite Automata, Nondeterministic Finite Automata, An Application: Text Search, Finite Automata with Epsilon-Transitions
**Duration:** 10 Hours

## **Introduction**

Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA) are fundamental concepts in the theory of computation. In this study material, we will explore the definitions, properties, and applications of these automata. We will also delve into the concept of text search using finite automata.

## **Deterministic Finite Automata (DFA)**

### Definition

A DFA is a mathematical model that can be in one of a finite number of states. It reads input symbols one at a time and, based on the current state and input symbol, it can transition to a new state.

### Properties

- Each state in a DFA is a distinct entity.
- The transition function determines the next state based on the current state and input symbol.
- The DFA can only be in one state at a time.

### Example

Suppose we want to build a DFA that recognizes the string "ab". We can define the following DFA:

| State | Input Symbol | Next State |
| ----- | ------------ | ---------- |
| s1    | a            | s2         |
| s1    | b            | accept     |
| s2    | a            | reject     |
| s2    | b            | s3         |

In this example, the DFA starts in state s1. If the input symbol is 'a', it transitions to state s2. If the input symbol is 'b', it stays in state s1.

### Key Concepts

- **State**: A distinct entity that the DFA can be in.
- **Transition function**: Determines the next state based on the current state and input symbol.
- **Accepting state**: A state that indicates the DFA has accepted a string.

## **Nondeterministic Finite Automata (NFA)**

### Definition

An NFA is a mathematical model that can be in one of a finite number of states, but unlike a DFA, it can have multiple possible next states for a given state and input symbol.

### Properties

- Each state in an NFA is a distinct entity.
- The transition function determines the possible next states based on the current state and input symbol.
- The NFA can be in multiple states at the same time.

### Example

Suppose we want to build an NFA that recognizes the string "ab". We can define the following NFA:

| State | Input Symbol | Possible Next States |
| ----- | ------------ | -------------------- |
| s1    | a            | s2, s3               |
| s1    | b            | reject               |
| s2    | a            | s2, s3               |
| s2    | b            | s4                   |
| s3    | a            | reject               |
| s3    | b            | s4                   |
| s4    | a            | accept               |
| s4    | b            | s4                   |

In this example, the NFA starts in state s1. If the input symbol is 'a', it can transition to either state s2 or s3.

### Key Concepts

- **State**: A distinct entity that the NFA can be in.
- **Transition function**: Determines the possible next states based on the current state and input symbol.
- **Accepting state**: A state that indicates the NFA has accepted a string.

## **Text Search using Finite Automata**

### Introduction

Text search is a fundamental problem in computer science that involves finding a pattern in a text. Finite automata can be used to solve text search problems.

### Example

Suppose we want to build a text search engine that finds all occurrences of the pattern "ab" in a given text. We can use a DFA to solve this problem.

### DFA for Text Search

| State | Input Symbol | Next State |
| ----- | ------------ | ---------- |
| s1    | a            | s2         |
| s1    | b            | accept     |
| s2    | a            | s3         |
| s2    | b            | reject     |
| s3    | a            | s3         |
| s3    | b            | reject     |

In this example, the DFA starts in state s1. If the input symbol is 'a', it transitions to state s2. If the input symbol is 'b', it stays in state s1.

### Key Concepts

- **Text search**: Finding a pattern in a text.
- **DFA for text search**: A DFA that can be used to solve text search problems.

## **Epsilon-Transitions**

### Definition

An epsilon-transition is a transition in a finite automaton where the input symbol is epsilon (ε), which means the automaton stays in the same state.

### Properties

- Epsilon-transitions allow the automaton to stay in the same state.
- Epsilon-transitions can be used to handle irregularities in the input string.

### Example

Suppose we want to build a DFA that recognizes the string "aεb". We can define the following DFA:

| State | Input Symbol | Next State |
| ----- | ------------ | ---------- |
| s1    | a            | s2         |
| s1    | ε            | s1         |
| s2    | b            | accept     |
| s2    | ε            | s2         |

In this example, the DFA starts in state s1. If the input symbol is 'a', it transitions to state s2. If the input symbol is ε, it stays in state s1.

### Key Concepts

- **Epsilon-transition**: A transition in a finite automaton where the input symbol is epsilon (ε).
- **Epsilon-transition**: A transition that allows the automaton to stay in the same state.

## **Conclusion**

In this study material, we have explored the concepts of Deterministic Finite Automata, Nondeterministic Finite Automata, and text search using finite automata. We have also introduced the concept of epsilon-transitions. These concepts are fundamental in the theory of computation and have numerous applications in computer science.

## **Key Takeaways**

- A DFA is a mathematical model that can be in one of a finite number of states.
- An NFA is a mathematical model that can be in one of a finite number of states, but unlike a DFA, it can have multiple possible next states for a given state and input symbol.
- Text search is a fundamental problem in computer science that involves finding a pattern in a text.
- Epsilon-transitions allow the automaton to stay in the same state.

## **Practice Problems**

1.  Design a DFA to recognize the string "abc".
2.  Design an NFA to recognize the string "ab".
3.  Design a DFA to recognize the string "aεb".
4.  Design an NFA to recognize the string "abε".

## **References**

- "Introduction to Automata Theory, Languages, and Computation" by John E. Hopcroft, Jeffrey D. Ullman
- "Automata Theory and Applications" by S. Sipser
