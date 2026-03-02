# Multicore and GPU Architecture

## Introduction

The landscape of computing has undergone a dramatic transformation in the past two decades. Traditional single-core processors, which dominated computing for decades, reached their physical limitations in terms of clock speed and power consumption. This gave rise to two revolutionary approaches: **multicore processors** (multiple CPU cores on a single chip) and **Graphics Processing Units (GPUs)** - originally designed for graphics rendering but evolved into powerful parallel computing engines.

For DU students pursuing Computer Science, understanding multicore and GPU architecture is essential not only for theoretical knowledge but also for practical applications in fields like machine learning, scientific computing, game development, and data science. Modern computing systems almost universally employ heterogeneous architectures combining multiple CPU cores with GPU accelerators. This topic explores the fundamental principles, architectural differences, and practical implications of these technologies that form the backbone of contemporary high-performance computing.

The evolution from single-core to multicore represents a paradigm shift in how we design and utilize computer systems. Instead of making a single processor faster, engineers began placing multiple processors on the same die, enabling true parallel processing. Similarly, GPUs evolved from fixed-function graphics accelerators to general-purpose parallel processors capable of handling thousands of concurrent threads, making them ideal for data-parallel workloads.

## Key Concepts

### 1. Multicore Processor Architecture

A **multicore processor** integrates two or more independent processing units (cores) onto a single physical chip. Each core is a complete processor capable of executing instructions independently, though they share certain resources like cache memory and system bus.

**Key characteristics of multicore processors:**

- **Symmetric Multicore (SMP)**: All cores are identical and have equal access to memory and I/O. Examples include Intel Core i7, AMD Ryzen processors.
- **Asymmetric Multicore (AMP)**: Cores may have different architectures or capabilities. ARM's big.LITTLE technology uses高性能 cores combined with high-efficiency cores.
- **Cache Hierarchy**: Modern multicore processors feature multi-level caches (L1, L2, L3). The L3 cache (last-level cache) is often shared among cores.
- **Interconnects**: Cores communicate through on-chip interconnects like Intel's QuickPath Interconnect (QPI) or AMD's Infinity Fabric.

### 2. GPU Architecture

A **Graphics Processing Unit (GPU)** is a specialized electronic circuit designed to manipulate memory and accelerate the creation of images, videos, and animations. Modern GPUs are **manycore** processors containing hundreds or thousands of smaller, efficient cores designed for handling parallel tasks.

**GPU Architecture Components:**

- **Streaming Multiprocessors (SMs)**: The basic computational unit in NVIDIA GPUs. Each SM contains multiple CUDA cores (execution units).
- **Thread Hierarchy**: GPU programming follows a hierarchy - threads are grouped into warps (32 threads in NVIDIA), warps into blocks, and blocks into grids.
- **Memory Hierarchy**: GPUs have global memory (high capacity, high latency), shared memory (fast, shared within block), registers (fastest, per-thread), and constant/texture caches.
- **SIMT (Single Instruction, Multiple Threads)**: GPUs execute the same instruction across multiple threads simultaneously, diverging when necessary.

### 3. CPU vs GPU: Fundamental Differences

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Core Count** | 2-64 cores (high-performance) | Hundreds to thousands of cores |
| **Focus** | Low latency, complex control flow | High throughput, massive parallelism |
| **Cache** | Large, sophisticated caches | Smaller, specialized caches |
| **Control Logic** | Complex branch prediction, out-of-order execution | Simple, deterministic execution |
| **Ideal Workload** | Serial, branch-heavy, low-latency | Data-parallel, SIMD-friendly tasks |
| **Power Consumption** | Moderate per core | Lower per core, but many more cores |

### 4. Parallel Computing Concepts

**Thread-Level Parallelism (TLP)**: Executing multiple threads simultaneously across multiple cores. Multicore CPUs excel at this with their complex control mechanisms.

**Data-Level Parallelism (DLP)**: Applying the same operation to multiple data elements simultaneously. GPUs are optimized for DLP through SIMT execution.

**Amdahl's Law**: States that the speedup of a program is limited by its serial portion. If 95% of a program is parallelizable, maximum speedup is 20x regardless of core count.

**Gustafson's Law**: Argues that with more cores, we can solve larger problems in the same time, emphasizing that parallel speedup grows with problem size.

### 5. GPU Programming Models

**CUDA (Compute Unified Device Architecture)**: NVIDIA's parallel computing platform and API. Uses functions called **kernels** that are executed in parallel by multiple threads.

