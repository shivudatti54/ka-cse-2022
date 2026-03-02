# **Deadlocks: System Model**

## **Introduction**

In operating systems, a deadlock is a situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource. This can lead to a system crash or other undesirable consequences. In this study material, we will explore the concept of deadlocks, its types, and how to detect and prevent them.

## **Definition**

A deadlock is a situation where two or more processes are blocked indefinitely, each waiting for the other to release a resource. This creates a cycle of waiting, where each process is waiting for a resource held by another process, which in turn is waiting for a resource held by the first process.

## **Types of Deadlocks**

- **Resource Deadlock**: This occurs when two or more processes are waiting for each other to release a resource.
- **Longest Job First (LJF) Deadlock**: This occurs when a process is waiting for a resource held by another process, which is waiting for a resource held by the first process.
- **Priority Ceiling Protocol (PCP) Deadlock**: This occurs when a process is waiting for a resource held by another process, which has a higher priority than the first process.

## **Characteristics of Deadlocks**

- **Cycle of Waiting**: Deadlocks occur when two or more processes are waiting for each other to release a resource.
- **Mutual Exclusion**: Deadlocks occur when two or more processes require access to the same resource.
- **Hold and Wait**: Deadlocks occur when a process holds a resource and waits for another resource held by another process.
- **No Preemption**: Deadlocks occur when the operating system cannot preempt one process to release a resource to another process.

## **Deadlock Detection Algorithms**

There are several algorithms used to detect deadlocks, including:

- **Werner's Test**: This algorithm checks if a process is holding a resource and waiting for another resource held by another process.
- **Banker's Algorithm**: This algorithm checks if a process can acquire all the resources it needs to run without deadlocking.
- **Dining Philosophers Algorithm**: This algorithm checks if a process can acquire all the resources it needs to run without deadlocking.

## **Deadlock Prevention Algorithms**

There are several algorithms used to prevent deadlocks, including:

- **Circular Wait Algorithm**: This algorithm checks if two or more processes are waiting for each other to release a resource.
- **Resource Ordering Algorithm**: This algorithm checks if a process can acquire all the resources it needs to run without deadlocking.
- **Priority Ceiling Protocol (PCP) Algorithm**: This algorithm checks if a process can acquire all the resources it needs to run without deadlocking.

## **Example**

Suppose we have three processes, P1, P2, and P3, each requiring two resources, R1 and R2. The process allocation matrix is as follows:

|     | P1  | P2  | P3  |
| --- | --- | --- | --- |
| R1  | 1   | 0   | 0   |
| R2  | 0   | 1   | 0   |

If P2 requests R1 and P1 requests R2, a deadlock occurs because P2 is waiting for R1 held by P1, and P1 is waiting for R2 held by P2.

## **Conclusion**

In this study material, we have explored the concept of deadlocks, its types, characteristics, and detection and prevention algorithms. Understanding deadlocks is crucial for designing and implementing efficient operating systems.
