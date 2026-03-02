### **Learning Purpose: Module 3 - Global States**

**1. Why is this topic important?**
Understanding global states is fundamental to building and analyzing reliable distributed systems. Since these systems lack a single global clock or shared memory, determining a consistent, system-wide view of the state (e.g., the status of all processes and communication channels) is a core challenge. This concept is critical for tasks like debugging, monitoring, and ensuring system correctness.

**2. What will students learn?**
Students will learn the formal definition of a global state (a "snapshot") and the challenges in capturing it due to concurrency and message delays. They will study algorithms, such as the Chandy-Lamport snapshot algorithm, for recording a consistent global state without halting system execution. This includes understanding concepts like consistent cuts, event ordering, and the difference between physical and logical time.

**3. How does it connect to other concepts?**
This topic directly builds upon earlier concepts of concurrency, message passing, and logical clocks (e.g., Lamport timestamps). It provides the foundational theory necessary for implementing more advanced distributed protocols, including those for distributed deadlock detection, checkpointing and recovery, distributed garbage collection, and ensuring stable properties.

**4. Real-world applications**
Recording a global state is essential for:

- **System Monitoring & Debugging:** Taking a snapshot of a live system (e.g., a cloud computing cluster) to diagnose issues.
- **Checkpointing:** Periodically saving the state of a long-running distributed computation (e.g., in Apache Flink or Spark) to enable recovery from failures.
- **Deadlock Detection:** Identifying a circular wait condition across multiple machines in a distributed database or network.
