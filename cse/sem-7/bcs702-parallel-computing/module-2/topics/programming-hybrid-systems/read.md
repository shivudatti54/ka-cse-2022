# Programming Hybrid Systems

## 1. Introduction to Hybrid Systems

### 1.1 Conceptual Foundation and Definition

Hybrid systems, also termed heterogeneous computing systems, represent a class of parallel architectures that integrate multiple distinct processing units with fundamentally different microarchitectures, instruction sets, and performance characteristics into a unified computational framework. The primary motivation for adopting hybrid architectures stems from the observation that no single processor type optimally executes all computational workloads; rather, different algorithms and program regions exhibit distinct performance requirements that various processing elements can satisfy with varying degrees of efficiency.

**Definition 1.1 (Heterogeneous Computing):** Heterogeneous computing refers to a system architecture employing processing units with divergent microarchitectures—such as central processing units (CPUs) and graphics processing units (GPUs)—coordinated through specialized execution pathways to solve computational problems by mapping specific workload characteristics to the most appropriate processing element.

The fundamental divergence between CPU and GPU architectures underlies the rationale for hybrid systems. CPUs are architected for sequential execution with sophisticated branch prediction mechanisms, out-of-order execution capabilities, and deep instruction pipelines—optimizing for low latency in complex control flow and irregular computation patterns. GPUs, conversely, employ a massively parallel single-instruction-multiple-thread (SIMT) architecture optimized for throughput-oriented workloads exhibiting regular data access patterns and homogeneous computation structures.

### 1.2 Historical Evolution and Motivation

The emergence of hybrid computing paradigms reflects the physical and economic constraints limiting single-processor performance scaling. Moore's Law's deceleration, coupled with the memory wall problem—the widening gap between processor computational bandwidth and memory access latency—has necessitated architectural specialization. GPUs, originally designed for graphics rendering pipelines, demonstrated exceptional efficiency for data-parallel workloads through massive thread-level parallelism, leading to their adoption as general-purpose accelerators (GPGPU).

