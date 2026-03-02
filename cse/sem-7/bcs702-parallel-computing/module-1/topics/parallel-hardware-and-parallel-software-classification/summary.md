# Parallel Hardware and Software Classification

=====================================

### Overview

Parallel computers are classified based on their hardware architecture and memory organization. Flynn's Taxonomy (1966) provides the primary classification framework using instruction streams and data streams, while memory architecture further subdivides systems into shared memory, distributed memory, and hybrid models.

### Key Points

- **Flynn's Taxonomy:** Classifies architectures by concurrent instruction and data streams: SISD, SIMD, MISD, MIMD.
- **SISD:** Traditional sequential (von Neumann) computer; single processor, single instruction, single data stream.
- **SIMD:** Single instruction broadcast to multiple processing elements, each operating on its own data; ideal for data-parallel tasks (GPUs, vector processors).
- **MISD:** Multiple instructions on single data stream; rare, used in fault-tolerant systems.
- **MIMD:** Most common; multiple processors execute independently with different instructions on different data (multicore CPUs, clusters).
- **Shared Memory (UMA):** Equal access time to all memory; symmetric multiprocessing. **NUMA:** Access time depends on memory location relative to processor.
- **Distributed Memory:** Each processor has private memory; communication via message passing; highly scalable (Beowulf clusters).
- **Hybrid (DSM):** Distributed Shared Memory presents physically distributed memory as a single shared address space.

### Important Concepts

- Flynn's Taxonomy is the most widely used classification framework for parallel computers
- MIMD is the dominant paradigm, subdivided by memory architecture (shared vs distributed)
- Shared memory simplifies programming but struggles to scale; distributed memory scales well but requires explicit communication
- Memory architecture directly impacts software design, scalability, and performance

### Notes

- Be prepared to define all four Flynn's Taxonomy categories with examples and classify real-world systems.
- For exams, link shared memory to OpenMP and distributed memory to MPI programming models.
- Most modern systems (laptops to supercomputers) are MIMD, often using hybrid memory models.
