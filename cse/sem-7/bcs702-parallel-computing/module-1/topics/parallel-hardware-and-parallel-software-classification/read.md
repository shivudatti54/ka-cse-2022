# Module 1: Parallel Hardware & Software - Classifications of Parallel Computers

## 1. Introduction

The relentless demand for higher computational power to solve complex problems in science, engineering, and data analysis has driven the evolution from single-processor systems to **parallel computers**. A parallel computer is defined as a collection of processing elements that cooperate to solve large problems faster by working concurrently on different parts of the problem. Understanding how these systems are classified is fundamental to grasping the landscape of parallel computing. This module explores the primary classifications of parallel computers based on their underlying hardware architecture, memory organization, and programming paradigms.

## 2. Flynn's Taxonomy

The most widely used framework for classifying parallel computers is **Flynn's Taxonomy** (1966), proposed by Michael J. Flynn. This taxonomy categorizes computer architectures based on the number of concurrent **instruction streams** (the sequence of instructions executed by a processor) and **data streams** (the sequence of data elements processed) they can handle.

### 2.1 Single Instruction, Single Data (SISD)

This represents the traditional sequential von Neumann computer architecture. A single processor executes a single instruction stream to operate on a single data stream. Instructions are processed one at a time in a strictly sequential manner.

- **Mathematical Model:** Let $I = (I_1, I_2, \ldots, I_n)$ be the instruction stream and $D = (d_1, d_2, \ldots, d_n)$ be the data stream. SISD computes sequentially: $I_1(d_1) \rightarrow I_2(d_2) \rightarrow \ldots \rightarrow I_n(d_n)$.
- **Example:** Conventional single-core desktop CPUs (e.g., Intel Core i3, AMD Ryzen 3).

### 2.2 Single Instruction, Multiple Data (SIMD)

In the SIMD model, a single control unit broadcasts the same instruction to multiple processing elements (PEs) operating in lockstep. Each PE executes this identical instruction simultaneously but operates on its own local data element. This architecture exploits **data-level parallelism** where the same operation is performed on multiple data points concurrently.

- **Mathematical Model:** For $n$ processing elements $PE_1, PE_2, \ldots, PE_n$, the operation $OP$ is applied as: $\{d_1, d_2, \ldots, d_n\} \xrightarrow{OP} \{OP(d_1), OP(d_2), \ldots, OP(d_n)\}$ in a single clock cycle.
- **Example:** Vector processors (e.g., Cray vector machines), Graphics Processing Units (GPUs), and SIMD extensions (SSE, AVX). A classic application is element-wise array addition: for arrays $A$ and $B$, computing $C[i] = A[i] + B[i]$ for all $i$.
- **Advantages:** Low control unit complexity, efficient for regular data-parallel computations.
- **Limitations:** Cannot handle irregular parallelism or branch-heavy code effectively.

### 2.3 Multiple Instruction, Single Data (MISD)

This is a rare and primarily theoretical classification. Multiple processing units execute different instruction streams on the same single data stream. Each processor applies its own algorithm to the incoming data, producing different results from the same input.

- **Mathematical Model:** For processors $P_1, P_2, \ldots, P_k$ and input data $d$, each processor computes $P_i(d) = f_i(d)$ where $f_i \neq f_j$ for $i \neq j$.
- **Application:** Primarily used in specialized fault-tolerant systems and redundant computations. A flight control system where multiple computers process identical sensor data using different control algorithms, with outputs compared for error detection.
- **Example:** The Space Shuttle flight control computers used multiple processors executing different software for reliability.

### 2.4 Multiple Instruction, Multiple Data (MIMD)

This is the most common and flexible general-purpose parallel computer architecture. In MIMD systems, multiple processors operate independently and asynchronously, each executing its own instruction stream on its own data stream. Processors coordinate through explicit communication or shared memory.

- **Mathematical Model:** $P$ processors execute instruction streams $\{I^1, I^2, \ldots, I^P\}$ on data $\{D^1, D^2, \ldots, D^P\}$ respectively, with potential synchronization points: $S = \{sync_1, sync_2, \ldots, sync_m\}$.
- **Example:** Modern multi-core CPUs, clusters of workstations, and large supercomputers (e.g., IBM Blue Gene, Sunway TaihuLight).

## 3. Memory Architecture (MIMD Systems)

Since MIMD dominates contemporary parallel computing, it is further subdivided based on memory organization and access patterns.

### 3.1 Shared Memory Multiprocessors

All processors share a single, global address space. Any processor can directly access any memory location. This simplifies programming but introduces challenges in **cache coherence** and memory contention.

#### 3.1.1 Uniform Memory Access (UMA)

All processors have equal access time to any memory location. Also known as Symmetric Multiprocessing (SMP). The memory controller ensures uniform latency.

- **Architecture:** $\text{Access Time}(P_i, M_j) = c$ for all $i, j$, where $c$ is a constant.
- **Example:** Multi-socket servers with multiple CPUs accessing shared DRAM (e.g., Dell PowerEdge, HP ProLiant).
- **Limitations:** Scalability constrained by memory bandwidth and interconnection network.

#### 3.1.2 Non-Uniform Memory Access (NUMA)

Access time depends on the physical distance between processor and memory location. Local memory attached to a processor is faster than remote memory.

- **Architecture:** $\text{Access Time}(P_i, M_i) < \text{Access Time}(P_i, M_j)$ for $i \neq j$, where $M_i$ is local memory and $M_j$ is remote memory.
- **Example:** AMD Opteron multi-socket systems, Intel QuickPath Interconnect (QPI) systems.
- **Performance Implication:** Programmers must consider data locality to minimize remote memory accesses.

