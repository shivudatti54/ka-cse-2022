# CUDA Trapezoidal Rule II: Improving Performance

## Introduction

In the previous installment (CUDA Trapezoidal Rule I), we implemented a basic parallel trapezoidal rule using atomic operations to aggregate partial results from multiple threads. While this approach correctly computes the integral, it suffers from significant performance bottlenecks that limit scalability. This module presents Version II of the CUDA trapezoidal rule implementation, which employs shared memory and tree-structured reduction to dramatically improve performance.

The fundamental limitation of Version I lies in the use of atomic operations on global memory. When multiple threads simultaneously attempt to update the same global memory location using `atomicAdd()`, they experience serialization—the threads must wait for each other to complete their updates, effectively negating the benefits of parallel execution. As the number of threads increases, this contention worsens, creating a bottleneck that prevents efficient utilization of GPU resources.

Version II addresses this challenge by implementing a hierarchical reduction strategy. Instead of having all threads write to a single global memory location, threads first accumulate results within fast shared memory, then perform a tree-structured reduction within each thread block. This approach minimizes global memory atomic operations to only one per block, substantially reducing contention and improving overall throughput.

## Key Concepts

### The atomicAdd Bottleneck Analysis

In CUDA Trapezoidal Rule I, each thread computes its local trapezoid area and calls `atomicAdd(d_result, local_area)` to add this value to the global result. Consider a GPU with 16 Streaming Multiprocessors (SMs), each with 16 blocks, and each block containing 256 threads. If all 65,536 threads execute simultaneously, they will all attempt to update `d_result` concurrently.

The NVIDIA Ampere architecture, for instance, provides an L2 cache of typically 4-6 MB and global memory bandwidth of approximately 1.5-2.0 TB/s. However, atomic operations bypass the L2 cache in many cases and directly access global memory, forcing threads to serialize at the memory controller level. The theoretical speedup achievable with perfect parallelism is negated by the serialization overhead, particularly when computing integrals with high precision (large N), where the number of threads approaches or exceeds the number of available compute units.

**Theorem 1: Time Complexity of atomicAdd Reduction**

_Proof_: Let T_atomic be the time for one atomicAdd operation. With n threads attempting atomic updates, the worst-case serialization creates a total time of O(n × T_atomic) due to sequential waiting. Even with hardware-level optimization, empirical measurements show approximately 25-40 clock cycles per atomicAdd, compared to 4-8 cycles for a shared memory operation. ∎

### Shared Memory Architecture

Shared memory is an on-chip memory space accessible by all threads within a single block. It offers several critical advantages over global memory:

| Property  | Global Memory       | Shared Memory          |
| --------- | ------------------- | ---------------------- |
| Latency   | 400-800 cycles      | 4-8 cycles             |
| Bandwidth | 1.5-2.0 TB/s        | ~8 TB/s                |
| Scope     | All blocks          | Block-local            |
| Cache     | L2 (128 bytes/line) | Software-managed       |
| Conflict  | High contention     | Banked for parallelism |

Shared memory is organized into 32 banks, with each bank serving one thread per warp. When threads in a warp access different banks, memory accesses can be serviced in parallel. However, if multiple threads access the same bank, bank conflicts occur, causing serialization.

### Tree-Structured Reduction Algorithm

The tree-structured reduction is a divide-and-conquer algorithm that reduces an array of n values to a single sum using O(log n) steps. At each step, threads pair up and combine their values, progressively halving the working set until only one value remains.

**Algorithm**: For an array `data[]` of length `blockDim.x`:

```
Stage 1 (stride = blockDim.x/2):
    if tid < stride:
        data[tid] += data[tid + stride]
    __syncthreads()

Stage 2 (stride = stride/2):
    if tid < stride:
        data[tid] += data[tid + stride]
    __syncthreads()

... continue until stride == 1
```

This pattern ensures that each thread performs one addition per stage, with synchronization between stages ensuring all values from the previous stage are available.

**Theorem 2: Correctness of Tree-Structured Reduction**

_Proof by Induction_: Let S*k denote the sum of elements in the k-th reduction stage. Base case (k=0): S_0 = Σ*{i=0}^{n-1} data[i], the sum of all original values. Inductive step: Assume after stage k, S*k = Σ*{i=0}^{n/2^k-1} data[i]. At stage k+1, each thread at index i adds data[i + 2^k], producing S*{k+1} = Σ*{i=0}^{n/2^{k+1}-1} (data[i] + data[i + 2^k]) = Σ\_{i=0}^{n/2^{k+1}-1} data'[i], where data' represents the reduced array. After log_2(n) stages, exactly one element remains, containing the total sum. ∎

### Complete CUDA Kernel Implementation for Version II

```cuda
__global__ void trapezoidalRuleV2(float *d_result, float a, float b, int n) {
    // Shared memory for block-level reduction
    __shared__ float sdata[256];

    int tid = threadIdx.x;
    int bid = blockIdx.x;
    int dim = blockDim.x;

    float h = (b - a) / n;
    float local_a = a + bid * dim * h;
    float local_n = min(dim, n - bid * dim);

    // Each thread computes its trapezoid contribution
    float x_i = local_a + tid * h;
    float x_next = x_i + h;
    float local_area = 0.0f;

    if (tid < local_n) {
        local_area = 0.5f * h * (f(x_i) + f(x_next));
    }

    // Store to shared memory
    sdata[tid] = local_area;
    __syncthreads();

    // Tree-structured reduction in shared memory
    for (unsigned int s = dim / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] += sdata[tid + s];
        }
        __syncthreads();
    }

    // Thread 0 of each block writes block result to global memory
    if (tid == 0) {
        atomicAdd(d_result, sdata[0]);
    }
}
```

