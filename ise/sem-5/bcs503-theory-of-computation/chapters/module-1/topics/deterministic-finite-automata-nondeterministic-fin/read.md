# **Deterministic Finite Automata (DFA)**

### Definition

A Deterministic Finite Automaton (DFA) is a mathematical model used to recognize patterns in strings. It consists of a set of states, an input alphabet, a transition function, and an initial state. The DFA is said to be deterministic if for every state, input symbol, and current state, there is at most one next state.

### Key Concepts

- **States**: The set of all possible states in the DFA.
- **Input Alphabet**: The set of symbols that can be read from the input string.
- **Transition Function**: A function that maps each state, input symbol, and current state to the next state.
- **Initial State**: The starting state of the DFA.
- **Accepting States**: The set of states that the DFA accepts as valid input strings.

### Example

Consider the DFA that recognizes the language of palindromes over the alphabet {a, b}. The states are:

- Q0 (initial state)
- Q1
- Q2 (accepting state)

The transition function is defined as follows:

| State | Input | Next State |
| ----- | ----- | ---------- |
| Q0    | a     | Q1         |
| Q0    | b     | Q0         |
| Q1    | a     | Q2         |
| Q1    | b     | Q0         |
| Q2    | a     | Q2         |
| Q2    | b     | Q2         |

### How it Works

1. The DFA starts in the initial state Q0.
2. The input string is read one symbol at a time.
3. For each input symbol, the DFA transitions to the next state based on the transition function.
4. If the DFA reaches an accepting state, it accepts the input string.

### Pseudocode

```
INPUT: input_string
STATE: Q0 (initial state)
FOR EACH SYMBOL IN input_string
  IF CURRENT STATE = Q0 AND SYMBOL = 'a'
    SET CURRENT STATE = Q1
  ELSE IF CURRENT STATE = Q0 AND SYMBOL = 'b'
    SET CURRENT STATE = Q0
  ELSE IF CURRENT STATE = Q1 AND SYMBOL = 'a'
    SET CURRENT STATE = Q2
  ELSE IF CURRENT STATE = Q1 AND SYMBOL = 'b'
    SET CURRENT STATE = Q0
  ELSE IF CURRENT STATE = Q2
    SET CURRENT STATE = Q2
END FOR
IF CURRENT STATE = Q2
  ACCEPT input_string
ELSE
  REJECT input_string
```

# **Nondeterministic Finite Automaton (NFA)**

### Definition

A Nondeterministic Finite Automaton (NFA) is a mathematical model used to recognize patterns in strings. It consists of a set of states, an input alphabet, a transition function, and an initial state. The NFA is said to be nondeterministic if for every state, input symbol, and current state, there can be multiple next states.

### Key Concepts

- **States**: The set of all possible states in the NFA.
- **Input Alphabet**: The set of symbols that can be read from the input string.
- **Transition Function**: A function that maps each state, input symbol, and current state to a set of next states.
- **Initial State**: The starting state of the NFA.
- **Accepting States**: The set of states that the NFA accepts as valid input strings.

### Example

Consider the NFA that recognizes the language of palindromes over the alphabet {a, b}. The states are:

- Q0 (initial state)
- Q1
- Q2 (accepting state)

The transition function is defined as follows:

| State | Input | Next States |
| ----- | ----- | ----------- |
| Q0    | a     | {Q1, Q0}    |
| Q0    | b     | {Q0, Q2}    |
| Q1    | a     | {Q2, Q1}    |
| Q1    | b     | {Q1}        |
| Q2    | a     | {Q2}        |
| Q2    | b     | {Q2}        |

### How it Works

1. The NFA starts in the initial state Q0.
2. The input string is read one symbol at a time.
3. For each input symbol, the NFA transitions to multiple next states based on the transition function.
4. If the NFA reaches an accepting state, it accepts the input string.

### Pseudocode

