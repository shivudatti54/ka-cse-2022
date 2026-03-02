# **9.4.2 Deadlock Detection and Prevention Algorithms**

- **Definition:** A set of processes that are blocked indefinitely, waiting for each other to release resources.
- **Characteristics:** Alternating resource allocation (one process allocates a resource, another releases it, and the first process waits), Mutual Exclusion (each process requires exclusive access to a resource), Hold and Wait (a process holds a resource and waits for another), No Preemption (the operating system doesn't interrupt a process to give up its resources).
- **Deadlock Detection Algorithms:**
  - Banker's Algorithm
  - Safety Analysis
  - Resource Allocation Graph (RAG)
- **Deadlock Prevention Algorithms:**
  - **Solution 1:** Timeout Algorithm
  - **Solution 2:** Resource Preemption
  - **Solution 3:** Resource Deallocation
- **Important Formulas and Definitions:**
  - Banker's Algorithm: `max(0, R_i) ≤ r_j`
  - Safety Theorem: If `R_i` and `M` are safe, then `R_i + M` is safe.
  - **Theorem:** If `R` is a safe sequence of resource allocations, then `R(i+1) = R(i) + M` is safe.

**Revision Tips:**

- Understand the characteristics of deadlocks.
- Familiarize yourself with deadlock detection and prevention algorithms.
- Focus on the key formulas and theorems that support the algorithms.
