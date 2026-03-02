# Theory of Computation

## Module: Deterministic Finite Automata, Nondeterministic Finite Automata, An Application: Text Search, Finite Automata with Epsilon-Transitions

### Deterministic Finite Automata (DFA)

#### Definition:

A Deterministic Finite Automaton (DFA) is a mathematical model that can be in one of a finite number of states. It can change state based on the current state and the input symbol read from the input tape. The DFA can only be in one state at a time.

#### Key Components:

- **States**: A set of states that the DFA can be in. The states are finite in number.
- **Alphabet**: The set of input symbols that the DFA can read.
- **Transition Function**: A function that maps each state and input symbol to a new state.
- **Initial State**: The starting state of the DFA.
- **Final State**: The state that the DFA accepts if it is in that state and has read the entire input.

#### Example:

Consider the DFA that recognizes the language of palindromes over the alphabet {0, 1}. The states are {q0, q1, qf}, where q0 is the initial state, q1 is the middle state, and qf is the final state. The transition function is defined as follows:

| Current State | Current Symbol | Next State |
| ------------- | -------------- | ---------- |
| q0            | 0              | q1         |
| q0            | 1              | q1         |
| q1            | 0              | q0         |
| q1            | 1              | qf         |
| qf            | 0              | qf         |
| qf            | 1              | q0         |

The DFA starts in state q0 and reads the input symbol. Based on the symbol, it transitions to state q1. If it reads another symbol, it transitions to state q0 or qf. If it reads a palindrome, it accepts and stays in state qf.

### Nondeterministic Finite Automaton (NFA)

#### Definition:

A Nondeterministic Finite Automaton (NFA) is a mathematical model that can be in one of a finite number of states, but it can also be in more than one state at a time. The NFA can change state based on the current state and the input symbol read from the input tape.

#### Key Components:

- **States**: A set of states that the NFA can be in. The states are finite in number.
- **Alphabet**: The set of input symbols that the NFA can read.
- **Transition Function**: A function that maps each state and input symbol to a set of new states.
- **Initial State**: The starting state of the NFA.
- **Final State**: The state that the NFA accepts if it is in that state and has read the entire input.

#### Example:

Consider the NFA that recognizes the language of all strings over the alphabet {0, 1}. The states are {q0, q1}, where q0 is the initial state and q1 is the accepting state. The transition function is defined as follows:

| Current State | Current Symbol | Next States |
| ------------- | -------------- | ----------- |
| q0            | 0              | q0, q1      |
| q0            | 1              | q1          |
| q1            | 0              | q1          |
| q1            | 1              | q1          |

The NFA starts in state q0 and reads the input symbol. Based on the symbol, it can transition to state q0 or q1. If it is in state q1, it accepts the input.

### Application: Text Search

Text search is a classic application of finite automata. Given a text and a pattern, we want to find all occurrences of the pattern in the text. We can use a DFA or NFA to achieve this.

**DFA Approach**

We can construct a DFA that recognizes the language of all strings that contain the pattern. The DFA will start in the initial state and read the text one character at a time. If it reads a character that is not in the pattern, it will stay in the same state. If it reads a character that is in the pattern, it will transition to a new state.

**NFA Approach**

We can construct an NFA that recognizes the language of all strings that contain the pattern. The NFA will start in the initial state and read the text one character at a time. If it reads a character that is not in the pattern, it will stay in the same state. If it reads a character that is in the pattern, it will transition to a set of new states.

### Finite Automata with Epsilon-Transitions

#### Definition:

A finite automaton with epsilon-transitions is a type of finite automaton that can make epsilon-transitions, i.e., it can stay in the same state even if it reads an empty string.

#### Example:

Consider the finite automaton that recognizes the language of all strings over the alphabet {0, 1} that have an even number of 1s. The states are {q0, q1}, where q0 is the initial state and q1 is the accepting state. The transition function is defined as follows:

| Current State | Current Symbol | Next States |
| ------------- | -------------- | ----------- |
| q0            | 0              | q0          |
| q0            | 1              | q1          |
| q1            | 0              | q0          |
| q1            | 1              | q1          |

The finite automaton starts in state q0 and reads the input symbol. If it reads an 0, it stays in the same state. If it reads a 1, it transitions to state q1. If it is in state q1, it accepts the input.

Note: Epsilon-transitions are important in many applications, such as regular expression matching and string matching.
