# **Global States Revision Notes**

**Definition:** Global state is the collection of information about the state of all processes in a distributed system.

**Key Points:**

- A global state is a snapshot of the entire system at a particular point in time.
- It is a function that maps each process ID to its current state.
- Global states are used to manage consistency and synchronization in distributed systems.
- Two global states are considered equal if all processes have the same state.

**Important Formulas:**

- **Global State Formula:** G(s) = (p_i, S_i) | pi ∈ P, Si ∈ S_i
- **Global State Equality:** G(s) = G'(s) if and only if G(s) = (p_i, S_i) = G'(s) = (p_i', S_i')

**Definitions:**

- **Process State:** The current state of a process.
- **Process ID:** The unique identifier of a process.

**Theorems:**

- **Global State Theorem:** If two global states are equal, then all processes have the same state.
- **Consistency Theorem:** If two global states are equal, then all processes have the same values for their variables.

**Important Concepts:**

- **Synchronization:** The process of ensuring that all processes have the same global state.
- **Consistency:** The property of a system that ensures all processes have the same state.

**Key Textbook Chapters:**

- Chapter 14.1: Introduction to Global States
- Chapter 14.2: Clocks and Events
- Chapter 14.3: Process States and Global States
- Chapter 14.4: Synchronization and Consistency
- Chapter 14.5: Global States and Distributed Systems
