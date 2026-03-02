# Deadlock Characterization

## Introduction

Deadlock is one of the most challenging problems in operating system design and concurrent programming. It represents a situation where two or more processes are permanently blocked, each waiting for a resource that another process holds. Unlike other system problems that can be resolved through simple intervention, deadlocks create a circular waiting condition that brings computation to a grinding halt unless external intervention occurs.

Understanding deadlock characterization is fundamental for computer science students because modern computing environments increasingly involve concurrent processes competing for limited resources. From database management systems to distributed applications, deadlocks can cause system crashes, data inconsistency, and severe performance degradation. The University of Delhi curriculum emphasizes this topic because system administrators and software developers must be equipped to identify, prevent, and resolve deadlock situations in real-world scenarios. This chapter explores the precise conditions that characterize deadlocks, the system model underlying deadlock formation, and the mathematical characterization that helps us understand when and how deadlocks occur.

## Key Concepts

### Definition of Deadlock

A deadlock is a state where a set of processes are permanently blocked because each process is waiting for a resource that is held by another process in the same set. Consider a simple scenario: Process P1 holds Resource R1 and requests Resource R2, while Process P2 holds Resource R2 and requests Resource R1. Both processes will wait forever—THIS IS A DEADLOCK. The processes cannot proceed because the circular waiting condition cannot be broken without external intervention.

### The System Model

To understand deadlock characterization, we must first understand the system model. In any computing system, processes require access to resources to complete their tasks. Resources can be of two types:

PREEMPTIBLE RESOURCES: These can be taken away from a process without causing problems. Examples include memory space and CPU time. The operating system can reclaim these resources forcefully.

NON-PREEMPTIBLE RESOURCES: These cannot be taken away from a process while the process is using them. Examples include printers, CD drives, and database locks. Forcing these resources away from a process may cause computational errors or system instability.

Processes request resources, use them, and then release them. The typical lifecycle involves three states: requesting, using, and releasing. A deadlock occurs when processes hold resources while waiting for additional resources held by others.

### The Four Necessary Conditions (Coffman Conditions)

In 1971, Edward Coffman identified four necessary conditions that MUST all hold true for a deadlock to occur. These are called the Coffman Conditions:

MUTUAL EXCLUSION: At least one resource must be held in a non-sharable mode. If a resource can be shared, processes would not need to wait for exclusive access. For instance, only one process can use a printer at a time—this creates the potential for deadlock.

HOLD AND WAIT: A process must be holding at least one resource while waiting to acquire additional resources that are currently held by other processes. The process holds its currently allocated resources while simultaneously requesting new ones.

NO PREEMPTION: Resources cannot be preempted—they cannot be forcibly taken away from a process. The operating system cannot simply reclaim a printer allocated to Process P1 and give it to Process P2. The process must voluntarily release the resource.

CIRCULAR WAIT: There must be a circular chain of processes where each process is waiting for a resource held by the next process in the chain. If P1 is waiting for a resource held by P2, P2 is waiting for a resource held by P3, and so on, until Pn is waiting for a resource held by P1, we have circular wait.

THESE FOUR CONDITIONS ARE NECESSARY BUT NOT SUFFICIENT. Their presence indicates potential for deadlock, not certainty of deadlock.

### Resource Allocation Graph

The Resource Allocation Graph (RAG) is a visual tool used to represent the state of the system and determine whether a deadlock exists. This directed graph consists of two types of nodes:

Process nodes: Represented by circles (P1, P2, P3, ...)

Resource nodes: Represented by squares with dots inside, where each dot represents an instance of that resource type (R1, R2, R3, ...)

The graph contains two types of edges:

Request edge: Directed from process to resource (P → R) indicating the process is waiting for that resource

Assignment edge: Directed from resource instance to process (R → P) indicating the resource is currently allocated to that process

A DEADLOCK EXISTS IF AND ONLY IF THE RESOURCE ALLOCATION GRAPH CONTAINS A CYCLE AND AT LEAST ONE RESOURCE INSTANCE PER RESOURCE TYPE IN THE CYCLE IS NON-SHARABLE. If all resources in the cycle have multiple instances, a cycle does not necessarily indicate deadlock—it might just indicate competing processes that can still proceed.

### State Transition Diagram

System states can be classified into three categories:

SAFE STATE: A state where there exists a sequence of process executions (called a safe sequence) that allows all processes to complete without deadlock. The system can guarantee all processes will finish even if all their requested resources are granted immediately.

UNSAFE STATE: A state where no safe sequence exists. An unsafe state does NOT mean deadlock is imminent—it means deadlock is POSSIBLE. The system might avoid deadlock through lucky timing, or deadlock might occur.

