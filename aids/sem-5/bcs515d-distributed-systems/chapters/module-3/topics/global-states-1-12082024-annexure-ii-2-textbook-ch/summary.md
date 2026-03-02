# **Global States Revision Notes**

### Definitions

- **Global state**: The current state of a distributed system, which includes all the processes and their respective states.
- **Global snapshot**: A complete and accurate representation of the global state of a distributed system at a particular point in time.

### Formulas

- **Consensus protocols**: ensure that all processes agree on a global state.
  - Example: Paxos protocol
- **Distributed algorithms**: designed to achieve a global state in a distributed system.
  - Example: Leader election algorithms

### Theorems

- **Banks' Theorem**: states that a distributed system with a finite number of processes can achieve a global state if the system is consistent and the processes can agree on the global state.
- **Castellan's Theorem**: states that a distributed system with a finite number of processes can achieve a global state if the system is consistent and the processes can agree on the global state, even in the presence of faults.

### Important Concepts

- **Clocks**: individual clocks that measure time for each process.
- **Events**: actions taken by processes in a distributed system.
- **Process states**: the current state of each process in a distributed system.
- **Global state convergence**: the process of achieving a consistent global state among all processes.

### Key Concepts to Remember

- Global states are the current states of all processes in a distributed system.
- Consensus protocols ensure that all processes agree on a global state.
- Distributed algorithms are designed to achieve a global state in a distributed system.
- Causality and consistency are essential for achieving a global state.

### Important Concepts from the Textbook (Chapter 14.1-14.5)

- **Leader election**: a distributed algorithm that elects a leader process in a distributed system.
- **Leader-follower model**: a distributed system with a single leader process and multiple follower processes.
- **Distributed clock synchronization**: the process of synchronizing clocks in a distributed system.
