# Deadlocks

## Introduction

A deadlock is a fundamental problem in operating systems where a set of processes are permanently blocked because each process is waiting for a resource that is held by another process in the set. This situation arises in multi-programmed systems where processes compete for limited resources such as printers, tape drives, semaphores, or database locks. When deadlock occurs, the system comes to a standstill—no progress can be made without external intervention.

Deadlocks are particularly problematic in transaction processing systems, database management systems, and distributed computing environments. Consider a scenario where process P1 holds resource R1 and requests resource R2, while process P2 holds resource R2 and requests resource R1. Both processes are now permanently blocked, waiting for resources that will never be released. This circular waiting condition represents the essence of a deadlock.

Understanding deadlocks is crucial for system designers and administrators. The goal is not merely to detect and recover from deadlocks, but to design systems that minimize their occurrence. The Banker's Algorithm, developed by Edsger Dijkstra, represents one of the classic solutions for deadlock avoidance. This topic carries significant weight in DU examinations, with questions frequently appearing on deadlock conditions, prevention techniques, avoidance algorithms, and detection methods.

## Key Concepts

### System Model

In the context of deadlocks, a system consists of a finite number of resources distributed among a finite number of processes. Resources can be of multiple types, with each type having several identical instances. For example, a computer system might have three printers (three instances of the printer resource type) or two CD-ROM drives.

Each process utilizes resources according to the following sequence: request, use, release. When a process requests a resource that is not immediately available, it must wait. Once obtained, the process can use the resource for its task, and subsequently release it back to the system for other processes to use. A deadlock occurs when processes wait indefinitely because resources they need are held by other waiting processes.

### Deadlock Characterization

Four necessary conditions must hold simultaneously for a deadlock to occur:

**Mutual Exclusion**: At least one resource must be held in a non-sharable mode. Only one process can use the resource at any given time. If another process requests that resource, the requesting process must wait until the resource is released.

**Hold and Wait**: A process must be holding at least one resource and waiting to acquire additional resources that are currently held by other processes. This means processes do not release their currently held resources while requesting new ones.

**No Preemption**: Resources cannot be preempted; that is, a resource can be released only voluntarily by the process holding it, after that process has completed its task. The system cannot force a process to release a resource.

**Circular Wait**: There must be a circular chain of processes where each process is waiting for a resource held by the next process in the chain. If P0 is waiting for a resource held by P1, P1 is waiting for a resource held by P2, and so on, with Pn waiting for a resource held by P0, a circular wait exists.

### Resource Allocation Graph

A resource allocation graph (RAG) is a directed graph that depicts which resources are allocated to which processes and which processes are waiting for which resources. The graph contains two types of vertices: process vertices (represented by circles) and resource vertices (represented by squares). Edges from resource to process (R → P) indicate the resource has been allocated to that process. Edges from process to resource (P → R) indicate the process is requesting that resource.

A key theorem states: If the resource allocation graph contains no cycles, then no deadlock exists. If the graph contains a cycle, a deadlock may or may not exist. If each resource type has exactly one instance, then a cycle implies deadlock. If resource types have multiple instances, a cycle does not necessarily mean deadlock.

### Methods for Handling Deadlocks

Operating systems can handle deadlocks through four main strategies:

**Deadlock Prevention**: Ensure that at least one of the four necessary conditions for deadlock cannot hold. This is achieved by restricting how processes can request resources.

**Deadlock Avoidance**: The system anticipates deadlock-prone situations by granting resources only if the resulting state remains safe. The Banker's Algorithm exemplifies this approach.

**Deadlock Detection and Recovery**: Allow deadlocks to occur, detect them when they happen, and then recover through process termination or resource preemption.

**Ignorance**: The system pretends that deadlocks never occur (the "ostrich algorithm"). This approach is used by many mainstream operating systems including UNIX and Windows due to the overhead of prevention/avoidance.

### Deadlock Prevention