**Theorem 1.1 (Amdahl's Law for Hybrid Systems):** For a computation with sequential fraction $f$ and parallel fraction $(1-f)$ executed on a hybrid system with CPU speedup $S_c$ and GPU speedup $S_g$, the maximum achievable speedup $S_{hybrid}$ is bounded by:

$$S_{hybrid} \leq \frac{1}{\frac{f}{S_c} + \frac{(1-f)}{S_g} + \frac{t_{comm}}{T_{total}}}$$

where $t_{comm}$ represents the data transfer overhead between host and device memories.

_Proof:_ The total execution time $T_{total}$ comprises sequential time $T_{seq} = f \cdot T_{original}$, parallel CPU time $T_{cpu} = (1-f) \cdot T_{original} / S_c$, parallel GPU time $T_{gpu} = (1-f) \cdot T_{original} / S_g$, and communication overhead $t_{comm}$. Minimizing total time yields the stated bound. $\square$

This theorem illustrates that effective hybrid programming requires minimizing sequential fractions and data transfer costs while maximizing GPU utilization for suitable workloads.

## 2. Architectural Foundations

### 2.1 Host-Device Execution Model

The canonical hybrid computing architecture employs a hierarchical relationship between the host processor (CPU) and accelerator devices (GPUs). The host manages system resources, executes sequential logic, handles input/output operations, and orchestrates device execution. The device functions as a coprocessor executing data-parallel kernels launched by the host through a runtime API.

```
+------------------------+      PCIe 4.0 x16       +------------------------+
|       Host (CPU)       | <====================> |     Device (GPU)       |
|                        |    32 GB/s             |                        |
| - Sequential logic     |   Control Commands      | - SIMT execution      |
| - Branch-intensive     | <-------------------   | - Data-parallel       |
|   code                 |                        |   kernels              |
| - System orchestration |   DMA Transfer         | - High throughput     |
| - Memory management    | <===================>  |   computation          |
+------------------------+   32 GB/s             +------------------------+
            |                                                |
            v                                                v
+------------------------+                        +------------------------+
|      System RAM        | <====================> |   Device Global Memory|
|   (DDR4/DDR5)          |    50-100 GB/s         |   (HBM2/HBM3)          |
|   64-128 GB            |                        |   16-80 GB             |
+------------------------+                        +------------------------+
```

The execution flow proceeds as follows: (1) host allocates device memory via CUDA malloc or similar API; (2) host transfers input data to device memory through DMA; (3) host launches kernel with specified grid and block dimensions; (4) device executes parallel kernels across thousands of threads; (5) results transfer back to host memory for final processing.

### 2.2 Memory Hierarchy and Bandwidth Analysis

The heterogeneous memory architecture presents significant optimization challenges. System RAM (DDR4/DDR5) typically delivers 50-100 GB/s bandwidth, while modern GPU memory (HBM2/HBM3) achieves 1-2 TB/s—creating a 10-20x bandwidth differential that fundamentally shapes data movement strategies.

**Theorem 2.1 (Memory Bottleneck Bound):** In hybrid systems, the achievable performance $P$ for a kernel with arithmetic intensity $AI$ executing on a device with peak FLOPS $F_{peak}$ and memory bandwidth $B$ is bounded by:

$$P \leq \min(F_{peak}, B \times AI)$$

This relationship, formalized in the roofline model, demonstrates that kernels with low arithmetic intensity—specifically those performing fewer than $F_{peak}/B$ floating-point operations per byte of memory traffic—are fundamentally limited by memory bandwidth rather than compute capacity. The peak performance $F_{peak}$ is attainable only when $AI \geq F_{peak}/B$.

_Proof:_ Each byte transferred from memory can support at most $AI$ floating-point operations. With memory bandwidth $B$ bytes/second, maximum operational throughput is $B \times AI$ FLOPs/second. Physical device limitations cap performance at $F_{peak}$. Therefore, actual performance is the minimum of these bounds. $\square$

### 2.3 Memory Hierarchy Comparison

| Level         | CPU Architecture | GPU Architecture                 |
| ------------- | ---------------- | -------------------------------- |
| Registers     | 32 × 32-bit      | 64K 32-bit registers/SM          |
| L1 Cache      | 48 KB            | 128 KB/SM (combined with shared) |
| L2 Cache      | 512 KB (private) | 6 MB (shared)                    |
| Shared Memory | N/A              | 48 KB/SM                         |
| Main Memory   | DDR5 64-128 GB   | HBM2 1 TB/s                      |
| Bandwidth     | 50-100 GB/s      | 1-2 TB/s                         |
| Latency       | ~100 ns          | ~500 ns (global memory)          |

The GPU memory hierarchy emphasizes high throughput over low latency, employing massive parallelism to hide memory latency through thread switching.

## 3. Programming Models for Heterogeneous Systems

### 3.1 CUDA Programming Model

CUDA (Compute Unified Device Architecture) provides NVIDIA's comprehensive framework for CPU-GPU cooperation. The model employs a hierarchical thread organization: grids contain thread blocks, and blocks contain individual threads. Threads execute kernel functions with unique identifiers determining data access patterns.

**Key CUDA Concepts:**

- **Thread**: Smallest execution unit, executes kernel instance
- **Block**: Group of threads sharing resources and synchronizing
- **Grid**: Collection of blocks executing kernel
- **Warp**: 32 threads executing in lockstep (SIMT)
- **SM**: Streaming Multiprocessor executing thread blocks

```cpp
// CUDA kernel demonstrating shared memory optimization for parallel reduction
__global__ void parallel_reduction(float* __restrict__ input,
                                    float* __restrict__ output,
                                    const int N) {
    __shared__ float shared_data[256];

    // Thread indexing
    int tid = threadIdx.x;
    int gid = blockIdx.x * blockDim.x + threadIdx.x;

    // Phase 1: Coalesced global memory load into shared memory
    if (gid < N) {
        shared_data[tid] = input[gid];
    } else {
        shared_data[tid] = 0.0f;
    }
    __syncthreads();

    // Phase 2: In-place reduction in shared memory (bank conflict avoidance)
    for (int stride = blockDim.x / 2; stride > 0; stride >>= 1) {
        if (tid < stride) {
            shared_data[tid] += shared_data[tid + stride];
        }
        __syncthreads();
    }

    // Phase 3: Write block result to global memory
    if (tid == 0) {
        output[blockIdx.x] = shared_data[0];
    }
}
```

**Launch Configuration:** The kernel launches with `parallel_reduction<<<gridSize, blockSize>>>(input, output, N)`, where optimal block size typically equals 256 or 512 threads for memory-bound kernels.

### 3.2 Memory Coalescing and Access Optimization

Memory coalescing refers to the alignment of memory accesses across threads in a warp to combine multiple requests into fewer memory transactions. Coalesced access significantly impacts performance.

**Theorem 3.1 (Coalesced Access Bound):** For a warp of $W=32$ threads each accessing $b$ bytes from consecutive addresses, the number of memory transactions $T$ is given by:

$$T = \lceil \frac{W \times b}{T_{bytes}} \rceil$$

where $T_{bytes}$ is the transaction size (typically 32, 64, or 128 bytes).

_Proof:_ Global memory accesses are serviced in fixed-size transactions of $T_{bytes}$ bytes. When thread $i$ accesses address $base + i \times b$, all accesses coalesce into $\lceil(W \times b)/T_{bytes}\rceil$ transactions if addresses fall within aligned segments. Misaligned or strided access increases transaction count proportionally. $\square$

### 3.3 OpenCL Programming Model

OpenCL (Open Computing Language) provides a vendor-agnostic heterogeneous programming framework. Unlike CUDA's NVIDIA-specific implementation, OpenCL offers portability across CPUs, GPUs, FPGAs, and accelerators from multiple vendors.

```cpp
// OpenCL kernel equivalent for parallel reduction
__kernel void reduction(__global const float* input,
                        __global float* output,
                        __local float* shared_data,
                        const int N) {
    int tid = get_local_id(0);
    int gid = get_global_id(0);
    int local_size = get_local_size(0);

    // Load into local memory
    if (gid < N) {
        shared_data[tid] = input[gid];
    } else {
        shared_data[tid] = 0.0f;
    }

    barrier(CLK_LOCAL_MEM_FENCE);

    // Reduction in local memory
    for (int stride = local_size / 2; stride > 0; stride >>= 1) {
        if (tid < stride) {
            shared_data[tid] += shared_data[tid + stride];
        }
        barrier(CLK_LOCAL_MEM_FENCE);
    }

    if (tid == 0) {
        output[get_group_id(0)] = shared_data[0];
    }
}
```

### 3.4 OpenMP Offload Model

OpenMP 4.0+ introduces target offload directives for heterogeneous computing, providing a directive-based approach simpler than explicit CUDA or OpenCL APIs.

```cpp
// OpenMP target offload example
void hybrid_computation(float* A, float* B, float* C, int N) {
    #pragma omp target data map(to: A[0:N], B[0:N]) map(from: C[0:N])
    {
        #pragma omp target teams distribute parallel for
        for (int i = 0; i < N; i++) {
            C[i] = A[i] + B[i];  // Vector addition on GPU
        }
    }
}
```

### 3.5 Unified Memory and Zero-Copy Access

Unified Memory provides a single pointer space accessible from both CPU and GPU, with the runtime automatically migrating data as needed. This simplifies programming at the cost of potential performance overhead.

```cpp
// CUDA Unified Memory allocation
float* data;
cudaMallocManaged(&data, size * sizeof(float));

// Automatic migration: access from GPU triggers page fault and migration
kernel<<<grid, block>>>(data, N);

// Explicit prefetching for performance optimization
cudaDevicePrefetchAsync(data, size * sizeof(float), deviceId);
```

**Theorem 3.2 (Data Transfer Cost Model):** The effective bandwidth $B_{eff}$ achieved during data transfer of size $D$ bytes with latency $L$ and asynchronous transfer overlap $\alpha$ is:

$$B_{eff} = \frac{D}{D/B + L(1-\alpha)}$$

_Proof:_ Total transfer time $T = D/B + L(1-\alpha)$, where $D/B$ represents transfer time and $L(1-\alpha)$ accounts for latency not overlapped with computation. Effective bandwidth follows directly. $\square$

## 4. Synchronization and Critical Sections

### 4.1 Thread Synchronization Primitives

Synchronization ensures correct execution order and data consistency in parallel operations.

**Intra-Block Synchronization:**

- `__syncthreads()` (CUDA): Blocks all threads in block until all reach barrier
- `barrier(CLK_LOCAL_MEM_FENCE)` (OpenCL): Equivalent synchronization

**Inter-Block Synchronization:** Requires kernel decomposition with multiple kernels or atomic operations:

```cpp
// Atomic operations for cross-block reduction
__device__ atomicAdd(&global_sum, local_sum);
```

### 4.2 Memory Consistency and Fences

Memory fences enforce ordering of memory operations across threads:

```cpp
// Thread fence ensuring all prior writes are visible
__threadfence();

// System fence (visible to CPU-GPU interactions)
__threadfence_system();
```

## 5. Performance Optimization Strategies

### 5.1 Roofline Analysis Procedure

The roofline model provides performance prediction through the following methodology:

1. Calculate kernel arithmetic intensity: $AI = \frac{\text{FLOPs}}{\text{Bytes accessed}}$
2. Determine device peak FLOPs $F_{peak}$ and memory bandwidth $B$
3. Compute performance ridge point: $AI_{ridge} = F_{peak}/B$
4. Predict achievable performance: $P = \min(F_{peak}, B \times AI)$

### 5.2 Optimization Checklist

| Optimization        | Target               | Impact                    |
| ------------------- | -------------------- | ------------------------- |
| Memory coalescing   | Global memory access | 2-10x bandwidth           |
| Shared memory usage | Frequent accesses    | 10-100x latency reduction |
| Register tiling     | Register pressure    | Occupancy improvement     |
| Warp specialization | Divergence           | Execution efficiency      |
| Zero-copy access    | Small data transfers | Latency elimination       |
| Kernel fusion       | Multiple kernels     | Overhead reduction        |

---

## Multiple Choice Questions

**Question 1 (Hard):** A hybrid system with CPU peak performance 100 GFLOPS and memory bandwidth 50 GB/s executes a kernel that performs 200 FLOPs while loading 64 bytes from global memory. Using the roofline model, the expected performance is:

- A) 50 GFLOPS
- B) 100 GFLOPS
- C) 200 GFLOPS
- D) 400 GFLOPS

