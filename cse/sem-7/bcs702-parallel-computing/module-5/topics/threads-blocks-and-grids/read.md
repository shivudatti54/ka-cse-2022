# Threads, Blocks, and Grids in CUDA

## Introduction

The CUDA programming model organizes parallel execution into a three-level hierarchy: **threads**, **blocks**, and **grids**. This hierarchy maps naturally to the GPU hardware and provides a scalable abstraction that allows the same CUDA program to run efficiently on GPUs with different numbers of Streaming Multiprocessors (SMs). Understanding thread indexing, the warp execution model, occupancy, and synchronization is essential for writing correct and efficient CUDA programs.

## The CUDA Thread Hierarchy

### Threads

A **thread** is the smallest unit of execution in CUDA. Each thread executes an instance of the kernel function and has access to:

- A unique thread index within its block (`threadIdx`)
- Its own set of registers (private local variables)
- Shared memory within its block
- Global, constant, and texture memory

### Thread Blocks (Blocks)

A **thread block** (or simply **block**) is a group of threads that:

- Execute on the same Streaming Multiprocessor (SM)
- Can cooperate through **shared memory**
- Can synchronize using `__syncthreads()`
- Are identified by a block index within the grid (`blockIdx`)

Key properties of thread blocks:

- Maximum threads per block: typically 1024 (hardware limit)
- Blocks can be 1D, 2D, or 3D
- All threads in a block are guaranteed to run concurrently on the same SM
- Threads in different blocks cannot directly synchronize or share data through shared memory

### Grids

A **grid** is the collection of all thread blocks launched by a single kernel invocation. Grids can be 1D, 2D, or 3D. The total number of threads launched is `gridDim * blockDim`.

### Kernel Launch Syntax

```c
kernel<<<gridDim, blockDim>>>(arguments);
```

Where:

- `gridDim` specifies the number of blocks in the grid (can be `dim3` for multi-dimensional grids)
- `blockDim` specifies the number of threads per block (can be `dim3` for multi-dimensional blocks)

### Visualization of the Hierarchy

```
Grid (launched by one kernel call)
|
+-- Block (0,0) Block (1,0) Block (2,0)
| +-- Thread (0,0) +-- Thread (0,0) +-- Thread (0,0)
| +-- Thread (1,0) +-- Thread (1,0) +-- Thread (1,0)
| +-- Thread (0,1) +-- Thread (0,1) +-- Thread (0,1)
| +-- Thread (1,1) +-- Thread (1,1) +-- Thread (1,1)
| ... ... ...
```

## Thread Indexing

### Built-in Variables

CUDA provides built-in variables for thread identification:

| Variable    | Type   | Description                                      |
| ----------- | ------ | ------------------------------------------------ |
| `threadIdx` | `dim3` | Thread index within the block (`.x`, `.y`, `.z`) |
| `blockIdx`  | `dim3` | Block index within the grid (`.x`, `.y`, `.z`)   |
| `blockDim`  | `dim3` | Number of threads per block (`.x`, `.y`, `.z`)   |
| `gridDim`   | `dim3` | Number of blocks in the grid (`.x`, `.y`, `.z`)  |

### 1D Indexing

For a simple 1D problem (e.g., processing an array of `N` elements):

```c
// Kernel
__global__ void process(float *data, int N) {
 int idx = blockIdx.x * blockDim.x + threadIdx.x;
 if (idx < N) {
 data[idx] = data[idx] * 2.0f;
 }
}

// Launch
int N = 10000;
int blockSize = 256;
int gridSize = (N + blockSize - 1) / blockSize; // Ceiling division
process<<<gridSize, blockSize>>>(d_data, N);
```

The global thread index formula for 1D:

```
globalIdx = blockIdx.x * blockDim.x + threadIdx.x
```

### 2D Indexing

For 2D problems (e.g., image processing, matrix operations):

```c
__global__ void processMatrix(float *matrix, int width, int height) {
 int col = blockIdx.x * blockDim.x + threadIdx.x;
 int row = blockIdx.y * blockDim.y + threadIdx.y;

 if (col < width && row < height) {
 int idx = row * width + col;
 matrix[idx] = matrix[idx] * 2.0f;
 }
}

// Launch with 2D grid and 2D blocks
dim3 blockSize(16, 16); // 256 threads per block
dim3 gridSize((width + 15) / 16, (height + 15) / 16);
processMatrix<<<gridSize, blockSize>>>(d_matrix, width, height);
```

