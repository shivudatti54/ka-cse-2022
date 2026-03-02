# Deadlock Detection and Recovery

### Introduction

- Deadlock: a situation where two or more processes are blocked indefinitely, waiting for each other to release resources.
- Deadlock can occur in a system with multiple processes and shared resources.

### Definitions

- **Resource**: a quantity or entity that can be used by multiple processes.
- **Process**: a program in execution.
- **Deadlock Detection**: identifying when a deadlock is occurring.
- **Deadlock Recovery**: restoring the system to a safe state after a deadlock has occurred.

### Key Concepts

- **Banker's Algorithm**: a deadlock detection and recovery algorithm.
- **Resource Allocation Graph (RAG)**: a graph representing resources and their availability.
- **Deadlock Detection Theorem**: a theorem stating that a deadlock can only occur if a process is holding a resource and requesting another resource that is also held by another process.

### Deadlock Detection Algorithms

- **Woods Algorithm**: a simple deadlock detection algorithm.
- **Lindholm Algorithm**: a more efficient deadlock detection algorithm.
- **Banker's Algorithm**: a deadlock detection and recovery algorithm.

### Deadlock Recovery Algorithms

- **Rollback Recovery**: restoring the system to a previous safe state.
- **Preemptive Rollback Recovery**: rolling back the current process to a previous safe state.
- **Process Termination**: terminating the processes involved in the deadlock.

### Important Formulas

- **Banker's Algorithm Formula**: a formula used in the Banker's Algorithm to calculate the availability of resources.
- **Deadlock Detection Formula**: a formula used in the Woods Algorithm to detect deadlocks.

### Theorems

- **Deadlock Detection Theorem**: a theorem stating that a deadlock can only occur if a process is holding a resource and requesting another resource that is also held by another process.
- **Banker's Algorithm Theorem**: a theorem stating that the Banker's Algorithm can detect and recover from deadlocks.

### Quick Revision Tips

- Understand the definitions of deadlock, process, resource, and Banker's Algorithm.
- Learn the key concepts of deadlock detection and recovery algorithms.
- Practice solving problems using the Banker's Algorithm and other deadlock detection and recovery algorithms.