```
INPUT: input_string
STATE: Q0 (initial state)
FOR EACH SYMBOL IN input_string
  SET NEXT_STATES = TRANSITION_FUNCTION(CURRENT_STATE, SYMBOL)
  SET CURRENT_STATE = SELECT NEXT_STATE FROM NEXT_STATES
END FOR
IF CURRENT_STATE = Q2
  ACCEPT input_string
ELSE
  REJECT input_string
```

# **An Application: Text Search**

Text search is a common application of finite automata. The goal is to find all occurrences of a pattern in a given text.

### Example

Consider the text search problem where we want to find all occurrences of the pattern "ab" in the text "ababcab".

### DFA Solution

We can use a DFA to recognize the language of strings that match the pattern "ab". The DFA has two states: Q0 (initial state) and Q1 (accepting state). The transition function is defined as follows:

| State | Input | Next State |
| ----- | ----- | ---------- |
| Q0    | a     | Q1         |
| Q0    | b     | Q0         |
| Q1    | a     | Q2         |
| Q1    | b     | Q1         |
| Q2    | a     | Q2         |
| Q2    | b     | Q2         |

The DFA starts in the initial state Q0 and transitions to the next state based on the input symbol. If the DFA reaches the accepting state Q1, it accepts the input string.

### NFA Solution

We can also use an NFA to recognize the language of strings that match the pattern "ab". The NFA has two states: Q0 (initial state) and Q1 (accepting state). The transition function is defined as follows:

| State | Input | Next States |
| ----- | ----- | ----------- |
| Q0    | a     | {Q1, Q0}    |
| Q0    | b     | {Q0, Q2}    |
| Q1    | a     | {Q2, Q1}    |
| Q1    | b     | {Q1}        |
| Q2    | a     | {Q2}        |
| Q2    | b     | {Q2}        |

The NFA starts in the initial state Q0 and transitions to multiple next states based on the input symbol. If the NFA reaches the accepting state Q1, it accepts the input string.

# **Finite Automata with Epsilon-Transitions**

### Definition

A finite automaton with epsilon-transitions is a mathematical model that allows for epsilon-transitions, where the automaton can transition to a state even if there is no input symbol.

### Key Concepts

- **Epsilon-Transitions**: Transitions that occur without reading an input symbol.
- **Epsilon-Nodes**: States that can be reached through epsilon-transitions.

### Example

Consider the finite automaton with epsilon-transitions that recognizes the language of strings that match the pattern "ab\*". The states are:

- Q0 (initial state)
- Q1
- Q2

The transition function is defined as follows:

| State | Input   | Next State |
| ----- | ------- | ---------- |
| Q0    | a       | Q1         |
| Q0    | b       | Q0         |
| Q1    | a       | Q2         |
| Q1    | b       | Q1         |
| Q1    | epsilon | Q1         |
| Q2    | a       | Q2         |
| Q2    | b       | Q2         |
| Q2    | epsilon | Q2         |

The finite automaton starts in the initial state Q0 and transitions to the next state based on the input symbol or epsilon-transition.

### How it Works

1. The finite automaton starts in the initial state Q0.
2. The input string is read one symbol at a time.
3. For each input symbol, the finite automaton transitions to the next state based on the transition function.
4. If the finite automaton reaches the accepting state Q2, it accepts the input string.
5. If the finite automaton reaches the epsilon-node Q1, it stays in the same state.

### Pseudocode

```
INPUT: input_string
STATE: Q0 (initial state)
FOR EACH SYMBOL IN input_string
  IF SYMBOL = 'a'
    SET CURRENT_STATE = TRANSITION_FUNCTION(CURRENT_STATE, 'a')
  ELSE IF SYMBOL = 'b'
    SET CURRENT_STATE = TRANSITION_FUNCTION(CURRENT_STATE, 'b')
  ELSE IF SYMBOL = epsilon
    SET CURRENT_STATE = CURRENT_STATE
  END FOR
IF CURRENT_STATE = Q2
  ACCEPT input_string
ELSE
  REJECT input_string
```
