# Measuring Cache Efficiency - Summary

## Key Definitions and Concepts

- **Cache Memory**: High-speed memory between CPU and main memory that stores frequently accessed data
- **Cache Hit**: Requested data found in cache; cache hit time is the access time
- **Cache Miss**: Requested data not in cache; miss penalty is additional time to fetch from main memory
- **Locality of Reference**: Principle stating programs access same/recent locations repeatedly

## Important Formulas and Theorems

- **Hit Ratio (h)** = Cache Hits / Total Memory Accesses
- **Miss Rate (m)** = 1 - Hit Ratio
- **Miss Penalty** = Main Memory Access Time - Cache Access Time
- **AMAT** = Hit Time + (Miss Rate × Miss Penalty)
- **Cache Efficiency** = (AMAT without Cache - AMAT with Cache) / AMAT without Cache × 100%
- **Speedup** = Memory Access Time without Cache / AMAT with Cache

## Key Points

- Cache efficiency directly impacts microcontroller execution speed, power consumption, and real-time responsiveness
- Higher hit ratios (typically >90%) indicate better cache performance
- AMAT provides a single metric combining all cache performance factors
- Three types of misses: Compulsory (first access), Capacity (cache too small), Conflict (mapping collisions)
- Measurement methods include hardware performance counters, simulation, and software instrumentation
- Cache design involves trade-offs between size, speed, associativity, and block size

## Common Mistakes to Avoid

- Confusing hit rate with efficiency; hit rate is a ratio while efficiency is a percentage comparison
- Using inconsistent units (mixing clock cycles with nanoseconds) in calculations
- Forgetting that miss penalty is additional time beyond cache access time
- Ignoring that cache misses have varying penalties depending on memory hierarchy

## Revision Tips

- Practice numerical problems calculating AMAT from given hit time, miss rate, and miss penalty
- Memorize the standard formulas before the exam
- Understand the concept of locality of reference as the foundation for cache effectiveness
- Review cache mapping techniques (direct, associative, set-associative) as they affect miss rates
