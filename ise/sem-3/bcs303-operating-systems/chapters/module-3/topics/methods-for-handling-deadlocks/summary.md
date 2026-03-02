# Methods for Handling Deadlocks

=====================================

### Definition

- A deadlock is a situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource.

### Theorem

- **Banker's Theorem**: If a system is deadlock-free, then for every resource, the number of processes requesting it must be less than or equal to the number of resources available.

### Methods for Handling Deadlocks

---

### 1. **Preemption**

- A process is interrupted and another process is given access to the resource it is waiting for.
- Formula: `P = (R1 - r1) * (R2 - r2) * ... * (Rn - rn)`

### 2. **Resource Preemption**

- All resources are allocated to one process, which is then allowed to proceed.
- Formula: `P = max(R1, R2, ..., Rn)`

### 3. **Rollback**

- When a deadlock is detected, the system reverts to the previous state.
- Formula: `P = (previous state)`

### 4. **Abort**

- A process is terminated and its resources are released.
- Formula: `P = (terminating process)`

### 5. **Deadlock Detection and Prevention Algorithms**

- **Banker's Algorithm**
  - Algorithm for preventing deadlocks using resource allocation and deallocation.
  - Formula: `R = (max(R1, R2, ..., Rn) - min(r1, r2, ..., rn))`
- **Woods Algorithm**
  - Algorithm for detecting deadlocks using resource allocation and deallocation.
  - Formula: `P = (deadlock detection)`

### 6. **Avoiding Deadlocks**

- Use algorithms like Banker's Algorithm to prevent deadlocks.
- Formula: `P = (preventing deadlock)`

Note: These formulas and definitions are key to understanding the methods for handling deadlocks in operating systems.
