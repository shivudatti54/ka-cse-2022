# Organization (Memory Systems) - Summary

## Key Definitions and Concepts

- MEMORY HIERARCHY: Arrangement of memory into levels based on speed, size, and cost trade-offs
- PRIMARY MEMORY: Fast, volatile memory directly accessible by CPU (cache, RAM)
- SECONDARY MEMORY: Non-volatile, slow storage for long-term data (hard drives, SSDs)
- VIRTUAL MEMORY: Abstraction that creates illusion of larger memory space using secondary storage
- CACHE MEMORY: Small, fast memory that stores frequently accessed data
- EFFECTIVE ACCESS TIME: Weighted average of memory access times considering hit/miss rates

## Important Formulas and Theorems

- EAT = Hit Rate × Cache Access Time + Miss Rate × (Cache Access Time + Memory Access Time)
- Miss Rate = 1 - Hit Rate
- Average access time with multiple cache levels considers hit rate at each level and cumulative miss penalty

## Key Points

- Memory is organized hierarchically with faster but smaller memory at the top
- Registers provide fastest access (1 cycle), followed by L1 cache (1-2 ns), L2 cache (3-10 ns), L3 cache (10-20 ns), RAM (50-100 ns), and SSD/HDD (microseconds to milliseconds)
- Cache memory exploits temporal and spatial locality to improve performance
- Virtual memory enables processes to use more memory than physically available
- Page faults are extremely expensive (milliseconds vs nanoseconds for memory access)
- Memory interleaving increases bandwidth by allowing parallel access to multiple banks

## Common Mistakes to Confusing

- Primary memory is volatile (loses data without power), secondary memory is non-volatile
- Cache hit rate and miss rate are complements (they sum to 1)
- Page fault handling involves disk I/O which is orders of magnitude slower than memory access
- Logical and physical addresses are different; translation involves the MMU

## Revision Tips

- Practice numerical problems on effective access time calculations with various hit rates
- Memorize approximate access times for different memory levels in a computer system
- Understand how locality of reference (temporal and spatial) makes caching effective
- Review how virtual memory address translation works and why page faults occur