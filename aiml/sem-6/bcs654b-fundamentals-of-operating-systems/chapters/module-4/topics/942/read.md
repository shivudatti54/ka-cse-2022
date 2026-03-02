# **9.4.2 Deadlocks: System Model**

## **Introduction**

Deadlocks are a type of failure in a multi-process system where each process is blocked indefinitely, waiting for another process to release a resource it needs. Deadlocks can occur in any system that uses multiple processes and shared resources.

## **Deadlock Characterization**

A deadlock is characterized by the following four conditions:

- **Mutual Exclusion**: Each process requires exclusive access to a common resource.
- **Hold and Wait**: A process is holding a resource and waiting for another resource it needs to complete its execution.
- **No Preemption**: The operating system does not preempt one process to give the resource to another process.
- **Circular Wait**: Each process is waiting for a resource held by another process.

## **Example of Deadlock**

Suppose we have three processes, P1, P2, and P3, and two resources, R1 and R2:

| Process | Resource 1 | Resource 2 |
| ------- | ---------- | ---------- |
| P1      | R1         | R2         |
| P2      | R2         | R1         |
| P3      | R1         | R2         |

If P1 requests R1, P2 requests R2, and P3 requests R1, a deadlock can occur:

- P1 holds R1 and waits for R2.
- P2 holds R2 and waits for R1.
- P3 holds R1 and waits for R2.
- Each process is waiting for a resource held by another process.

## **Deadlock Detection Algorithms**

There are several algorithms to detect deadlocks in a system:

- **Banker's Algorithm**: This algorithm uses a resource allocation matrix to detect deadlocks.
- **Dining Philosophers Problem**: This algorithm uses a circular wait to detect deadlocks.

## **Deadlock Prevention Algorithms**

There are several algorithms to prevent deadlocks in a system:

- **Resource Allocation Graph**: This algorithm uses a graph to model the resources and processes.
- **Round-Robin Scheduling**: This algorithm uses a round-robin scheduling algorithm to prevent deadlocks.

## **Deadlock Recovery Algorithms**

There are several algorithms to recover from deadlocks in a system:

- **Process Termination**: This algorithm terminates one process to recover from the deadlock.
- **Resource Preemption**: This algorithm preempts one process to recover from the deadlock.

## **Conclusion**

Deadlocks are a type of failure in a multi-process system where each process is blocked indefinitely, waiting for another process to release a resource it needs. Understanding deadlock characterization, deadlock detection algorithms, deadlock prevention algorithms, and deadlock recovery algorithms is crucial for designing and implementing robust operating systems.
