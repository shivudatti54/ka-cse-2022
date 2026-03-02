Of course. Here is a comprehensive educational note on Multiple-Processor Scheduling for  engineering students.

# **Module 2: Multiple-Processor Scheduling**

## **1. Introduction**

In a traditional single-processor system, scheduling focuses on selecting one process from the ready queue to run on the single CPU. However, modern computing heavily relies on **multiprocessor systems** (also called multi-core systems), where multiple processing cores reside on a single chip. This architecture introduces new complexities and opportunities for the operating system's scheduler. Multiple-processor scheduling is the mechanism by which the OS assigns processes to these multiple CPUs, aiming to maximize throughput, efficiency, and maintain load balance across all processors.

---

## **2. Core Concepts**

### **2.1. Types of Multiprocessor Systems**

1.  **Symmetric Multiprocessing (SMP):** This is the most common approach. Each processor is self-scheduling and operates independently. All processors are peers; each has its own private set of registers and cache, but they share the same main memory and I/O devices. The scheduler for each processor examines the shared ready queue and selects a process to run.
    *   **Advantage:** Simplicity and flexibility.
    *   **Challenge:** Must avoid having two processors choose the same process and ensure data structures are accessed atomically to prevent race conditions.

2.  **Asymmetric Multiprocessing (ASMP):** In this model, one master server processor handles all scheduling decisions, I/O processing, and other system activities. The other processors (slaves) only execute user code.
    *   **Advantage:** Simpler to implement as only one processor accesses system data structures.
    *   **Disadvantage:** The master can become a performance bottleneck.

### **2.2. Key Challenges in Multiple-Processor Scheduling**

*   **Processor Affinity:** When a process runs on a specific processor, the data in that processor's cache (e.g., L1, L2) becomes warm (contains the process's memory locations). Migrating the process to another processor invalidates this cache, causing a performance penalty known as a **cache miss**. To avoid this, schedulers try to keep a process on the same processor.
    *   **Soft Affinity:** The scheduler tries to keep a process on the same processor but does not guarantee it (e.g., if that CPU is overloaded).
    *   **Hard Affinity:** Allows a process to specify a set of processors it *must* run on, enforced by the OS.

*   **Load Balancing:** This is the process of redistributing the workload across all processors to ensure no CPU is idle while others have a long queue of processes. Load balancing is necessary to maximize CPU utilization but often conflicts with processor affinity.
    *   **Push Migration:** A specific task (e.g., a load balancer kernel thread) periodically checks the load on each processor. If an imbalance is found, it pushes processes from overloaded CPUs to idle ones.
    *   **Pull Migration:** An idle processor actively "pulls" a waiting task from a busy processor's queue.

*   **Synchronization:** With multiple schedulers (in SMP) accessing a shared ready queue, the OS must ensure that the queue's data structures are not corrupted. This is typically done using **spinlocks**. If a processor tries to acquire a lock held by another, it will "spin" in a loop waiting for the lock to be released. This is efficient for short wait times but wasteful for long critical sections.

### **2.3. Multi-Core Processors and Scheduling**

A multi-core chip is an SMP on a single physical package. While this reduces physical space and power consumption, it introduces a new consideration: **memory stall**. A thread may spend significant time waiting for data to become available from memory. To combat this, modern OS schedulers often use **chip multithreading**.

*   **Coarse-Grained Multithreading:** A thread executes on a core until a long-latency event (e.g., a cache miss) occurs. The core must then switch to another thread, which incurs a context-switch penalty.
*   **Fine-Grained Multithreading (Hyper-Threading):** The physical core has duplicate architectural states (like registers) but shares main execution resources (ALUs, caches). It can switch between logical threads at the instruction cycle level, interleaving instructions from multiple threads. This allows the core to better utilize its execution units, hiding memory latency. The OS scheduler sees each logical core as a separate CPU.

---

## **3. Example**

Consider a dual-core SMP Linux system with a shared ready queue.

1.  **Process A** starts executing on **CPU 0**. Its data gets cached in CPU 0's L1/L2 cache.
2.  The scheduler (due to a timer interrupt) preempts Process A on CPU 0.
3.  Now, the scheduler on **CPU 1** is looking for work. It finds **Process A** in the ready queue.
4.  **Without Affinity:** CPU 1 schedules Process A. When it runs, it experiences many cache misses because its data is not in CPU 1's cache, leading to slower performance as it fetches data from main memory.
5.  **With Affinity:** The scheduler on CPU 1, seeing that Process A was last run on CPU 0, might skip it in favor of another process (e.g., Process B) to respect soft affinity. This preserves the warm cache if Process A is later scheduled back on CPU 0.

---

## **4. Key Points / Summary**

| Concept | Description |
| :--- | :--- |
| **Goal** | To efficiently schedule processes across multiple CPUs, maximizing throughput and utilization. |
| **SMP vs. ASMP** | **SMP:** Each CPU self-schedules from a shared queue. **ASMP:** A master CPU controls all scheduling. |
| **Processor Affinity** | The tendency of a process to stay on the same CPU to avoid the performance cost of cache misses. |
| **Load Balancing** | Redistributing work across CPUs to prevent idling. Can **push** or **pull** processes. |
| **Synchronization** | Crucial for protecting shared scheduler data structures, often implemented using **spinlocks**. |
| **Multi-Core Consideration** | Schedulers must be aware of **memory stalls** and can leverage **hyper-threading** to improve core utilization. |
| **Trade-off** | A fundamental tension exists between **load balancing** (spreading work out) and **processor affinity** (keeping work together). |