**Question 2 (Hard):** For a kernel with 15% sequential code and 85% parallelizable code, if CPU achieves 10x speedup on the parallel portion and GPU achieves 50x speedup with 5ms communication overhead in a 100ms total execution, what is the total speedup?

- A) 25.4x
- B) 31.2x
- C) 42.8x
- D) 50.0x

**Question 3 (Hard):** A CUDA warp performs strided access with stride 4 to float arrays. If each thread accesses 4 bytes, the transaction size is 32 bytes, and the array starts at a 128-byte aligned address, how many memory transactions are required for 32 threads?

- A) 1
- B) 4
- C) 8
- D) 16

**Question 4 (Hard):** Given a GPU with 1.5 TB/s memory bandwidth and 15 TFLOPS peak performance, a kernel with arithmetic intensity 5 FLOPs/byte is executed. The theoretical peak performance using roofline model is:

- A) 1.5 TFLOPS
- B) 7.5 TFLOPS
- C) 15 TFLOPS
- D) 30 TFLOPS

**Question 5 (Hard):** In a hybrid OpenMP implementation, if data transfer takes 10ms, kernel execution takes 50ms, and computation-to-transfer overlap is 60%, what is the effective kernel execution time?

- A) 40ms
- B) 50ms
- C) 54ms
- D) 60ms