Deadlock prevention attacks one of the four necessary conditions:

**Attacking Mutual Exclusion**: Not always possible since some resources are inherently non-sharable (printers). Spooling can sometimes make printers shareable, but this has limitations.

**Attacking Hold and Wait**: Require processes to request all resources before they begin execution (static allocation). Alternatively, allow processes to request resources only when they have none (release all before requesting new ones). Both approaches have significant drawbacks: static allocation causes poor resource utilization, and the second approach requires additional overhead.

**Attacking No Preemption**: If a process holding some resources requests another resource that cannot be immediately allocated, all its currently held resources are preempted. The process must wait, but its held resources are released and added to the resource pool.

**Attacking Circular Wait**: Impose a total ordering of resource types and require that each process request resources in strictly increasing order. This prevents circular wait because a process cannot request a lower-numbered resource while holding a higher-numbered one.

### Deadlock Avoidance

The Banker's Algorithm is a classic deadlock avoidance algorithm that requires the system to maintain additional state information. The algorithm requires knowledge of the maximum possible resource needs of each process in advance.

**Safe State**: A state is safe if the system can allocate resources to each process in some order (a safe sequence) without encountering deadlock. A safe sequence is an ordering of processes such that if each process requests resources up to its maximum need, the system can satisfy all requests by granting resources one at a time following the sequence.

**Banker's Algorithm**: For each resource request, the system simulates granting the request and checks if the resulting state is safe. If safe, the request is granted; otherwise, it is denied. The algorithm maintains several data structures:
- Available: Vector indicating the number of available resources of each type
- Max: Matrix indicating maximum demand of each process
- Allocation: Matrix indicating currently allocated resources
- Need: Matrix indicating remaining resource needs (Need = Max - Allocation)

The safety algorithm works by finding a process whose Need vector is less than or equal to Available, then assumes that process completes (releasing its Allocation), and repeats until all processes can complete or no such process exists.

### Deadlock Detection

Detection algorithms identify when deadlock has actually occurred. The wait-for graph is a simplified detection method where nodes represent processes and an edge from Pi to Pj exists if Pi is waiting for a resource held by Pj. A cycle in the wait-for graph indicates deadlock.

For systems with multiple instances of each resource type, a detection algorithm similar to the Banker's safety algorithm is used. The algorithm finds a process whose Need is less than or equal to Available, assumes it completes, adds its Allocation to Available, and continues. If some processes cannot complete, they are deadlocked.

The frequency of detection depends on how often deadlocks occur and the cost of detection. Running detection too frequently adds overhead; running too rarely allows deadlocks to persist and waste resources.

### Recovery from Deadlock

When deadlock is detected, the system must recover through one of these methods:

**Process Termination**: Abort one or more processes to break the circular wait. Options include:
- Terminate all deadlocked processes (brutal but guarantees recovery)
- Terminate processes one at a time until the deadlock is broken (requires running detection after each termination)

**Resource Preemption**: Preempt resources from some processes and give them to others until the deadlock is broken. Issues include:
- Selecting a victim: Choose processes to preempt based on cost criteria
- Rollback: Return preempted processes to a safe state and restart them
- Starvation: Ensure the same process is not perpetually selected as victim

## Examples

### Example 1: Analyzing a Resource Allocation Graph

Consider a system with two processes P1 and P2, and two resource types R1 and R2, each with one instance. Suppose the RAG shows: R1 is allocated to P1, R2 is allocated to P2, P1 is requesting R2, and P2 is requesting R1.

**Solution**: This graph contains a cycle: P1 → R2 → P2 → R1 → P1. Since each resource type has exactly one instance, the cycle implies deadlock. Both processes are deadlocked.

### Example 2: Banker's Algorithm - Safety Check

Consider a system with 5 processes P0 through P4, and 3 resource types A (10 instances), B (5 instances), C (7 instances).

