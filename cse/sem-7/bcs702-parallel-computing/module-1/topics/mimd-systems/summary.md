# MIMD Systems in Parallel Computing

=====================================

### Overview

MIMD (Multiple Instruction, Multiple Data) is the most common parallel computing architecture where multiple processors execute different instructions on different data simultaneously. It forms the foundation of modern multicore processors, clusters, and supercomputers, offering greater flexibility than SIMD for handling irregular and diverse computational tasks.

### Key Points

- **Independent Execution:** Each processor has its own control unit and can execute different programs or different parts of the same program independently.
- **Asynchronous Operation:** Processors work at their own pace without lock-step synchronization.
- **Shared Memory MIMD:** All processors share a global address space; communication through memory reads/writes; programmed with OpenMP.
- **Distributed Memory MIMD:** Each processor has private local memory; communication through message passing; programmed with MPI.
- **Cache Coherence Protocols:** Required in shared memory MIMD; MSI (Modified, Shared, Invalid) and MESI (adds Exclusive state).
- **Write-Invalidate vs Write-Update:** Two approaches for maintaining cache coherence when a processor writes to shared data.
- **Interconnection Networks:** Bus (simple, limited), mesh (scalable), hypercube (high connectivity), crossbar (non-blocking, expensive).
- **Real-World Examples:** Shared memory (Intel Core i7, AMD Ryzen); Distributed memory (IBM Summit, Fugaku, Beowulf clusters).

### Important Concepts

- SIMD vs MIMD: SIMD executes same instruction on multiple data elements; MIMD executes different instructions on different data
- Shared memory advantages: simpler programming, implicit communication; disadvantages: memory contention, limited scalability
- Distributed memory advantages: excellent scalability, cost-effective; disadvantages: complex programming, explicit communication
- Performance factors: load balancing, communication overhead, synchronization, and scalability

### Notes

- Be able to compare shared and distributed memory MIMD with a table covering memory, communication, programming model, scalability, and cost.
- Practice drawing diagrams of both MIMD architectures and interconnection networks for descriptive answers.
- Know when to use OpenMP (shared memory) vs MPI (distributed memory) and their basic syntax patterns.
