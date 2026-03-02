# Introduction to Parallel Programming

=====================================

### Overview

Parallel programming is the process of designing software that executes multiple operations simultaneously using multiple processing units. It aims to decrease execution time and increase computational throughput by dividing work among processors, cores, or computing nodes working concurrently.

### Key Points

- **Need for Parallelism:** Physical limitations (speed of light), power wall (unsustainable heat from higher clock speeds), big data processing, and real-time requirements drive parallel computing.
- **Flynn's Taxonomy:** SISD (sequential, single core), SIMD (same instruction on multiple data, GPUs), MISD (rare, fault-tolerant systems), MIMD (different instructions on different data, multicore CPUs, clusters).
- **Shared Memory (UMA/NUMA):** All processors share a global address space; UMA has equal access time, NUMA has location-dependent access time.
- **Distributed Memory:** Each processor has private memory; communication via message passing (MPI) over an interconnection network.
- **Cache Coherence:** Multiple caches can hold stale copies of shared data; MESI protocol (Modified, Exclusive, Shared, Invalid) maintains consistency.
- **Programming Models:** Shared memory (OpenMP, Pthreads), message passing (MPI), data parallel (CUDA, OpenCL).
- **Key Challenges:** Partitioning (domain vs functional decomposition), communication overhead, synchronization (locks, barriers), and load balancing.

### Important Concepts

- Flynn's Taxonomy classifies architectures by instruction streams and data streams
- SIMD: control unit broadcasts one instruction to all PEs, each operates on local data
- MIMD: most common; each processor fetches own instructions, operates on own data
- Interconnection topologies: bus (simple, bottleneck), ring, mesh (scalable), hypercube (low latency, complex)

### Notes

- Be able to define SISD, SIMD, MIMD, MISD with clear examples; this is a common exam question.
- Create a mental comparison table for shared vs distributed memory covering programming, scalability, and communication.
- Connect hardware architectures to their natural programming models (shared memory to OpenMP, distributed to MPI).
