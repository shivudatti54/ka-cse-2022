# **Methods for Handling Deadlocks**

### Introduction

Deadlocks are a problem in operating systems where two or more processes are blocked indefinitely, each waiting for the other to release a resource.

### Definition

- A deadlock is a situation where two or more processes are unable to proceed because each is waiting for the other to release a resource.

### Theorem

- **Deadlock Theorem**: A system is in a deadlock state if and only if there is a set of processes, each of which is waiting for some resource held by another process in the set.

### Methods for Handling Deadlocks

---

### 1. **Prevention**

- **Mutual Exclusion**: Ensure that only one process can access a resource at a time.
- **Resource Allocation**: Allocate resources in a way that minimizes the likelihood of deadlocks.

### 2. **Detection and Recovery**

- **Deadlock Detection Algorithm**: Detect deadlocks by monitoring the system for resource requests and releases.
- **Rollback Recovery**: Roll back the system to a previous state before a deadlock occurred.
- **Abort and Restart**: Abort the processes involved in the deadlock and restart the system.

### 3. **Avoidance**

- **Banker's Algorithm**: A dynamic algorithm that allocates resources to processes while preventing deadlocks.
- **Eisenberg's Algorithm**: A static algorithm that allocates resources to processes while preventing deadlocks.

### Important Formulas

- **Banker's Algorithm**: `A[i] = [d[i], m[i], w[i]]`, where `A[i]` is the available resources, `d[i]` is the demand of process `i`, `m[i]` is the maximum allocation of process `i`, and `w[i]` is the current allocation of process `i`.
- **Eisenberg's Algorithm**: `F = \sum_{i=1}^{n} a_{ij} * d_{j}`, where `F` is the available resource, `a_{ij}` is the allocation of resource `j` to process `i`, and `d_{j}` is the demand of process `j`.

### Important Definitions

- **Resource**: A quantity that can be allocated to a process.
- **Process**: A program in execution.
- **Deadlock**: A situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource.
