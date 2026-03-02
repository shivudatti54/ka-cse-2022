# 9.4.2 Deadlocks

=====================================================

## Introduction

---

In a multi-process system, deadlocks are a phenomenon where two or more processes are blocked indefinitely, waiting for each other to release resources. This can lead to a system-wide failure and is considered a critical issue in operating system design.

## System Model

---

A system model is a representation of the operating system and its components. In the context of deadlocks, the system model is crucial in understanding the causes and effects of deadlocks.

### Process Model

- A process is a program in execution.
- A process has a unique process ID (PID) and identity.
- A process requests resources from the system.
- A process can send messages to other processes.

### Resource Model

- A resource is an object that can be allocated to a process.
- Resources can be divided into two categories:
  - Mutual Exclusion (M) resources: A process can't hold two or more M resources at the same time.
  - Shared Resources (S) resources: A process can hold multiple S resources simultaneously.
- Resources can be allocated using operating system services.

### Synchronization Model

- Synchronization is the mechanism by which processes interact with each other.
- Synchronization primitives include semaphores, monitors, and condition variables.

## Deadlock Characterization

---

A deadlock is characterized by the following properties:

### 1. Mutual Exclusion (M) resources are held by processes

- A deadlock occurs when two or more processes are blocked indefinitely, waiting for each other to release resources.
- M resources ensure that only one process can access a resource at a time.

### 2. Hold and Wait

- A process holds a resource and waits for another resource to be released.
- If a process is holding an M resource and waiting for an S resource, it is in a deadlock state.

### 3. No Preemption

- In a deadlock, the operating system cannot preempt the process holding a resource.
- Preemption allows the operating system to allocate resources to other processes.

### 4. Circular Wait

- In a deadlock, a process waits for a resource held by another process, which in turn waits for a resource held by another process, and so on.
- This creates a circular dependency between processes.

### Example

Suppose we have three processes - P1, P2, and P3 - and three resources - R1, R2, and R3.

| Process | Resource | Requesting Resource |
| ------- | -------- | ------------------- |
| P1      | R1       | R2                  |
| P2      | R2       | R3                  |
| P3      | R3       | R1                  |

In this scenario, P1 holds R1 and waits for R2, while P2 holds R2 and waits for R3. P3 holds R3 and waits for R1. This creates a circular wait, and the system is in a deadlock state.

## Methods for Handling Deadlocks

---

### 1. Avoid Deadlocks

- The best way to handle deadlocks is to avoid them altogether.
- To avoid deadlocks, follow these rules:
  - Acquire resources in the same order each time.
  - Always release resources as soon as possible.
  - Use locks to protect shared resources.

### 2. Detection and Recovery

- If deadlocks occur, detection and recovery mechanisms can be used to resolve the issue.
- Detection mechanisms include:
  - Deadlock detection algorithms.
  - Resource counting mechanisms.
- Recovery mechanisms include:
  - Process termination.
  - Resource allocation.
  - Rollback recovery.

### 3. Deadlock Prevention Algorithms

- Deadlock prevention algorithms can be used to prevent deadlocks from occurring in the first place.
- These algorithms include:
  - Banker's algorithm.
  - Dining philosophers algorithm.

## Conclusion

---

In conclusion, deadlocks are a critical issue in operating system design. Understanding the system model, deadlock characterization, and methods for handling deadlocks is essential for designing and implementing efficient operating systems. By avoiding deadlocks, detecting and recovering from them, and using deadlock prevention algorithms, we can ensure that our systems are reliable and efficient.
