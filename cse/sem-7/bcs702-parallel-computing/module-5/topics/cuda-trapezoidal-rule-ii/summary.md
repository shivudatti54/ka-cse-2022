# CUDA Trapezoidal Rule

=====================================

### Overview

The CUDA implementation of the trapezoidal rule leverages massive GPU parallelism by assigning each thread to evaluate the function at a specific subinterval point. The kernel uses shared memory for efficient block-level parallel reduction, and the host performs final summation of block partial sums. This approach can achieve 10x-100x speedup over single-threaded CPU implementations.

### Key Points

- **Thread Mapping:** Global index `i = threadIdx.x + blockIdx.x * blockDim.x` maps each thread to a subinterval point x_i = a + i\*h
- **Boundary Handling:** First (i=0) and last (i=n) points are weighted by 0.5; interior points get full weight
- **Shared Memory Reduction:** Tree-based reduction within each block using `__shared__` memory and `__syncthreads()`
- **Block Partial Sums:** Thread 0 of each block writes the block sum to global memory; host sums all block results
- **Guard Condition:** `if (i <= n)` prevents extra threads from contributing garbage values
- **Block Size:** Must be a power of 2 (typically 128, 256, or 512) for correct tree-based reduction
- **Grid Size:** `numBlocks = (n + 1 + threadsPerBlock - 1) / threadsPerBlock` ensures all points are covered

### Important Concepts

- Reduction takes log2(blockDim.x) steps with stride halving at each step
- Memory hierarchy: registers (x_i, mySum) -> shared memory (reduction) -> global memory (block sums)
- `__syncthreads()` is mandatory between reduction steps to prevent reading stale values
- Final result: `integral = h * sum_of_all_block_partial_sums`

### Notes

- atomicAdd is simpler but slower due to serialization of concurrent writes
- Error is O(h^2) regardless of parallelization method (CUDA, MPI, or OpenMP)
- Always multiply by h after summing -- the kernel computes the sum of f(x_i) values only
- Be able to write the kernel with thread mapping, boundary handling, shared memory reduction, and host code
