# Introduction to Finite Automata

Finite Automata is a fundamental concept in the theory of computation, which deals with the study of abstract machines that can perform computations on input strings. These machines are called finite automata because they have a finite number of states and can only recognize a finite number of strings.

## Structural Representations

A finite automaton can be represented in several ways, including:

- **Transition Diagram**: A graphical representation of the automaton, where states are represented as nodes and transitions are represented as edges between nodes.
- **Transition Table**: A table that lists all possible transitions between states.
- **State Diagram**: A diagram that shows the current state of the automaton and the possible next states.

## Automata and Complexity

The study of finite automata is closely related to the study of complexity theory, which deals with the resources required to solve computational problems. The complexity of a finite automaton is measured by the number of states it has, and the time and space required to recognize a string.

## Deterministic Finite Automata (DFA)

A DFA is a finite automaton that can be in only one state at a time. It is defined by a set of states, an alphabet, a transition function, and a set of accepting states.

### Example

Consider a DFA that recognizes the language of all strings that end with the symbol "1". The transition diagram for this DFA is shown below:

```
      +-------+
      |  q0  |
      +-------+
           |
           | 0
           v
      +-------+
      |  q1  |
      +-------+
           |
           | 1
           v
      +-------+
      |  q2  |
      +-------+
```

In this example, the DFA has three states: q0, q1, and q2. The transition function is defined as follows:

- δ(q0, 0) = q1
- δ(q0, 1) = q2
- δ(q1, 0) = q1
- δ(q1, 1) = q2
- δ(q2, 0) = q1
- δ(q2, 1) = q2

The accepting state is q2.

## Nondeterministic Finite Automata (NFA)

An NFA is a finite automaton that can be in multiple states at the same time. It is defined by a set of states, an alphabet, a transition function, and a set of accepting states.

### Example

Consider an NFA that recognizes the language of all strings that contain the symbol "1". The transition diagram for this NFA is shown below:

```
      +-------+
      |  q0  |
      +-------+
           |
           | 0
           v
      +-------+
      |  q1  |
      +-------+
           |
           | 1
           v
      +-------+
      |  q2  |
      +-------+
           |
           | ε
           v
      +-------+
      |  q3  |
      +-------+
```

In this example, the NFA has four states: q0, q1, q2, and q3. The transition function is defined as follows:

- δ(q0, 0) = {q1}
- δ(q0, 1) = {q2, q3}
- δ(q1, 0) = {q1}
- δ(q1, 1) = {q2, q3}
- δ(q2, 0) = {q1}
- δ(q2, 1) = {q2, q3}
- δ(q3, 0) = {q1}
- δ(q3, 1) = {q2, q3}

The accepting states are q2 and q3.

## Comparison of DFA and NFA

The following table compares the characteristics of DFA and NFA:

| Characteristic        | DFA           | NFA              |
| --------------------- | ------------- | ---------------- |
| Number of states      | Finite        | Finite           |
| Number of transitions | Finite        | Finite           |
| Transition function   | Deterministic | Nondeterministic |
| Accepting states      | Single        | Multiple         |
| Recognition power     | Limited       | More powerful    |

## Exam Tips

To perform well in an exam on finite automata, make sure to:

- Understand the definitions of DFA and NFA
- Know how to construct transition diagrams and tables for DFA and NFA
- Be able to prove that a language is regular or not
- Practice solving problems on finite automata
