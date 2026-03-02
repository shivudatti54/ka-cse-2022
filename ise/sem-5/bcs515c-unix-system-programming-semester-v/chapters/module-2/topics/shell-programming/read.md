# Introduction to Parallel Programming

## What is Parallel Programming?

Parallel programming is the process of designing and implementing software that can execute multiple operations simultaneously. Unlike traditional sequential programming where instructions are executed one after another, parallel programming leverages multiple processing units to solve problems faster by dividing work among them.

The fundamental goal is to **decrease execution time** and **increase computational throughput** by utilizing multiple processors, cores, or computing nodes working concurrently on different parts of a problem.

## The Need for Parallel Computing

Several factors drive the need for parallel computing:

1.  **Physical Limitations:** The speed of light and quantum effects limit how fast a single processor can operate (clock frequency).
2.  **Power Consumption:** Increasing clock frequency leads to unsustainable power consumption and heat generation (power wall).
3.  **Big Data:** Modern scientific, engineering, and commercial applications process massive datasets that are impractical for single processors.
4.  **Real-time Processing:** Applications like weather forecasting, financial modeling, and AI require results in a feasible timeframe.

## Parallel Hardware Architectures

Parallel hardware can be classified based on how processors access memory.

### Flynn's Taxonomy

This is a classic classification system for computer architectures:

| Architecture                                   | Description                                                                                        | Example                  |
| :--------------------------------------------- | :------------------------------------------------------------------------------------------------- | :----------------------- |
| **SISD** (Single Instruction, Single Data)     | A single processor executes a single instruction stream on a single data stream.                   | Traditional uniprocessor |
| **SIMD** (Single Instruction, Multiple Data)   | A single instruction is executed simultaneously by multiple processors on different data elements. | GPUs, Vector Processors  |
| **MISD** (Multiple Instruction, Single Data)   | Multiple instructions operate on a single data stream. Rarely used.                                | Fault-tolerant systems   |
| **MIMD** (Multiple Instruction, Multiple Data) | Multiple processors execute different instruction streams on different data streams.               | Multicore CPUs, Clusters |

#### SIMD Explained

In SIMD, a control unit broadcasts the same instruction to all processing elements (PEs), but each PE applies it to its own local data. This is highly efficient for data-parallel tasks.

```
Control Unit
    |
    | (Broadcasts Instruction)
    |
+---+---+---+---+
| PE | PE | PE | PE |
+---+---+---+---+
| D1 | D2 | D3 | D4 |
+---+---+---+---+
```

_Example: Adding a constant value to every element in a large array._

#### MIMD Explained

MIMD is the most common architecture. Each processor fetches its own instructions and operates on its own data, allowing for more flexible task and data parallelism.

```
+-----------------+    +-----------------+
| Processor + Mem |    | Processor + Mem |
| Instruction Stream A |    | Instruction Stream B |
| Data Stream A       |    | Data Stream B       |
+-----------------+    +-----------------+
```

_Example: Different processors calculating different parts of a scientific simulation._

### Memory Architectures: Shared vs. Distributed

#### 1. Shared-Memory Systems

All processors share a common, global address space. They can access the same memory modules.

- **Uniform Memory Access (UMA):** Access time to memory is the same for all processors (symmetric multiprocessing - SMP).
  ```
  +-----+    +-----+    +-----+
  | CPU |    | CPU |    | CPU |
  +-----+    +-----+    +-----+
      \        |        /
       \       |       /
        \      |      /
      +-----------------+
      |   Global Memory |
      +-----------------+
  ```
- **Non-Uniform Memory Access (NUMA):** Access time depends on the memory location relative to the processor. Memory is physically distributed but logically shared.
  ```
  +-----------+---------+    +-----------+---------+
  | Processor | Local   |    | Processor | Local   |
  |           | Memory  |    |           | Memory  |
  +-----------+---------+    +-----------+---------+
          |                         |
          +-------------------------+
                    Interconnect
  ```
  _Advantages:_ Easier to program due to a single memory view.
  _Disadvantages:_ Memory bandwidth can become a bottleneck; harder to scale.