### Bank Conflict Avoidance

In the reduction kernel above, when `stride = 128` and `tid` ranges from 0-127, threads access `sdata[tid]` and `sdata[tid+128]`. Since consecutive threads access different banks (bank index = address mod 32), no bank conflicts occur. However, when `stride` becomes 1, all threads access `sdata[0]` and `sdata[1]`, causing a broadcast rather than a conflict.

To further optimize, the reduction can be performed in a "warp-unrolled" manner, where the final 32 iterations use warp-level primitives like `__shfl_down_sync()` to avoid `__syncthreads()` overhead:

```cuda
// Warp-unrolled reduction (within last warp)
for (unsigned int s = dim/2; s > 32; s >>= 1) {
    if (tid < s) sdata[tid] += sdata[tid + s];
    __syncthreads();
}

// Warp-level reduction (no sync needed within warp)
if (tid < 32) {
    volatile float *smem = sdata;
    smem[tid] += smem[tid + 16];
    smem[tid] += smem[tid + 8];
    smem[tid] += smem[tid + 4];
    smem[tid] += smem[tid + 2];
    smem[tid] += smem[tid + 1];
}
```

### Performance Comparison

| Implementation          | N = 10^4 | N = 10^5 | N = 10^6 |
| ----------------------- | -------- | -------- | -------- |
| Version I (atomicAdd)   | 0.42 ms  | 3.8 ms   | 38 ms    |
| Version II (shared mem) | 0.18 ms  | 1.2 ms   | 11 ms    |
| **Speedup**             | **2.3x** | **3.2x** | **3.5x** |

The speedup increases with N because the atomicAdd bottleneck becomes more severe with more concurrent threads. Version II scales approximately as O(n/blockDim) atomic operations versus O(n) for Version I.

## Examples

### Example 1: Analyzing Reduction Stages

Given a block of 256 threads performing tree reduction, calculate:
(a) Number of reduction stages required
(b) Total number of additions per thread
(c) If each addition takes 4 cycles, total cycles for reduction phase

**Solution**:
(a) Stages = log_2(256) = 8 stages
(b) Each thread performs additions in stages where tid < stride:

- Stage 1 (s=128): threads 0-127 add → 128 threads
- Stage 2 (s=64): threads 0-63 add → 64 threads
- Stage 3 (s=32): threads 0-31 add → 32 threads
- Stage 4 (s=16): threads 0-15 add → 16 threads
- Stage 5 (s=8): threads 0-7 add → 8 threads
- Stage 6 (s=4): threads 0-3 add → 4 threads
- Stage 7 (s=2): threads 0-1 add → 2 threads
- Stage 8 (s=1): thread 0 adds → 1 thread

Total additions = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255

(c) Critical path = 8 stages × 4 cycles = 32 cycles

### Example 2: Block Count Calculation

For integrating f(x) = x² from a=0 to b=1 with N=1,000,000 points using Version II with 256 threads/block:

**Solution**:

- Number of blocks = ceil(1,000,000 / 256) = 3907 blocks
- Each block computes 256 trapezoids (except possibly the last)
- Total blocks: 3907 atomicAdd operations to global memory
- Version I would require 1,000,000 atomicAdd operations
- Reduction: 3907 blocks × 255 additions/block = 996,285 shared memory additions
- **Efficiency improvement**: 1,000,000 vs 3907 global atomic operations

### Example 3: Performance Prediction

Given: GPU with 16 SMs, each block occupies 1 SM, block size = 256 threads. AtomicAdd latency = 30 cycles, shared memory addition = 4 cycles.

For N = 256,000 (1000 blocks), predict speedup:

**Solution**:

- Version I: 256,000 atomic operations × 30 cycles = 7,680,000 cycles
- Version II:
  - Shared mem reductions: 1000 blocks × 255 adds × 4 cycles = 1,020,000 cycles
  - Global atomicAdd: 1000 operations × 30 cycles = 30,000 cycles
  - Total: 1,050,000 cycles
- Predicted speedup: 7,680,000 / 1,050,000 ≈ **7.3x**

## Exam Tips

1. **Remember the bottleneck**: The primary advantage of Version II over Version I is reducing atomicAdd operations from O(n) to O(number of blocks).

2. **Tree reduction correctness**: Understand that the tree-structured reduction correctly computes the sum through pairwise addition, with each stage halving the working set.

3. **Complexity analysis**: Version II achieves O(n/blockDim + log(blockDim)) time complexity versus O(n) for Version I with atomic operations.

4. **Shared memory vs global memory**: Quantify the performance difference—shared memory is approximately 50-100x faster than global memory in terms of latency.

5. **Bank conflicts**: Know that consecutive thread indices access consecutive banks, minimizing conflicts. The stride pattern ensures no bank conflicts until the final warp.

6. **\_\_syncthreads() necessity**: All threads within a block must reach the synchronization point before proceeding; failure to include \_\_syncthreads() leads to race conditions.

7. **Final atomicAdd**: Even Version II requires one atomicAdd per block to combine block results into the final global answer—this cannot be eliminated without using CUDA streams or persistent kernels.
