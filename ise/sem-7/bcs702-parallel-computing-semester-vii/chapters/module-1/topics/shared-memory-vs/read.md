# Shared-Memory vs Distributed-Memory Systems

## Introduction to Parallel Memory Architectures

In parallel computing, the way memory is organized and accessed by multiple processors is a fundamental distinction that shapes both the hardware design and the software programming model. The two primary architectures are **Shared-Memory** and **Distributed-Memory**. Understanding their differences is crucial for selecting the right parallel programming approach, as outlined in Modules 3 (MPI) and 4 (OpenMP) of your syllabus.

## Shared-Memory Systems

### Core Concept
In a shared-memory system, multiple processing units (CPUs/cores) have access to a single, common, unified address space. This means all processors can read from and write to the same main memory locations. Coordination between processors is handled through this shared memory.

### Key Characteristics
*   **Uniform Memory Access (UMA):** All processors have equal access time to all memory locations. This is typical in Symmetric Multiprocessing (SMP) systems, like a multi-core CPU.
*   **Non-Uniform Memory Access (NUMA):** Access time to memory depends on the memory location relative to the processor. Memory is physically distributed but remains logically shared. A processor can access its local memory faster than the memory attached to another processor.

### Hardware Implementation
A shared-memory system is often built using a single physical machine with multiple processors/cores connected via a system bus or a crossbar switch to a common memory bank.

```
+-------------------------------------------------+
|                 Shared Global Memory            |
+-------------------------------------------------+
|   Memory Controller   |   Memory Controller     |
+--------||-------------||--------||--------------+
         ||             ||        ||
+--------\/-------------\/--------\/--------------+
|    Core 0    |    Core 1    |    Core 2    | ... |
|   (CPU 0)   |   (CPU 1)   |   (CPU 2)   |     |
+-------------+-------------+-------------+-----+
|                 System Bus / Interconnect      |
+-------------------------------------------------+
```

### Programming Model (e.g., OpenMP)
Programming for shared-memory systems is often considered simpler for beginners. Programmers use directives, pragmas, and libraries to manage threads that all operate on the same data in the global address space. Synchronization primitives like locks and semaphores are crucial to prevent race conditions when multiple threads write to the same memory location.

**Example (Pseudocode):**
```cpp
#pragma omp parallel for
for (i = 0; i < N; i++) {
    shared_array[i] = compute(i); // All threads write to shared memory
}
// Synchronization is implicit at the end of the parallel loop
```

### Advantages
*   **Ease of Programming:** The global address space is easier to reason about. Data sharing between threads is implicit and fast.
*   **Dynamic Load Balancing:** The system can often dynamically allocate work to processors, as all data is equally accessible.
*   **No Explicit Data Partitioning:** The programmer does not need to manually split and distribute data structures across memories.

### Disadvantages
*   **Scalability Limitation:** The memory bandwidth and the system bus can become a severe bottleneck as the number of processors increases, limiting scalability to tens or hundreds of cores.
*   **Memory Coherence Overhead:** Hardware must ensure **cache coherence** (e.g., using the MESI protocol), which adds complexity and overhead. This keeps all processor caches synchronized with the main memory and each other.
*   **Synchronization Complexity:** While sharing is easy, controlling access to shared data with locks and mutexes can introduce bugs like deadlocks and performance issues.

## Distributed-Memory Systems

### Core Concept
In a distributed-memory system, each processor has its own local private memory. There is no global memory address space. Processors are connected via a high-speed network (an **interconnection network** like InfiniBand, Ethernet, or a custom mesh) and must communicate explicitly by passing messages.

### Key Characteristics
*   **Local Memory Access:** Each processor operates on data in its own local memory. Access to this local memory is very fast.
*   **Explicit Communication:** To operate on non-local data, processors must explicitly send and receive messages over the network.
*   **Scalability:** These systems are highly scalable. Adding more nodes (processor + memory pairs) adds more aggregate memory bandwidth and computational power.

### Hardware Implementation
A distributed-memory system is a cluster of independent machines (nodes), each with its own CPU(s) and memory.

