# System Model in Operating Systems


## Table of Contents

- [System Model in Operating Systems](#system-model-in-operating-systems)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Types of System Models](#1-types-of-system-models)
  - [2. Process Model](#2-process-model)
  - [3. Resource Model](#3-resource-model)
  - [4. System Assumptions for Deadlock Study](#4-system-assumptions-for-deadlock-study)
  - [5. Resource Allocation Graph (RAG)](#5-resource-allocation-graph-rag)
- [Examples](#examples)
- [Exam Tips](#exam-tips)

## Introduction

A **System Model** in operating systems is a conceptual framework that defines the structure, components, and interactions within a computing system. It provides the foundational abstraction upon which process synchronization and deadlock handling mechanisms are built. The system model helps us understand how processes compete for resources, how they interact, and under what conditions problematic situations like deadlocks can arise.

In the context of process synchronization and deadlocks, the system model establishes the fundamental assumptions about the computing environment—including the number of processors, the nature of resources, and the behavior of processes. By clearly defining these assumptions, we can develop rigorous mathematical models to analyze and solve synchronization problems. The system model serves as the baseline for studying classical synchronization problems such as the Producer-Consumer problem, Readers-Writers problem, and Dining Philosophers problem.

This topic introduces the essential components of a system model: processes (or threads), resources, and their interactions. Understanding these components is crucial before delving into deadlock characterization, prevention, avoidance, and detection algorithms.

## Key Concepts

### 1. Types of System Models

**Uniprocessor Systems:** In a uniprocessor system, there is only a single processing unit. All processes share this single CPU through context switching. Since only one process can execute at any given instant, the critical issue is managing access to the CPU rather than coordinating multiple CPUs. However, processes still compete for other resources like memory, I/O devices, and files. The system model for uniprocessors assumes that the operation of process P_i can be interleaved with operations of other processes, but the underlying semantics remain serial.

**Multiprocessor Systems:** Multiprocessor systems contain multiple processing units that can execute processes concurrently (truly parallel execution). This introduces additional complexity because processes may compete for resources on different processors simultaneously. The system model must account for memory consistency issues, cache coherence, and the need for hardware-level synchronization primitives. Symmetric Multiprocessing (SMP) and Asymmetric Multiprocessing (AMP) are two common variants.

**Distributed Systems:** In distributed systems, processes run on multiple interconnected computers. The system model must account for network delays, partial failures, and the absence of shared memory. While deadlock handling in distributed systems is more complex, the fundamental principles remain similar to centralized systems.

### 2. Process Model

A **process** is an executing program that represents the basic unit of work in a system. The process model treats each process as an independent entity with its own:

- **Program counter**: Indicates the next instruction to execute
- **Registers**: Hold current working values
- **Stack**: Stores temporary data (function parameters, return addresses, local variables)
- **Address space**: The memory region where the process executes

In the context of synchronization and deadlocks, processes are considered **sequential** entities that execute instructions atomically (indivisibly). This assumption simplifies analysis, though in practice, individual instructions are not always atomic at the hardware level.

### 3. Resource Model

A **resource** is any system component that a process requires to make progress. Resources are categorized into two types:

**Preemptible Resources:** These can be taken away from a process without causing any harm or inconsistency. Examples include CPU time, memory (in some systems), and storage space. Preemptible resources typically do not lead to deadlocks because they can be reclaimed.

**Non-Preemptible Resources:** These cannot be taken away from a process once allocated without causing problems. Examples include printers, tape drives, database locks, and file handles. Deadlocks typically involve non-preemptible resources because once allocated, they remain with the process until the process voluntarily releases them.

Each resource type R_i has a finite number of instances. For example, a printer system might have 3 identical printers. The resource allocation model tracks:

- The total number of instances of each resource type
- The number of instances currently allocated to processes
- The number of instances still available

### 4. System Assumptions for Deadlock Study

For systematic analysis of deadlock problems, the following assumptions are made in the classical system model:

1. **Mutual Exclusion:** At least one resource must be held in a non-sharable mode. If a process requests a resource, only that process can use it.

2. **Hold and Wait:** Processes must hold at least one resource while waiting to acquire additional resources that are currently held by other processes.

3. **No Preemption:** Resources cannot be preempted; they can only be released voluntarily by the process holding them.

4. **Circular Wait:** There must exist a circular chain of processes where each process is waiting for a resource held by the next process in the chain.

These four conditions (Coffman conditions) are necessary for a deadlock to occur. The system model assumes these conditions may exist, and deadlock handling mechanisms address one or more of these conditions.

### 5. Resource Allocation Graph (RAG)

The **Resource Allocation Graph** is a visual representation of the system state showing which resources are allocated to which processes and which processes are waiting for which resources. It consists of:

- **Vertices (V):** Two disjoint sets—P = {P₁, P₂, ..., Pₙ} (processes) and R = {R₁, R₂, ..., Rₘ} (resources)
- **Edges (E):**
- Request Edge: Directed edge Pᵢ → Rⱼ indicating process Pᵢ is waiting for resource Rⱼ
- Assignment Edge: Directed edge Rⱼ → Pᵢ indicating resource Rⱼ is allocated to process Pᵢ

A **cycle** in the resource allocation graph is necessary (but not sufficient in all cases) for a deadlock. If each resource type has exactly one instance, a cycle is both necessary and sufficient for deadlock.

## Examples

**Example 1: Simple Resource Allocation**

Consider a system with:

- 2 processes: P1, P2
- 2 resource types: R1 (1 instance), R2 (1 instance)

Suppose:

- R1 is allocated to P1
- P2 requests R1 (request edge P2 → R1)
- R2 is allocated to P2
- P1 requests R2 (request edge P1 → R2)

This creates a cycle: P1 → R2 → P2 → R1 → P1. Since both resources have only one instance each, this cycle indicates a deadlock. Both processes are waiting for resources held by the other.

**Example 2: Multiple Instances**

Consider a system with:

- 1 process: P1
- 1 resource type: R1 with 3 instances
- P1 requests 2 instances, gets 1, requests 1 more

This cannot deadlock because there is only one process. Deadlock requires at least two competing processes.

**Example 3: Sufficient Resources**

Consider a system with:

- 2 processes: P1, P2
- 1 resource type: R1 with 2 instances

Both P1 and P1 request 1 instance each. Since there are 2 instances available, both can proceed. No circular wait forms because sufficient resources exist.

## Exam Tips

1. **Remember the Four Coffman Conditions:** Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait. All four must hold for a deadlock to exist.

2. **Distinguish Preemptible vs Non-Preemptible Resources:** Deadlocks typically involve non-preemptible resources. If resources were preemptible, deadlocks could be resolved by force.

3. **Resource Allocation Graph Interpretation:** A cycle in RAG indicates potential deadlock only when each resource type has exactly one instance. With multiple instances, a cycle is necessary but not sufficient.

4. **System Model Determines Solution Approach:** The type of system (uniprocessor vs multiprocessor) affects which synchronization primitives are available and appropriate.

5. **Not All Cycles Cause Deadlock:** In systems with multiple resource instances, a cycle may exist without deadlock if sufficient resources are available to break the cycle.

6. **Address Space is Process-Specific:** Each process has its own address space, which is why inter-process communication requires explicit mechanisms.

7. **Relationship to Synchronization:** The system model provides the context within which synchronization mechanisms (semaphores, monitors, mutexes) operate to prevent deadlock or other race conditions.
