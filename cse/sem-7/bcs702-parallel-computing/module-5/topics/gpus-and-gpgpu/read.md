# GPUs and GPGPU (General-Purpose Computing on Graphics Processing Units)

## 1. Introduction

Graphics Processing Units (GPUs) have undergone a remarkable transformation from specialized graphics accelerators to general-purpose parallel processors capable of tackling computationally intensive workloads across scientific computing, machine learning, and data analytics. This paradigm, termed General-Purpose computing on Graphics Processing Units (GPGPU), represents a fundamental shift in high-performance computing architecture.

## 2. Fundamental Concepts

### 2.1 GPU Architecture Fundamentals

A GPU differs fundamentally from a CPU in its design philosophy. While CPUs optimize for **latency minimization** through sophisticated control logic, branch prediction, and hierarchical caches, GPUs optimize for **throughput maximization** by dedicating silicon area to massive parallel execution units.

**Theorem: Throughput-Area Trade-off**
Given a fixed transistor budget $T$, let $A_{control}$ represent area for control logic and $A_{alu}$ represent area for arithmetic logic units. For a CPU: $A_{control} \approx 0.3T$ and $A_{alu} \approx 0.2T$. For a GPU: $A_{control} \approx 0.1T$ and $A_{alu} \approx 0.7T$. This results in GPU achieving $N_{gpu}/N_{cpu} \approx 3.5\times$ more parallel execution capacity per transistor.

Modern GPUs contain thousands of processing cores organized hierarchically. The NVIDIA A100 GPU, for instance, comprises 108 streaming multiprocessors (SMs), each containing 64 CUDA cores, totaling 6,912 cores operating at 1.41 GHz.

### 2.2 Memory Architecture

GPUs employ a distinct memory hierarchy optimized for parallel throughput:

| Memory Type   | Scope  | Latency         | Bandwidth     |
| ------------- | ------ | --------------- | ------------- |
| Register      | Thread | ~1 cycle        | Very High     |
| Shared Memory | Block  | ~1-2 cycles     | Very High     |
| L1 Cache      | SM     | ~4-6 cycles     | High          |
| L2 Cache      | Device | ~40 cycles      | Medium        |
| Global Memory | Device | ~400-800 cycles | 2 TB/s (A100) |

The **memory bandwidth equation** characterizes GPU performance:
$$B_{effective} = \frac{N_{threads} \times Bytes_{per\_thread}}{T_{execution}}$$

Achieving high bandwidth utilization requires careful data layout and access patterns.

### 2.3 SIMT Execution Model

GPUs execute under the Single Instruction, Multiple Threads (SIMT) model. Threads are organized into **warps** of 32 threads that execute in lockstep. The GPU schedules warps across available SMs, hiding latency through simultaneous multithreading.

**Definition: Warp Divergence**
When threads within a warp take different execution paths due to conditional statements, the warp executes both paths serially, degrading performance. This phenomenon is known as warp divergence. The efficiency loss factor is:
$$\eta_{warp} = \frac{min(N_{path1}, N_{path2})}{32}$$

## 3. Evolution of GPU Computing

### 3.1 Historical Progression

| Era                  | Period    | Key Development               | Significance              |
| -------------------- | --------- | ----------------------------- | ------------------------- |
| Fixed-Function       | 1990s     | Rigid graphics pipeline       | Limited programmability   |
| Programmable Shaders | 2001-2006 | Vertex/Fragment shaders       | First GPGPU experiments   |
| CUDA Revolution      | 2006-2007 | Direct general-purpose access | Unified programming model |
| Fermi Architecture   | 2010      | Unified addressing, ECC       | Enterprise computing      |
| Kepler/Maxwell       | 2012-2014 | Dynamic parallelism           | Multi-GPU scaling         |
| Volta/Turing         | 2017-2018 | Tensor cores, RT cores        | AI/ML acceleration        |
| Ampere               | 2020      | Multi-instance GPU            | Cloud virtualization      |

### 3.2 From Graphics to General-Purpose Computing

Early GPGPU required mapping computations to graphics primitives:

1. Encode input data as texture pixels
2. Execute computation as fragment shader
3. Read results from framebuffer

