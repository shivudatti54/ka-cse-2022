# Performance Evaluation of MPI Programs

=====================================

### Overview

Performance evaluation of MPI programs involves measuring execution time, calculating speedup and efficiency, and identifying communication bottlenecks. MPI provides the `MPI_Wtime()` function for high-resolution wall-clock timing, which is the primary tool for benchmarking parallel programs on distributed memory systems.

### Key Points

- **MPI_Wtime():** Returns wall-clock time in seconds as a double; used to measure execution time
- **Speedup:** S(p) = T_serial / T_parallel(p); ideal speedup equals the number of processes p
- **Efficiency:** E(p) = S(p) / p; measures how effectively each process is utilized (ideal = 1.0)
- **Communication Overhead:** Time spent in MPI_Send, MPI_Recv, and collective operations
- **Computation-to-Communication Ratio:** Higher ratio indicates better parallel efficiency
- **Amdahl's Law:** S(p) <= 1 / (f + (1-f)/p), where f is the serial fraction
- **Scalability:** Ability to maintain efficiency as the number of processes increases

### Important Concepts

- Elapsed time = `end_time - start_time` where both are obtained via `MPI_Wtime()`
- Timing should be measured at rank 0 (or use MPI_Reduce with MPI_MAX across all ranks)
- Parallel overhead includes communication latency, synchronization waits, and load imbalance
- Strong scaling: fixed problem size, increase processes; Weak scaling: increase both proportionally

### Notes

- Always place MPI_Wtime() calls around the section of code being measured, not around MPI_Init/Finalize
- Use MPI_Barrier before timing to ensure all processes start simultaneously
- Run multiple trials and report average time to account for system variability
- Identify whether the program is compute-bound or communication-bound before optimizing
