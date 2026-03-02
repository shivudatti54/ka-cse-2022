# Distributed Memory Systems

=====================================

### Overview

In a distributed-memory system, each processor has its own local private memory with no global address space. Processors communicate explicitly by passing messages over an interconnection network. This architecture is highly scalable and forms the basis for clusters, supercomputers, and large-scale parallel systems programmed using MPI.

### Key Points

- **Private Address Spaces:** Each processor operates on data in its own local memory; no processor can directly access another's memory.
- **Explicit Communication:** Processors must use send and receive operations to exchange data over a network (e.g., InfiniBand, Ethernet).
- **High Scalability:** Adding more nodes increases both computational power and aggregate memory bandwidth, scaling to millions of cores.
- **No Cache Coherence Overhead:** Since there is no shared memory, complex hardware cache coherence protocols are unnecessary.
- **Cost-Effectiveness:** Can be built from commodity, off-the-shelf components (e.g., Beowulf clusters).
- **Programming Model (MPI):** Programmer must decompose the problem, partition data, and define explicit communication points using send/receive.
- **Key Challenge:** Communication latency and bandwidth of the network can become performance bottlenecks.

### Important Concepts

- Distributed memory is associated with MPI (Message Passing Interface) programming model
- Shared memory uses a single global address space; distributed memory uses multiple private address spaces
- Hybrid architectures combine distributed memory (between nodes) with shared memory (within each node) using MPI + OpenMP
- UMA and NUMA are shared-memory concepts; distributed memory has only local memory access

### Notes

- For exams, clearly associate distributed memory with MPI and shared memory with OpenMP/Pthreads.
- The fundamental distinction is the address space: one (shared) vs. many (distributed). All other differences stem from this.
- Be able to draw and label the distributed-memory architecture diagram showing nodes, local memory, and interconnect.
