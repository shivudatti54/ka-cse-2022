# Bcs402 Module 5 Cache Efficiency

**Core Concepts**: Cache efficiency measurement relies on key metrics including cache hit ratio (h = N_hits/N_total), miss rate (m = 1-h), and Average Memory Access Time (AMAT = T_h + m × T_m). The AMAT formula is derived using the law of total expectation, showing that average access time equals hit time plus the product of miss rate and miss penalty. Cache misses are classified into compulsory (cold), capacity, and conflict types, each requiring different optimization strategies.

**Measurement Techniques**: ARM microcontrollers provide CP15 registers for hardware-based performance monitoring, enabling direct measurement of cache hits, misses, and cycle counts. Software instrumentation and simulation tools offer alternative measurement approaches for systems lacking hardware counters.

**Key Derivations**: Multi-level cache AMAT extends to AMAT = T_L1 + m_L1 × (T_L2 + m_L2 × T_Memory), accounting for hierarchical cache structures. Cache efficiency is calculated as η = (T_Memory - AMAT)/T_Memory × 100%, quantifying performance improvement.

**Practical Application**: Students should be able to calculate AMAT for given cache parameters, compare cache configurations using efficiency metrics, and interpret performance counter data for cache optimization in embedded systems.
