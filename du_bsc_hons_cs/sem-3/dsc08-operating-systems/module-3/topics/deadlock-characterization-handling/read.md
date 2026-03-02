# Deadlock: Characterization and Handling

## Introduction

In modern computer systems, multiple processes compete for limited resources such as CPU time, memory, printers, scanners, and file locks. When processes are granted exclusive access to these resources, a dangerous situation can arise where two or more processes are waiting indefinitely for each other to release resources. This situation is known as a **deadlock**, and it represents one of the most challenging problems in operating system design and concurrent programming.

Deadlocks are particularly prevalent in multi-process environments where resource sharing is essential. Consider a scenario where two database transactions need to update multiple tables. If transaction A holds a lock on table 1 while waiting for a lock on table 2, and transaction B holds a lock on table 2 while waiting for a lock on table 1, both transactions will wait forever. This is a classic deadlock situation that can bring database operations to a halt.

Understanding deadlock characterization and handling is crucial for several reasons. First, deadlocks degrade system performance and responsiveness, leading to frustrated users and potential financial losses in commercial systems. Second, detecting and recovering from deadlocks requires careful system design and implementation. Third, as systems become increasingly concurrent and distributed, the probability of deadlocks increases exponentially. For DU students preparing for semester examinations, this topic carries significant weight, with questions frequently appearing in both theoretical and problem-solving sections.

## System Model and Deadlock Fundamentals

### What is a Deadlock?

A deadlock is a state where a set of processes are permanently blocked because each process is waiting for a resource that is held by another process in the set. The processes are stuck in a circular wait condition, with none able to proceed without external intervention.

In formal terms, a deadlock occurs when there is a circular wait chain of processes such that each process in the chain is waiting for a resource held by the next process in the chain. The operating system's resource allocation mechanism must handle these situations gracefully.

### Types of Resources

Resources in a computer system can be classified into two categories:

1. **Preemptible Resources**: These can be taken away from a process without causing problems. Examples include CPU time and memory. The operating system can typically reclaim these resources.

2. **Non-Prememptible Resources**: These cannot be taken away from a process while it is using them. Examples include printers, scanners, and file locks. If a process has been allocated a non-preemptible resource, the system must wait for the process to explicitly release it.

Deadlocks typically involve non-preemptible resources, as preemptible resources can be reallocated to break circular wait conditions.

## Deadlock Characterization: The Four Necessary Conditions

For a deadlock to occur in a system, all four of the following conditions, known as the Coffman conditions, must hold simultaneously. These conditions were first described by Coffman in 1971 and remain the foundational framework for deadlock analysis.

### 1. Mutual Exclusion Condition

At least one resource must be held in a non-sharable mode. If a resource can be shared, multiple processes could access it simultaneously without waiting. For instance, a printer can handle only one print job at a time, creating a mutual exclusion scenario. Similarly, a database row with an exclusive lock can be modified by only one transaction at a time.

This condition is inherent in many system resources. Some resources, like read-only files, can be shared, but when exclusive access is required (such as for writing), mutual exclusion becomes necessary.

### 2. Hold and Wait Condition

A process must be holding at least one resource and waiting to acquire additional resources that are currently held by other processes. This means the process does not release its current resources while waiting for others.

In practical terms, this is seen when a process requests multiple resources and gets some but waits for the remaining ones. For example, a process might acquire a file lock and then request a printer, holding the file lock while waiting for printer access.

### 3. No Preemption Condition

Resources cannot be preempted; that is, a resource cannot be forcibly taken away from a process. The process must explicitly release the resource. The operating system cannot simply reclaim a printer allocated to a process, nor can it force-release a database lock.

This condition makes deadlock handling challenging because the system cannot intervene to break the circular wait by forcibly taking resources away from processes.

### 4. Circular Wait Condition

There must be a circular chain of processes where each process is waiting for a resource held by the next process in the chain. This creates a cycle in the wait-for graph.

For example, if Process P1 holds Resource R1 and waits for Resource R2 held by Process P2, and Process P2 holds Resource R2 and waits for Resource R1 held by Process P1, a circular wait exists.

**Crucially, all four conditions must be present for a deadlock to occur. If even one condition is violated, deadlock cannot happen.**

## Resource Allocation Graph (RAG)

The Resource Allocation Graph is a visual tool used to represent the current state of resource allocation in the system. It helps in understanding whether a deadlock exists or may occur.

### Graph Components

The graph consists of two types of vertices:
- **Process vertices**: Represented by circles (P1, P2, ..., Pn)
- **Resource vertices**: Represented by squares (R1, R2, ..., Rm)

Edges in the graph include:
- **Request edge**: Directed edge from process to resource (P → R) indicating the process has requested the resource
- **Assignment edge**: Directed edge from resource to process (R → P) indicating the resource is currently allocated to the process

### Using RAG for Deadlock Detection

A key theorem in deadlock theory states: **If the Resource Allocation Graph contains no cycle, then no deadlock exists. If a cycle exists, a deadlock may or may not exist depending on the resource instances.**

Consider a simple example with two processes P1 and P2, and two resources R1 and R2, each with one instance. If there is an assignment edge from R1 to P1, a request edge from P1 to R2, an assignment edge from R2 to P2, and a request edge from P2 to R1, a cycle exists (P1 → R2 → P2 → R1 → P1). This indicates a deadlock.

However, if a resource has multiple instances, a cycle does not necessarily imply deadlock. For instance, if R1 has two instances and the allocation forms a cycle, deadlock might not occur because one instance might remain available.

## Methods for Handling Deadlocks

Operating systems employ several strategies to deal with deadlocks, each with its own advantages and trade-offs.