This approach was cumbersome. The CUDA paradigm eliminated graphics abstractions, enabling direct general-purpose programming.

## 4. CUDA Programming Model

### 4.1 Execution Hierarchy

CUDA defines a four-level thread organization:

```
Grid
  └── Block (Thread Block)
        └── Warp (32 threads)
              └── Thread
```

- **Thread**: Smallest execution unit with unique ID `(blockIdx.x, blockIdx.y, threadIdx.x, threadIdx.y, threadIdx.z)`
- **Warp**: Group of 32 threads executing in lockstep
- **Block**: Group of threads (up to 1024) sharing shared memory and synchronization
- **Grid**: Collection of blocks executing the same kernel

### 4.2 Memory Types in CUDA

```c
__global__ void kernel() {
    __shared__ float shared_data[256];  // Block-scoped, fast
    __device__ float global_data[1024]; // Device-scoped
    // Register variables for thread-local storage
}
```

### 4.3 Optimization Principles

**Memory Coalescing**: Sequential threads accessing sequential memory addresses results in optimal memory transactions. The coalescing efficiency is:
$$\eta_{coalesce} = \frac{N_{actual\_transactions}}{N_{ideal\_transactions}} \times 100\%$$

**Occupancy**: The ratio of active warps to maximum warps per SM:
$$Occupancy = \frac{N_{active\_warps}}{N_{max\_warps}} = \frac{N_{threads\_per\_block} \times N_{blocks\_per\_SM}}{N_{max\_threads\_per\_SM}}$$

Higher occupancy generally improves latency hiding but does not guarantee maximum performance.

## 5. Comparative Analysis: CPU vs GPU

| Characteristic       | CPU (Modern x86)  | GPU (NVIDIA A100)                  |
| -------------------- | ----------------- | ---------------------------------- |
| Core Count           | 8-64 cores        | 6,912 cores                        |
| Thread Capacity      | 16-128 threads    | 10,000+ threads                    |
| Control Logic        | Complex, OoO      | Simple, in-order                   |
| Cache Hierarchy      | Deep (L1/L2/L3)   | Shallow (L1/L2 only)               |
| Memory Bandwidth     | 50-100 GB/s       | 2 TB/s                             |
| Latency Optimization | Excellent         | Throughput-oriented                |
| Suitable Workload    | Latency-sensitive | Data-parallel, throughput-oriented |

**Theorem: Amdahl's Law for GPU Acceleration**
Given a parallel fraction $f$ of a workload, the maximum speedup $S$ achievable with $N$ GPU cores is:
$$S_{max} = \frac{1}{(1-f) + \frac{f}{N}}$$

This emphasizes that GPU acceleration is most effective for workloads with high parallel fractions (typically $f > 0.95$).

## 6. Modern GPGPU Frameworks

### 6.1 Framework Comparison

| Framework      | Vendor  | Portability  | Performance | Use Case            |
| -------------- | ------- | ------------ | ----------- | ------------------- |
| CUDA           | NVIDIA  | NVIDIA only  | Highest     | Deep learning, HPC  |
| OpenCL         | Khronos | Cross-vendor | High        | Portable computing  |
| HIP            | AMD     | AMD/NVIDIA   | High        | Migration from CUDA |
| SYCL           | Khronos | Cross-vendor | Moderate    | C++ abstraction     |
| Vulkan Compute | Khronos | Cross-vendor | High        | Graphics + compute  |

### 6.2 CUDA Compute Capabilities

Each GPU architecture supports specific compute capabilities:

| Compute Capability | Architecture | Features                                    |
| ------------------ | ------------ | ------------------------------------------- |
| 1.0-1.2            | Tesla        | Basic features                              |
| 2.0-2.1            | Fermi        | Concurrent kernels, ECC                     |
| 3.0-3.7            | Kepler       | Dynamic parallelism                         |
| 5.0-5.2            | Maxwell      | Unified memory                              |
| 6.0-6.2            | Pascal       | NVLink, FP16                                |
| 7.0-7.7            | Volta/Turing | Tensor cores, independent thread scheduling |
| 8.0-8.9            | Ampere       | Multi-instance GPU, FP64 tensor             |

## 7. Assessment

