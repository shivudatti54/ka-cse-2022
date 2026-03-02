# Threads, Blocks, and Grids in CUDA

=====================================

### Overview

The CUDA programming model organizes parallel execution into a three-level hierarchy: threads, blocks, and grids. This hierarchy maps to GPU hardware (Streaming Multiprocessors) and provides a scalable abstraction for parallel programming. Understanding thread indexing, warp execution, occupancy, and synchronization is essential for writing efficient CUDA programs.

### Key Points

- **Thread:** Smallest execution unit; each runs an instance of the kernel with unique threadIdx
- **Block:** Group of threads on the same SM; can share memory and synchronize via \_\_syncthreads()
- **Grid:** Collection of all blocks launched by a single kernel; can be 1D, 2D, or 3D
- **Kernel Launch:** kernel<<<gridDim, blockDim>>>(args); gridDim = number of blocks, blockDim = threads per block
- **Warp:** 32 consecutive threads that execute together in SIMT (Single Instruction, Multiple Threads) fashion
- **Warp Divergence:** When threads in a warp take different branches, execution serializes, reducing throughput
- **Occupancy:** Ratio of active warps to maximum warps per SM; affected by registers, shared memory, and block size
- **\_\_syncthreads():** Barrier synchronization for all threads in a block; must be reached by all threads
- **Grid-Stride Loop:** Pattern where each thread processes multiple elements using stride = blockDim.x \* gridDim.x

### Important Concepts

- 1D global index: globalIdx = blockIdx.x \* blockDim.x + threadIdx.x
- 2D indexing: col = blockIdx.x _ blockDim.x + threadIdx.x; row = blockIdx.y _ blockDim.y + threadIdx.y
- Grid size calculation: gridSize = (N + blockSize - 1) / blockSize (ceiling division)
- Occupancy = Active Warps / Max Warps per SM; limited by registers, shared memory, and block size
- Block size should always be a multiple of 32 (warp size); common choices: 128, 256, 512
- Maximum threads per block: 1024 on most modern GPUs

### Notes

- Memorize the built-in variables: threadIdx, blockIdx, blockDim, gridDim (all dim3 type with .x, .y, .z)
- Always use block sizes that are multiples of 32 to avoid wasting threads in partial warps
- Minimize warp divergence by structuring conditionals so all threads in a warp take the same path
- Maximum occupancy does not always mean maximum performance -- balance registers and shared memory usage