#### 2. Distributed-Memory Systems

Each processor has its own private memory. There is no global address space. Processors communicate by passing messages (e.g., MPI) over an interconnection network.

```
+-----------------+    +-----------------+
| Processor + Mem |    | Processor + Mem |
+-----------------+    +-----------------+
        |                       |
        +-----------------------+
              Interconnect
```

_Advantages:_ Highly scalable; avoids memory contention.
_Disadvantages:_ More complex to program; requires explicit communication.

### Interconnection Networks

The network connecting processors and memory is critical for performance. Topologies define how components are wired together.

| Topology      | Diagram                      | Pros                             | Cons                                            |
| :------------ | :--------------------------- | :------------------------------- | :---------------------------------------------- | ------------------ | ---------------- | -------------- |
| **Bus**       | `P0--P1--P2--P3--...--Pn`    | Simple, inexpensive              | Becomes a bottleneck with many devices          |
| **Ring**      | `P0 -> P1 -> P2 -> P3 -> P0` | Simple, bidirectional            | Latency increases with number of nodes          |
| **Mesh**      | `P00-P01-P02`<br>`           |                                  |                                                 | `<br>`P10-P11-P12` | Good scalability | Uneven latency |
| **Hypercube** | Complex multi-dimensional    | Very low latency, high bandwidth | Complex wiring, number of nodes is a power of 2 |

### The Cache Coherence Problem

In shared-memory multicore systems, each core has its own small, fast cache memory. This introduces the **cache coherence** problem: multiple copies of the same data (e.g., variable `x`) can exist in different caches. If one core updates its copy, the others become stale (inconsistent).

**Solution: Cache Coherence Protocols**
Protocols like **MESI** (Modified, Exclusive, Shared, Invalid) ensure all caches have a consistent view of memory.

- **M (Modified):** The cache line is dirty (changed) and is the only copy.
- **E (Exclusive):** The cache line is clean (matches main memory) and is the only copy.
- **S (Shared):** The cache line is clean and other caches may have a copy.
- **I (Invalid):** The cache line is stale and cannot be used.

These states transition as processors read and write data, triggering communication between caches to maintain consistency. This is a crucial overhead in shared-memory systems.

## Parallel Software Concepts

### Programming Models

1.  **Shared Memory Model (e.g., OpenMP, Pthreads):** Threads communicate by reading and writing shared variables. The programmer is responsible for synchronizing access to avoid race conditions.
2.  **Message Passing Model (e.g., MPI):** Processes have separate address spaces. They explicitly send and receive messages to exchange data and coordinate work.
3.  **Data Parallel Model (e.g., CUDA, OpenCL):** The same operation is applied concurrently to different elements in a data structure. Well-suited for SIMD/GPU architectures.

### Key Challenges

- **Partitioning:** Dividing the problem and its data among processing units (Domain Decomposition vs. Functional Decomposition).
- **Communication:** The overhead of exchanging data between processes/threads.
- **Synchronization:** Coordinating the tasks to ensure correct results (e.g., locks, barriers).
- **Load Balancing:** Ensuring all processing units are kept busy to maximize efficiency.

## Exam Tips

1.  **Understand Flynn's Taxonomy:** Be able to define SISD, SIMD, MIMD, and MISD and give clear examples of each. This is a common exam question.
2.  **Contrast Shared vs. Distributed Memory:** Create a mental table comparing their programming complexity, scalability, and communication methods. You will likely be asked to compare and contrast them.
3.  **Explain Cache Coherence:** Don't just state the problem; be prepared to explain _why_ it happens (multiple caches) and _how_ it's solved (protocols like MESI).
4.  **Visualize Topologies:** Be able to sketch simple diagrams of bus, ring, and mesh networks and discuss their advantages/disadvantages.
5.  **Connect Hardware to Software:** Understand which programming models (shared memory/message passing) are most naturally suited to which hardware architectures.
