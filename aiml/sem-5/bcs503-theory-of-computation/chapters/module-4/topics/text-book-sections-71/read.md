# **Theory of Computation**

## **Module: 10 Hours**

## **Topic: TEXT BOOK: Sections 7.1**

### Introduction

In this module, we will explore the basics of Theory of Computation, focusing on the different models of computation, including finite state machines, pushdown automata, and Turing machines. We will also delve into the concept of decidability and undecidability, which are crucial in understanding the limitations of different computational models.

### Finite State Machines (FSMs)

---

A Finite State Machine is a mathematical model that consists of a set of states, transitions between states, and an initial state. FSMs are used to recognize patterns in data and are commonly used in compiler design and parser implementation.

**Key Concepts:**

- **States:** A set of states that a machine can be in.
- **Transitions:** A set of rules that define how the machine moves from one state to another based on the input it receives.
- **Initial State:** The starting state of the machine.

**Example:**

Suppose we want to design a FSM to recognize the language `L = {a^n b^n | n ≥ 0}`. The FSM would have the following states:

- `q0` (initial state)
- `q1`
- `q2`

The transitions would be defined as follows:

| Input | Transition |
| ----- | ---------- |
| `a`   | `q0 -> q1` |
| `b`   | `q1 -> q2` |
| `a`   | `q2 -> q0` |
| `b`   | `q2 -> q0` |

### Pushdown Automata (PDAs)

---

A Pushdown Automaton is a mathematical model that consists of a stack that can push and pop elements. PDAs are used to recognize context-free languages and are commonly used in compiler design and parsing.

**Key Concepts:**

- **Stack:** A set of elements that can be pushed and popped.
- **Push:** Adding an element to the top of the stack.
- **Pop:** Removing the top element from the stack.

**Example:**

Suppose we want to design a PDA to recognize the language `L = {a^n b^n | n ≥ 0}`. The PDA would have the following stack:

- `q0` (initial state)
- `q1`
- `q2`

The transitions would be defined as follows:

| Input | Transition                       |
| ----- | -------------------------------- |
| `a`   | `q0 -> q1` (push `a` onto stack) |
| `b`   | `q1 -> q2` (pop `a` from stack)  |
| `a`   | `q2 -> q0` (push `a` onto stack) |
| `b`   | `q2 -> q0` (pop `a` from stack)  |

### Turing Machines (TM)

---

A Turing Machine is a mathematical model that consists of a tape that can be read and written. TMs are used to recognize recursively enumerable languages and are commonly used in the study of undecidability.

**Key Concepts:**

- **Tape:** A infinite sequence of cells that can be read and written.
- **Head:** A read/write head that can move along the tape.
- **State:** A set of states that the machine can be in.

**Example:**

Suppose we want to design a TM to recognize the language `L = {a^n b^n | n ≥ 0}`. The TM would have the following states:

- `q0` (initial state)
- `q1`
- `q2`

The transitions would be defined as follows:

| Input | Transition                                   |
| ----- | -------------------------------------------- |
| `a`   | `q0 -> q1` (move head one cell to the right) |
| `b`   | `q1 -> q2` (move head one cell to the right) |
| `a`   | `q2 -> q0` (move head one cell to the left)  |
| `b`   | `q2 -> q0` (move head one cell to the left)  |

### Decidability and Undecidability

---

A problem is said to be decidable if there exists an algorithm that can solve it in a finite amount of time. A problem is said to be undecidable if there exists no algorithm that can solve it in a finite amount of time.

**Key Concepts:**

- **Decidable:** A problem that has a solution in a finite amount of time.
- **Undecidable:** A problem that does not have a solution in a finite amount of time.

**Example:**

The halting problem is a classic example of an undecidable problem. The halting problem is the problem of determining whether a given program will halt (stop executing) or run forever. The halting problem is undecidable because there exists no algorithm that can solve it in a finite amount of time.

### Conclusion

---

In this module, we have explored the basics of Theory of Computation, focusing on finite state machines, pushdown automata, and Turing machines. We have also delved into the concept of decidability and undecidability, which are crucial in understanding the limitations of different computational models.
