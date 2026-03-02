# Cache Line Replacement Policies - Summary

## Key Definitions and Concepts

- **Cache Line Replacement Policy**: Algorithm that determines which cache line to evict when a cache miss occurs and the cache set is full.
- **Cache Hit**: Requested data found in cache; **Cache Miss**: Data not in cache, must be fetched from main memory.
- **Temporal Locality**: Recently accessed items are likely to be accessed again—exploited by LRU.
- **Associativity**: Determines number of cache lines per set (direct-mapped, n-way set-associative, fully-associative).

## Important Formulas and Theorems

- **Hit Ratio** = Hits / Total Memory References
- **Miss Penalty** = Time to fetch from main memory - Time to fetch from cache
- **Average Memory Access Time (AMAT)** = Hit Time + (Miss Rate × Miss Penalty)
- **Belady's Anomaly**: Paradox where increasing cache size can decrease hit ratio with FIFO policy.

## Key Points

- **LRU (Least Recently Used)**: Evicts least recently accessed line; best practical performance, exploits temporal locality.
- **FIFO (First In First Out)**: Evicts oldest line; simple hardware but can suffer from Belady's anomaly.
- **LFU (Least Frequently Used)**: Evicts least accessed line; good for non-uniform access but doesn't adapt to changes.
- **Random Replacement**: Evicts random line; simplest hardware but unpredictable performance.
- **Optimal Replacement**: Theoretically best (evicts line used furthest in future) but unimplementable.
- Hardware complexity increases: Random < FIFO < LFU < LRU
- LRU is most widely implemented despite complexity due to excellent hit ratio.
- Pseudo-LRU provides approximate LRU with less hardware in real processors.

## Common Mistakes to Avoid

1. Confusing LRU with FIFO—LRU tracks usage time, FIFO tracks insertion time only.
2. Belady's anomaly only occurs with non-stack algorithms like FIFO, not with LRU.
3. Remember that Optimal policy is theoretical—cannot be implemented in practice.
4. Don't forget that cache line size affects spatial locality benefits, not just replacement policy.

## Revision Tips

1. Practice tracing reference strings through cache with different policies—university exams frequently ask for this.
2. Memorize the complexity order: Random → FIFO → LFU → LRU (simplest to most complex).
3. Remember that LRU exploits temporal locality; understand why this matters for real programs.
4. Review the difference between hit ratio and miss rate (they sum to 1).
5. Understand that replacement policy choice impacts microcontroller performance and power consumption.
