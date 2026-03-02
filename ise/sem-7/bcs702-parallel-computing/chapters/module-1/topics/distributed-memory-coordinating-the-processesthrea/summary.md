# Distributed-Memory, Coordinating the Processes/Threads, Shared-Memory, Distributed-Memory

=====================================================================================

### Overview

---

This summary covers key concepts in parallel computing, focusing on distributed-memory, coordinating processes/threads, shared-memory, and distributed-memory.

### Definitions and Formulas

---

- **Distributed-Memory**: A parallel computing model where each processing unit (node) has its own memory, and data is exchanged between nodes through communication.
  - Formula: `T = T_P + T_C`, where `T` is the total time, `T_P` is the parallel time, and `T_C` is the communication time.
- **Shared-Memory**: A parallel computing model where all processing units have access to a shared memory space, allowing fast data sharing and minimal communication.
- **Coordinating Processes/Threads**: The process of managing and scheduling parallel processes or threads to execute concurrently, ensuring efficient resource utilization and minimizing overhead.
- **Load Balancing**: A technique to distribute workload evenly among nodes in a distributed-memory system.

### Distributed-Memory

---

- **Advantages**:
  - Scalability
  - Flexibility
  - Easy to implement
- **Disadvantages**:
  - Higher communication overhead
  - Complexity in managing and coordinating processes
- **Parallel Algorithms**:
  - Message Passing (MP) paradigm
  - Remote Procedure Call (RPC) paradigm

### Shared-Memory

---

- **Advantages**:
  - Faster data access
  - Reduced communication overhead
  - Simplified programming model
- **Disadvantages**:
  - Limited scalability
  - Shared memory can be a bottleneck
- **Parallel Algorithms**:
  - Shared-Memory Parallelism (SMP) paradigm
  - Data Parallelism (DP) paradigm

### Coordinating Processes/Threads

---

- **Scheduling Algorithms**:
  - Earliest Deadline First (EDF)
  - Rate Monotonic Scheduling (RMS)
  - Priority Scheduling
- **Process Synchronization**:
  - Semaphores
  - Monitors
  - Condition Variables
- **Deadlocks and Starvation**:
  - Causes and effects
  - Prevention techniques

### Distributed-Memory Revision Notes

---

- **Key Concepts**:
  - Distributed-memory model
  - Communication overhead
  - Load balancing
- **Parallel Algorithms**:
  - MP paradigm
  - RPC paradigm
- **Challenges**:
  - Scalability
  - Complexity in managing and coordinating processes
