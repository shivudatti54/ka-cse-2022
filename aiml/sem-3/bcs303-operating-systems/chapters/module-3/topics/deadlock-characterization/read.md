# Deadlock Characterization

## Introduction

In modern operating systems, multiple processes frequently compete for limited resources such as printers, memory blocks, database locks, or CPU time. When processes hold some resources while waiting for others that are held by other processes, a dangerous situation can arise where no process can proceed. This situation is known as a DEADLOCK, and it represents one of the most challenging problems in concurrent programming and operating system design.

Deadlock characterization is the systematic process of understanding, identifying, and defining the precise conditions under which deadlocks occur in a computer system. Without proper characterization, detecting and resolving deadlocks becomes nearly impossible. The Coffman conditions, formulated by Edward G. Coffman Jr. in 1971, provide the foundational framework for characterizing deadlocks. These conditions are universally applicable across all operating systems and form the theoretical basis for deadlock prevention, avoidance, and detection algorithms studied in operating system courses at the University of Delhi.

Understanding deadlock characterization is essential for system administrators managing production servers, software developers writing concurrent applications, and computer science students preparing for competitive examinations and semester examinations. This topic carries significant weight in the DU syllabus, and students must master both the theoretical conditions and practical tools like resource allocation graphs to excel in their internal assessments and end semester examinations.

## Key Concepts

### Definition of Deadlock

A deadlock is a situation in which two or more processes are unable to proceed because each is waiting for a resource held by another process. More formally, a set of processes is in a deadlock state if every process in the set is waiting for an event that only another process in the set can cause. The events that processes wait for are typically the acquisition of resources. Consider a classic scenario: Process A holds Resource 1 and requests Resource 2, while Process B holds Resource 2 and requests Resource 1. Neither process can proceed, and the system grinds to a halt.

### The Four Coffman Conditions

A deadlock can occur if and only if all four conditions, known as the Coffman conditions, hold simultaneously in the system. These conditions were first published in 1971 and remain the cornerstone of deadlock theory.

**Mutual Exclusion Condition:** At least one resource must be held in a non-sharable mode. This means that only one process can use a particular resource at a time. Resources like printers, tape drives, and database locks exhibit this property. If resources could be simultaneously shared by all processes, deadlocks would not occur. For instance, read-only files can be shared by multiple processes simultaneously, making them non-controversial from a deadlock perspective.

**Hold and Wait Condition:** A process must be holding at least one resource and waiting to acquire additional resources that are currently held by other processes. This condition implies that processes do not release their currently held resources before requesting new ones. A process that acquires all required resources at once and then releases them would not participate in a deadlock. This is a critical condition because it creates the circular waiting pattern essential for deadlock formation.

**No Preemption Condition:** Resources cannot be preempted. That is, a resource can be released only voluntarily by the process holding it, not by external intervention. The operating system cannot forcibly take a printer from one process and give it to another. This condition distinguishes deadlocks from simple resource contention where the system can intervene. Some resources, like CPU time and memory, can be preempted, but physical devices like tape drives typically cannot.

**Circular Wait Condition:** There must be a circular chain of processes where each process is waiting for a resource held by the next process in the chain. If we construct a wait-for graph with processes as nodes and "process P is waiting for resource R held by process Q" as directed edges, a cycle in this graph indicates circular wait. This is the final condition that completes the deadlock formation.

### Resource Allocation Graph

The resource allocation graph (RAG) is a visual tool used to characterize deadlock situations in a system. It provides a pictorial representation of the current state of resource allocation and pending requests. The graph consists of two types of nodes: process nodes (represented by circles) and resource nodes (represented by squares). Each resource node contains small circles called instances, representing the number of identical copies of that resource available.

Edges in the graph are of two types. A request edge is a directed edge from a process node to a resource node, indicating that the process has requested but not yet acquired one instance of that resource. An assignment edge is a directed edge from a resource node to a process node, indicating that the process currently holds one instance of that resource.

A deadlock, if it exists, will always be accompanied by a cycle in the resource allocation graph. However, the presence of a cycle does not necessarily guarantee a deadlock. If each resource type has exactly one instance, then a cycle implies a definite deadlock. But when resource types have multiple instances, a cycle indicates potential deadlock but not certainty. Students must remember this crucial distinction for examination purposes.

### System Model for Deadlock Characterization

To formally characterize deadlocks, we consider a system with a finite set of processes and a finite set of resource types. Each resource type has multiple instances. The system model typically includes:

The process set P = {P1, P2, P3, ..., Pn} represents all processes in the system. The resource types are denoted as E = {R1, R2, R3, ..., Rm}, where each resource type Rk has Ck instances.

The system maintains two key data structures for characterization. The allocation matrix shows which resources are currently assigned to each process. The request matrix indicates which resources each process is currently waiting for. The state of the system at any time can be completely described by these matrices along with the total available resources of each type.

## Examples

### Example 1: Banker's Algorithm Scenario