Current state:
- Available: A=3, B=3, C=2
- Maximum needs:
  - P0: A=7, B=5, C=3
  - P1: A=3, B=2, C=2
  - P2: A=9, B=0, C=2
  - P3: A=2, B=2, C=2
  - P4: A=4, B=3, C=3

Current allocation:
- P0: A=0, B=1, C=0
- P1: A=2, B=0, C=0
- P2: A=3, B=0, C=2
- P3: A=2, B=1, C=1
- P4: A=0, B=0, C=2

**Step-by-step solution**:
1. Calculate Need matrices: Need = Maximum - Allocation
   - P0: A=7, B=4, C=3
   - P1: A=1, B=2, C=2
   - P2: A=6, B=0, C=0
   - P3: A=0, B=1, C=1
   - P4: A=4, B=3, C=1

2. Compare Need with Available (A=3, B=3, C=2):
   - P1: Need(1,2,2) ≤ Available(3,3,2)? YES
   - Available becomes: (3+2, 3+0, 2+0) = (5, 3, 2)

3. Compare Need with new Available(5,3,2):
   - P3: Need(0,1,1) ≤ Available(5,3,2)? YES
   - Available becomes: (5+2, 3+1, 2+1) = (7, 4, 3)

4. Compare with Available(7,4,3):
   - P4: Need(4,3,1) ≤ Available(7,4,3)? YES
   - Available becomes: (7+0, 4+0, 3+2) = (7, 4, 5)

5. Compare with Available(7,4,5):
   - P0: Need(7,4,3) ≤ Available(7,4,5)? YES
   - Available becomes: (7+0, 4+1, 5+0) = (7, 5, 5)

6. Compare with Available(7,5,5):
   - P2: Need(6,0,0) ≤ Available(7,5,5)? YES
   - All processes can complete

**Safe sequence**: P1 → P3 → P4 → P0 → P2. The system is in a safe state.

### Example 3: Applying Circular Wait Prevention

Suppose we have resource types with ordering: R1(1) < R2(2) < R3(3). A process that first requests R3 and later needs R1 must follow this approach: request R1 first, then request R2, then request R3. A process cannot request R2 while holding R3 because that would violate the increasing order requirement.

**Solution**: By imposing this ordering, circular wait is impossible because a process holding a higher-numbered resource can only wait for resources with even higher numbers, never lower. This breaks the circular chain.

## Exam Tips

1. **Remember all four deadlock conditions**: Mutual exclusion, hold and wait, no preemption, and circular wait—all four are necessary for deadlock. Questions frequently ask which condition to attack for prevention.

2. **Distinguish between prevention and avoidance**: Prevention attacks one of the four conditions directly (structural approach). Avoidance makes decisions dynamically to keep the system in safe states (algorithmic approach).

3. **Banker's Algorithm is exam-intensive**: Know how to calculate Need, check safety, and determine if resource requests should be granted. Practice numerical problems thoroughly.

4. **Resource allocation graph interpretation**: Remember—a cycle does not always mean deadlock. It only means deadlock when each resource type has exactly one instance.

5. **Safe sequence is not unique**: A system can have multiple safe sequences. Finding one safe sequence is sufficient to prove the state is safe.

6. **Trade-offs matter**: Understand the advantages and disadvantages of each deadlock handling method. Prevention reduces resource utilization; avoidance requires advance knowledge; detection incurs overhead.

7. **Real-world examples**: Be prepared to explain deadlock scenarios in practical systems like database transactions or printer spooling to demonstrate conceptual understanding.

8. **Formula recall**: Remember that Need = Maximum - Allocation. This is fundamental to the Banker's Algorithm.

9. **Preemption challenges**: When discussing recovery, explain why preemption is difficult—it requires rollback capability and may cause starvation.

10. **Time complexity awareness**: The Banker's Algorithm has complexity O(m × n²) where m is resource types and n is processes. This is important for large systems.