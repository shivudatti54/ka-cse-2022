# Loop-Carried Dependencies in OpenMP

=====================================

### Overview

A loop-carried dependency occurs when a computation in iteration i depends on data computed in a previous iteration j (j < i), creating a sequential ordering constraint that conflicts with parallel execution. Identifying and resolving these dependencies is a critical skill for parallelizing loops with OpenMP.

### Key Points

- **Flow Dependency (RAW):** Read-After-Write; iteration i reads a value written by iteration i-1 (e.g., `a[i] = a[i-1] + 1`)
- **Anti-Dependency (WAR):** Write-After-Read; a value read in iteration i is overwritten in iteration i+1
- **Output Dependency (WAW):** Same memory location is written by multiple iterations (e.g., accumulating into `sum`)
- **Reduction Clause:** Solves output dependencies on accumulation variables (`reduction(+:sum)`)
- **Loop Restructuring:** Split loops into parallelizable and sequential parts
- **Algorithmic Change:** Use parallel algorithms like tree-based prefix sum for complex dependencies
- **Synchronization:** Using `#pragma omp critical` or `atomic` is correct but destroys performance

### Important Concepts

- `a[i] = a[i] + b[i]` is parallelizable; `a[i] = a[i-1] + b[i]` is NOT (flow dependency)
- Dependencies within a single iteration do not prevent parallelization
- The `depend` clause (OpenMP 4.0+) enables explicit task-ordering constraints
- Prefix sum has a parallel tree-based algorithm: O(log N) time with O(N) processors

### Notes

- First check if a loop variable is a reduction candidate (sum, product, min, max)
- Index patterns using i-1, i+1, or i+k are red flags for flow dependencies
- Never suggest `critical` or `atomic` as a solution for simple reductions -- use the `reduction` clause
- Draw a table tracking array values across iterations to make dependencies visually obvious
