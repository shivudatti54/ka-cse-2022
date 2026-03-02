# System Model in Operating Systems - Summary

## Key Definitions and Concepts

A PROCESS is an instance of a program in execution, characterized by its own program counter, registers, stack, and process control block containing state information, memory management details, and resource allocation records.

The RESOURCE ALLOCATION MODEL defines how processes request, receive, use, and release system resources including CPU time, memory, I/O devices, and synchronization primitives. Each resource type may have multiple instances.

A CRITICAL SECTION is a portion of code that accesses shared variables or resources and must not be concurrently executed by more than one process.

DEADLOCK occurs when two or more processes are unable to proceed because each is waiting for resources held by the others, forming a circular wait condition.

## Important Formulas and Theorems

**Five Necessary Conditions for Deadlock**:
1. Mutual Exclusion: At least one resource must be held in a non-sharable mode
2. Hold and Wait: A process must be holding at least one resource while waiting for others
3. No Preemption: Resources cannot be forcibly taken from processes
4. Circular Wait: There must be a circular chain of processes, each waiting for a resource held by the next

**Banker's Algorithm Safety Test**:
A state is safe if there exists a sequence of process executions that allows all processes to complete without deadlock. The algorithm simulates resource allocation for each possible sequence to verify safety.

## Key Points

The resource allocation graph (RAG) uses directed edges to show which resources are allocated to which processes and which processes are waiting for which resources. A cycle indicates potential deadlock.

Semaphores are integer variables with atomic wait (P) and signal (V) operations. Binary semaphores provide mutual exclusion; counting semaphores manage multiple resource instances.

The critical section problem requires three conditions: mutual exclusion (only one process in critical section), progress (processes not in remainder section can participate in decision), and bounded waiting (limit on entries after request).

The producer-consumer problem uses two semaphores—empty (counting available slots) and full (counting filled slots)—plus a mutex for buffer access.

Deadlock prevention works by violating one of the four necessary conditions; deadlock avoidance uses algorithms like Banker's to make safe allocation decisions; deadlock detection periodically checks system state for unreachable processes.

## Common Mistakes to Avoid

Confusing deadlock prevention with deadlock avoidance—prevention eliminates one of the necessary conditions, while avoidance dynamically ensures safe states during resource allocation.

Assuming a cycle in the resource allocation graph always indicates deadlock—a cycle with multi-instance resources may not cause deadlock; single-instance resources in a cycle guarantee deadlock.

Forgetting that semaphore operations must be atomic—non-atomic implementation of wait and signal can lead to race conditions within the synchronization mechanism itself.

## Revision Tips

Draw resource allocation graphs for various deadlock scenarios to build visual intuition. Practice identifying which necessary deadlock condition each prevention strategy targets.

Implement the producer-consumer solution on paper multiple times until the logic of empty/full semaphores becomes automatic.

Memorize the five necessary deadlock conditions and for each prevention technique, identify which condition it violates.

Review Banker's Algorithm with multiple worked examples, practicing both safety checking and request evaluation.