# Shared-Memory Programming with OpenMP – OpenMP Pragmas and Directives - Summary

## Key Definitions and Concepts

- **OpenMP**: API for shared-memory parallel programming using compiler directives
- **Pragma**: Compiler-specific directive (`#pragma omp ...`) for parallelization
- **Parallel Region**: Code block executed by multiple threads simultaneously
- **Fork-Join Model**: Execution model where master thread spawns worker threads
- **Work-Sharing Constructs**: Directives like `parallel for` to distribute loop iterations
- **Implicit Barrier**: Synchronization point where all threads wait (default at end of parallel region)
- **Master Thread**: Thread with ID 0 that exists throughout program execution

## Important Formulas and Theorems

1. **Trapezoidal Rule (Parallel Version)**:
   ```c
   #pragma omp parallel for reduction(+:integral)
   for(i=0; i<n; i++) {
       integral += (f(x[i]) + f(x[i+1])) * (x[i+1]-x[i])/2;
   }
   ```
2. **Amdahl's Law (Speedup)**:
   `S = 1 / ((1 - P) + P/N)` where P=parallel fraction, N=processors

3. **Chunk Size in Scheduling**:
   `chunk = ceil(n_iterations / n_threads)` for static scheduling

## Key Points

- OpenMP uses **#pragma** directives to parallelize code without rewriting entire programs
- Basic structure:
  ```c
  #pragma omp parallel [clause]
  {
      // Parallel region
  }
  ```
- Thread count controlled by `omp_set_num_threads()` or `OMP_NUM_THREADS` environment variable
- **Variable Scoping**:
  - `shared` (default for global variables)
  - `private` (new instance per thread)
  - `firstprivate` (private with initialization)
- **Reduction Clause**:
  ```c
  #pragma omp parallel for reduction(+:sum)
  ```
  Handles conflicts in cumulative operations
- **Loop Scheduling Options**:
  - `static`: Pre-determined chunks
  - `dynamic`: Runtime allocation
  - `guided`: Decreasing chunk sizes
- **Tasking**:
  ```c
  #pragma omp task
  ```
  For irregular parallelism (e.g., recursive algorithms)
- **False Sharing**: Performance killer when threads modify adjacent memory locations (same cache line)

## Common Mistakes to Avoid

1. **Missing `default(none)` clause**: Leads to unintended shared variables
2. **Incorrect reduction operator**: Using `*` instead of `+` for summation
3. **Ignoring loop-carried dependencies**: Parallelizing loops with data dependencies
4. **Overlooking false sharing**: Not padding critical variables in arrays

## Revision Tips

1. **Practice Core Pragmas**: Memorize syntax for:
   ```c
   #pragma omp parallel
   #pragma omp parallel for
   #pragma omp critical
   #pragma omp barrier
   ```
2. **Scope Flowchart**: Create decision tree for variable scoping (shared vs private)
3. **Trapezoidal Rule Code**: Write from memory including reduction clause
4. ** Pattern Focus**: Study previous questions on parallel region creation and loop scheduling
