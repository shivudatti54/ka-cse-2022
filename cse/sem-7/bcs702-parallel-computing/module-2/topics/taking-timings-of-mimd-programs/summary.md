# Taking Timings of MIMD Programs - Summary

## Key Definitions

- **Wall-Clock Time**: Actual elapsed time from program start to completion as observed by a user; the primary metric for measuring parallel program performance.
- **CPU Time**: Total time the CPU spends executing instructions; in parallel programs, sum of CPU times across all processors exceeds wall-clock time.
- **Speedup (S(p))**: Ratio of sequential execution time to parallel execution time with p processors: S(p) = T(1) / T(p).
- **Efficiency (E(p))**: Ratio of speedup to number of processors: E(p) = S(p) / p, indicating how effectively processors are utilized.
- **Synchronization Overhead**: Time spent waiting at synchronization points (barriers, locks) for threads to coordinate.
- **Communication Overhead**: Time spent transferring data between processing elements in distributed memory systems.
- **Load Imbalance**: Uneven work distribution causing some processors to idle while others continue working.

## Important Formulas

- **Speedup**: S(p) = T(1) / T(p), where T(1) is sequential time and T(p) is parallel time with p processors
- **Efficiency**: E(p) = S(p) / p × 100% (expressed as percentage)
- **Total CPU Time**: T_cpu_total = Σ T_cpu_i (sum of CPU times across all processors)
- **Parallel Overhead**: T_overhead = p × T(p) - T(1)

## Key Points

1. Wall-clock time is the preferred metric for parallel program timing as it reflects actual user-perceived execution time.

2. MIMD programs involve multiple overhead sources: synchronization, communication, load imbalance, and thread management.

3. MPI provides MPI_Wtime() for accurate wall-clock timing with nanosecond resolution.

4. OpenMP provides omp_get_wtime() for timing parallel regions.

5. Timing methodology requires multiple runs to account for system variability; discard the first run.

6. Speedup can exceed processor count (super-linear speedup) due to cache effects but usually indicates measurement issues.

7. Efficiency of 100% indicates perfect linear speedup; practical MIMD programs typically show 50-90% efficiency.

8. Strong scaling measures performance with fixed problem size; weak scaling measures performance when problem size increases with processor count.

9. Load imbalance is a major source of overhead when work is unevenly distributed among processors.

10. Timer resolution must be sufficient relative to the measured interval to ensure accurate readings.

## Common Mistakes

1. **Using CPU time instead of wall-clock time**: This leads to inflated time estimates that don't reflect actual program execution duration.

2. **Timing only computation**: Forgetting to include communication and synchronization phases gives an incomplete picture of parallel performance.

3. **Single-run measurements**: Failing to run multiple iterations introduces high variability and unreliable results.

4. **Including initialization time**: Timing should exclude one-time setup costs unless they are relevant to the analysis.

5. **Ignoring load imbalance**: Not considering work distribution effects leads to incorrect conclusions about parallel efficiency.

6. **Wrong timing granularity**: Timing too small code sections can produce meaningless results due to timer resolution limitations.