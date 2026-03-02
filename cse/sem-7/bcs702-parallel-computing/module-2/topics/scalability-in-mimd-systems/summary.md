# Scalability in MIMD Systems

=====================================

### Overview

Scalability measures a parallel system's ability to handle increasing workloads by adding more resources while maintaining or improving efficiency. It is evaluated through speedup, efficiency, and scaling analysis (strong vs weak), and is constrained by communication overhead, memory hierarchy, workload imbalance, and synchronization costs.

### Key Points

- **Speedup:** S(p) = T(1) / T(p), where T(1) is sequential time and T(p) is parallel time with p processors.
- **Efficiency:** E(p) = S(p) / p. Ideal efficiency is 1.0; in practice it decreases as processors increase.
- **Strong Scaling:** Fixed problem size, increasing processors; goal is to reduce execution time. Limited by Amdahl's Law.
- **Weak Scaling:** Problem size grows proportionally with processors; goal is to maintain constant execution time.
- **Amdahl's Law:** S(p) <= 1 / [f + (1-f)/p], where f is sequential fraction. Maximum speedup = 1/f.
- **Gustafson's Law:** S(p) = p - alpha(p-1), where alpha is sequential fraction. More optimistic for scaled problems.
- **Scalability Bottlenecks:** Communication overhead (CPU-GPU transfer), memory hierarchy constraints, workload imbalance, synchronization overhead.
- **GPU Scalability Factors:** Grid/block organization, coalesced memory access patterns, occupancy (active warps per SM).

### Important Concepts

- Strong scaling is limited by Amdahl's Law; weak scaling follows Gustafson's Law
- Linear speedup S(p) = p is ideal but rarely achieved due to overheads
- Roofline model relates performance to operational intensity; LogP model accounts for latency, overhead, gap, and processors
- Optimization strategies: minimize data transfer, maximize coalesced access, balance workload, use asynchronous operations, optimize for memory hierarchy

### Notes

- Memorize both Amdahl's and Gustafson's Laws and know when each applies (fixed vs scaled problem size).
- Be able to calculate speedup and efficiency from given execution times.
- Understand how GPU features (memory hierarchy, warp scheduling, occupancy) affect scalability.
