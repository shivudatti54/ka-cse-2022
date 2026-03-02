# GPU Architectures

## Introduction

Understanding GPU architecture is essential for writing efficient CUDA programs. NVIDIA GPUs are built around a hierarchical structure of processing units and memory systems, each level of which has different capacity, bandwidth, and latency characteristics. This topic covers the key architectural components of NVIDIA GPUs, from Streaming Multiprocessors and CUDA cores to the multi-level memory hierarchy that feeds them.

## High-Level GPU Architecture

At the highest level, an NVIDIA GPU consists of:

1. **An array of Streaming Multiprocessors (SMs)**: These are the primary compute units. The number of SMs varies by GPU model (e.g., the A100 has 108 SMs, the RTX 3090 has 82 SMs).
2. **A memory subsystem**: Including on-chip caches and off-chip global memory (DRAM).
3. **A GigaThread Engine**: The global scheduler that distributes thread blocks to SMs.
4. **Interconnect fabric**: Connecting SMs to memory controllers and other system components.

When a CUDA kernel is launched, the GigaThread Engine assigns thread blocks to available SMs. Each SM then independently schedules and executes the threads within its assigned blocks.

## Streaming Multiprocessors (SMs)

The Streaming Multiprocessor is the fundamental building block of NVIDIA GPU compute architecture. Each SM contains:

### CUDA Cores (Streaming Processors)

CUDA cores are the individual processing elements that perform integer and floating-point arithmetic. Each CUDA core contains:

- An integer arithmetic logic unit (INT ALU)
- A floating-point unit (FPU)
- Dispatch logic

The number of CUDA cores per SM has varied across generations:

| Architecture | Year | CUDA Cores per SM           | Notable Features              |
| ------------ | ---- | --------------------------- | ----------------------------- |
| Fermi        | 2010 | 32                          | First support for ECC, 64-bit |
| Kepler       | 2012 | 192 (SMX)                   | High throughput               |
| Maxwell      | 2014 | 128 (SMM)                   | Efficiency focus              |
| Pascal       | 2016 | 64                          | NVLink, HBM2                  |
| Volta        | 2017 | 64 FP32 + Tensor Cores      | Independent thread scheduling |
| Turing       | 2018 | 64 FP32 + Tensor Cores      | Ray tracing cores             |
| Ampere       | 2020 | 64 FP32 (or 128 concurrent) | Third-gen Tensor Cores        |
| Ada Lovelace | 2022 | 128 FP32                    | Fourth-gen Tensor Cores       |
| Hopper       | 2023 | 128 FP32                    | Fifth-gen Tensor Cores, FP8   |

### Theoretical GFLOPS Calculation

The theoretical peak floating-point performance of a GPU can be calculated using the formula:

$$GFLOPS = \frac{N_{cores} \times N_{SM} \times f_{clock} \times 2}{10^9}$$

Where:

- $N_{cores}$ = CUDA cores per SM
- $N_{SM}$ = Number of SMs on the GPU
- $f_{clock}$ = GPU clock frequency in Hz
- The factor of 2 accounts for the FMA (Fused Multiply-Add) operation, which performs 2 FLOPS per cycle

**Example**: Calculate the theoretical peak FP32 performance of an NVIDIA A100 with 108 SMs, 64 FP32 cores per SM, and a base clock of 1.41 GHz:

$$GFLOPS = \frac{64 \times 108 \times 1.41 \times 10^9 \times 2}{10^9} = 19,492.8 \text{ GFLOPS} \approx 19.5 \text{ TFLOPS}$$

### Tensor Cores

Introduced in the Volta architecture (2017), Tensor Cores are specialized units designed for matrix multiply-and-accumulate operations. They dramatically accelerate deep learning training and inference by performing mixed-precision matrix math.

A Tensor Core performs the operation:
$$D = A \times B + C$$

Where A and B are typically in FP16, BF16, or TF32 format, while C and D are in FP32. This mixed-precision approach provides:

- Higher throughput (up to 4x compared to FP32)
- Reduced memory bandwidth requirements
- Maintained accuracy through FP32 accumulation

### Special Function Units (SFUs)

SFUs handle transcendental functions such as sine, cosine, reciprocal, and square root. These operations would be very expensive to compute in the main ALUs. Modern GPUs dedicate approximately 1/8 of the execution resources to SFUs.

### Load/Store Units

