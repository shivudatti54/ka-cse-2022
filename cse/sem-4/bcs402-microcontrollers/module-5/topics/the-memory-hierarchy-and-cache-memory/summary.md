# Memory Hierarchy and Cache Memory - Summary

## Key Definitions and Concepts

- **Memory Hierarchy**: Organized structure of memory types balancing speed, capacity, and cost
- **Cache Memory**: Fast, small memory that stores frequently accessed data between CPU and main memory
- **Temporal Locality**: Principle that recently accessed data will likely be accessed again
- **Spatial Locality**: Principle that data near recently accessed locations will likely be accessed soon
- **Cache Line**: Basic unit of data transfer (typically 32-64 bytes)
- **Hit Rate**: Fraction of memory accesses found in cache
- **Miss Rate**: Fraction of accesses not in cache (1 - hit rate)
- **AMAT**: Average Memory Access Time = Hit Time + (Miss Rate × Miss Penalty)

## Important Formulas and Theorems

- **Hit Rate** = Hits / Total Accesses
- **Miss Rate** = 1 - Hit Rate
- **AMAT** = Hit Time + (Miss Rate × Miss Penalty)
- **Cache Line Index** = (Block Address) mod (Number of Cache Lines)
- **Offset Bits** = log₂(Line Size)
- **Index Bits** = log₂(Number of Sets)
- **Total Cache Size** = Sets × Associativity × Line Size

## Key Points

1. Memory hierarchy uses multiple levels to balance speed, cost, and capacity
2. Cache operates on locality principles (temporal and spatial)
3. Three mapping techniques: direct, fully associative, set associative
4. Direct mapping is simple but causes conflict misses
5. Set associative is the practical compromise with 2-16 ways
6. Write-through is simpler but slower; write-back is faster but complex
7. LRU replacement policy is most common for temporal locality
8. Multi-level caches (L1, L2, L3) progressively increase size and latency
9. Cache misses consist of cold misses, conflict misses, and capacity misses
10. Cache coherence is critical in multi-core systems

## Common Mistakes to Avoid

1. Confusing cache line with cache set - a set contains multiple lines (ways)
2. Forgetting that address decomposition includes offset bits for byte within line
3. Not considering that miss penalty includes both memory access and data transfer time
4. Assuming write-back always performs better - write-through is better for I/O
5. Overlooking that cache is volatile - data lost when power is removed

## Revision Tips

1. Practice at least 3-4 address mapping problems to master index/tag calculation
2. Memorize the AMAT formula as it's frequently tested
3. Remember the trade-offs between mapping techniques
4. Understand the difference between hit time and miss penalty clearly
5. Review cache configuration problems where you determine cache organization from specifications
