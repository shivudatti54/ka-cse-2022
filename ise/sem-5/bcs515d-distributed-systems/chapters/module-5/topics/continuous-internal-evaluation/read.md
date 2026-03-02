**Subject: Distributed Systems (18CS65)**
**Module 5: Distributed File Systems & Distributed Shared Memory**
**Topic: Continuous Internal Evaluation (CIE)**

---

### **1. Introduction to Module 5 CIE**

Welcome, future engineers! This document is designed to guide your preparation for the Continuous Internal Evaluation (CIE) based on Module 5 of the Distributed Systems curriculum. Module 5 delves into two critical abstractions that enable efficient and seamless distributed computing: **Distributed File Systems (DFS)** and **Distributed Shared Memory (DSM)**. Mastering these concepts is not only crucial for your exams but also forms the bedrock for understanding modern cloud storage, big data platforms, and high-performance computing clusters.

---

### **2. Core Concepts Explained**

A CIE for this module will likely test your understanding of the following core concepts:

#### **2.1 Distributed File Systems (DFS)**

A DFS is a classic client-server application that provides a transparent, unified view of a file system stored across multiple networked machines. Key characteristics and components include:

- **Transparency:** The distributed nature is hidden from the client. A file's location (location transparency) and the movement between servers (migration transparency) should not be apparent to the user or application.
- **Client-Server Architecture:** File servers manage disk storage and make it available to clients. Clients access files by making requests to these servers.
- **Naming:** A crucial service. Files can be named using:
  - **Remote Mounting:** Clients explicitly mount a directory from a remote server (e.g., NFS).
  - **A Single Global Namespace:** A unified directory tree that spans all servers (e.g., Google File System, Hadoop HDFS).
- **Stateful vs. Stateless Servers:**
  - **Stateless Server** (e.g., NFS v2): Does not maintain any client-specific information (state) between requests. Each request must be self-contained (file handle, offset, count). Simplifies crash recovery.
  - **Stateful Server** (e.g., AFS): Maintains client state (e.g., open files, current file pointer). Can enable performance optimizations like caching and read-ahead but complicates crash recovery.
- **Caching & Replication:** To improve performance and availability, file blocks are cached on client machines and replicated across multiple servers. This introduces challenges in maintaining **consistency** among the cached copies.

#### **2.2 Distributed Shared Memory (DSM)**

DSM is a software abstraction that provides the illusion of a single, shared memory address space across multiple nodes in a distributed system, even though each node has its own private physical memory.

- **The Illusion:** DSM systems allow processes on different machines to share data by simply reading from and writing to shared variables, as if they were in a multiprocessor system. This simplifies programming for distributed applications.
- **Page-Based DSM:** A common implementation technique. The shared memory space is divided into pages. The DSM system, often integrated with the OS, handles:
  - **Page Faulting:** When a process accesses a page not in its local memory, a page fault occurs.
  - **Page Migration:** The required page is fetched from the node that currently holds it.
  - **Replication:** Pages can be replicated on multiple nodes for faster read access.
- **The Central Challenge: Consistency Models**
  The biggest challenge is defining when a write operation by one process will be visible to others. This is governed by a **consistency model**.
  - **Sequential Consistency:** The result of any execution is the same as if the operations of all processes were executed in some sequential order, and the operations of each individual process appear in this sequence in the order specified by its program. This is the strongest and most intuitive model.
  - **Weak Consistency:** Does not guarantee that writes are instantly visible. It uses synchronization variables (e.g., locks). Only when a lock is acquired/released are all previous writes guaranteed to be visible to others. This allows for higher performance.

#### **2.3 Examples**

- **DFS:** **Sun NFS** (Network File System) is a prime example of a stateless, remote-mounting DFS. **Hadoop HDFS** is an example designed for large data processing with a single global namespace and high replication for fault tolerance.
- **DSM:** The **Ivy** system is a classic example of a page-based DSM. Modern equivalents are found in software environments for scientific computing and machine learning that distribute data across clusters.

---

### **3. Key Points & Summary**

| Concept                             | Key Idea                                                                                         | Primary Challenge                                                                            |
| :---------------------------------- | :----------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------- |
| **Distributed File System (DFS)**   | Provides transparent access to files stored across a network.                                    | Maintaining consistency in the face of caching and replication.                              |
| **Stateless vs. Stateful Server**   | Trade-off between simplicity of recovery (stateless) and potential performance gains (stateful). | Designing protocols for state management and recovery.                                       |
| **Distributed Shared Memory (DSM)** | Illusion of a shared memory address space across separate machines.                              | Implementing efficient and understandable consistency models.                                |
| **Consistency Models**              | Rules governing the visibility of writes.                                                        | Balancing programmer intuition (strong consistency) with system performance (weaker models). |

**Summary:** Module 5 teaches you how distributed systems manage two fundamental resources: storage (via DFS) and memory (via DSM). You must understand the architectures (client-server), the techniques used (caching, replication, page migration), and the critical trade-offs involved, especially the central challenge of maintaining consistency while ensuring performance, scalability, and transparency. Focus on differentiating the goals and mechanisms of DFS and DSM for your CIE.