These units handle memory operations, computing addresses and issuing memory requests to the cache and memory hierarchy. Each SM typically has 8-16 load/store units.

### Warp Schedulers

Each SM contains multiple warp schedulers (typically 2 or 4, depending on the architecture generation). A warp scheduler selects a ready warp (a group of 32 threads) and issues one or more instructions from that warp each clock cycle.

**Latency Hiding**: The ability to switch between warps with zero overhead is a key mechanism for hiding memory latency. When a warp is waiting for a memory access (100-300 cycles), the scheduler can issue instructions from another ready warp. This is formalized as:

$$Effective\_Latency = \frac{Latency}{N_{parallel\_warps}}$$

Where $N_{parallel\_warps}$ is the number of warps that can be scheduled in parallel. Higher occupancy (more active warps) enables better latency hiding.

### Dispatch Units

Each warp scheduler has one or more dispatch units that send instructions to the execution pipelines (CUDA cores, SFUs, load/store units, Tensor Cores).

## Warp Execution Model

Threads on a GPU are executed in groups of 32 called **warps**. All threads in a warp execute the same instruction at the same time (SIMT -- Single Instruction, Multiple Threads). This is similar to SIMD but with the important distinction that each thread has its own program counter and register state, allowing limited divergence.

### Warp Divergence

When threads within a warp take different branches of a conditional statement (an `if-else`), the warp must serialize execution: it first executes the `if` branch with some threads masked off, then the `else` branch with the remaining threads masked off. This is called **warp divergence** and can significantly reduce performance.

**Performance Impact Analysis**: Consider a warp executing an if-else where 16 threads take the if-branch and 16 take the else-branch:

- Without divergence: 1 instruction cycle
- With divergence: 2 instruction cycles
- Efficiency loss: 50%

For maximum efficiency, threads within a warp should follow the same control path. This is achieved through:

1. Branch predication (if only a few threads diverge)
2. Restructuring code to minimize divergent paths
3. Using warp-level primitives (`__syncwarp()`)

## Compute Capabilities

NVIDIA's Compute Capability (CC) version indicates the feature set and architectural generation:

| Compute Capability | Architecture | Key Features                                           |
| ------------------ | ------------ | ------------------------------------------------------ |
| 3.0-3.7            | Kepler       | Dynamic parallelism, GPU debugging                     |
| 5.0-5.2            | Maxwell      | Unified memory, atomic operations                      |
| 6.0-6.2            | Pascal       | NVLink, page migration                                 |
| 7.0                | Volta        | Independent thread scheduling, Tensor Cores            |
| 7.5                | Turing       | Ray tracing, mesh shaders                              |
| 8.0-8.9            | Ampere/Ada   | Third/fourth-gen Tensor Cores, FP64 improvements       |
| 9.0                | Hopper       | Fifth-gen Tensor Cores, FP8, distributed shared memory |

## GPU Memory Hierarchy

The GPU memory hierarchy is one of the most critical aspects of GPU architecture for performance. Understanding the trade-offs between capacity, latency, and bandwidth is essential for optimization.

### Memory Hierarchy Comparison

| Memory Type    | Scope      | Location | Capacity     | Latency        | Bandwidth        |
| -------------- | ---------- | -------- | ------------ | -------------- | ---------------- |
| Registers      | Per-thread | On-chip  | 256 KB/SM    | 1 cycle        | Very High        |
| Shared Memory  | Per-block  | On-chip  | 48-164 KB/SM | 1-2 cycles     | ~15 TB/s         |
| L1 Cache       | Per-SM     | On-chip  | 32-192 KB/SM | 10-20 cycles   | ~12 TB/s         |
| L2 Cache       | Chip-wide  | On-chip  | 6-40 MB      | 40-80 cycles   | ~2 TB/s          |
| Constant Cache | Per-SM     | On-chip  | 8 KB/SM      | 1-2 cycles     | High (broadcast) |
| Texture Cache  | Per-SM     | On-chip  | 12-48 KB/SM  | 20-40 cycles   | High             |
| Global Memory  | Global     | Off-chip | 8-80 GB      | 400-800 cycles | 1.5-3.5 TB/s     |

### 1. Registers

- **Per-thread, on-chip** storage
- The fastest form of memory on the GPU
- Each SM has a large register file (e.g., 65,536 32-bit registers on many architectures)
- Registers are partitioned among all active threads on the SM
- Variables declared in a kernel function typically reside in registers
- If a kernel uses too many registers per thread, it reduces the number of threads that can be active on the SM (reduces **occupancy**)

