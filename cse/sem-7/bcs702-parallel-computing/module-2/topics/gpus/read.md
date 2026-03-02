# GPUs in Parallel Computing

## Introduction

Graphics Processing Units (GPUs) have evolved from specialized graphics accelerators to highly parallel general-purpose computing engines. Modern GPUs contain thousands of lightweight processing cores designed to execute thousands of threads concurrently, making them exceptionally efficient for data-parallel computations where the same operation is applied simultaneously to large datasets. The parallel computing curriculum requires understanding GPUs as architectural solutions for achieving massive throughput in applications ranging from scientific simulations to deep learning.

The fundamental distinction between Central Processing Units (CPUs) and GPUs lies in their design philosophies. CPUs are optimized for low-latency execution of sequential code, featuring sophisticated control logic, large caches, and fewer but more powerful cores. GPUs, in contrast, prioritize throughput over latency by employing many simpler cores that execute operations in lockstep, sacrificing branch prediction and complex caching in favor of massive parallelism. This architectural difference makes GPUs particularly effective for Single Instruction Multiple Data (SIMD) and Single Instruction Multiple Thread (SIMT) workloads where identical operations are performed on large data arrays.

## Key Concepts

### SIMT Execution Model

The Single Instruction Multiple Thread (SIMT) model represents the foundation of GPU parallelism. Unlike traditional SIMD that operates on fixed-width vectors, SIMT allows individual threads to follow independent execution paths while executing the same instruction. Threads are organized into warps—typically containing 32 threads—that execute in lockstep. When threads within a warp take different branch paths (branch divergence), the GPU executes both paths sequentially, masking the inactive threads, which introduces performance overhead.

### Streaming Multiprocessors (SMs)

GPU architecture centers on Streaming Multiprocessors (SMs), also known as Compute Units. Each SM contains multiple processing cores (ALUs), shared memory, registers, and scheduling logic. For example, NVIDIA's Ampere architecture features SMs with 128 CUDA cores. The SM executes threads in groups called warps, scheduling instructions when operands are ready and hiding memory latency through thread switching. The number of SMs and cores per SM determines the GPU's theoretical peak throughput.

### Memory Hierarchy

GPUs exhibit a complex memory hierarchy with distinct characteristics:

- **Registers**: Fastest storage (1-cycle latency), allocated per thread, typically 255 per thread on NVIDIA GPUs
- **Shared Memory**: On-chip memory (4-6 cycles latency), shared among threads within a block, enables data reuse and memory coalescing
- **Global Memory**: Off-chip DRAM (400-800 cycles latency), high bandwidth but high latency, primary storage for GPU data
- **Constant Memory**: Read-only cache optimized for uniform access patterns
- **Texture Memory**: Optimized for spatially correlated data access with built-in interpolation

### GPU-CPU Comparison

| Aspect            | CPU                       | GPU                           |
| ----------------- | ------------------------- | ----------------------------- |
| Core Count        | 4-64 cores                | Thousands of cores            |
| Thread Support    | Limited (hardware)        | Massive (software)            |
| Control Logic     | Complex branch prediction | Simplified                    |
| Cache Size        | Large (MB)                | Small (KB per SM)             |
| Latency Tolerance | Low (optimized)           | High (hidden via parallelism) |
| Best For          | Sequential, branch-heavy  | Data-parallel, throughput     |

### Performance Considerations

**Occupancy** refers to the ratio of active warps to maximum warps per SM. Higher occupancy generally improves performance by better hiding memory latency. Factors affecting occupancy include block size, shared memory usage, and register allocation per thread.

**Memory Coalescing** occurs when threads in a warp access consecutive memory addresses, enabling the GPU to combine multiple memory requests into fewer transactions. Coalesced access significantly improves bandwidth utilization.

## Examples

### Example 1: Thread Index Calculation in 2D Grid

For a kernel launched with 2D block and grid dimensions, the global thread index is computed as:

```
global_id_x = blockIdx.x * blockDim.x + threadIdx.x
global_id_y = blockIdx.y * blockDim.y + threadIdx.y
linear_index = global_id_y * (gridDim.x * blockDim.x) + global_id_x
```

Given a grid of (4, 3) blocks with block dimensions (8, 4), the total threads are 4×3×8×4 = 384.

### Example 2: Occupancy Calculation

For a GPU with maximum 2048 threads per SM, 32 threads per warp, and if a kernel uses 256 threads per block with 48KB shared memory per block:

- Maximum blocks per SM = min(2048/256, 48KB/48KB) = min(8, 1024) = 8 blocks
- Threads per SM = 8 × 256 = 2048
- Warps per SM = 2048/32 = 64
- Occupancy = 2048/2048 × 100% = 100%

### Example 3: Memory Bandwidth Calculation

For a GPU with 512 GB/s memory bandwidth executing a kernel that performs 8 bytes per thread access with 50% arithmetic intensity:

Effective bandwidth = Bandwidth × Arithmetic Intensity = 512 × 0.5 = 256 GB/s

## Exam Tips

1. Understand the difference between SIMD and SIMT execution models clearly—SIMT allows thread-level divergence while SIMD operates on fixed vectors.

2. Remember that warp size is typically 32 threads on NVIDIA GPUs and 64 on AMD GPUs; this affects scheduling and divergence analysis.

3. When calculating global thread indices, always consider both block and grid dimensions in all applicable dimensions.

4. For memory coalescing questions, identify whether consecutive threads access consecutive addresses—coalesced access occurs when thread N accesses address N.

5. Branch divergence only affects threads within the same warp; threads in different warps execute independently without penalty.

6. Know the latency hierarchy: registers < shared memory << global memory; design kernels to maximize use of faster memory types.

7. Occupancy alone does not guarantee performance—consider register pressure, shared memory usage, and memory bandwidth constraints.

8. In GPU programming questions, always verify thread counts do not exceed hardware limits (e.g., maximum threads per block typically 1024).
