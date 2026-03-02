# Caches and Memory Management Units - Summary

## Key Definitions and Concepts

- **Cache Memory**: High-speed SRAM storage between CPU and main memory that stores frequently accessed data to reduce memory access latency.
- **Cache Hit**: When requested data is found in cache; **Cache Miss**: When data is not in cache and must be fetched from main memory.
- **Memory Management Unit (MMU)**: Hardware component that translates virtual addresses to physical addresses and provides memory protection.
- **Cache Mapping**: Technique that determines how main memory blocks are placed in cache (direct, associative, set-associative).
- **TLB (Translation Lookaside Buffer)**: Specialized cache storing recent virtual-to-physical address translations.

## Important Formulas and Theorems

- **Average Memory Access Time (AMAT)**: AMAT = Hit Time + (Miss Rate × Miss Penalty)
- **Number of Cache Lines**: Cache Size ÷ Line Size
- **Offset Bits**: log₂(Line Size)
- **Index Bits**: log₂(Number of Sets)
- **Tag Bits**: Address Bits - (Offset Bits + Index Bits)

## Key Points

- Cache memory solves the "memory wall" problem by providing fast storage for frequently accessed data.
- Direct-mapped cache is simple but can cause conflict misses; set-associative is the most common implementation.
- Write-through updates both cache and memory simultaneously; write-back updates memory only during eviction.
- MMU enables virtual memory, memory protection, and access control in embedded systems.
- The TLB accelerates address translation by caching page table entries.
- Most Cortex-M microcontrollers don't include caches, but advanced variants (Cortex-M7) do.
- Cache line contains valid bit, dirty bit, tag, and data storage.
- Multi-level cache hierarchies (L1, L2, L3) further improve performance in complex systems.

## Common Mistakes to Avoid

1. Confusing cache associativity with number of sets - remember: Sets = Lines ÷ Associativity
2. Forgetting that offset bits always come from the lowest-order address bits
3. Not considering write policy implications for data consistency in embedded systems
4. Assuming all microcontrollers have caches - most embedded MCUs use direct memory access

## Revision Tips

1. Practice address mapping problems - this is the most common exam question type.
2. Memorize the AMAT formula and be able to apply it with given parameters.
3. Create a comparison table for cache mapping techniques covering complexity, flexibility, and hit rate.
4. Understand the relationship between virtual memory, page tables, and TLB.
5. Review how cache and MMU concepts apply specifically to microcontroller architectures.