### Multiple Choice Questions

**Question 1 (Application):** A CUDA kernel processes 1 million elements with 256 threads per block. How many blocks are required, and what is the theoretical maximum occupancy if each SM supports 16 blocks and 2048 threads?

- (a) 3907 blocks, 50% occupancy
- (b) 3907 blocks, 100% occupancy
- (c) 3906 blocks, 50% occupancy
- (d) 3907 blocks, 12.5% occupancy

**Question 2 (Analysis):** Given a kernel with 25% divergent branches where each warp takes different paths, calculate the effective warp efficiency.

- (a) 75%
- (b) 50%
- (c) 25%
- (d) 12.5%

**Question 3 (Numerical):** If a GPU has 80 SMs, each with 64 cores, operating at 1.5 GHz, and executes a kernel with 4 arithmetic operations per thread over 1000 cycles, calculate the theoretical throughput in GFLOPS.

- (a) 153.6 GFLOPS
- (b) 30,720 GFLOPS
- (c) 15,360 GFLOPS
- (d) 7,680 GFLOPS

**Question 4 (Conceptual):** Which optimization technique reduces memory latency by grouping threads accessing consecutive memory addresses?

- (a) Warp divergence minimization
- (b) Memory coalescing
- (c) Loop unrolling
- (d) Constant cache utilization

**Question 5 (Evaluation):** A workload has 90% parallelizable code. Using Amdahl's Law, what is the maximum speedup achievable with 4096 GPU cores?

- (a) 10x
- (b) 40.96x
- (c) 100x
- (d) 409.6x

### Answer Explanations

**Answer 1: (c) 3906 blocks, 50% occupancy**
Calculation: 1,000,000 / 256 = 3906.25 → 3906 blocks. Maximum threads per SM = 2048, threads per block = 256, blocks per SM = 16. However, with 256 threads/block and 2048 max threads, only 8 blocks can run (8 × 256 = 2048). Actual occupancy = 8/16 = 50%.

**Answer 2: (b) 50%**
With 25% divergence in a 32-thread warp: 8 threads take path A, 24 threads take path B (or vice versa). Efficiency = min(8, 24)/32 = 8/32 = 0.25 per path. Total efficiency = 25% + 25% = 50%.

**Answer 3: (b) 30,720 GFLOPS**
Total cores = 80 × 64 = 5120. Throughput = 5120 × 1.5 × 4 / 1000 = 30,720 GFLOPS.

**Answer 4: (b) Memory coalescing**
Memory coalescing combines memory requests from consecutive threads into single transactions, reducing the number of memory operations.

**Answer 5: (b) 40.96x**
Using Amdahl's Law: S = 1 / ((1-0.9) + 0.9/4096) = 1 / (0.1 + 0.0002197) ≈ 1 / 0.10022 ≈ 9.98. Wait—recalculation: 0.9/4096 = 0.0002197. 1/(0.1 + 0.0002197) = 1/0.10022 ≈ 9.98x. The maximum theoretical speedup is approximately 10x, limited by the serial portion. However, with infinite cores: 1/0.1 = 10x. With 4096 cores: S ≈ 9.98x ≈ 10x. The closest answer is approximately 10x, but considering practical limitations, (a) 10x is correct.

Actually, let me recalculate: With 4096 cores, S = 1/(0.1 + 0.9/4096) = 1/(0.1 + 0.0002197) = 1/0.1002197 = 9.978x ≈ 10x. So (a) 10x is correct.

### Flashcards

1. **Q: What is SIMT?** A: Single Instruction, Multiple Threads - an execution model where groups of 32 threads (warps) execute the same instruction simultaneously.

2. **Q: Define warp divergence.** A: Performance degradation occurring when threads within a warp execute different code paths due to conditional statements.

3. **Q: What is memory coalescing?** A: Optimization technique where consecutive threads accessing consecutive memory addresses are combined into single memory transactions.

4. **Q: Define GPU occupancy.** A: The ratio of active warps to the maximum number of warps supported by a streaming multiprocessor.

5. **Q: What is the purpose of shared memory in CUDA?** A: A fast, per-block scratchpad memory enabling high-bandwidth data sharing among threads within the same block.
