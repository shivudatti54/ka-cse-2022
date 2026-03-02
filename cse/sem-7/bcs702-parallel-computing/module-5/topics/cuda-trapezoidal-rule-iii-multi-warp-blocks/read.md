# CUDA Trapezoidal Rule III: Blocks with More Than One Warp

## Recap: Tree-Based Reduction from Trapezoidal Rule II

In the previous version of the CUDA trapezoidal rule, every iteration of the tree-based reduction used `__syncthreads()` to ensure all threads completed their additions before the next step:

```cuda
for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
 if (tid < s) {
 sdata[tid] += sdata[tid + s];
 }
 __syncthreads(); // Called every iteration
}
```

For a block of 256 threads, this performs 8 reduction steps (log2(256) = 8) with 8 calls to `__syncthreads()`. But some of these synchronization barriers are unnecessary, and removing them yields measurable performance gains.

## The Multi-Warp Problem

### Warp: The Fundamental Execution Unit

A **warp** is a group of 32 consecutive threads that execute instructions in lockstep on a single Streaming Multiprocessor (SM). This is NVIDIA's SIMT (Single Instruction, Multiple Threads) execution model:

- Warp 0: threads 0-31
- Warp 1: threads 32-63
- Warp 2: threads 64-95
- Warp 3: threads 96-127
- ...and so on

All threads within a warp execute the same instruction at the same time. They do not need explicit synchronization because they are physically unable to diverge in their execution order (excluding branch divergence, which is a separate concern).

### How Many Warps per Block?

The number of warps depends on the block size:

| Block Size (threads) | Number of Warps | Sync Needed Between Warps? |
| -------------------- | --------------- | -------------------------- |
| 32                   | 1               | No                         |
| 64                   | 2               | Yes                        |
| 128                  | 4               | Yes                        |
| 256                  | 8               | Yes                        |
| 512                  | 16              | Yes                        |
| 1024                 | 32              | Yes                        |

When a block has more than one warp, threads in different warps can be at different points in their execution. Warp 0 might be on reduction step 3 while Warp 4 is still on step 2. This is why `__syncthreads()` is needed -- it creates a barrier that all threads in the block must reach before any can proceed.

### When Synchronization Becomes Unnecessary

Consider a block of 256 threads performing tree reduction. The stride values are:

```
Step 1: stride = 128 (threads 0-127 active, spans all 8 warps) -> need __syncthreads()
Step 2: stride = 64 (threads 0-63 active, spans warps 0-1) -> need __syncthreads()
Step 3: stride = 32 (threads 0-31 active, all in warp 0) -> NO sync needed!
Step 4: stride = 16 (threads 0-15 active, all in warp 0) -> NO sync needed!
Step 5: stride = 8 (threads 0-7 active, all in warp 0) -> NO sync needed!
Step 6: stride = 4 (threads 0-3 active, all in warp 0) -> NO sync needed!
Step 7: stride = 2 (threads 0-1 active, all in warp 0) -> NO sync needed!
Step 8: stride = 1 (thread 0 only) -> NO sync needed!
```

Once the stride drops to 32 or below, all remaining active threads belong to a single warp (warp 0). Since warp execution is lockstep, these threads are implicitly synchronized. The last 5 iterations (strides 32, 16, 8, 4, 2, 1) never need `__syncthreads()`.

## Approach 1: Unrolling the Last Warp with volatile

### The volatile Keyword for Shared Memory

On architectures before Volta (i.e., before compute capability 7.0), when we remove `__syncthreads()` from the last warp's reduction, the compiler might optimize away shared memory reads by caching values in registers. To prevent this, the shared memory pointer must be declared `volatile`:

```cuda
volatile double* vsdata = sdata;
```

The `volatile` keyword forces every read and write to go directly to shared memory, ensuring that one thread can see another thread's most recent write without an explicit synchronization barrier.

### Optimized Kernel with Warp Unrolling