### Deadlock Prevention

Deadlock prevention involves ensuring that at least one of the four necessary conditions cannot hold. This eliminates the possibility of deadlock entirely.

**Attacking Mutual Exclusion**: Some resources can be made shareable. For example, read operations on files can be shared, but this doesn't work for resources requiring exclusive access.

**Attacking Hold and Wait**: Processes can be required to request all resources before starting execution. However, this leads to poor resource utilization since resources may remain allocated but unused for long periods. Alternatively, a process can be required to release all held resources before requesting new ones.

**Attacking No Preemption**: If a process holding certain resources requests another resource that cannot be immediately allocated, all its currently held resources are preempted. This approach is practical for some resources like CPU and memory but difficult for printers and other non-preemptible devices.

**Attacking Circular Wait**: Impose a total ordering of resource types and require that processes request resources in increasing order. This prevents circular wait because a process cannot request a lower-numbered resource while holding a higher-numbered one.

### Deadlock Avoidance

Deadlock avoidance allows the four necessary conditions but carefully manages resource allocation to ensure the system never enters an unsafe state. The most famous avoidance algorithm is the **Banker's Algorithm**.

#### Banker's Algorithm

The Banker's Algorithm, developed by Dijkstra in 1965, simulates resource allocation with a "what-if" analysis before actually allocating resources. It ensures the system always remains in a safe state—a state where there exists a sequence of process execution (safe sequence) that allows all processes to complete without deadlock.

**Key Data Structures**:
- **Available**: Vector indicating the number of available resources of each type
- **Maximum**: Matrix indicating the maximum demand of each process for each resource type
- **Allocation**: Matrix indicating currently allocated resources to each process
- **Need**: Matrix calculated as Maximum - Allocation, indicating remaining resource needs

**Safety Algorithm**:
1. Initialize Work = Available and Finish[i] = false for all processes
2. Find an process i such that Finish[i] = false and Need[i] ≤ Work
3. If found, update Work = Work + Allocation[i] and Finish[i] = true, then go to step 2
4. If all Finish[i] = true, the system is in a safe state

#### Worked Example

Consider a system with 3 processes (P0, P1, P2) and 3 resource types (A=10, B=5, C=7).

**Initial State**:
```
Maximum:
P0: A=7, B=5, C=3
P1: A=3, B=2, C=2
P2: A=9, B=0, C=2

Allocation:
P0: A=0, B=1, C=2
P1: A=2, B=0, C=0
P2: A=3, B=0, C=2

Available: A=5, B=3, C=3
```

**Step 1**: Calculate Need matrices (Maximum - Allocation)
```
Need:
P0: A=7, B=4, C=1
P1: A=1, B=2, C=2
P2: A=6, B=0, C=0
```

**Step 2**: Check safety. Find P1 where Need ≤ Available:
- P1 needs (1,2,2), Available is (5,3,3) → OK
- After P1 completes: Available = (5,3,3) + (2,0,0) = (7,3,3)
- Mark P1 as complete

**Step 3**: Find next process. Check P0: Need (7,4,1) ≤ Available (7,3,3)? No. Check P2: Need (6,0,0) ≤ Available (7,3,3)? Yes.
- After P2 completes: Available = (7,3,3) + (3,0,2) = (10,3,5)
- Mark P2 as complete

**Step 4**: Now check P0: Need (7,4,1) ≤ Available (10,3,5)? Yes.
- After P0 completes: Available = (10,3,5) + (0,1,2) = (10,4,7)
- Mark P0 as complete

**Result**: Safe sequence is P1 → P2 → P0. The system is in a safe state.

Now, if P1 requests (1,0,2), we would check if this allocation keeps the system safe before granting it.

### Deadlock Detection

When neither prevention nor avoidance is used, deadlocks may occur. The system must periodically check for deadlock conditions and take action. Detection algorithms analyze the system state to identify if a deadlock exists.

**Wait-for Graph**: A simplified version of the Resource Allocation Graph that shows only process-to-process dependencies. An edge from Pi to Pj indicates Pi is waiting for a resource held by Pj. A cycle in this graph indicates deadlock.

**Detection Algorithm**: Similar to the safety algorithm in Banker's Algorithm, but run when deadlock is suspected or periodically. The algorithm identifies all processes that can complete; those that cannot are deadlocked.

### Recovery from Deadlock

Once deadlock is detected, the system must recover. Common strategies include:

**Process Termination**:
- Abort all deadlocked processes (simplest but wasteful)
- Abort processes one at a time until deadlock is broken (requires running detection after each abortion)

**Resource Preemption**:
- Preempt resources from processes and give them to others
- Requires careful selection of victim processes to minimize cost
- May lead to starvation if the same process is always selected as victim

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Remember all four Coffman conditions** in order: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. Questions often ask you to list and explain each condition.

2. **Draw the Resource Allocation Graph correctly**: Use circles for processes and squares for resources. Label all edges clearly with arrows showing direction.

3. **Banker's Algorithm is highly exam-relevant**: Practice problems involving determining if a request can be granted and finding safe sequences. Remember to calculate the Need matrix first.

4. **Distinguish between prevention, avoidance, and detection**: Understand that prevention attacks one of the four conditions, avoidance ensures safe states, and detection identifies existing deadlocks.

5. **Safe vs Unsafe State**: A safe state means there exists a safe sequence; it does not guarantee deadlock will occur. An unsafe state may or may not lead to deadlock.

6. **Remember the key theorem**: No cycle in RAG means no deadlock. Cycle with single-instance resources means definite deadlock.

7. **For recovery strategies**, be prepared to explain both process termination and resource preemption methods, including their advantages and disadvantages.