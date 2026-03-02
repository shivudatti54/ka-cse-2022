# Basic Architecture of a Cache Memory - Summary

## Key Definitions and Concepts

- **Cache Memory**: A high-speed memory layer between the CPU and main memory that stores frequently accessed data and instructions.
- **Cache Line (Block)**: The smallest unit of data that can be transferred between cache and main memory, typically 16-64 bytes.
- **Cache Hit**: When the requested data is found in cache memory.
- **Cache Miss**: When the requested data is not found in cache memory, requiring access to main memory.
- **Tag**: A portion of the memory address used to identify which main memory block is stored in a cache line.

## Important Formulas and Theorems

- **Cache Size = Number of Lines × Line Size**
- **AMAT = Hit Time + (Miss Rate × Miss Penalty)**
- **Miss Rate = 1 - Hit Rate**
- **Direct-Mapped Index = (Block Address) mod (Number of Cache Lines)**
- **Set-Associative Sets = Total Lines / Associativity**
- **Total Address Bits = Tag Bits + Index Bits + Offset Bits**

## Key Points

- Cache memory exploits temporal and spatial locality of reference to improve system performance.
- Three mapping techniques exist: direct-mapped (one location), fully associative (any location), and set-associative (limited locations per set).
- Write-through writes to both cache and memory; write-back delays memory writes until line eviction.
- Cache misses are categorized as compulsory (first access), capacity (cache too small), and conflict (mapping collisions).
- LRU replacement provides good performance but requires additional hardware for tracking.
- Modern microcontrollers typically use set-associative L1 caches for both instructions and data.
- The effectiveness of cache depends heavily on the program's access patterns exhibiting locality.

## Common Mistakes to Avoid

1. Confusing cache "lines" with "sets" - a line is a single storage location, a set is a group of lines.
2. Forgetting that offset bits don't participate in tag comparison.
3. Assuming write-back is always better - it adds complexity and potential data inconsistency.
4. Mixing up hit rate and miss rate - they are complements (sum to 1).

## Revision Tips

1. Practice address decomposition problems: Given cache parameters, identify tag, index, and offset bits.
2. Memorize the three cache mapping techniques and draw their organizational diagrams.
3. Review numerical problems on AMAT calculation - these are frequently asked in university exams.
4. Understand the trade-offs between associativity, hit time, and hardware cost.
5. Create a comparison table of all cache characteristics for quick last-minute review.
