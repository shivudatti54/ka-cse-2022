# Shared Memory vs Distributed Memory

=====================================

### Overview

Shared-memory and distributed-memory are the two primary parallel memory architectures. Shared-memory systems provide a single global address space accessed by all processors, while distributed-memory systems give each processor its own private memory with inter-processor communication via message passing. This distinction fundamentally shapes hardware design and programming models.

### Key Points

- **Shared Memory:** Single global address space; all processors can read/write the same memory locations; programmed with OpenMP/Pthreads.
- **UMA (Uniform Memory Access):** Equal access time for all processors; typical in SMP systems (multi-core CPUs).
- **NUMA (Non-Uniform Memory Access):** Access time depends on memory proximity to the processor; physically distributed but logically shared.
- **Distributed Memory:** Each processor has private local memory; no global address space; communication via message passing (MPI).
- **Scalability Trade-off:** Shared memory limited to tens-hundreds of cores (bus/bandwidth bottleneck); distributed memory scales to thousands-millions of cores.
- **Cache Coherence:** Required in shared memory (MESI protocol overhead); not applicable in distributed memory.
- **Hybrid Architectures:** Modern HPC systems combine both: MPI between nodes (distributed) + OpenMP within nodes (shared memory).

### Important Concepts

- Fundamental distinction: one address space (shared) vs many address spaces (distributed)
- Shared memory: implicit data sharing (fast), explicit synchronization needed (locks, semaphores)
- Distributed memory: explicit communication (send/receive), no cache coherence overhead, cost-effective with commodity hardware
- Programming model mapping: Shared Memory -> OpenMP (Module 4), Distributed Memory -> MPI (Module 3)

### Notes

- The core exam comparison: address space is the root difference; all other trade-offs (programming, scalability, cost) derive from it.
- Be able to draw and label architectural diagrams for both systems.
- Mentioning hybrid systems (MPI + OpenMP) demonstrates deeper understanding of real-world HPC practice.
