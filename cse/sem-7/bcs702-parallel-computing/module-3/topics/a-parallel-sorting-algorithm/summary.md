# Parallel Sorting Algorithms in MPI

=====================================

### Overview

Parallel sorting algorithms distribute the sorting workload across multiple processes in distributed memory systems using MPI. The key challenge is dividing work evenly while minimizing communication overhead. Common algorithms include Sample Sort, Bitonic Sort, Odd-Even Transposition Sort, and Parallel QuickSort, each suited to different data characteristics and system architectures.

### Key Points

- **Data Decomposition:** Block decomposition (contiguous chunks per process) and cyclic decomposition (round-robin distribution).
- **Sample Sort:** Local sort -> select samples -> gather at root -> determine splitters -> broadcast splitters -> redistribute data -> final local sort. Highly efficient for large datasets.
- **Bitonic Sort:** Creates and merges bitonic sequences using compare-exchange operations; works on power-of-two processes; suited for hypercube networks.
- **Odd-Even Transposition Sort:** Alternates odd and even phases of compare-exchange between neighbor processes in a linear array; conceptually simple.
- **Parallel QuickSort:** Root selects pivot, broadcast it; each process partitions data; exchange subsets between process pairs; recurse.
- **Key MPI Functions:** MPI_Scatter (distribute), MPI_Gather (collect), MPI_Alltoall (all-to-all exchange), MPI_Bcast (broadcast), MPI_Barrier (synchronize).
- **Complexity:** Sample Sort O((n/p)log(n/p)), Bitonic Sort O(log^2 n), Odd-Even Sort O(n), Parallel QuickSort O((n/p)log n).

### Important Concepts

- Sample Sort uses p-1 splitters to partition data into p buckets for redistribution
- Communication patterns: point-to-point (direct), collective (all processes), synchronization (barriers)
- Amdahl's Law applies: Speedup <= 1 / [s + (1-s)/p], where s is sequential fraction
- Strong scaling (fixed problem size) vs weak scaling (problem grows with processors)

### Notes

- Know the step-by-step process of Sample Sort; it is commonly asked and demonstrates key MPI concepts.
- Be able to compare algorithms by time complexity, communication cost, and suitability for different scenarios.
- Understand load balancing importance: uneven distribution causes idle processors and reduced efficiency.
