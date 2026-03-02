# Distributed Systems - Module 5: Semester-End Examination Guide

## Introduction

Module 5 of a typical Distributed Systems curriculum often serves as the culmination of the course, focusing on advanced and emerging topics that build upon the foundational concepts of communication, synchronization, processes, and consistency. As you prepare for your semester-end examination, this module tests your ability to synthesize earlier knowledge and apply it to complex, real-world distributed scenarios. Key areas usually include Distributed File Systems, Distributed Shared Memory (DSM), and case studies of real-world systems.

## Core Concepts Explained

### 1. Distributed File Systems (DFS)
A Distributed File System is a classic client-server model that provides a transparent, unified view of files stored across multiple servers. It is a critical application of distributed systems, enabling shared storage and access.

*   **Key Features:** The core design goals are **transparency** (hiding the distributed nature), **concurrency** (managing simultaneous access), **replication** (for fault tolerance and performance), and **heterogeneity**.
*   **Mechanisms:** Important mechanisms you must understand are:
    *   **Caching:** Clients store recently accessed file blocks locally to reduce network traffic and server load. The challenge involves maintaining **cache consistency** (e.g., write-through vs. delayed-write policies).
    *   **Replication:** Having multiple copies of a file on different servers enhances availability and performance. This introduces issues of **replica management** and consistency.
    *   **Fault Tolerance:** DFSs must handle server and network failures gracefully, often using techniques like **stateless servers** (e.g., NFS) or **recovery protocols**.

**Example:** The **Network File System (NFS)** is a quintessential example. Understand its VFS layer, stateless server design, and how it uses file handles and mounts. Contrast it with a stateful system like **Andrew File System (AFS)**, which focuses on scalability through whole-file caching and callbacks.

### 2. Distributed Shared Memory (DSM)
DSM is an abstraction that provides the illusion of a single, shared memory address space across multiple interconnected computers that only have private physical memory. It's an alternative to message-passing for process communication.

*   **The Illusion:** DSM systems use software and hardware to map local memory pages to a global address space. When a process accesses a non-local memory segment, a trap occurs, and the DSM runtime fetches the required data page from another node.
*   **Design Issues:** The major challenge is maintaining **memory consistency**. You must be familiar with the **Consistency Models** that define the rules for visibility of memory writes:
    *   **Sequential Consistency:** The result of any execution is as if all operations were executed in some sequential order.
    *   **Weak Consistency:** Relaxes the rules, allowing for higher performance but requiring synchronization primitives (like locks) to enforce consistency at critical sections.
*   **Page-Based Systems:** Most DSM implementations are page-based (e.g., using the MMU for tracking), leading to issues like **false sharing** (where unrelated variables reside on the same page, causing unnecessary data movement).

### 3. Case Studies & Emerging Trends
Exam questions often ask you to analyze real-world systems, linking their design to the theories you've learned.

*   **Case Study - Google File System (GFS):** A seminal paper in the field. Be prepared to discuss its design choices tailored for Google's needs: a single master for metadata, large chunk size (64MB), and a relaxed consistency model that prioritizes append-heavy workloads ("record append") over strict consistency.
*   **Trends:** You may be asked to comment on modern paradigms:
    *   **Blockchain:** A decentralized, distributed ledger. Relate it to concepts like consensus (Proof-of-Work), Byzantine fault tolerance, and immutable data replication.
    *   **Edge/Fog Computing:** Extending cloud computing to the network edge to reduce latency. This is a natural evolution of distributed systems principles applied to IoT.

## Key Points & Summary

| Topic | Key Focus Areas for Exam |
| :--- | :--- |
| **Distributed File Systems (DFS)** | Transparency, Caching & Consistency (e.g., write-back vs. write-through), Replication strategies, Fault Tolerance (stateless vs. stateful). Know NFS and AFS as primary examples. |
| **Distributed Shared Memory (DSM)** | The abstraction, how it works (page fetching/trapping), Memory Consistency Models (Sequential vs. Weak), and challenges like false sharing. |
| **Case Studies** | **GFS:** Understand its architecture (single master, chunkservers), design rationale for large data processing, and its specific consistency approach. |
| **Synthesis** | Be ready to compare and contrast: e.g., message-passing vs. DSM, different DFS architectures, or strict vs. relaxed consistency models. Explain the trade-offs between performance, scalability, and consistency. |

**Examination Tip:** Questions are likely to be application-based. Rather than just defining terms, you will be expected to *explain why* a system is designed a certain way, *analyze* the consequences of a design choice, or *compare* different approaches. Use the examples provided (NFS, AFS, GFS) to ground your answers in practical reality.