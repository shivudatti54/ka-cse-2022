# GPU Performance in Parallel Computing

## Introduction

Graphics Processing Units (GPUs) have undergone a remarkable transformation from specialized graphics rendering hardware to powerful, general-purpose parallel processors capable of delivering teraflops of computational throughput. Their fundamental architectural divergence from traditional Central Processing Units (CPUs) makes them exceptionally well-suited for data-parallel workloads characterized by high computational intensity and regular memory access patterns. The effective utilization of GPU resources requires a deep understanding of the underlying architectural principles that govern GPU performance, including the Single Instruction Multiple Thread (SIMT) execution model, sophisticated memory hierarchies, and specialized scheduling mechanisms. This knowledge is indispensable for engineers and researchers working in scientific computing, deep learning, computer graphics, and high-performance simulation domains.

## 1. Massive Parallelism and SIMT Architecture

### 1.1 Fundamental Architecture

The performance advantage of GPUs stems from their massively parallel architecture, which differs fundamentally from the latency-optimized design of CPUs. A modern GPU comprises thousands of execution cores organized into hierarchical units called Streaming Multiprocessors (SMs) or Compute Units (CUs), depending on the vendor terminology (NVIDIA uses SMs while AMD employs CUs). Each SM contains multiple processing elements (PEs) that execute instructions in lockstep under the SIMT paradigm.

In the SIMT execution model, threads are grouped into warps (NVIDIA terminology) or wavefronts (AMD terminology), with each warp containing 32 consecutive threads that execute the same instruction simultaneously. This fine-grained parallelism enables GPUs to achieve high throughput by amortizing instruction fetch and decode overhead across many threads. However, performance is maximized only when all threads within a warp follow the same execution path; divergence caused by conditional branches results in serial execution of different paths, significantly degrading performance.

**Mathematical Model of Parallel Throughput:**

The theoretical peak throughput $T_{peak}$ of a GPU kernel can be expressed as:

$$T_{peak} = N_{SM} \times N_{warps/SM} \times N_{threads/warp} \times \frac{1}{CPI} \times f_{clock}$$

Where $N_{SM}$ represents the number of streaming multiprocessors, $N_{warps/SM}$ denotes the maximum warps per SM, CPI is cycles per instruction, and $f_{clock}$ is the GPU clock frequency. Achieving throughput close to this theoretical maximum requires careful attention to thread utilization and memory access patterns.

### 1.2 Latency Hiding Through Multithreading

GPU architectures employ simultaneous multithreading (SMT) to hide the latency of memory operations and arithmetic instructions. While a CPU typically relies on sophisticated branch prediction and out-of-order execution to hide latency, GPUs employ a different strategy: massive thread-level parallelism. When threads in a warp stall due to memory accesses, the GPU scheduler rapidly switches to executing a different warp that has its operands available. This context switching occurs with minimal overhead because register state is maintained for all active threads.

The effectiveness of latency hiding is quantified by the **occupancy** metric, defined as the ratio of active warps to the maximum possible active warps per SM:

$$Occupancy = \frac{N_{active\_warps}}{N_{max\_warps}} \times 100\%$$

Higher occupancy generally correlates with better latency hiding, though the relationship is not strictly linear due to other factors such as memory bandwidth saturation and execution resource constraints.

## 2. Memory Hierarchy and Bandwidth Optimization

### 2.1 Hierarchical Memory Organization

GPU memory systems are designed with multiple tiers, each offering different trade-offs between capacity, bandwidth, and latency. Understanding this hierarchy is critical for writing efficient GPU code.

**Global Memory (Device Memory):** The largest memory tier (typically 4-24 GB on modern discrete GPUs), implemented as high-bandwidth GDDR6 or HBM2e DRAM. While peak bandwidth can exceed 1 TB/s, the actual achieved bandwidth depends heavily on access patterns. Global memory accesses exhibit high latency (400-800 cycles), necessitating effective latency hiding through concurrent thread execution.

**Shared Memory (Scratchpad):** Each SM possesses a small but extremely fast on-chip memory (typically 48-128 KB per SM) that functions as a software-managed cache. Shared memory provides bandwidth an order of magnitude higher than global memory with latency of only a few cycles. However, shared memory is organized into multiple banks, and simultaneous access to the same bank results in serialization (bank conflict).

**Registers:** The fastest storage tier, with each thread having access to private registers. The register file per SM is limited (typically 65536-256000 registers), and exceeding this limit causes register spilling to local memory, dramatically reducing performance.

### 2.2 Memory Coalescing

Global memory access efficiency is maximized when threads within a warp access consecutive memory locations, a pattern known as coalesced access. The GPU's memory controller can service a single memory transaction for multiple simultaneous requests when addresses are contiguous.

