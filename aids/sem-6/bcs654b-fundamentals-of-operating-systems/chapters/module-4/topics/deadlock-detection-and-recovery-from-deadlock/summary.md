# **Deadlock Detection and Recovery from Deadlock**

### Definition and Key Concepts

- **Deadlock**: A situation where two or more processes are unable to proceed because each is waiting for the other to release a resource.
- **Resource**: A system object that can be accessed by multiple processes.
- **Hold and Wait**: A process is holding a resource and waiting for another resource.
- **No Preemption**: The operating system does not allow for preemption of one process by another.

### Deadlock Detection Methods

- **Banker's Algorithm**: A static prediction method that uses resource allocation matrices to detect deadlocks.
- **Widening Algorithm**: A dynamic detection method that uses a graph search algorithm to detect deadlocks.
- **Dining Philosophers Problem**: A classic synchronization problem that demonstrates the concept of deadlocks.

### Deadlock Recovery Methods

- **Process Termination**: Terminating one or more processes involved in the deadlock.
- **Resource Preemption**: Forcefully releasing a resource from a process involved in the deadlock.
- **Deadlock Detection and Rollback**: Detecting the deadlock and rolling back the transactions to a safe state.

### Important Formulas and Theorems

- **Banker's Algorithm Formula**: `A[i,j] = min (a[i,j], b[j,c], c[j,d])`
- **Liveway Theorem**: If `P1` is holding `R1` and waiting for `R2`, then either `P1` will be released or another process will hold `R2` and wait for `R1`.
- **Ferrante's Theorem**: If `P1` is holding `R1` and waiting for `R2`, then either `P1` will be released or a deadlock will occur.

### Important Definitions

- **Critical Section**: A section of code that accesses shared resources.
- **Semaphore**: A variable that controls access to a shared resource.
- **Monotonic Algorithm**: An algorithm that ensures that the number of processes entering a critical section never increases.

### Key Points

- Deadlock detection and recovery are crucial in ensuring the stability of a system.
- Banker's algorithm and widening algorithm are common deadlock detection methods.
- Process termination and resource preemption are common deadlock recovery methods.
- The Liveway Theorem and Ferrante's Theorem provide insight into deadlock detection.
