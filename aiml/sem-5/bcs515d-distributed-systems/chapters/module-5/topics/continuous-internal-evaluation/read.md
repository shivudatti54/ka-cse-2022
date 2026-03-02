# Continuous Internal Evaluation (CIE) in Distributed Systems (Module 5)

## Introduction

For  engineering students, Continuous Internal Evaluation (CIE) is an integral part of the learning and assessment process, designed to gauge your understanding of a subject throughout the semester rather than relying solely on a final examination. In a complex and conceptual subject like Distributed Systems, CIE becomes crucial. Module 5 often covers advanced and critical topics such as Distributed File Systems (e.g., NFS, AFS), Distributed Shared Memory (DSM), and Peer-to-Peer Systems. Successfully navigating the CIE for this module requires a deep conceptual understanding and the ability to apply these concepts to solve problems.

## Core Concepts of CIE in Distributed Systems

The CIE for Distributed Systems typically consists of two components, often adding up to a total of 50 marks:

1.  **CIE-1 (25 Marks):** Usually conducted in the first half of the semester. For Module 5, this might cover the initial parts, such as the architecture and design principles of Distributed File Systems.
2.  **CIE-2 (25 Marks):** Conducted later, covering the latter parts of the syllabus, which could include protocols like NFS, concepts of DSM, and Peer-to-Peer architectures.

The exams can be a mix of:
*   **Short Answer Questions:** Testing definitions and basic concepts.
    *   *Example: "Define Distributed Shared Memory (DSM). List one advantage and one challenge."*
*   **Long Answer Questions:** Requiring detailed explanations, comparisons, and diagrams.
    *   *Example: "Explain the architecture and working of the Network File System (NFS) protocol with a neat diagram. Discuss its key features."*
*   **Numerical Problems:** While less common in Module 5, some aspects might involve simple calculations related to consistency models or performance.
*   **Case Studies:** You might be asked to analyze a real-world system (e.g., BitTorrent for P2P, Dropbox for file storage) based on the concepts learned.

## Key Topics for Module 5 CIE Preparation

To excel, you must thoroughly understand these core areas:

### 1. Distributed File Systems (DFS)
*   **Concept:** A classic example of a distributed service. Understand the design goals: transparency (access, location, mobility), concurrent updates, replication, and performance.
*   **Examples:**
    *   **Sun NFS (Network File System):** Be prepared to explain its stateless server design, VFS layer, and the RPC-based protocol (mounting, reading, writing). Know the purpose of the *file handle* and how client-side caching is handled.
    *   **Andrew File System (AFS):** Contrast with NFS. Understand its stateful design, the concept of *sessions*, and its focus on scalability through whole-file caching and callback mechanisms.

### 2. Distributed Shared Memory (DSM)
*   **Concept:** An abstraction that provides a shared memory space in a system that has no physical shared memory. It's a software-implemented shared memory on top of a message-passing system.
*   **Key Aspects:** Focus on the various **memory consistency models** (Sequential, Causal, Weak, etc.). You should be able to differentiate between them and understand the trade-offs between performance and ease of programming.
*   **Example:** A question might present a sequence of read/write operations performed by different processes and ask you to determine if it violates a given consistency model.

### 3. Peer-to-Peer (P2P) Systems
*   **Concept:** Distributed systems without centralized control, where all nodes (peers) are equal participants sharing resources.
*   **Structured vs. Unstructured P2P:** This is a crucial distinction.
    *   **Unstructured:** e.g., Gnutella. Peers connect arbitrarily. Searching is done by flooding. Understand the scalability issues.
    *   **Structured:** e.g., Chord DHT (Distributed Hash Table). This is a very important topic. You must understand how a DHT works—how data is assigned to nodes (*hashing*), how nodes are organized in a *ring*, and how routing is done efficiently using *finger tables*. Be able to draw a Chord ring and trace a lookup query.

## Summary and Key Points

*   **Purpose of CIE:** CIE is a continuous assessment tool to ensure you are building your knowledge of Distributed Systems concepts incrementally throughout the semester.
*   **Focus on Concepts:** Module 5 is highly conceptual. Rote learning will not suffice. Focus on understanding the *'why'* behind the designs of NFS, AFS, DSM, and P2P systems.
*   **Diagrams are Crucial:** For long answers, always support your explanation with clear, labeled diagrams (e.g., NFS architecture, Chord ring structure). This demonstrates a clear understanding and can fetch significant marks.
*   **Compare and Contrast:** Be ready to compare different systems (e.g., NFS vs. AFS, Structured vs. Unstructured P2P). Highlight their design philosophies, advantages, and disadvantages in a tabular format for clarity.
*   **Practice Previous Questions:** The best way to prepare is to practice with previous years' CIE question papers. This familiarizes you with the expected format, question depth, and key areas of focus.

By moving beyond memorization and truly grasping the architectural principles and trade-offs in these distributed paradigms, you will be well-equipped to excel in your Continuous Internal Evaluation for Module 5.