Consider a system with three processes P1, P2, P3 and two resource types R1 (printers) and R2 (plotters), each with 2 instances. The current state is:

- P1 holds 1 instance of R1 and requests 1 instance of R2
- P2 holds 1 instance of R2 and requests 1 instance of R1
- P3 holds no resources and requests 1 instance of R1

Draw the resource allocation graph and identify if a deadlock exists.

**Solution:**

Step 1: Identify processes and resources
- Process nodes: P1, P2, P3
- Resource nodes: R1 (2 instances), R2 (2 instances)

Step 2: Draw assignment edges (resource to process)
- R1 → P1 (P1 holds 1 R1)
- R2 → P2 (P2 holds 1 R2)

Step 3: Draw request edges (process to resource)
- P1 → R2 (P1 requests 1 R2)
- P2 → R1 (P2 requests 1 R1)
- P3 → R1 (P3 requests 1 R1)

Step 4: Check for cycles
Looking at the graph, we can trace: P1 holds R1, requests R2; P2 holds R2, requests R1. This forms a cycle: P1 → R2 → P2 → R1 → P1.

Since each resource type has multiple instances, we need to verify if all conditions are met. With the current allocation, P1 and P2 are in a circular wait. P1 holds R1 and waits for R2; P2 holds R2 and waits for R1. The four Coffman conditions are satisfied, confirming deadlock between P1 and P2. P3 is not involved in the deadlock as it is not holding any resource while waiting.

### Example 2: Multiple Resource Instances Without Deadlock

Consider a similar system but with different allocation:
- P1 holds 1 R1, requests 1 R2
- P2 holds 1 R1, requests 1 R2
- R1 has 3 instances, R2 has 3 instances

**Solution:**

Step 1: Analyze the request and allocation
- P1: holds 1 R1, requests 1 R2
- P2: holds 1 R1, requests 1 R2
- Available: 2 R1, 2 R2

Step 2: Check circular wait
Although P1 and P2 both request R2 and both hold R1, there is no circular wait. P1 waits for R2, P2 waits for R2, but neither holds a resource the other wants. The wait-for graph shows both processes waiting on the same resource type, not on each other.

Step 3: Verify conditions
- Mutual exclusion: satisfied (R1 and R2 are non-sharable)
- Hold and wait: satisfied (both hold R1 while waiting for R2)
- No preemption: satisfied
- Circular wait: NOT satisfied

Since circular wait is not satisfied, no deadlock exists despite the cycle in the graph structure. Both processes can proceed if sufficient R2 instances become available. This example illustrates that cycles in resource allocation graphs with multiple instances only indicate potential deadlock.

### Example 3: Real-World Database Deadlock

Consider two transactions in a database system:
- Transaction T1: Locks Record A in exclusive mode, then attempts to lock Record B
- Transaction T2: Locks Record B in exclusive mode, then attempts to lock Record A

**Solution:**

Step 1: Map to resource allocation model
- Each database record is a resource with one instance (exclusive lock)
- Each transaction is a process

Step 2: Apply Coffman conditions
- Mutual Exclusion: satisfied (exclusive locks can only be held by one transaction)
- Hold and Wait: satisfied (T1 holds A while waiting for B; T2 holds B while waiting for A)
- No Preemption: satisfied (locks cannot be forcibly removed)
- Circular Wait: satisfied (T1 waits for T2 to release B; T2 waits for T1 to release A)

Step 3: Characterize the deadlock
The system enters a deadlock state. Database management systems typically implement deadlock detection by maintaining awaits-for graph (similar to resource allocation graph) and running detection algorithms periodically. When detected, one transaction is typically selected as victim and rolled back to break the deadlock.

## Exam Tips

For DU semester examinations, students should note the following important points:

The four Coffman conditions are mandatory and sufficient for deadlock formation. Remember them as MUTUAL EXCLUSION, HOLD AND WAIT, NO PREEMPTION, and CIRCULAR WAIT. A common examination question asks students to explain all four conditions with examples.

The resource allocation graph is a frequently examined topic. Remember the key rule: with single-instance resources, a cycle means definite deadlock; with multiple instances, a cycle means possible deadlock. Students should practice drawing and analyzing RAGs from allocation matrices.

Distinguish carefully between deadlock prevention and deadlock avoidance. Prevention eliminates one of the Coffman conditions, while avoidance uses algorithms like Banker's Algorithm to ensure safe states.

The Banker's Algorithm requires the system to maintain additional information about maximum possible resource needs. This algorithm is used for deadlock avoidance, not detection or prevention.

For cycle detection in RAGs, students should be able to trace paths manually. Remember that request edges point from process to resource, and assignment edges point from resource to process.

A deadlock is different from starvation. Deadlock involves circular waiting where no process can proceed. Starvation involves a process waiting indefinitely but not in a circular pattern, often due to priority issues.

The hold and wait condition can be eliminated by requiring processes to request all resources before starting (preventing hold) or by requiring processes to release resources before requesting new ones (preventing wait). These are prevention strategies.