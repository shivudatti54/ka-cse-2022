# Multiple Processor Scheduling - Summary

## Key Definitions and Concepts

- **Multiprocessor Scheduling:** The allocation of processes to multiple processors in a computer system, considering which processor should execute which process and when.

- **Symmetric Multiprocessing (SMP):** Architecture where all processors are identical and share common memory, with any process executable on any processor.

- **Asymmetric Multiprocessing (AMP):** Architecture with hierarchical processor roles where a master processor controls slave processors.

- **Processor Affinity:** The tendency of a process to run on the same processor to benefit from cached data, classified as soft (preferred) or hard (mandatory).

- **Load Balancing:** Distributing processes evenly across all processors to prevent idle processors while others are overloaded.

- **Migration:** Moving a process from one processor to another, incurring costs from cache invalidation and TLB flushes.

- **Gang Scheduling:** Scheduling related processes simultaneously on multiple processors, essential for parallel applications with frequent synchronization.

- **NUMA (Non-Unorm Memory Access):** Architecture where memory access time depends on memory location relative to the processor.

## Important Scheduling Approaches

| Approach | Key Feature | Best Use Case |
|----------|-------------|---------------|
| Load Sharing | Work distributed to idle processors | General-purpose SMP systems |
| Gang Scheduling | Related processes scheduled together | Parallel computing applications |
| Dedicated Assignment | Process binds to specific processor | Real-time and embedded systems |
| Work-Stealing | Idle processors steal from busy queues | Task-parallel frameworks |

## Key Points

- Modern multi-core processors are essentially SMP systems requiring sophisticated scheduling algorithms.

- Processor affinity improves performance significantly (up to 10×) for cache-intensive processes by reducing cache misses.

- Migration has substantial costs including context switches, cache invalidation, and potential TLB flushes.

- The scheduler must balance two competing goals: maintaining processor affinity for cache efficiency and achieving load balance across processors.

- Gang scheduling is crucial for parallel applications where threads communicate frequently, reducing synchronization delays.

- NUMA-aware scheduling allocates processes to processors closest to their memory pages to minimize latency.

- Cache coherence becomes a major concern in multiprocessor systems with separate caches for each processor.

- Real-world schedulers like Linux CFS and Windows scheduler use hybrid approaches combining multiple strategies.

## Common Mistakes to Avoid

- Confusing SMP with AMP: Remember SMP has equal processors with shared memory, AMP has master-slave hierarchy.

- Ignoring migration costs: Students often assume process migration is free, but cache and TLB effects are significant.

- Overlooking cache affinity: Focusing only on load balance while destroying valuable cache state wastes performance.

- Thinking more processors always means better performance: Poor scheduling can cause cache thrashing that degrades performance below uniprocessor levels.

## Revision Tips

- Create a comparison table of all scheduling approaches with pros, cons, and use cases for quick recall.

- Practice calculating simple load distribution scenarios to understand makespan minimization.

- Remember the affinity-performance relationship: affinity ≈ cache locality ≈ reduced memory access time.

- Study real operating system schedulers (Linux CFS, Windows NUMA scheduler) as practical examples of multiprocessor scheduling concepts.