**Coalescing Efficiency Calculation:**

For a warp of 32 threads accessing $N$ distinct 32-bit words, the number of memory transactions $T$ required depends on the access pattern:

- **Coalesced (stride=1):** $T = \lceil N/32 \rceil$ transactions
- **Strided (stride=S):** $T = N \times \lceil S/32 \rceil$ transactions (worst case)
- **Scattered (random):** $T = N$ transactions (worst case)

Achieving high coalescing efficiency is one of the most impactful optimizations in GPU programming.

### 2.3 Bank Conflicts in Shared Memory

Shared memory is partitioned into 32 banks (corresponding to the warp size), and each bank can service only one transaction per cycle. When multiple threads in a warp access different addresses within the same bank, a bank conflict occurs, forcing serial execution of the conflicting accesses. The degree of conflict determines the performance penalty:

$$Effective\_Bandwidth = \frac{Base\_Bandwidth}{Max\_Conflict\_Degree}$$

Designers can avoid bank conflicts by padding shared memory arrays or ensuring accesses follow conflict-free access patterns.

## 3. Performance Modeling and Analysis

### 3.1 Roofline Model for GPU Performance

The Roofline model provides an intuitive visual representation of kernel performance limits, plotting achieved performance against operational intensity. The model defines two ceiling constraints:

**Memory Bandwidth Ceiling:** $Performance_{max} = Bandwidth \times OperationalIntensity$

**Compute Ceiling:** $Performance_{max} = PeakFLOPs$

For GPU kernels, the actual performance is bounded by whichever ceiling is lower at a given operational intensity. Operational Intensity (OI) is defined as the ratio of floating-point operations to bytes of memory traffic:

$$OI = \frac{FLOPs}{Bytes\_transferred}$$

**Example Calculation:**

Given a GPU with memory bandwidth of 900 GB/s and a kernel with OI = 50 FLOPs/byte:

- Memory-bound ceiling: $900 \times 50 = 45,000$ GFLOPs/s
- If peak compute is 10,000 GFLOPs/s, the kernel is memory-bound and limited to 45,000 GFLOPs/s

### 3.2 Occupancy Calculation

Occupancy is constrained by three primary resources: registers, shared memory, and thread block size. The limiting factor determines maximum active warps.

**Register-Limited Occupancy:**
$$Occupancy_{reg} = \min\left(1, \frac{Registers\_per\_SM}{Threads\_per\_block \times Registers\_per\_thread}\right)$$

**Shared Memory-Limited Occupancy:**
$$Occupancy_{sm} = \min\left(1, \frac{Shared\_Memory\_per\_SM}{Threads\_per\_block \times Shared\_Memory\_per\_block}\right)$$

**Example:**
If a GPU has 65536 registers/SM, a kernel uses 32 registers/thread, and thread blocks contain 256 threads:

- Register usage per block = $256 \times 32 = 8192$ registers
- Maximum blocks = $65536 / 8192 = 8$ blocks
- Maximum warps = $8 \times (256/32) = 64$ warps (if no other constraints)

## 4. Common Performance Bottlenecks

### 4.1 Warp Divergence

When threads within a warp take different execution paths due to conditional statements, the warp must execute each path serially, reducing effective parallelism. Divergence can be minimized by:

- Restructuring code to minimize divergent branches
- Using predicated execution instead of branches where possible
- Organizing data to ensure threads in a warp follow similar paths

**Divergence Overhead:** If a warp has $D$ divergent paths with $P_i$ threads on path $i$, and each path takes $C_i$ cycles, the effective execution time is $\sum_{i=1}^{D} C_i$ rather than $\max(C_i)$ in the non-divergent case.

### 4.2 Memory Access Patterns

Beyond coalescing, several other factors affect memory performance:

- **Alignment:** Memory accesses should be aligned to 32-byte (float4) or 128-byte (float4x4) boundaries
- **Prefetching:** Hardware prefetchers work best with regular access patterns
- **Write coalescing:** Both reads and writes benefit from coalescing

## Summary

| Aspect                | Key Metric             | Optimization Strategy                           |
| --------------------- | ---------------------- | ----------------------------------------------- |
| Parallelism           | Active warps/SM        | Maximize thread count, minimize divergence      |
| Memory Coalescing     | Transaction efficiency | Ensure strided-1 access within warps            |
| Shared Memory         | Bank conflict rate     | Use padding and conflict-free patterns          |
| Occupancy             | Active warps/maximum   | Balance register/shared memory usage            |
| Operational Intensity | FLOPs/byte             | Maximize computation relative to memory traffic |

Achieving peak GPU performance requires systematic optimization across all these dimensions, guided by quantitative profiling and performance modeling.
