# Amdahl's Law

=====================================

### Overview

Amdahl's Law is a fundamental principle describing the theoretical maximum speedup achievable when parallelizing a computation. Formulated by Gene Amdahl in 1967, it shows that speedup is fundamentally limited by the sequential (non-parallelizable) portion of a program, regardless of how many processors are used.

### Key Points

- **Formula:** Speedup = 1 / [(1 - P) + (P / N)], where P = parallelizable fraction, N = number of processors.
- **Maximum Speedup (N -> infinity):** Speedup_max = 1 / (1 - P). Even with infinite processors, speedup is bounded by the sequential fraction.
- **Example:** If P = 0.9 (90% parallelizable) with 10 processors: Speedup = 1 / [0.1 + 0.09] = 5.26x (not 10x).
- **Parallel Efficiency:** Efficiency = Speedup / N. Efficiency decreases as N increases due to the fixed sequential component.
- **GPU Context:** Data transfer (CPU-GPU), kernel launch overhead, and memory hierarchy effects add to the sequential component.
- **Gustafson's Law (Alternative):** Scaled Speedup = N + (1 - N) \* S. Assumes problem size grows with processors, giving a more optimistic outlook.
- **Extended Formula with Overhead:** Speedup = 1 / [S + (1-S)/N + O(N)], where O(N) represents parallel overhead.

### Important Concepts

- Sequential portion includes: initialization, I/O, control structures with data dependencies, result aggregation
- Diminishing returns: small sequential fractions still dramatically limit speedup at large N
- Gustafson's Law is more applicable when problem size scales with available parallelism (weak scaling)
- Optimizing the sequential portion often provides better returns than adding more processors

### Notes

- Memorize the formula and be able to calculate speedup given P and N; also calculate maximum speedup as N approaches infinity.
- In GPU programming questions, remember that data transfer between CPU and GPU is a significant sequential component.
- Compare Amdahl's Law (fixed problem size, pessimistic) with Gustafson's Law (scaled problem size, optimistic).
