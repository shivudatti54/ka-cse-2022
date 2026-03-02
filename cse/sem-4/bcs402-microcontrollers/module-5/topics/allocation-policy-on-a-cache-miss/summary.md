# Cache Miss Allocation Policy - Summary

## Key Definitions and Concepts

- **Cache Hit**: CPU request satisfied by data in cache (fast access)
- **Cache Miss**: CPU request not in cache; must fetch from main memory
- **Fetch-on-Miss (Allocate on Miss)**: Policy that loads block into cache upon miss before CPU access
- **No-Allocate (Write-Around)**: Policy that bypasses cache on write miss, writes directly to memory
- **Write-Allocate**: Fetches block into cache on write miss, then performs the write
- **Eviction Policy**: Strategy to select victim block when cache is full (LRU, FIFO, Random)

## Important Formulas and Theorems

- **Cache Line Mapping**: For direct-mapped cache, line = (Block Address) mod (Number of Lines)
- **Set Mapping**: For set-associative cache, set = (Block Address) mod (Number of Sets)
- **Hit Rate**: Hit Rate = (Hits) / (Total Accesses)
- **Miss Rate**: Miss Rate = 1 - Hit Rate
- **Average Memory Access Time (AMAT)**: AMAT = Hit Time + (Miss Rate × Miss Penalty)

## Key Points

- Cache miss allocation policy determines how newly fetched data from main memory is placed in cache
- Fetch-on-miss exploits temporal and spatial locality, improving subsequent access performance
- No-allocate prevents cache pollution for write-intensive or streaming operations
- Write-allocate combines write operations with cache allocation; best for write locality
- Three types of misses: compulsory (first access), capacity (cache too small), conflict (mapping collisions)
- Eviction policies (LRU, FIFO, Random) determine which block to replace when cache is full
- In microcontrollers with limited cache, proper allocation policy is critical for performance
- Larger cache block size improves spatial locality but increases miss penalty

## Common Mistakes to Avoid

1. Confusing write-through with write-back - allocation policy is independent of write policy
2. Believing that more cache always means better performance - allocation policy matters
3. Ignoring conflict misses in set-associative caches when analyzing performance
4. Assuming fetch-on-miss is always better - no-allocate is preferable for certain access patterns

## Revision Tips

1. Practice mapping memory addresses to cache lines for different cache configurations
2. Trace through example access sequences to understand hit/miss behavior
3. Remember that allocation policy primarily affects miss handling, not hit behavior
4. Focus on understanding when each policy (fetch-on-miss vs no-allocate) is preferable
5. Review previous year questions on cache memory for pattern understanding
