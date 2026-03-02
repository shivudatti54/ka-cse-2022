**Subject: Distributed Systems (18CSMP65)**
**Module 5: Distributed File Systems & Distributed Shared Memory**
**Topic: Continuous Internal Evaluation (CIE)**

### Introduction to CIE in Distributed Systems

The Continuous Internal Evaluation (CIE) is a structured assessment method designed to gauge your understanding of the subject matter consistently throughout the semester, rather than relying solely on a single final examination. For a complex and foundational subject like Distributed Systems, CIE ensures you build and retain knowledge incrementally. This module, covering Distributed File Systems (DFS) like NFS and AFS, and the challenging concept of Distributed Shared Memory (DSM), is particularly suited for this form of assessment due to its mix of theoretical models and practical architectural implementations.

---

### Core Concepts of CIE and Its Application

The CIE process for this module is typically broken down into components that test different cognitive levels—from remembering facts to applying concepts to solve novel problems.

**1. Components of CIE:**
CIE is not a single exam but a series of evaluations. For a theory-oriented module like this, it often includes:
*   **Unit Tests / Quizzes:** Short, focused tests on specific sub-topics (e.g., a quiz on NFS architecture or DSM consistency models). These check your foundational knowledge.
*   **Assignments:** Detailed problems requiring you to apply concepts. For example, you might be asked to compare the sync and async replication models in a DFS or design a simple DSM protocol for a given scenario.
*   **Mini-Project / Case Study Analysis:** A significant component where you research a real-world system (e.g., analyze the Google File System (GFS) as a case study of a DFS or examine the coherence protocols used in modern NUMA architectures as a form of DSM). This develops research and analytical skills.
*   **Seminar / Presentation:** Explaining a complex topic like the "Session Semantics" of AFS or the "Migrant/Home-based" approach in DSM to your peers reinforces your own understanding and improves communication skills.

**2. Aligning CIE with Module 5 Content:**
The questions and tasks in CIE are designed to map directly to the key learning outcomes of the module.

*   **For Distributed File Systems (DFS):**
    *   **Conceptual Understanding:** A CIE question might ask: "Explain the key design goals of a DFS (transparency, concurrency, replication, etc.)." This tests your knowledge of core principles.
    *   **Comparative Analysis:** An assignment could be: "Compare and contrast the client-side caching mechanisms of NFSv4 and AFS, highlighting their impact on performance and consistency." This tests higher-order analytical skills.
    *   **Example:** You might be given a scenario: "An NFS client machine crashes after writing a file but before the server's write-behind cache is flushed. What are the implications for data consistency?" This tests application of knowledge.

*   **For Distributed Shared Memory (DSM):**
    *   **Model Identification:** A quiz question could be: "Which DSM consistency model (Sequential, Release, Entry) would be most suitable for a parallel matrix multiplication algorithm? Justify your answer."
    *   **Protocol Design:** An advanced assignment might task you with outlining a simple write-invalidate protocol for a page-based DSM system, explaining the message exchange between nodes when a page is updated.
    *   **Problem Solving:** A test problem could be: "Identify a potential false sharing scenario in a DSM and propose a solution to avoid it." This tests your ability to identify and solve real-world implementation issues.

**3. The Purpose Beyond Grading:**
The true value of CIE is formative. Poor performance on a quiz about consistency models acts as an early warning, indicating you need to revisit that topic. Feedback from assignments guides your study focus. It transforms assessment from a one-time judgment into an ongoing feedback loop for learning.

---

### Key Points & Summary

*   **Purpose of CIE:** To provide continuous, formative assessment that promotes consistent learning and identifies knowledge gaps early in the semester.
*   **Relevance to Module 5:** The concepts of DFS and DSM are layered and complex. CIE breaks them down into manageable, assessable chunks, ensuring you understand the architecture of systems like NFS and the abstract models of DSM coherence.
*   **Common CIE Components:** Includes unit tests (for fundamentals), assignments (for application), and case studies/mini-projects (for analysis and synthesis of real-world systems).
*   **Focus Areas for Assessment:**
    *   **DFS:** Design goals, transparency, caching, replication strategies, and specific system architectures (NFS, AFS).
    *   **DSM:** Various consistency models (e.g., Sequential, Weak, Release), implementation issues (granularity, false sharing), and replication techniques.
*   **Strategic Approach:** Use CIE as a tool for learning. Actively engage with each component, seek feedback, and revise concepts based on your performance. This will not only help you score well in CIE but will also build a strong foundation for the final end-semester examination.