# The Relationship Between Cache and Main Memory - Summary

## Key Definitions and Concepts

- **Cache Memory**: A high-speed, small-capacity memory located between the CPU and main memory that stores frequently accessed data and instructions.
- **Main Memory**: The primary storage in a computer system, typically DRAM, providing larger capacity but slower access times than cache.
- **Temporal Locality**: The tendency of recently accessed items to be accessed again in the near future.
- **Spatial Locality**: The tendency of items near recently accessed items to be accessed soon.
- **Hit Rate**: The percentage of memory accesses that are satisfied by the cache.
- **Miss Rate**: The percentage of memory accesses that require fetching from main memory.

## Important Formulas and Theorems

- **Average Memory Access Time (AMAT)** = Hit Time + (Miss Rate × Miss Penalty)
- **Number of Cache Lines** = Cache Size / Block Size
- **Total Tag Bits** = Address Bits - Index Bits - Offset Bits
- **Cache Size (Set Associative)** = Associativity × Number of Sets × Block Size

## Key Points

- Cache memory exploits temporal and spatial locality to reduce average memory access time.
- Direct mapping is simple but causes conflict misses; fully associative maximizes flexibility but requires expensive hardware.
- Set-associative mapping offers a practical balance between hit rate and hardware complexity.
- Write-through policy ensures data consistency but slower writes; write-back is faster but requires more complex management.
- Write allocate loads data into cache on miss; write-around writes directly to main memory.
- MESI protocol maintains cache coherence with Modified, Exclusive, Shared, and Invalid states.
- Larger cache and higher associativity improve hit rate but increase latency and cost.

## Common Mistakes to Confuse

- Confusing cache line with cache block: A cache line is one storage location in cache that holds a block of data.
- Mixing up index and offset: Index selects which cache line/set, offset selects the byte within the block.
- Forgetting that block offset determines bytes per block, not the number of blocks.

## Revision Tips

1. Practice address decomposition problems: Given cache size, block size, and address width, determine tag, index, and offset bits.
2. Memorize the AMAT formula and practice numerical problems.
3. Create a comparison table of mapping techniques with pros and cons.
4. Draw the state diagram for MESI protocol to understand cache coherence transitions.
5. Relate these concepts to real microcontroller applications like ARM Cortex-M series that feature cache memory.
