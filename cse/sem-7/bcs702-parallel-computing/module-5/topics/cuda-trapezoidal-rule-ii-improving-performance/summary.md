# CUDA Trapezoidal Rule II: Improving Performance

=====================================

### Overview

The improved CUDA trapezoidal rule replaces the atomicAdd bottleneck of version I with a tree-structured parallel reduction in shared memory. Each thread loads its computed f(x_i) value into shared memory, then threads cooperate to reduce all values within the block in O(log n) steps using \_\_syncthreads() barriers. Only thread 0 of each block writes a single partial sum to global memory. The host (or a second kernel) performs a final summation of the small number of block-level results.

### Key Points

- **atomicAdd bottleneck**: Serializes all N thread writes to one global address, making performance O(N) -- worse with more threads
- **Shared memory reduction**: Threads within a block cooperatively sum values in fast on-chip shared memory (~5 cycle latency vs ~400-800 for global)
- **Tree-structured algorithm**: Stride halves each step (blockDim/2, blockDim/4, ..., 1), requiring log2(blockDim) steps
- **\_\_syncthreads()**: Mandatory barrier between every reduction step; must be reached by all threads in the block (place outside conditionals)
- **One write per block**: Thread 0 writes sdata[0] to blockSums[blockIdx.x], replacing blockDim.x atomic operations with one store
- **Host final reduction**: CPU sums the numBlocks partial sums and multiplies by h
- **Power-of-2 block sizes**: Required for correct stride-halving reduction (use 128, 256, or 512)
- **Sequential addressing preferred**: Stride-halving keeps adjacent threads accessing adjacent memory, avoiding warp divergence and bank conflicts

### Important Concepts

- Stride-halving reduction: `for (s = blockDim.x/2; s > 0; s >>= 1)` with `sdata[tid] += sdata[tid + s]`
- Dynamic shared memory: `extern __shared__ double sdata[]` sized at launch via third <<<>>> argument
- Extra threads beyond n contribute zero (guard: `if (i <= n)` with myVal initialized to 0.0)
- Shared memory bank conflicts minimized by sequential addressing pattern
- Two-kernel approach possible: kernel 1 reduces within blocks, kernel 2 reduces block sums entirely on GPU

### Notes

- Typical speedup of version II over version I: 10x-50x for large N
- The stride-doubling (older) pattern causes warp divergence and bank conflicts -- avoid it
- The mathematical result is identical; only the performance differs between versions I and II
- This reduction pattern is the foundation of nearly all high-performance CUDA applications