### 2. Shared Memory

- **Per-block, on-chip** scratchpad memory
- Accessible by all threads within the same thread block
- Much faster than global memory (comparable to L1 cache speeds)
- Typically 48 KB to 164 KB per SM (configurable with L1 cache on some architectures)
- Declared with `__shared__` qualifier in CUDA
- Organized into **banks** (typically 32 banks). Bank conflicts occur when multiple threads in a warp access different addresses in the same bank, causing serialization

**Bank Conflict Analysis**: With 32 banks and a warp size of 32 threads:

- Optimal access: Each thread accesses a different bank (0 conflicts)
- 2-way conflict: 2 threads access same bank (2x serialization)
- Worst case: All threads access same bank (32x serialization)

Example usage:

```c
__shared__ float tile[BLOCK_SIZE][BLOCK_SIZE];
tile[threadIdx.y][threadIdx.x] = input[globalIdx];
__syncthreads(); // Ensure all threads have written before reading
float value = tile[threadIdx.x][threadIdx.y]; // Transposed access
```

### 3. L1 Cache

- **Per-SM, on-chip** cache
- Automatically caches accesses to global memory
- On many architectures, L1 cache and shared memory share the same physical on-chip memory, and the partition can be configured
- Typical size: 32 KB to 192 KB per SM
- Helps reduce latency for repeated global memory accesses
- Implements LRU (Least Recently Used) replacement policy

### 4. L2 Cache

- **Chip-wide, on-chip** cache
- Shared by all SMs
- Typical size: 6 MB (Pascal) to 40 MB (Hopper)
- Reduces traffic to global memory by caching frequently accessed data
- Critical for memory coalescing effectiveness

### 5. Constant Memory

- **Global scope, cached**
- 64 KB dedicated constant memory per GPU
- Read-only access optimized for broadcast (same value to all threads in a warp)
- Ideal for storing configuration parameters, lookup tables

### 6. Texture Memory

- **Global scope, cached**
- Optimized for 2D/3D spatial locality
- Supports hardware interpolation (bilinear, trilinear)
- Useful for image processing, physics simulation

### Global Memory

- **Off-chip DRAM**
- Highest capacity (8-80 GB)
- Highest latency (400-800 cycles)
- Primary storage for kernel data
- **Memory Coalescing**: Accesses from threads in the same warp are combined into fewer transactions when addresses are contiguous.

**Coalescing Efficiency**: For a warp accessing consecutive 4-byte elements:

- Perfect coalescing: 1 memory transaction
- Strided access (stride=2): 2 transactions
- Random access: Up to 32 transactions

### Theoretical Memory Bandwidth Calculation

Theoretical peak memory bandwidth is calculated as:

$$BW_{peak} = 2 \times Bus_{width} \times Clock_{memory} \times Efficiency$$

**Example**: NVIDIA A100 with HBM2e memory:

- Memory clock: 2.5 GHz (1215 MHz effective)
- Bus width: 5120 bits (640 bytes)
- Typical efficiency: 70-80%

$$BW_{peak} = 2 \times 640 \text{ bytes} \times 2.5 \text{ GHz} \times 0.75 = 2.4 \text{ TB/s}$$

## Occupancy Analysis

GPU occupancy is defined as the ratio of active warps to the maximum possible warps per SM:

$$Occupancy = \frac{W_{active}}{W_{max}} \times 100\%$$

Factors limiting occupancy:

1. **Register usage**: Each thread uses N registers → $N_{threads} \times N_{registers} \leq Registers_{available}$
2. **Shared memory**: Each block uses M bytes → $N_{blocks} \times M \leq SharedMemory_{available}$
3. **Warps per block**: Minimum of 1 warp per block, typically multiple

**Example Calculation**:

- SM has 2048 registers per thread limit
- Kernel uses 32 registers per thread
- Kernel uses 4 KB shared memory per block
- Block size: 256 threads (8 warps)

Maximum threads per SM = 2048 / 32 = 64 threads
This is clearly suboptimal; typical limits are much higher.

With 64 threads: 64 / 32 = 2 warps per SM
Occupancy = 2 / (maximum warps, typically 32-64) = 3-6%

To increase occupancy:

- Reduce register usage per thread
- Reduce shared memory per block
- Increase block size appropriately
