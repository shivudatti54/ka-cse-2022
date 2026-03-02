# **Global States**

### Introduction

In the context of distributed systems, a global state refers to the complete and consistent state of all processes in the system. It is the overall configuration of the system, including the values of variables, the states of processes, and the status of resources.

### Definition

A global state is a snapshot of the entire system, capturing the current values of all variables, process states, and resource statuses.

### Types of Global States

There are two types of global states:

- **Global State of a System**: The global state of a system is the complete and consistent state of all processes in the system.
- **Global State of a Process**: The global state of a process is the state of the process itself, including the values of its variables and the status of its resources.

### Key Concepts

- **Consistency**: The global state must be consistent, meaning that it must satisfy all the constraints and rules of the system.
- **Completeness**: The global state must be complete, meaning that it must capture all the relevant information about the system.
- **Validity**: The global state must be valid, meaning that it must be consistent with the current state of the system.

### Examples

- A distributed database system maintains a global state of all transactions in progress, ensuring consistency and completeness of the data.
- A message-passing system maintains a global state of all processes, ensuring that messages are delivered correctly and in the correct order.

### Key Properties

- **Determinism**: The global state must be deterministic, meaning that given the current state of the system, the global state can be uniquely determined.
- **Transitivity**: The global state must be transitive, meaning that if a process changes its state, the global state must also change accordingly.

### Notations

- **σ**: The global state of a system.
- **π**: The global state of a process.

### Definitions

- **σ = (π, v)**: The global state of a system, where π is the global state of each process and v is the value of each variable.
- **π = (p1, p2, ..., pn)**: The global state of each process, where p1, p2, ..., pn are the process IDs.

### Example

Consider a distributed system with three processes, P1, P2, and P3. The global state of the system is σ = (π1, π2, π3), where π1 = (P1, V1), π2 = (P2, V2), and π3 = (P3, V3). The global state of each process is:

| Process | Global State |
| ------- | ------------ |
| P1      | (P1, V1)     |
| P2      | (P2, V2)     |
| P3      | (P3, V3)     |

The global state of the system is σ = ((P1, V1), (P2, V2), (P3, V3)).

### Exercises

1. Define the global state of a system with n processes.
2. Explain the concept of consistency in the context of global states.
3. Provide an example of a distributed system that maintains a global state of all transactions in progress.

### Solutions

1. The global state of a system with n processes is σ = (π1, π2, ..., πn), where πi = (Pi, vi) is the global state of the ith process.
2. Consistency in the context of global states refers to the property that the global state must satisfy all the constraints and rules of the system, ensuring that the system remains in a valid and consistent state.
3. An example of a distributed database system that maintains a global state of all transactions in progress is a distributed relational database system.