### 3D Indexing

For 3D problems (e.g., volumetric data processing):

```c
__global__ void processVolume(float *volume, int W, int H, int D) {
 int x = blockIdx.x * blockDim.x + threadIdx.x;
 int y = blockIdx.y * blockDim.y + threadIdx.y;
 int z = blockIdx.z * blockDim.z + threadIdx.z;

 if (x < W && y < H && z < D) {
 int idx = z * W * H + y * W + x;
 volume[idx] = volume[idx] * 2.0f;
 }
}

dim3 blockSize(8, 8, 8); // 512 threads per block
dim3 gridSize((W+7)/8, (H+7)/8, (D+7)/8);
processVolume<<<gridSize, blockSize>>>(d_volume, W, H, D);
```

### Grid-Stride Loops

When the data size is much larger than the number of threads launched, a **grid-stride loop** allows each thread to process multiple elements:

```c
__global__ void processLargeArray(float *data, int N) {
 int idx = blockIdx.x * blockDim.x + threadIdx.x;
 int stride = blockDim.x * gridDim.x;

 for (int i = idx; i < N; i += stride) {
 data[i] = data[i] * 2.0f;
 }
}
```

This pattern is more flexible and often more efficient than launching exactly one thread per data element because:

- It decouples data size from grid dimensions
- It maintains good occupancy regardless of problem size
- Each thread amortizes kernel launch overhead across multiple iterations

## The Warp Execution Model

### What Is a Warp?

A **warp** is a group of 32 consecutive threads within a thread block that execute together on the GPU hardware. Warps are the fundamental unit of scheduling and execution on NVIDIA GPUs.

Thread-to-warp mapping:

- Threads 0--31 form warp 0
- Threads 32--63 form warp 1
- Threads 64--95 form warp 2
- And so on...

For a block of 256 threads, there are 256 / 32 = 8 warps.

### SIMT Execution

All threads in a warp execute the same instruction at the same time under the **Single Instruction, Multiple Threads (SIMT)** model. Each thread has its own registers and can operate on different data, but they all follow the same instruction stream.

### Warp Divergence

When threads in a warp encounter a branch (e.g., an `if-else` statement) and not all threads take the same path, **warp divergence** occurs:

```c
if (threadIdx.x < 16) {
 // Path A -- executed by threads 0-15 (others are masked)
} else {
 // Path B -- executed by threads 16-31 (others are masked)
}
// Both paths reconverge here
```

During divergence, the warp serializes: first all threads in Path A execute (with Path B threads masked/idle), then all threads in Path B execute. This effectively halves the throughput for that warp.

**Best practice**: Structure conditionals so that all threads in a warp take the same branch. Branch on `blockIdx.x` or `warpId` rather than `threadIdx.x` when possible.

### Warp-Level Primitives

Modern CUDA architectures provide warp-level operations that allow threads within a warp to communicate directly without shared memory:

- `__shfl_sync()`: Shuffle data between threads in a warp
- `__ballot_sync()`: Collect a 1-bit vote from each thread
- `__any_sync()` / `__all_sync()`: Warp-wide predicate tests
- `__reduce_sync()`: Warp-wide reduction

These are extremely fast because they use direct register-to-register transfers within the warp.

## Occupancy

### Definition

**Occupancy** is the ratio of active warps on an SM to the maximum number of warps the SM supports:

```
Occupancy = Active Warps / Max Warps per SM
```

For example, if an SM supports 64 warps and a kernel configuration results in 32 active warps, the occupancy is 50%.

### Factors Limiting Occupancy

1. **Registers per thread**: More registers per thread means fewer threads can fit on the SM.

- Example: SM has 65,536 registers, max 2048 threads. If a kernel uses 64 registers/thread, only 1024 threads (32 warps) can be active.

2. **Shared memory per block**: More shared memory per block means fewer blocks can be resident on the SM.