```
+--------------+    +--------------+    +--------------+
|   Node 0     |    |   Node 1     |    |   Node 2     |
| +----------+ |    | +----------+ |    | +----------+ |
| | Processor| |    | | Processor| |    | | Processor| |
| +----------+ |    | +----------+ |    | +----------+ |
|      |       |    |      |       |    |      |       |
| +----------+ |    | +----------+ |    | +----------+ |
| | Local    | |    | | Local    | |    | | Local    | |
| | Memory   | |    | | Memory   | |    | | Memory   | |
| +----------+ |    | +----------+ |    | +----------+ |
+------||------+    +------||------+    +------||------+
       ||                 ||                 ||
       \\-----------------||-----------------//
         \\========== Interconnect =========//
          (e.g., Network Switch, Mesh)
```

### Programming Model (e.g., MPI)
Programming for distributed memory uses a message-passing model. The programmer is responsible for decomposing the problem, partitioning the data, and explicitly defining communication points using send and receive operations.

**Example (Pseudocode, inspired by MPI):**
```cpp
if (my_rank == 0) { // Process 0 is the sender
    data = prepare_data();
    send(data, destination: 1); // Explicitly send data to Process 1
} else if (my_rank == 1) { // Process 1 is the receiver
    receive(data, source: 0); // Explicitly receive data from Process 0
    process(data);
}
// Each process operates on its own local copy of 'data'
```

### Advantages
*   **High Scalability:** Can be scaled to thousands or even millions of cores by adding more nodes. The memory bandwidth scales with the number of nodes.
*   **No Cache Coherence Overhead:** Since there is no shared memory, there is no need for complex and expensive hardware cache coherence protocols.
*   **Cost-Effectiveness:** Can be built from commodity, off-the-shelf components.

### Disadvantages
*   **Complex Programming:** The programmer must manage data decomposition, distribution, and all communication, which adds significant complexity.
*   **Communication Overhead:** The latency and bandwidth of the network can become a performance bottleneck. Careful algorithm design is needed to minimize communication.
*   **Load Balancing:** The programmer must often statically balance the computational load across nodes to avoid idle processors waiting for others.

## Comparative Analysis: Shared vs. Distributed Memory

| Feature | Shared-Memory (UMA/NUMA) | Distributed-Memory (Clusters) |
| :--- | :--- | :--- |
| **Memory Address Space** | Single, global address space | Multiple, private address spaces |
| **Data Sharing** | Implicit (through reads/writes to memory) | Explicit (through message passing) |
| **Hardware** | Single physical machine with multiple CPUs/cores | Network of independent nodes |
| **Scalability** | Limited by memory/bus bandwidth (10s-100s of cores) | Highly scalable (1000s-1000000s of cores) |
| **Programming Model** | Multithreading (e.g., OpenMP, Pthreads) | Message Passing (e.g., MPI) |
| **Ease of Programming** | Easier for data-sharing, harder for synchronization | Harder due to explicit communication |
| **Key Challenge** | Cache coherence, memory contention | Communication latency/bandwidth |
| **Cost** | Higher for large, coherent systems | Lower, uses commodity hardware |
| **Typical Use Case** | Multi-core servers, workstations | Supercomputers, large compute clusters |

## Hybrid Models

Many modern high-performance computing (HPC) systems are **hybrid architectures**. They combine both models. A cluster (distributed memory) is made up of individual nodes, each of which is a multi-core shared-memory machine (e.g., a multi-socket server).

This leads to hybrid programming models, such as:
*   **MPI + OpenMP:** Use MPI for communication between nodes and OpenMP for parallelism within a node. This exploits the shared memory within a node for efficient data sharing and uses message passing for scalable communication across nodes.

## Exam Tips

1.  **Understand the Core Difference:** The fundamental distinction is the address space—**one** vs. **many**. All other differences (programming, scalability, hardware) stem from this.
2.  **Link to Syllabus Modules:** Clearly associate **Shared-Memory with OpenMP** (Module 4) and **Distributed-Memory with MPI** (Module 3). Be prepared to explain why each is suited to its respective architecture.
3.  **Know the Trade-offs:** Be ready to discuss the pros and cons of each architecture. Scalability vs. ease of programming is a classic trade-off.
4.  **Visualize the Diagrams:** Being able to draw and label the simple architectural diagrams for each system will help you score points in descriptive answers.
5.  **Mention Hybrid Systems:** Acknowledging that modern systems are often hybrid shows a deeper understanding of real-world HPC.
6.  **Use Correct Terminology:** Precisely use terms like "address space," "message passing," "cache coherence," "interconnection network," "UMA/NUMA," and "synchronization."