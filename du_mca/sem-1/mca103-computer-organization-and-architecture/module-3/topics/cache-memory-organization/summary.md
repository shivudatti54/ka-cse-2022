# Cache Memory Organization - Summary

## Key Definitions and Concepts

- **Cache Memory**: A small, fast memory located between the CPU and main memory that stores frequently accessed data and instructions to reduce memory access latency.
- **Cache Hit**: When the requested data is found in the cache, providing fast access.
- **Cache Miss**: When the requested data is not in the cache, requiring access to slower main memory.
- **Locality of Reference**: The tendency of programs to repeatedly access the same locations (temporal) or nearby locations (spatial).
- **Block/Line**: The basic unit of data transferred between cache and main memory, typically 32-128 bytes.
- **Tag**: Part of the address used to identify which main memory block is stored in a cache line.

## Important Formulas and Theorems

- **AMAT = Hit Time + (Miss Rate × Miss Penalty)** — The fundamental cache performance equation
- **For multi-level caches**: AMAT = L1 Hit Time + L1 Miss Rate × (L2 Hit Time + L2 Miss Rate × L3 Hit Time + ...)
- **Address field calculations**: 
  - Offset bits = log₂(block size)
  - Index bits = log₂(number of cache lines)
  - Tag bits = Address bits - Offset bits - Index bits

## Key Points

- Cache memory exploits temporal and spatial locality to achieve high hit rates (typically 90%+)
- Direct-mapped cache is simple but prone to thrashing; fully associative is flexible but expensive
- Set-associative caching balances complexity and performance (4-way and 8-way are common)
- Write-through ensures data consistency but generates more memory traffic than write-back
- LRU replacement approximates optimal replacement but is complex for high associativity
- Modern processors use hierarchical caches: L1 (split, fastest), L2 (unified), L3 (shared)
- Cache block size trade-offs: larger blocks improve spatial locality but increase miss penalty

## Common Mistakes to Avoid

- Confusing hit rate with miss rate (they sum to 1, but students often use the wrong one in formulas)
- Forgetting that miss penalty includes the time to fetch the block, not just detect the miss
- Not distinguishing between different levels' hit times when calculating multi-level AMAT
- Overlooking the fact that write-back reduces traffic but requires dirty bit tracking

## Revision Tips

- Practice numerical problems calculating AMAT for various cache configurations
- Draw cache diagrams for direct, associative, and set-associative mappings
- Memorize the relationship between address bits and cache parameters
- Understand why each design choice (replacement policy, write policy) exists and what workloads it favors