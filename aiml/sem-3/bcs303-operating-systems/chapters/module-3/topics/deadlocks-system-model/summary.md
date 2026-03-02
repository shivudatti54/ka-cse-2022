# **Deadlocks: System Model**

## **Key Concepts**

- A deadlock is a situation in which two or more processes are unable to proceed because each is waiting for the other to release a resource.
- Deadlocks can occur when multiple processes are competing for a set of resources.

## **Types of Deadlocks**

- **Resource Deadlock**: A deadlock where processes are competing for resources.
- **Starvation**: When a process is unable to get a resource it needs, even though it has been available for a long time.

## **Deadlock Detection and Prevention**

- **Deadlock Detection**: Techniques used to identify deadlocks in a system.
  - **Banker's Algorithm**: A deadlock detection algorithm that uses a set of resource availability matrices to detect deadlocks.
  - **Wait-for Graph**: A graph-based algorithm that represents the dependencies between processes and resources to detect deadlocks.
- **Deadlock Prevention**: Techniques used to prevent deadlocks from occurring in a system.
  - **Resource Ordering**: Ordering the allocation and deallocation of resources to prevent deadlocks.
  - **Resource Preemption**: Preempting a process if it is detected to be in a deadlock situation.

## **Deadlock Resolution**

- **Abort**: Terminating a process that is involved in a deadlock.
- **Rollback**: Rolling back to a previous state to avoid a deadlock.
- **Priority Inheritance**: Inheriting the priority of the process holding the resource, allowing the process to proceed.

## **Important Formulas and Definitions**

- **Banker's Algorithm Formula**: `M[i][j] - A[j] >= 0` for each resource `r_j` and process `p_i`, where `M[i][j]` is the available amount of resource `r_j` for process `p_i`, and `A[j]` is the allocated amount of resource `r_j`.
- **Wait-for Graph Formula**: A graph where each node represents a process, and each edge between two nodes represents a dependency between the two processes.

## **Key Theorems**

- **Termination Theorem**: A system will terminate if it does not contain a deadlock.
- **Safety Theorem**: A system is safe if it does not contain a deadlock.
