# Caches in Parallel Computing

=====================================

### Overview

Caches are small, high-speed memory buffers between the CPU and main memory that store frequently accessed data to bridge the processor-memory speed gap. In parallel computing, understanding cache behavior is critical because cache management directly impacts performance and correctness of multi-threaded programs, especially through phenomena like false sharing.

### Key Points

- **Cache Hit:** Data found in cache; processed at high speed
- **Cache Miss:** Data not found; must be fetched from slower main memory
- **Memory Hierarchy:** Registers > L1 Cache > L2 Cache > L3 Cache (shared) > RAM > Secondary Storage
- **Cache Lines:** Data transferred in fixed-size blocks (typically 64 bytes), not individual bytes
- **Temporal Locality:** Recently accessed data is likely to be accessed again soon
- **Spatial Locality:** Data near recently accessed locations is likely to be accessed next
- **Cache Coherency:** Protocols (e.g., MESI) ensure all cores see consistent shared data
- **False Sharing:** Different threads writing to different variables on the same cache line cause unnecessary invalidations

### Important Concepts

- L1 cache is often split into Instruction cache and Data cache, private to each core
- L3 cache is typically shared among all cores on the chip
- MESI protocol states: Modified, Exclusive, Shared, Invalid
- When one core writes, it invalidates or updates copies in other caches

### Notes

- False sharing does not cause incorrect results but can cause massive performance slowdowns
- Mitigate false sharing with memory padding to align variables to separate cache lines
- Efficient cache usage is fundamental, not optional, for achieving high parallel performance
- Understand the entire memory hierarchy and how data flows through it for exam questions
