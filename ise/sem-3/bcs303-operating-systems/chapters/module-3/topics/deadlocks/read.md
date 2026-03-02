# Deadlocks

## Introduction

A deadlock is one of the most challenging problems in operating systems where two or more processes are unable to proceed because each is waiting for resources held by the other. In a deadlock situation, processes remain in a permanent waiting state, neither completing their task nor releasing the resources they already hold. This phenomenon is particularly critical in multi-process systems where multiple processes compete for limited resources such as printers, tape drives, scanners, semaphores, or database locks.

The study of deadlocks is essential for computer science students because deadlocks can cause entire systems to become unresponsive, leading to significant performance degradation and system crashes. In real-world scenarios, database management systems, transaction processing systems, and distributed computing environments frequently encounter deadlock situations. Understanding deadlocks helps developers design more robust systems and implement appropriate handling mechanisms. The University of Delhi curriculum emphasizes deadlock handling as it represents a fundamental concept in operating system design and forms a critical component of competitive examinations and semester assessments.

## Key Concepts

### System Model

In a deadlock scenario, the system consists of a finite number of resources distributed among competing processes. Each resource type contains multiple identical instances, such as two printers or three tape drives. Processes must request resources before using them and release them after use. The operating system manages resource allocation through a resource allocation graph, which provides a visual representation of which processes hold which resources and which processes are waiting for additional resources.

### Necessary Conditions for Deadlock

A deadlock situation arises only when all four conditions, known as the Coffman conditions, hold simultaneously. First, MUTUAL EXCLUSION ensures that only one process can use a resource at a time. Second, HOLD AND WAKE means processes hold resources while waiting for additional resources. Third, NO PREEMPTION states that resources cannot be forcibly taken from processes; they must be voluntarily released. Fourth, CIRCULAR WAIT establishes a circular chain of processes where each process waits for a resource held by the next process in the chain. These conditions are not independent; eliminating any one of them prevents deadlocks from occurring.

### Resource Allocation Graph

The resource allocation graph is a directed graph that helps in deadlock detection and visualization. It consists of two types of nodes: process nodes represented by circles and resource nodes represented by squares. Edges include request edges (from process to resource) and assignment edges (from resource to process). A cycle in the resource allocation graph indicates a potential deadlock, though cycles do not always guarantee a deadlock when multiple instances of resources exist.

### Deadlock Prevention

Deadlock prevention involves designing the system such that at least one of the necessary conditions cannot hold. For instance, to eliminate hold and wait, a process must request all required resources before beginning execution or release all held resources before requesting new ones. To eliminate circular wait, a total ordering of resource types can be enforced, requiring processes to request resources in a predetermined sequence. Another approach involves preemptive resource allocation, allowing the system to take resources away from processes, though this strategy is rarely practical for certain resource types like printers.

### Deadlock Avoidance

Deadlock avoidance requires the system to have additional information about resource requests in advance. The Banker's Algorithm, developed by Dijkstra, is the most famous avoidance algorithm. It simulates resource allocation with a safety check before granting any request, ensuring the system remains in a safe state where all processes can complete. A safe state is one where there exists a sequence of process execution that allows all processes to complete without deadlock. The Banker's Algorithm requires the maximum resource needs of each process, currently allocated resources, and available resources.

### Deadlock Detection and Recovery

Deadlock detection involves periodically examining the system state to identify whether a deadlock has occurred. For systems with single instances of each resource type, detection is straightforward using cycle detection in the resource allocation graph. For multiple resource instances, the detection algorithm uses a waiting graph and applies a variant of the Banker's algorithm. Once detected, recovery can occur through several methods: process termination (aborting one or more processes), resource preemption (selectively taking resources from processes), or system restart.

## Examples

### Example 1: Two Processes and Two Resources

Consider two processes P1 and P2 competing for a printer and a plotter. Initially, both resources are available. P1 acquires the printer while P2 acquires the plotter. Then P1 requests the plotter (which is held by P2) while P2 requests the printer (held by P1). Neither process can proceed, resulting in a deadlock.

Using the resource allocation graph approach, we have two request edges and two assignment edges forming a cycle: P1 → Printer (request) → P2 (holds) → Plotter (request) → P1 (holds) → Printer. To resolve this deadlock, either P1 or P2 must be terminated, or one process must voluntarily release its resource.

### Example 2: Banker's Algorithm Safety Check

Suppose a system has three process types: P0, P1, and P2, with available resources currently: Available = [3, 3, 2]. The maximum demand, allocation, and need matrices are:

Maximum: P0=[7,5,3], P1=[3,2,2], P2=[9,5,2]
Allocation: P0=[0,1,0], P1=[3,0,2], P2=[3,0,2]
Need: P0=[7,4,3], P1=[0,2,0], P2=[6,5,0]

To check safety, we start with Available=[3,3,2]. P1's need [0,2,0] ≤ Available, so we can allocate to P1. After P1 completes and releases resources, Available becomes [6,3,4]. Next, P0's need [7,4,3] > Available, so we skip to P2. P2's need [6,5,0] ≤ [6,3,4] is false. With no process satisfiable, the system is UNSAFE, indicating potential deadlock.

### Example 3: Dining Philosophers Problem

Five philosophers sit around a circular table, each thinking or eating. Each philosopher needs two forks to eat, but only five forks exist between them. If each philosopher picks up the fork on their left simultaneously, all pick up one fork and wait indefinitely for the right fork, creating a classic deadlock scenario. Solutions include imposing a total ordering on fork acquisition, allowing a philosopher to pick up both forks only when both are available, or using a central waiter to coordinate access. This problem illustrates how seemingly simple resource sharing can lead to deadlocks in concurrent systems.

## Exam Tips

For DU semester examinations, students should focus on understanding the four Coffman conditions thoroughly, as questions frequently ask about the necessary conditions for deadlock. The Banker's Algorithm is extremely important and students must be able to work through both safety and resource request algorithms completely.

Resource allocation graphs are frequently tested in examinations, so students should practice drawing and analyzing these graphs for both single and multiple resource instances. Understanding the difference between deadlock prevention, avoidance, and detection is crucial, as exam questions often ask students to distinguish between these approaches.

Students should memorize the formulas: Need = Maximum Demand - Allocation, and the safety check condition Need ≤ Available. Common exam questions include determining whether a given state is safe or unsafe, processing resource request scenarios using the Banker's Algorithm, and identifying deadlock situations from resource allocation graphs.

Key distinctions to remember include that prevention eliminates one Coffman condition, avoidance requires advance information about resource needs, and detection allows deadlocks to occur then recovers. The difference between hold-and-wait and no-hold-and-wait conditions often appears in multiple-choice questions.