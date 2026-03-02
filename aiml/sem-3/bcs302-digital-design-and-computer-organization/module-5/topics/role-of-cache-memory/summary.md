# Role Of Cache Memory
### Quick Summary

1. **Purpose:** Cache memory is a small, high-speed buffer that bridges the CPU-main memory speed gap, mitigating the von Neumann bottleneck.

2. **Operating Principle:** Based on locality of reference—temporal (recently accessed items likely accessed again) and spatial (nearby addresses accessed together).

3. **Performance:** Measured by hit ratio (h) and Average Memory Access Time (AMAT = t_hit + (1-h) × t_miss).

4. **Mapping Techniques:**

- Direct: Simple, one-to-one mapping, conflict misses possible
- Fully Associative: Flexible, any location, expensive hardware
- Set Associative: Compromise between the two (common in modern CPUs)

5. **Replacement Policies:** LRU (optimal), FIFO (simple), Random (unpredictable), MRU (streaming).

6. **Write Policies:** Write-through (memory always consistent) vs. Write-back (faster, uses dirty bits).

7. **Levels:** L1 (fastest, smallest), L2 (medium), L3 (largest, shared among cores).

8. **Multi-level AMAT:** Must consider miss rates and hit times at each level: AMAT = t_L1 + m_L1 × (t_L2 + m_L2 × t_L3 + ...)

### Key Terms

- Cache Hit/Miss, Hit Ratio, AMAT
- Temporal/Spatial Locality
- Direct/Set/Fully Associative Mapping
- LRU/FIFO/Random Replacement
- Write-through/Write-back
- MESI Protocol (coherence)