DEADLOCK STATE: An actual deadlock has occurred. Processes are permanently blocked.

The transition from safe to unsafe to deadlock represents increasing severity. The goal of deadlock avoidance algorithms is to keep the system in safe states.

## Examples

### Example 1: Two Processes and Two Resources

Consider a system with two printers (R1) and two plotters (R2). Process P1 requests Printer 1 and gets it, then requests Plotter 1. Process P2 requests Plotter 1 and gets it, then requests Printer 1.

Using the Resource Allocation Graph:
- Assignment edge: R1-instance → P1 (printer allocated to P1)
- Assignment edge: R2-instance → P2 (plotter allocated to P2)
- Request edge: P1 → R2 (P1 waiting for plotter)
- Request edge: P2 → R1 (P2 waiting for printer)

The graph shows a cycle: P1 → R2 → P2 → R1 → P1

Each resource type has exactly one instance, so THIS CYCLE REPRESENTS A DEADLOCK. Both processes will wait forever.

### Example 2: Banker's Algorithm Scenario

Suppose a system has 5 processes (P0 to P4) and 3 resource types (A=10, B=5, C=7).

Current allocation:
- P0: (3, 2, 2)
- P1: (1, 0, 3)
- P2: (2, 1, 1)
- P3: (3, 1, 4)
- P4: (2, 2, 1)

Current need:
- P0: (2, 1, 1)
- P1: (3, 2, 2)
- P2: (3, 1, 2)
- P3: (1, 1, 1)
- P4: (2, 2, 2)

Available resources: (2, 1, 1)

To check if this is a safe state, we find a safe sequence. Starting with available (2, 1, 1):
- P3 needs (1, 1, 1), which is ≤ available. Grant P3. After P3 completes, available becomes (2+3, 1+1, 1+4) = (5, 2, 5)
- P0 needs (2, 1, 1), which is ≤ available. Grant P0. Available becomes (7, 3, 6)
- P1 needs (3, 2, 2), which is ≤ available. Grant P1. Available becomes (8, 3, 9)
- P2 needs (3, 1, 2), which is ≤ available. Grant P2. Available becomes (10, 4, 10)
- P4 needs (2, 2, 2), which is ≤ available. Grant P4. Available becomes (12, 6, 11)

Safe sequence: P3 → P0 → P1 → P2 → P4

This is a SAFE STATE because we found a sequence where all processes can complete.

### Example 3: Violation of Coffman Conditions

Scenario: A system with one printer and multiple processes attempting to use it.

Condition 1 (Mutual Exclusion): TRUE - Only one process can use the printer at a time.

Condition 2 (Hold and Wait): Can we prevent this? YES. If processes request all resources before starting (pre-allocation), no process holds resources while waiting. This is deadlock prevention.

Condition 3 (No Preemption): Can we preempt? YES. If the operating system can take the printer away and give it to another process after timeout, deadlock can be prevented.

Condition 4 (Circular Wait): Can we prevent this? YES. If we impose a total ordering on resource requests (all processes must request R1 before R2), circular wait cannot occur.

By violating ANY ONE of the four conditions, we can PREVENT deadlocks entirely.

## Exam Tips

FOR YOUR DU SEMESTER EXAMS, REMEMBER THESE CRITICAL POINTS:

1. THE FOUR COFFMAN CONDITIONS ARE NECESSARY BUT NOT SUFFICIENT—all four must be present for deadlock to exist.

2. IN THE RESOURCE ALLOCATION GRAPH, A CYCLE INDICATES DEADLOCK ONLY if each resource type in the cycle has exactly ONE instance. With multiple instances, a cycle might be safe.

3. UNDERSTAND THE DIFFERENCE BETWEEN PREEMPTIBLE AND NON-PREEMPTIBLE RESOURCES—this determines whether certain deadlock handling techniques apply.

4. SAFE STATE ≠ NO DEADLOCK—it means deadlock can be avoided with proper resource allocation. Unsafe state ≠ deadlock—it means deadlock is possible.

5. TO PREVENT DEADLOCK, VIOLATE ANY ONE OF THE FOUR COFFMAN CONDITIONS. Common approaches: eliminate hold and wait by requiring all resources upfront; allow preemption; impose resource ordering to eliminate circular wait.

6. THE BANKER'S ALGORITHM REQUIRES KNOWING THE MAXIMUM NEED OF EACH PROCESS IN ADVANCE—this is rarely practical in real systems.

7. WHEN DRAWING RESOURCE ALLOCATION GRAPHS, ALWAYS distinguish between request edges (process to resource) and assignment edges (resource to process).

8. MEMORIZE THE FOUR CONDITIONS USING THIS AID: M-H-N-C (Mutual Exclusion, Hold and Wait, No Preemption, Circular wait).