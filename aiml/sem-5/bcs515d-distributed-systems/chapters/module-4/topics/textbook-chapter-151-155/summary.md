# **Distributed Systems: Coordination and Agreement**

## **Chapter 15.1-15.5 Revision Notes**

### Introduction

- Distributed systems: a collection of autonomous computers that work together to achieve a common goal
- Coordination and agreement are key challenges in distributed systems

### Distributed Mutual Exclusion

- Problem: multiple processes trying to access a shared resource simultaneously
- Solution: use a lock or token to ensure exclusive access
- Key concepts:
  - Mutual exclusion
  - Locks
  - Tokens

### Peterson's Problem

- Problem: three processes trying to access a shared resource
- Solution: use tokens and a consensus protocol to resolve conflicts
- Key concepts:
  - Peterson's algorithm
  - Token passing

### Bakery Algorithm

- Problem: multiple processes trying to access a shared resource
- Solution: use a bakery algorithm to resolve conflicts
- Key concepts:
  - Bakery algorithm
  - Process scheduling

### Deadlocks

- Problem: a situation where multiple processes are blocked indefinitely
- Causes:
  - Mutual exclusion
  - Hold and wait
  - No-preemption
- Detection and prevention techniques:
  - Banker's algorithm
  - Resource allocation graphs

### Starvation

- Problem: a situation where a process is unable to access a resource
- Causes:
  - Priority inversion
  - Round-robin scheduling
- Prevention techniques:
  - Upper bound on priority
  - Priority scheduling

### Livelocks

- Problem: a situation where multiple processes are repeatedly switching between two or more states
- Causes:
  - Starvation
  - Mutual exclusion
- Prevention techniques:
  - Token passing
  - Bakery algorithm

### Starvation and Livelocks

- Comparison of starvation and livelocks
- Prevention techniques:
  - Round-robin scheduling
  - Resource allocation graphs

### Important Formulas and Definitions

- **Mutual Exclusion**: a situation where only one process can access a shared resource at a time
- **Lock**: a mechanism that allows only one process to access a shared resource
- **Token**: a mechanism that allows multiple processes to access a shared resource
- **Peterson's Algorithm**: a consensus protocol used to resolve conflicts in distributed systems
- **Bakery Algorithm**: a process scheduling algorithm used to resolve conflicts in distributed systems

### Important Theorems

- **Banker's Algorithm**: a deadlock detection and prevention algorithm
- **Resource Allocation Graph**: a graph used to model resource allocation in distributed systems