**Cache Coherence Protocols:** In shared-memory systems with private caches, maintaining consistency is critical:

- **Snooping Protocols:** Cache controllers monitor bus/network transactions. The **MESI protocol** (Modified, Exclusive, Shared, Invalid) is widely used, where cache lines can be in one of four states, and invalidation or broadcast updates maintain coherence.
- **Directory-Based Protocols:** A central directory maintains the state of each memory block, tracking which caches hold copies. When a processor requests a block, the directory coordinates the data transfer or invalidation.

### 3.2 Distributed Memory Multiprocessors

Each processor has its own local private memory with no global address space. Processors cannot directly access another processor's memory. Communication occurs explicitly via **message passing** over an interconnection network.

- **Mathematical Model:** Memory consists of $P$ partitions $\{M_1, M_2, \ldots, M_P\}$, where processor $P_i$ can only access $M_i$ directly. Communication requires explicit send/receive operations: $\text{Send}(M_i, j) \leftrightarrow \text{Receive}(M_j, i)$.
- **Example:** Beowulf clusters, supercomputers (e.g., IBM SP2), and modern GPU clusters.
- **Interconnection Networks:** Performance heavily depends on network topology (bus, hypercube, mesh, torus) and routing algorithms. **Bandwidth** and **latency** are critical metrics.

## 4. Parallel Software Classification

Parallel software classification addresses how computation is structured and coordinated, independent of the underlying hardware.

### 4.1 Single Program Multiple Data (SPMD)

Multiple instances of the same program execute concurrently on different processors, each operating on different data. Processors may follow divergent execution paths based on their rank or local conditions, synchronizing at specific points.

- **Execution Model:** $P$ processors execute program $P$ with unique process ID $pid \in \{0, 1, \ldots, P-1\}$. Each process operates on data subset $D_{pid}$.
- **Example:** MPI programs where rank 0 distributes data and gathers results; distributed matrix multiplication.

### 4.2 Multiple Program Multiple Data (MPMD)

Different processors execute different programs or distinct subroutines, potentially developed and compiled separately. This model suits heterogeneous systems where specialized processors perform specific tasks.

- **Example:** A simulation where one processor handles fluid dynamics (CFD), another handles structural analysis, and a third manages visualization.

### 4.3 Data Parallelism vs. Task Parallelism

- **Data Parallelism:** The same operation is applied concurrently to multiple data elements (mirrors SIMD). Examples: array operations, image processing pipelines.
- **Task Parallelism:** Different operations execute concurrently on different data (mirrors MIMD). Examples: pipeline stages, independent computational tasks.

### 4.4 Programming Models

- **Shared Memory Model (e.g., OpenMP):** Processors share a global address space; synchronization via locks, barriers, and atomic operations.
- **Message Passing Model (e.g., MPI):** Explicit communication between processes with send/receive primitives.
- **Accelerator Model (e.g., CUDA, OpenCL):** Host CPU offloads compute-intensive kernels to accelerators (GPUs, FPGAs).

## 5. Performance Considerations: Amdahl's Law

The theoretical speedup $S$ achievable by parallelization is governed by **Amdahl's Law**.

- **Theorem (Amdahl's Law):** If $f$ is the fraction of a computation that must be executed serially, and $(1-f)$ is the perfectly parallelizable portion, then the maximum speedup with $P$ processors is:
  $$S(P) \leq \frac{1}{f + \frac{1-f}{P}} = \frac{P}{1 + f(P-1)}$$

- **Proof:** Let $T_1$ be execution time on a single processor. The serial portion takes time $f \cdot T_1$. The parallel portion, executed on $P$ processors, takes time $\frac{(1-f) \cdot T_1}{P}$. Total parallel time:
  $$T_P = f \cdot T_1 + \frac{(1-f) \cdot T_1}{P} = T_1 \left(f + \frac{1-f}{P}\right)$$
  Therefore, speedup $S(P) = \frac{T_1}{T_P} = \frac{1}{f + \frac{1-f}{P}}$.

- **Implication:** As $P \to \infty$, $S(P) \to \frac{1}{f}$, demonstrating the fundamental limitation of parallel computing: even with infinite processors, speedup is bounded by the reciprocal of the serial fraction.

- **Example:** If $f = 0.05$ (5% serial), maximum theoretical speedup is 20× regardless of processor count.

---

## 6. Assessment

### Multiple Choice Questions

**Question 1:** A system comprises 64 processing elements, each executing the same instruction in lockstep on different data elements. Which Flynn category and memory architecture best describe this system?

- (a) MIMD, Distributed Memory
- (b) SIMD, Shared Memory
- (c) SIMD, Distributed Memory
- (d) MISD, Shared Memory

**Question 2:** Consider a program where 90% of execution time is parallelizable. Using 16 processors, what is the maximum theoretical speedup according to Amdahl's Law?

- (a) 10.27×
- (b) 14.4×
- (c) 16×
- (d) 8×

**Question 3:** In a NUMA system with 4 sockets, each socket has local memory of 64 GB. If a process on Socket 0 accesses its local memory in 50 ns, what is the approximate access time to memory on Socket 2?

- (a) 50 ns
- (b) 100-150 ns
- (c) 200-300 ns
- (d) 400-500 ns

**Question 4:** Which programming model is most appropriate for a heterogeneous system where CPUs handle control logic and GPUs accelerate matrix operations?

- (a) Pure MPI
- (b) OpenMP only
- (c) CUDA/OpenCL with host offloading
- (d) MapReduce

**Question 5:** A cache coherence protocol where each cache controller monitors broadcast bus transactions to maintain consistency is called:

- (a) Directory-based protocol
- (b) Snooping protocol
- (c) Write-back protocol
- (d) Circuit switching protocol