```cuda
__global__ void trapKernelV3(double a, double h, int n,
 double* partialSums) {
 extern __shared__ double sdata[];
 int tid = threadIdx.x;
 int i = threadIdx.x + blockIdx.x * blockDim.x;

 // Compute this thread's contribution
 double mySum = 0.0;
 if (i <= n) {
 double x_i = a + i * h;
 mySum = f(x_i);
 if (i == 0 || i == n) mySum *= 0.5;
 }

 sdata[tid] = mySum;
 __syncthreads();

 // Tree reduction: synchronized phase (multiple warps active)
 for (unsigned int s = blockDim.x / 2; s > 32; s >>= 1) {
 if (tid < s) {
 sdata[tid] += sdata[tid + s];
 }
 __syncthreads();
 }

 // Warp-level reduction: no __syncthreads() needed
 if (tid < 32) {
 volatile double* vsdata = sdata;
 vsdata[tid] += vsdata[tid + 32];
 vsdata[tid] += vsdata[tid + 16];
 vsdata[tid] += vsdata[tid + 8];
 vsdata[tid] += vsdata[tid + 4];
 vsdata[tid] += vsdata[tid + 2];
 vsdata[tid] += vsdata[tid + 1];
 }

 if (tid == 0) {
 partialSums[blockIdx.x] = sdata[0];
 }
}
```

Key changes from the version II kernel:

1. The loop now stops at `s > 32` instead of `s > 0`
2. The final 6 additions (strides 32 through 1) are manually unrolled
3. A `volatile` pointer is used for the unrolled section
4. No `__syncthreads()` calls in the unrolled section

### Why This Works

Since threads 0-31 all belong to warp 0, they execute in lockstep:

- All 32 threads simultaneously execute `vsdata[tid] += vsdata[tid + 32]`
- All 32 threads simultaneously execute `vsdata[tid] += vsdata[tid + 16]`
- And so on for strides 8, 4, 2, 1

No thread can "get ahead" of another within the same warp, so no synchronization is needed. The `volatile` keyword ensures that the writes to shared memory are visible to all threads in the warp immediately.

## Approach 2: Warp Shuffle Instructions (\_\_shfl_down_sync)

### What Are Warp Shuffle Instructions?

Starting with compute capability 3.0 (Kepler architecture), NVIDIA introduced **warp shuffle instructions** that allow threads within a warp to directly read each other's register values without using shared memory at all.

The key instruction for reductions is:

```cuda
int __shfl_down_sync(unsigned mask, int var, unsigned delta, int width=32);
double __shfl_down_sync(unsigned mask, double var, unsigned delta, int width=32);
```

Parameters:

- `mask`: Bitmask specifying which threads participate (0xFFFFFFFF for all 32 threads)
- `var`: The register value to share
- `delta`: The lane offset -- thread `i` receives the value from thread `i + delta`
- `width`: The logical warp width (default 32)

### How \_\_shfl_down_sync Works

For a shuffle down with `delta = 16` among 32 threads:

```
Thread 0 gets value from Thread 16
Thread 1 gets value from Thread 17
Thread 2 gets value from Thread 18
...
Thread 15 gets value from Thread 31
Thread 16 gets its own value (16 + 16 = 32 >= warp size, so identity)
...
Thread 31 gets its own value
```

This is exactly what we need for tree reduction -- each thread adds the value from a thread that is `delta` positions ahead.

### Warp-Level Reduction Using Shuffles

```cuda
__device__ double warpReduceSum(double val) {
 val += __shfl_down_sync(0xFFFFFFFF, val, 16);
 val += __shfl_down_sync(0xFFFFFFFF, val, 8);
 val += __shfl_down_sync(0xFFFFFFFF, val, 4);
 val += __shfl_down_sync(0xFFFFFFFF, val, 2);
 val += __shfl_down_sync(0xFFFFFFFF, val, 1);
 return val; // Thread 0 (lane 0) of the warp holds the sum
}
```

After this function:

- Lane 0 of the warp holds the sum of all 32 values
- No shared memory was used
- No `__syncthreads()` was called
- No bank conflicts are possible (no shared memory access)

### Advantages of Warp Shuffles Over Shared Memory