- Example: SM has 96 KB shared memory. If each block uses 48 KB, only 2 blocks can be resident.

3. **Block size**: The block size must divide evenly into warp-sized groups.

- A block of 96 threads uses 3 warps (96/32).
- If max warps per SM is 64 and max blocks per SM is 16, a block size of 64 (2 warps) allows 16 blocks = 32 warps (50% of 64).

### Optimizing Occupancy

- Use the **CUDA Occupancy Calculator** or `cudaOccupancyMaxPotentialBlockSize()` API.
- Reduce register usage with the `__launch_bounds__()` qualifier or `-maxrregcount` compiler flag.
- Balance shared memory usage with the number of blocks.
- Choose block sizes that are multiples of 32 (warp size).

**Important note**: Maximum occupancy does not always yield maximum performance. Sometimes using more registers per thread for data reuse or more shared memory for caching provides greater speedup despite lower occupancy.

## Thread Synchronization

### \_\_syncthreads()

The `__syncthreads()` function is a **barrier synchronization** that blocks all threads in a block until every thread has reached the synchronization point. It is essential when threads in a block communicate through shared memory:

```c
__shared__ float tile[256];

// Each thread writes to shared memory
tile[threadIdx.x] = global_data[globalIdx];

// Wait for all threads to finish writing
__syncthreads();

// Now safe to read any element of tile
float value = tile[255 - threadIdx.x];
```

**Rules for \_\_syncthreads()**:

- Must be called by **all threads in the block** -- placing it inside a conditional that only some threads enter causes undefined behavior (potential deadlock).
- Only synchronizes threads within the same block, not across blocks.
- Has low but non-zero overhead.

### Cooperative Groups (CUDA 9+)

The Cooperative Groups API provides more flexible synchronization:

```c
#include <cooperative_groups.h>
namespace cg = cooperative_groups;

__global__ void kernel() {
 cg::thread_block block = cg::this_thread_block();
 cg::thread_block_tile<32> warp = cg::tiled_partition<32>(block);

 // Synchronize entire block
 block.sync();

 // Synchronize just the warp
 warp.sync();
}
```

Cooperative Groups enables:

- Warp-level synchronization
- Multi-block synchronization (grid-level sync with cooperative kernel launch)
- Flexible partitioning of threads into groups

## Choosing Block and Grid Dimensions

### Guidelines for Block Size

1. **Multiple of 32**: Always use block sizes that are multiples of the warp size (32) to avoid wasted threads in the last warp.
2. **Common choices**: 128, 256, or 512 threads per block.
3. **At least 2 warps per block**: Having multiple warps per block helps hide instruction latency.
4. **Hardware limits**: Maximum 1024 threads per block on most modern GPUs.

### Guidelines for Grid Size

1. **Cover the problem**: `gridSize = (N + blockSize - 1) / blockSize` for 1D problems.
2. **Enough blocks for full GPU**: Launch enough blocks to keep all SMs busy. A modern GPU with 80+ SMs needs at least 80 blocks, but ideally many more (thousands) for good load balancing.
3. **Grid-stride loops**: For very large problems or when you want a fixed grid size.

### Example: Finding Optimal Configuration

```c
int blockSize;
int minGridSize;

// Let the runtime find an optimal block size
cudaOccupancyMaxPotentialBlockSize(&minGridSize, &blockSize, myKernel, 0, N);

// Calculate grid size
int gridSize = (N + blockSize - 1) / blockSize;
myKernel<<<gridSize, blockSize>>>(d_data, N);
```

## Summary

The CUDA thread hierarchy -- threads grouped into blocks grouped into a grid -- provides a powerful and scalable model for parallel execution. Thread indexing using `threadIdx`, `blockIdx`, and `blockDim` enables each thread to identify its unique data element. The warp execution model (32 threads executing in SIMT fashion) is the fundamental unit of scheduling, and warp divergence must be minimized for performance. Occupancy, determined by register usage, shared memory usage, and block size, affects how well the GPU can hide latency. Thread synchronization via `__syncthreads()` enables safe inter-thread communication within a block. Choosing appropriate block and grid dimensions requires balancing multiple factors including hardware limits, occupancy, and problem structure.
