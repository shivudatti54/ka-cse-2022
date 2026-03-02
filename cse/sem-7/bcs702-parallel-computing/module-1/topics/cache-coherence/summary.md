# Cache Coherence in Parallel Programming

=====================================

### Overview

Cache coherence refers to the consistency of data stored in multiple local caches of a shared-memory multiprocessor system. When multiple processors cache copies of the same memory location, updates by one processor can leave others with stale data, leading to incorrect program behavior. Cache coherence protocols ensure all processors see a consistent view of memory.

### Key Points

- **Cache Coherence Problem:** Multiple cached copies of the same memory location can become inconsistent when one processor updates its copy without notifying others.
- **Write-Through:** Every write to cache also writes to main memory immediately; ensures consistency but generates high memory traffic.
- **Write-Back:** Writes only update the cache; main memory updated on eviction. Reduces traffic but needs careful coherence management.
- **Snooping Protocols:** Broadcast-based approach where all cache controllers monitor the shared bus for memory transactions.
- **Write-Invalidate:** On a write, invalidates all other cached copies; subsequent reads cause cache misses and fetch updated values.
- **Write-Update:** On a write, updates all other cached copies in real-time; keeps caches current but generates more bus traffic.
- **Directory-Based Protocols:** Use a central directory tracking which caches hold copies; more scalable than snooping for large systems.
- **False Sharing:** Different variables on the same cache line cause unnecessary invalidations; solved by padding or alignment.

### Important Concepts

- MESI Protocol states: Modified (dirty, only copy), Exclusive (clean, only copy), Shared (clean, may exist elsewhere), Invalid (stale)
- Snooping is suitable for bus-based systems with fewer processors; directory-based is better for larger systems
- Directory states: Uncached, Shared, Exclusive, Owned
- False sharing occurs when unrelated variables share a cache line, degrading performance

### Notes

- Be able to trace through MESI state transitions for given read/write patterns in exam questions.
- Compare snooping vs directory-based protocols: snooping uses broadcast (simpler, less scalable), directory uses point-to-point messages (more scalable).
- Cache coherence protocols solve data consistency but not higher-level synchronization issues like race conditions.