| Aspect          | Shared Memory + volatile     | Warp Shuffle (\_\_shfl_down_sync) |
| --------------- | ---------------------------- | --------------------------------- |
| Memory usage    | Requires shared memory array | No shared memory needed           |
| Bank conflicts  | Possible                     | Impossible                        |
| Latency         | ~5 cycles per access         | ~1 cycle per instruction          |
| Code complexity | Need volatile pointer        | Clean, single-line operations     |
| Minimum CC      | Any                          | 3.0+ (Kepler and later)           |
| Synchronization | Implicit via SIMT            | Explicit via mask parameter       |

## Two-Phase Reduction: The Complete Optimized Approach

When a block has multiple warps, a single call to `warpReduceSum` only reduces within one warp. We need a **two-phase reduction**:

**Phase 1:** Each warp independently reduces its 32 values to a single value using warp shuffles.
**Phase 2:** The per-warp results are collected and reduced using shared memory.

### Complete Optimized Kernel

```cuda
__device__ double warpReduceSum(double val) {
 val += __shfl_down_sync(0xFFFFFFFF, val, 16);
 val += __shfl_down_sync(0xFFFFFFFF, val, 8);
 val += __shfl_down_sync(0xFFFFFFFF, val, 4);
 val += __shfl_down_sync(0xFFFFFFFF, val, 2);
 val += __shfl_down_sync(0xFFFFFFFF, val, 1);
 return val;
}

__device__ double blockReduceSum(double val) {
 __shared__ double warpSums[32]; // Max 32 warps per block (1024/32)
 int lane = threadIdx.x % 32; // Lane within the warp (0-31)
 int warpId = threadIdx.x / 32; // Which warp this thread belongs to

 // Phase 1: Reduce within each warp
 val = warpReduceSum(val);

 // Lane 0 of each warp writes its result to shared memory
 if (lane == 0) {
 warpSums[warpId] = val;
 }
 __syncthreads(); // Wait for all warps to write

 // Phase 2: First warp reduces the warp sums
 // Only threads in warp 0 participate
 int numWarps = blockDim.x / 32;
 val = (threadIdx.x < numWarps) ? warpSums[threadIdx.x] : 0.0;
 if (warpId == 0) {
 val = warpReduceSum(val);
 }

 return val; // Thread 0 holds the block sum
}

__global__ void trapKernelOptimized(double a, double h, int n,
 double* partialSums) {
 int i = threadIdx.x + blockIdx.x * blockDim.x;

 // Compute this thread's contribution
 double mySum = 0.0;
 if (i <= n) {
 double x_i = a + i * h;
 mySum = f(x_i);
 if (i == 0 || i == n) mySum *= 0.5;
 }

 // Two-phase reduction
 mySum = blockReduceSum(mySum);

 // Thread 0 writes block result
 if (threadIdx.x == 0) {
 partialSums[blockIdx.x] = mySum;
 }
}
```

### Detailed Walkthrough: 256-Thread Block

For a block with 256 threads (8 warps):

**Phase 1 -- Intra-warp shuffle reduction:**

```
Warp 0 (threads 0-31): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 1 (threads 32-63): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 2 (threads 64-95): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 3 (threads 96-127): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 4 (threads 128-159): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 5 (threads 160-191): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 6 (threads 192-223): 32 values -> 1 value in lane 0 (5 shuffles)
Warp 7 (threads 224-255): 32 values -> 1 value in lane 0 (5 shuffles)
```

After Phase 1: 8 partial sums stored in `warpSums[0..7]`.

**Phase 2 -- Inter-warp shared memory reduction:**

```
Warp 0 loads warpSums[0..7] (threads 0-7 load values, threads 8-31 load 0)
Warp 0 performs warpReduceSum -> thread 0 holds the final block sum
```

Total synchronization calls: **just 1** `__syncthreads()` (between Phase 1 and Phase 2), compared to 8 in the original version.

## The Shared Memory Array for Warp Sums

In the two-phase approach, shared memory usage is dramatically reduced:

| Approach                     | Shared Memory Per Block (256 threads, double) |
| ---------------------------- | --------------------------------------------- |
| Original (Rule II)           | 256 \* 8 = 2048 bytes                         |
| Two-phase with warp shuffles | 32 \* 8 = 256 bytes (only for warp sums)      |

The shared memory array `warpSums[32]` needs at most 32 entries because the maximum block size is 1024 threads = 32 warps.

## Performance Comparison: Three Versions

### Version I: Basic (atomicAdd)

- Every thread does `atomicAdd(result, myVal)`
- Extreme serialization, slowest approach
- No shared memory, no reduction tree

### Version II: Tree Reduction with Full Sync

- Tree-based reduction in shared memory
- `__syncthreads()` at every level of the tree
- log2(blockDim.x) sync barriers per block

### Version III: Multi-Warp Optimized

- Warp shuffle for intra-warp reduction (no shared memory, no sync)
- Shared memory only for inter-warp communication
- Only 1 `__syncthreads()` call per block

### Typical Speedup (256-thread blocks, large n)

| Version     | Sync Barriers | Shared Mem (bytes) | Relative Performance |
| ----------- | ------------- | ------------------ | -------------------- |
| I (atomic)  | 0             | 0                  | 1.0x (baseline)      |
| II (tree)   | 8             | 2048               | ~10-20x              |
| III (warps) | 1             | 256                | ~12-25x              |

The improvement from Version II to III comes from:

1. Fewer synchronization barriers (1 vs 8) -- each `__syncthreads()` has overhead
2. Warp shuffles are faster than shared memory reads (~1 cycle vs ~5 cycles)
3. No shared memory bank conflicts during warp-level reduction
4. Reduced shared memory usage allows higher occupancy (more blocks per SM)

## Important Considerations

### The 0xFFFFFFFF Mask

The mask `0xFFFFFFFF` (all 32 bits set) tells the hardware that all 32 threads in the warp participate in the shuffle. This is required since CUDA 9.0 (Volta architecture) because independent thread scheduling means threads within a warp may no longer be perfectly synchronized without explicit synchronization.

For earlier architectures, the simpler `__shfl_down()` (without the sync suffix) was available but is now deprecated.

### Volta and Beyond: Independent Thread Scheduling

Starting with Volta (compute capability 7.0), threads within a warp can have independent program counters. This means:

- The `volatile` approach (Approach 1) may not be correct on Volta+ without additional care
- The `__shfl_down_sync()` approach (Approach 2) explicitly synchronizes the specified threads, making it the preferred method on modern hardware
- Always use the `_sync` variants of warp-level primitives on Volta and newer

### Block Sizes That Are Not Powers of 2

The two-phase approach naturally handles any block size that is a multiple of 32 (the warp size). If `blockDim.x` is not a multiple of 32, the last warp will have some inactive threads, which the hardware handles via predication.

## Exam Tips

1. **Know the warp size**: NVIDIA GPUs use a warp size of 32 threads. This is fundamental to all warp-level optimizations.
2. **Explain why \_\_syncthreads() is unnecessary within a warp**: Threads in a warp execute in lockstep (SIMT), so they are implicitly synchronized.
3. **Write warpReduceSum**: Be able to write the 5-line warp shuffle reduction using `__shfl_down_sync(0xFFFFFFFF, val, delta)` with deltas 16, 8, 4, 2, 1.
4. **Explain two-phase reduction**: Phase 1 reduces within warps using shuffles, Phase 2 reduces warp results using shared memory and one more warp shuffle.
5. **volatile keyword**: Know that pre-Volta architectures need `volatile` on shared memory pointers when `__syncthreads()` is removed, to prevent register caching of shared memory values.
6. **Compare all three versions**: atomicAdd (simple but slow), full tree reduction (fast but over-synchronized), warp-optimized (fastest with minimal synchronization).
7. **Performance impact**: Fewer sync barriers, less shared memory, no bank conflicts, and higher occupancy all contribute to the speedup of Version III.

### Further Reading

Refer to your prescribed textbook and official course materials.
