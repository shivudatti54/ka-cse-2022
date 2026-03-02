# Memory Hierarchy and Cache Memory - Summary

## Key Definitions and Concepts

- **Memory Hierarchy**: Tiered arrangement of memory types (registers → cache → RAM → secondary storage) balancing speed, capacity, and cost.
- **Cache**: Fast, small memory between CPU and main memory storing frequently accessed data.
- **Temporal Locality**: Tendency to reuse recently accessed items.
- **Spatial Locality**: Tendency to access nearby items.
- **Hit Rate**: Fraction of memory accesses found in cache.
- **Miss Penalty**: Time to fetch data from main memory on cache miss.

## Important Formulas and Theorems

- **AMAT (Single-level)**: Hit Time + (Miss Rate × Miss Penalty)
- **AMAT (Two-level)**: L1 Hit Time + (L1 Miss Rate × L2 Hit Time) + (L1 Miss Rate × L2 Miss Rate × Memory Penalty)
- **Address Division**: Total bits = Tag bits + Index bits + Offset bits
- **Cache Lines**: 2^(Index bits); Block size = 2^(Offset bits)

## Key Points

- Memory hierarchy exploits locality principles to bridge the processor-memory speed gap.
- Cache mapping: Direct mapped (simple, conflict misses), Fully associative (expensive, lowest miss rate), Set associative (balanced).
- Write-through writes to both cache and memory; write-back writes only to cache, updates memory on eviction.
- LRU replacement performs best in most scenarios; FIFO is simple but can perform poorly.
- Multi-level caches significantly reduce average memory access time.
- Typical cache sizes: L1 (16-64KB), L2 (256KB-1MB), L3 (1-8MB).
- Block/line size typically 32-64 bytes; larger blocks reduce compulsory misses but increase miss penalty.

## Common Mistakes to Confuse

- Confusing miss rate with hit rate (they sum to 1, or 100%).
- Forgetting that cache size refers to data capacity only, not including tag/valid bits.
- Not distinguishing between different types of cache misses: compulsory, capacity, and conflict.
- Mixing up write-through and write-back policies' characteristics.

## Revision Tips

1. Practice at least 3-4 numerical problems on AMAT calculation and address mapping.
2. Draw cache organization diagrams to reinforce understanding of mapping techniques.
3. Memorize the hierarchy from fastest to slowest: Registers → L1 → L2 → L3 → RAM → SSD/HDD.
4. Review previous year DU examination questions on cache memory — they often repeat question patterns.