```cuda
// Simple CUDA kernel example
__global__ void vectorAdd(int *a, int *b, int *c, int n) {
    int index = blockIdx.x * blockDim.x + threadIdx.x;
    if (index < n) {
        c[index] = a[index] + b[index];
    }
}
```

**OpenCL (Open Computing Language)**: Vendor-neutral parallel programming framework for heterogeneous systems.

**Compute Shaders**: GPU compute API integrated into graphics APIs like DirectX and Vulkan.

### 6. Heterogeneous Computing

Modern systems combine CPUs and GPUs in a **heterogeneous computing** model:

- **CPU**: Handles sequential tasks, system control, I/O operations
- **GPU**: Accelerates parallel compute kernels
- **Unified Memory**: Technologies like NVIDIA's Unified Memory and Intel's Xeon Phi enable shared memory spaces
- **Offloading**: Strategic distribution of workloads between CPU and GPU

## Examples

### Example 1: Calculating Speedup in Multicore Processing

**Problem**: A program takes 100 seconds to execute on a single-core processor. If 80% of the program is parallelizable, calculate the theoretical speedup using 4 cores.

**Solution**:

Using Amdahl's Law:
- Serial portion: 20% = 20 seconds
- Parallel portion: 80% = 80 seconds
- With 4 cores, parallel portion takes: 80/4 = 20 seconds
- Total time: 20 + 20 = 40 seconds
- Speedup: 100/40 = 2.5x

The theoretical maximum speedup with infinite cores would be 100/20 = 5x (limited by the 20% serial portion).

### Example 2: GPU Thread Configuration

**Problem**: Given a GPU with 16 streaming multiprocessors (SMs), each SM can execute 4 warps (128 threads) concurrently. If you have 1 million elements to process, determine the grid and block configuration.

**Solution**:

For efficient GPU utilization:
- Block size: 256 threads (multiple of 32, warp size)
- Number of blocks needed: 1,000,000 / 256 = 3907 blocks (round up)
- Blocks per SM: 3907 / 16 = 244 blocks per SM (exceeds capacity, so limit to 16-32 blocks per SM)

Optimal configuration:
```cuda
dim3 blockSize(256);
dim3 gridSize((n + blockSize.x - 1) / blockSize.x);
kernel<<<gridSize, blockSize>>>(parameters);
```

### Example 3: Vector Addition Performance Analysis

**Problem**: Compare the execution time of adding two arrays of 10 million elements on CPU (single-threaded) vs GPU (parallel).

**Solution**:

Assume:
- CPU: 3 GHz, can process 1 element per 10 cycles → 300 million elements/sec
- GPU: Can process 10,000 elements per microsecond (per SM), 16 SMs available

CPU time: 10,000,000 / 300,000,000 = 0.033 seconds
GPU time: 10,000,000 / (16 × 10,000) = 62.5 microseconds ≈ 0.00006 seconds

Speedup: 0.033 / 0.00006 ≈ 550x

This demonstrates why GPUs excel at data-parallel operations, though actual speedups are typically 10-100x due to memory transfer overhead and kernel launch latency.

## Exam Tips

1. **Understand the difference between TLP and DLP**: CPU cores handle thread-level parallelism with complex control flow, while GPUs optimize data-level parallelism through SIMT execution.

2. **Memorize Amdahl's Law formula**: Speedup = 1 / (S + (1-S)/N), where S is serial fraction and N is number of processors. This is frequently tested in exams.

3. **Know GPU memory hierarchy**: Global memory (slowest), shared memory (fast, block-level), registers (fastest). Understanding memory access patterns is crucial for GPU programming.

4. **Why GPUs are faster for parallel tasks**: Hundreds of simple cores vs few complex cores, thousands of concurrent threads to hide memory latency, SIMD execution for data-parallel operations.

5. **Multicore cache considerations**: Shared L3 cache improves communication but can become a bottleneck. Understand cache coherence protocols (MESI).

6. **Heterogeneous computing benefits**: CPU handles control logic and serial tasks efficiently; GPU accelerates parallel kernels. Know examples like CUDA programming.

7. **Thread hierarchy**: Grid → Block → Warp → Thread. Remember that a warp contains 32 threads in NVIDIA GPUs and they execute in lockstep.

8. **Real-world applications**: Be ready to give examples where multicore (database engines, web servers) and GPU (deep learning, scientific simulation, gaming) architectures excel.