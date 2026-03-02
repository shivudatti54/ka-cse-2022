# MIMD Systems (Module 2)

=====================================

### Overview

MIMD (Multiple Instruction, Multiple Data) is the most common and flexible parallel computing architecture, where multiple processors independently execute different instructions on different data. MIMD systems are classified into shared memory (global address space, OpenMP) and distributed memory (private address spaces, MPI), each with distinct advantages for different use cases.

### Key Points

- **Independent Execution:** Each processor has its own control unit, executing different programs or program parts asynchronously.
- **Shared Memory MIMD:** Global shared memory; implicit communication via reads/writes; limited scalability due to memory bandwidth and cache coherence.
- **Distributed Memory MIMD:** Private local memory per processor; explicit message passing; excellent scalability using commodity hardware.
- **Cache Coherence Protocols:** Write-Invalidate (invalidates other copies), Write-Update (updates all copies), MSI (3 states), MESI (4 states with Exclusive).
- **Network Topologies:** Bus (simple, limited), mesh (scalable, used in supercomputers), hypercube (high connectivity), crossbar (non-blocking, expensive).
- **Programming Models:** OpenMP for shared memory (#pragma omp parallel), MPI for distributed memory (MPI_Init, MPI_Comm_rank).
- **Real-World Examples:** Shared (Intel i7, AMD Ryzen), Distributed (IBM Summit, Fugaku, Beowulf clusters, cloud computing).

### Important Concepts

- SIMD vs MIMD: SIMD = same instruction on multiple data (lockstep); MIMD = different instructions on different data (asynchronous)
- Shared memory trade-off: easy programming but limited scalability; distributed memory: complex programming but highly scalable
- Performance considerations: load balancing, communication overhead, synchronization, and scalability
- MESI protocol adds Exclusive state to MSI, providing optimization for single-copy clean cache lines

### Notes

- Be able to draw and compare shared memory and distributed memory MIMD architectures with labeled diagrams.
- Know cache coherence protocols (MSI, MESI) and explain how they maintain consistency.
- Remember real-world examples and classify them as shared or distributed memory MIMD systems.
