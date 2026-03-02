# **Logical Time and Logical Clocks**

### Definitions

- **Logical time**: A mathematical representation of the sequence of events in a distributed system, independent of physical time.
- **Logical clock**: A clock that keeps track of logical time, used to synchronize processes and events in a distributed system.

### Concepts

- **Monotonicity**: A logical clock must satisfy the monotonicity property, i.e., if process P finishes event E before process Q, then the logical clock value of P is less than or equal to the logical clock value of Q.
- **Boundedness**: A logical clock must be bounded, i.e., there exists a maximum value that the logical clock can take.
- **Lamport Clocks**: A type of logical clock that assigns a unique value to each process, based on the sequence of events it has experienced.
- **Dijkstra Clocks**: A type of logical clock that assigns a unique value to each process, based on the minimum number of events it has experienced.

### Formulas and Theorems

- **Lamport's Bakery Algorithm**: A protocol for synchronizing logical clocks, based on the Lamport clock type.
- **Dijkstra's Bakery Algorithm**: A protocol for synchronizing logical clocks, based on the Dijkstra clock type.
- **Logical Time Theorem**: If two processes have the same logical clock value, then they can synchronize their physical clocks.

### Important Concepts

- ** causality**: The relationship between events in a distributed system, where an event is causally related to another event if it occurs before it.
- **happens-before relation**: A relation between events that indicates the causal relationship between them.

### Key Points

- Logical time and logical clocks are used to synchronize processes and events in a distributed system.
- Monotonicity and boundedness are essential properties of a logical clock.
- Lamport Clocks and Dijkstra Clocks are two types of logical clocks used to synchronize processes.
- The Logical Time Theorem ensures that processes with the same logical clock value can synchronize their physical clocks.
