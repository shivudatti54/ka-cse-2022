# **Global States**

### Introduction

In distributed systems, a global state refers to the current status or configuration of the system as a whole. It encompasses the state of all processes, threads, and nodes in the system, taking into account their interactions and dependencies. Understanding global states is crucial for designing and implementing reliable and efficient distributed systems.

### Clocks and Time

In a distributed system, clocks are used to synchronize the timing of different nodes and processes. However, clocks can have different values on different nodes, leading to inconsistencies and potential conflicts.

- **Local Clocks:** Each node has its own local clock that keeps track of time.
- **Global Clocks:** A global clock is a synchronized clock that represents the current time across all nodes in the system.

### Events and Process States

In a distributed system, events are the occurrences or changes that happen in the system, while process states refer to the current status of a process.

- **Event Types:** There are two main types of events:
  - **Internal Events:** Happen within a process, such as a process starting or finishing.
  - **External Events:** Happen outside a process, such as a message arrival or a network packet transmission.
- **Process States:** A process can be in one of three states:
  - **Ready State:** The process is ready to execute and has a valid CPU time slice.
  - **Running State:** The process is executing and using the CPU.
  - **Waiting State:** The process is waiting for an event, such as a message arrival or a network packet transmission.

### Global States: Definitions and Concepts

A global state is defined as the current configuration of the system, consisting of the states of all processes, threads, and nodes.

- **Global State Variables:** Global state variables are variables that represent the current state of the system, such as the number of processes, threads, and nodes.
- **Global State Transition Functions:** Global state transition functions define how the global state changes over time, based on the events and process states.

### Key Concepts

- **Consistency:** Global states must be consistent across all nodes in the system.
- **Availability:** Global states must be available to all nodes in the system.
- **Partition Tolerance:** Global states must be tolerant of partitions, where some nodes or processes are disconnected from others.
- **Synchronization:** Global states must be synchronized across all nodes in the system.

### Example

Suppose we have a distributed system with three nodes (A, B, and C), each with their own local clock. The nodes are connected through a network, and the system has a global clock that represents the current time across all nodes.

- Node A has a local clock value of 10.0.
- Node B has a local clock value of 15.0.
- Node C has a local clock value of 20.0.
- The system has a global clock value of 10.0.

In this example, the global state of the system is the state of all nodes, including their local clock values and the global clock value. The system must ensure that the global state is consistent across all nodes, taking into account the local clock values and the global clock value.

### Textbook References

- Chapter 14.1: Introduction to Distributed Systems
- Chapter 14.2: Clocks and Time in Distributed Systems
- Chapter 14.3: Events and Process States in Distributed Systems
- Chapter 14.4: Global States in Distributed Systems
- Chapter 14.5: Synchronization and Consistency in Distributed Systems
