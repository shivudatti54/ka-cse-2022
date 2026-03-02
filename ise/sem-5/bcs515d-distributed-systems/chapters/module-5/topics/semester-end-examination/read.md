# Distributed Systems - Semester-End Examination Guide (Module 5)

## Introduction

As you prepare for your  semester-end examination in Distributed Systems, Module 5 stands out as a critical component. This module typically covers advanced and often contemporary topics that build upon the foundational principles learned in earlier modules. A strong grasp of these concepts is essential not only for your exam but also for understanding the real-world systems you will encounter in your engineering career. This guide provides a concise yet thorough overview of key areas you are likely to be tested on.

## Core Concepts Explained

Based on the standard  curriculum, Module 5 frequently delves into **Distributed Multimedia Systems**, **Distributed Shared Memory (DSM)**, and **Distributed File Systems**. Here’s a breakdown of these core concepts:

### 1. Distributed Multimedia Systems

This topic deals with the challenges of delivering time-dependent media (audio, video) over a network. The key challenge is providing **Quality of Service (QoS)** guarantees.

- **QoS Parameters:** These are metrics that define the performance of the multimedia stream.
  - **Bandwidth:** The data rate required (e.g., 5 Mbps for HD video).
  - **Latency:** The delay between sending and receiving a packet. Low latency is crucial for real-time interaction.
  - **Jitter:** The variation in latency. Jitter can cause choppy audio/video and is handled using buffering.
  - **Loss Rate:** The proportion of packets that are lost in transit.

- **Resource Management:** To guarantee QoS, the system must **reserve resources** (bandwidth, buffer space, CPU cycles) in advance along the communication path. Protocols like **RSVP (Resource reSerVation Protocol)** are designed for this purpose.

- **Example:** A video conferencing application like Zoom or Microsoft Teams. Your client software negotiates a certain QoS level with the servers and your network to ensure your video call is smooth, with minimal delay and distortion.

### 2. Distributed Shared Memory (DSM)

DSM is an abstraction that allows processes on separate computers to share a region of memory (a shared address space) without using explicit message passing. It creates the illusion of a single, shared memory space across all nodes.

- **The Illusion:** The DSM system, typically a runtime library or middleware, is responsible for mapping local memory addresses to physical memory, which may be on a remote machine.
- **Memory Coherence:** The major challenge is maintaining **memory consistency**. When one process updates a variable in the shared space, how and when do other processes see that change? Models like **Sequential Consistency** (all updates appear in a single, global order) are used.
- **Replication vs. Migration:** To improve performance, data can be _replicated_ (copied to multiple nodes for faster read access) or _migrated_ (moved to the node that needs it). This introduces the problem of keeping all copies consistent.
- **Example:** Scientific computations where a large matrix is shared among multiple computers, each working on a different part of the calculation but needing to read the results from others.

### 3. Distributed File Systems

A DFS provides a unified view of files stored on multiple machines, making them accessible from any node on the network, just like local files.

- **Transparency:** A key goal is **access transparency** (client programs are unaware of the file's location) and **location transparency** (the file path does not reveal its physical storage location).
- **Key Architecture:** Most DFSs follow a **client-server model** (e.g., NFS - Network File System). Clients make requests to a file server, which manages storage and access.
- **Replication and Caching:** Files are often _replicated_ across multiple servers for fault tolerance and load balancing. _Caching_ (storing recently used file data on the client's local disk) is crucial for performance to reduce network traffic.
- **Example:** **Network File System (NFS)** by Sun Microsystems is a classic example. In a university lab, your home directory might be stored on a central server but appear as a local folder on every lab machine you log into.

## Key Points & Summary

| Topic Area                          | Key Focus                                                                   | Main Challenge                                                                               |
| :---------------------------------- | :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Distributed Multimedia Systems**  | Quality of Service (QoS) guarantees for time-sensitive data.                | Managing bandwidth, latency, jitter, and loss to ensure smooth playback.                     |
| **Distributed Shared Memory (DSM)** | Abstraction of a shared memory address space across nodes.                  | Maintaining memory consistency and coherence efficiently.                                    |
| **Distributed File Systems**        | Providing transparent, unified access to files stored on multiple machines. | Ensuring performance (through caching), reliability (through replication), and transparency. |

**Examination Tips:**

- Be prepared to **define and differentiate** key terms like QoS, jitter, consistency models (e.g., sequential vs. eventual).
- Understand the **architecture** of systems like NFS and the purpose of protocols like RSVP.
- **Write examples** to illustrate your points. This demonstrates a deeper understanding.
- **Compare and contrast** concepts, e.g., message passing vs. DSM, or different consistency models.

Focus on understanding the "why" behind each concept—the problems they solve and the trade-offs involved. This approach will be far more effective than pure memorization for tackling your exam questions. Good luck
