# Multiple Processor Scheduling - Summary

## Key Definitions
- **Multiprocessor Scheduling**: Allocation of processes/threads across multiple processors to optimize system performance
- **Symmetric Multiprocessing (SMP)**: All processors are equal, each can execute kernel and user code with independent run queues
- **Asymmetric Multiprocessing (ASMP)**: Master-slave configuration where one processor controls scheduling
- **Processor Affinity**: Preference to keep a process on the same processor to maintain cache warmth
- **Load Balancing**: Distributing work evenly across processors to prevent idle time
- **Gang Scheduling**: Scheduling groups of related threads simultaneously on multiple processors

## Important Formulas
- **Load Balance Factor**: Standard deviation of processor utilization percentages
- **Affinitized Execution Time**: T_affinity = (cache_hit_ratio × cache_hit_cost) + (cache_miss_ratio × cache_miss_cost)
- **Makespan**: Maximum completion time across all processors in a scheduling period

## Key Points
1. SMP is the dominant multiprocessor architecture due to better scalability and fault tolerance.
2. Load balancing and processor affinity are complementary but often conflicting objectives.
3. Hard affinity mandates specific processors; soft affinity merely prefers them.
4. Gang scheduling eliminates synchronization delays for parallel applications but wastes resources for independent tasks.
5. Multi-core processors introduce cache hierarchy considerations (L1 per core, shared L2/L3).
6. NUMA systems require memory locality awareness in scheduling decisions.
7. Migration overhead includes cache invalidation, TLB flushes, and potential memory bandwidth saturation.

## Common Mistakes
1. Confusing symmetric and asymmetric multiprocessing—ASMP has a master processor handling all OS functions.
2. Assuming load balancing always improves performance—migration costs may exceed benefits for cache-intensive workloads.
3. Treating all multiprocessor systems identically—scheduling depends on architecture (UMA vs NUMA), cache hierarchy, and application characteristics.
4. Ignoring the difference between thread scheduling and process scheduling in multiprocessor contexts.