# **Deadlocks: System Model**

## **Key Points**

- **Definition**: A deadlock is a situation in a computer system where two or more processes are blocked indefinitely, each waiting for the other to release a resource.
- **Characteristics**:
  - Mutual exclusion: Each process requires exclusive access to a resource.
  - Hold and wait: A process holds a resource and waits for another resource.
  - No preemption: The operating system cannot take a resource from a process.
  - Circular wait: Each process waits for a resource held by another process.
- **Types of Deadlocks**:
  - **Resource Deadlock**: When two processes are blocked, each waiting for a resource held by the other.
  - **Priority Ceiling Deadlock**: When the priority ceiling of a process is higher than the priority of the process holding a resource.

## **Important Concepts**

- **Banker's Algorithm**: A dynamic algorithm to prevent deadlocks by limiting the number of resources a process can request.
- **Resource Allocation Graph (RAG)**: A graph representation of resource allocation and request.
- **Deadlock Detection Algorithm**: An algorithm to detect deadlocks and find the deadlock threads.

## **Theorems**

- **Dining Philosophers Theorem**: If n>or= 2 philosophers, then there is a deadlock.
- **Banker's Theorem**: If the available resources are limited, then deadlock is avoided.

## **Formulas**

- **Banker's Algorithm Formula**: If r[i] is the number of resources requested by process i, and m[i] is the maximum number of resources that can be allocated to process i, then the safe sequence length is calculated using the formula: S = max (r[i] - m[i]) + 1
- **Dining Philosophers Formula**: If p[0] and p[1] are the two philosophers, and f[i] is the fork available at table i, then the time taken by philosopher i to finish eating is calculated using the formula: t[i] = max (f[i] - p[i], f[i] - p[i+1])

These key points, important concepts, theorems, and formulas are essential for quick revision before exams on deadlocks in system models.
