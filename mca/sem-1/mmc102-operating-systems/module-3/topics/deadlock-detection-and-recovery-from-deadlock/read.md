# Deadlock Detection And Recovery From Deadlock


## Table of Contents

- [Deadlock Detection And Recovery From Deadlock](#deadlock-detection-and-recovery-from-deadlock)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Resource Allocation Graph (RAG)](#resource-allocation-graph-rag)
  - [Wait-For Graph](#wait-for-graph)
  - [Deadlock Detection Algorithm](#deadlock-detection-algorithm)
  - [Banker's Algorithm for Detection](#bankers-algorithm-for-detection)
  - [Recovery Strategies](#recovery-strategies)
- [Examples](#examples)
  - [Example 1: Resource Allocation Graph Cycle Detection](#example-1-resource-allocation-graph-cycle-detection)
  - [Example 2: Deadlock Detection Algorithm Execution](#example-2-deadlock-detection-algorithm-execution)
  - [Example 3: Recovery Through Process Termination](#example-3-recovery-through-process-termination)
- [Exam Tips](#exam-tips)

## Introduction

Deadlock is one of the most challenging problems in operating system design, representing a situation where two or more processes are unable to proceed because each is waiting for resources held by the other. While prevention and avoidance techniques aim to ensure deadlocks never occur, deadlock detection and recovery operates on a different philosophy: allow deadlocks to potentially occur, but periodically check for their presence and then take corrective action when detected. This approach is particularly suitable for systems where the cost of maintaining deadlock-free operation (in terms of resource utilization and throughput) is too high, or where deadlocks are relatively rare but must be handled when they occur.

In modern operating systems, deadlock detection is implemented through sophisticated algorithms that analyze resource allocation patterns. The Resource Allocation Graph (RAG) provides a powerful visual and mathematical tool for detecting cycles that indicate deadlock conditions. When a deadlock is detected, the system must employ recovery strategies to break the deadlock and restore normal operation. These recovery mechanisms range from simple process termination to complex resource preemption with checkpointing and rollback capabilities. Understanding these detection and recovery mechanisms is essential for system administrators and software engineers who design and manage multi-process systems, database management systems, and distributed computing platforms.

## Key Concepts

### Resource Allocation Graph (RAG)

The Resource Allocation Graph is a directed bipartite graph that models the allocation state of all resources in the system. The graph consists of two sets of vertices: process vertices (represented as circles) and resource vertices (represented as squares). Each resource vertex contains dots equal to the number of instances of that resource type in the system. Edges in the graph are of two types: request edges (process to resource) and assignment edges (resource to process). A request edge indicates that a process has requested a resource instance but has not yet acquired it, while an assignment edge indicates that a resource instance has been allocated to a process.

The critical theorem for RAG analysis states that a deadlock exists in the system if and only if the RAG contains a cycle. However, this holds true only when each resource type has exactly one instance. When resource types have multiple instances, a cycle in the RAG is necessary but not sufficient for deadlock existence; in such cases, every process in the cycle must be waiting for a resource held by another process in the cycle.

### Wait-For Graph

The Wait-For Graph is a simplified variant of the Resource Allocation Graph that focuses solely on process dependencies. It is derived from the RAG by removing all resource nodes and connecting processes directly based on their waiting relationships. Specifically, if process Pi is waiting for a resource held by process Pj, there exists a directed edge from Pi to Pj in the Wait-For Graph. A deadlock exists if and only if the Wait-For Graph contains a cycle. The Wait-For Graph is particularly useful because it provides a cleaner representation of deadlock conditions, making cycle detection more straightforward.

### Deadlock Detection Algorithm

The deadlock detection algorithm operates under the assumption that the system allows processes to request resources dynamically. The algorithm maintains data structures including an available vector (number of available instances of each resource type), an allocation matrix (resources currently allocated to each process), and a request matrix (current requests from each process). The algorithm proceeds in steps: first, it initializes a work vector equal to the available vector and sets all processes as unmarked. Then, it repeatedly finds an unmarked process whose request matrix is less than or equal to the work vector. When such a process is found, the algorithm pretends to allocate all requested resources to that process, adds its allocated resources to the work vector, and marks the process as completed. This process continues until no more processes can be marked. Any unmarked processes remaining at the end are deadlocked.

### Banker's Algorithm for Detection

While the Banker's Algorithm is traditionally used for deadlock avoidance, it can be adapted for deadlock detection by treating the current state as if a resource request has been made. The detection variant checks whether granting the maximum requested resources to all processes would lead to a safe state. If no safe sequence exists, the current state contains deadlock. This approach is computationally more expensive than the standard detection algorithm but provides additional safety guarantees.

### Recovery Strategies

When deadlock is detected, the system must employ recovery mechanisms to break the deadlock. There are three primary approaches:

**Process Termination**: This strategy involves terminating one or more processes involved in the deadlock. Abortive recovery can be implemented through two methods: terminating all deadlocked processes (simplest but most expensive) or terminating processes one at a time until the deadlock is resolved. The choice of which process to terminate depends on factors such as process priority, execution time remaining, resources held, and whether the process can be rolled back easily. Terminating a process releases all its held resources, potentially breaking the deadlock cycle.

**Resource Preemption**: This approach involves preempting (taking away) resources from deadlocked processes and allocating them to other processes. The key challenges in resource preemption include selecting which resources to preempt and which processes should be victims. The system must also handle the issue of rollbacks, as preempted processes may need to return to a previous safe state. Depending on the resource type, preemption may be straightforward (for memory, CPU) or very difficult (for printers, tape drives).

**Rollback and Checkpointing**: In sophisticated systems, processes are periodically checkpointed, saving their complete state including register values, memory contents, and resource allocations. When deadlock is detected, the system can roll back one or more processes to a previous checkpoint, effectively freeing their allocated resources. This approach requires significant system overhead for maintaining checkpoints but provides a more graceful recovery mechanism than simple termination.

## Examples

### Example 1: Resource Allocation Graph Cycle Detection

Consider a system with three processes P1, P2, and P3, and two resource types R1 (with 1 instance) and R2 (with 1 instance). The current allocation state is: P1 holds R1 and requests R2, P2 holds R2 and requests R1, P3 holds no resources. Draw the RAG and identify if deadlock exists.

**Solution**: The RAG shows assignment edge from R1 to P1, request edge from P1 to R2, assignment edge from R2 to P2, and request edge from P2 to R1. This creates a cycle: P1 → R2 → P2 → R1 → P1. Since each resource type has exactly one instance and a cycle exists in the RAG, deadlock is present involving processes P1 and P2. Process P3 is not part of the deadlock.

### Example 2: Deadlock Detection Algorithm Execution

Consider a system with 3 processes and 2 resource types with the following state:

Available: A=3, B=3
Allocation: P1(A=2,B=1), P2(A=0,B=0), P3(A=2,B=0)
Request: P1(A=1,B=0), P2(A=0,B=1), P3(A=1,B=0)

Apply the deadlock detection algorithm.

**Solution**: Initialize Work = (3,3), all processes unmarked.

Step 1: Find unmarked process with Request ≤ Work.
- P1: Request(1,0) ≤ Work(3,3)? YES
- Mark P1, Work = Work + Allocation(P1) = (3,3) + (2,1) = (5,4)

Step 2: Find unmarked process with Request ≤ Work.
- P2: Request(0,1) ≤ Work(5,4)? YES
- Mark P2, Work = Work + Allocation(P2) = (5,4) + (0,0) = (5,4)

Step 3: Find unmarked process with Request ≤ Work.
- P3: Request(1,0) ≤ Work(5,4)? YES
- Mark P3, Work = Work + Allocation(P3) = (5,4) + (2,0) = (7,4)

All processes are marked. NO DEADLOCK exists in this system.

### Example 3: Recovery Through Process Termination

Assume deadlock exists with two processes P1 and P2, each holding one resource and waiting for the other. If the system decides to terminate P1 to break the deadlock, describe the recovery process.

**Solution**: When P1 is terminated, the operating system performs the following actions: first, it removes P1 from all waiting queues and cancels any pending I/O operations. Second, it releases all resources held by P1 (in this case, one resource instance). Third, the released resource becomes available and can be allocated to P2, which then completes its execution. The system must also perform cleanup operations including removing process control block, deallocating memory pages, and closing file descriptors. P2 can now acquire the needed resource and proceed to completion, at which point it releases all its resources. The system returns to a deadlock-free state.

## Exam Tips

For DU semester examinations, focus on these key areas:

1. RAG and Wait-For Graph construction and cycle detection are frequently tested. Remember that for single-instance resources, a cycle in RAG directly indicates deadlock.

2. The deadlock detection algorithm is computation-intensive but straightforward. Practice the step-by-step execution with different system states to gain speed and accuracy.

3. Understand the difference between deadlock prevention, avoidance, and detection. Detection allows deadlocks but finds them; avoidance predicts and prevents them before they occur.

4. Recovery strategies are often asked in exam questions. Be prepared to compare process termination, resource preemption, and rollback approaches with their advantages and disadvantages.

5. Time complexity of deadlock detection using RAG is O(n²) where n is the number of processes, because detecting cycles in a graph with n vertices requires O(n²) operations.

6. Remember that multiple instances of resource types require the more general detection algorithm, not just cycle detection in RAG.

7. The Banker's Algorithm can be used for detection by checking if the current state is safe. This is a common exam question variant.

8. Be careful with terminology: "deadlock detection" checks for existing deadlocks, while "deadlock avoidance" prevents deadlocks from occurring.