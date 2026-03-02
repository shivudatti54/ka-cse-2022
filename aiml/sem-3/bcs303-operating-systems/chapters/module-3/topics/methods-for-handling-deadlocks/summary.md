# Methods for Handling Deadlocks

=====================================

## Key Concepts

### Definitions

- **Deadlock**: A situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource.
- **Resource**: A variable amount of a shared system resource that can be accessed by multiple processes.

### Important Formulas and Theorems

- **Banker's Algorithm**: A deadlock detection and prevention algorithm that uses a set of rules to prevent deadlocks.
- **Resource Allocation Graph (RAG)**: A graph that represents the resources and processes, used to detect deadlocks.

### Methods for Handling Deadlocks

#### 1. **Deadlock Detection and Prevention**

- **Banker's Algorithm**:
  - Algorithm 1: Deadlock detection
  - Algorithm 2: Deadlock prevention (using Resource Allocation Graph)
- **Resource Allocation**: Allocate resources to processes in a way that prevents deadlocks.

#### 2. **Restart, Abort, or Rollback Recovery**

- **Restart**: Restart the process that caused the deadlock.
- **Abort**: Abort the process that caused the deadlock.
- **Rollback**: Rollback the process that caused the deadlock to a previous safe state.

#### 3. **Priority Scheduling**

- **Dynamic Priority Scheduling**: Adjust the priority of processes based on the number of resources being held.
- **Fixed Priority Scheduling**: Assign a fixed priority to each process.

#### 4. **Resource Preemption**

- **Resource Preemption**: Preempt resources from a process to prevent deadlocks.

#### 5. **Timed Deadlock Detection**

- **Timed Deadlock Detection**: Detect deadlocks after a certain time period.

## Key Points

- Banker's Algorithm is a deadlock detection and prevention algorithm.
- Resource Allocation Graph is used to detect deadlocks.
- Deadlock detection and prevention can be achieved using algorithms and resource allocation techniques.
- Restart, abort, or rollback recovery can be used to recover from deadlocks.
- Priority scheduling and resource preemptive scheduling can be used to prevent deadlocks.
