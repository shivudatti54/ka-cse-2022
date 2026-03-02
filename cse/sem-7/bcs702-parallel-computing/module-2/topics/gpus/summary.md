# Summary: GPU Computing Fundamentals

## Overview

Graphics Processing Units have evolved from fixed-function graphics accelerators to general-purpose parallel processors capable of executing thousands of concurrent threads. The CUDA platform enables this transition through a hierarchical thread organization and explicit memory management model.

## Core Concepts

### GPU Architecture
Modern GPUs consist of multiple Streaming Multiprocessors (SMs), each containing numerous simple cores optimized for arithmetic operations rather than branch prediction and out-of-order execution. This throughput-oriented architecture processes many parallel operations simultaneously, accepting higher latency per individual operation in exchange for greater aggregate throughput.

### SIMT Execution Model
The Single Instruction, Multiple Threads model extends SIMD by allowing threads to execute independently while following the same instruction path. Threads are organized into warps (32 threads in NVIDIA GPUs), which execute in lockstep. Divergent control flow within a warp causes performance degradation due to serialized execution.

### CUDA Programming Model
CUDA extends C/C++ with:
- **Qualifiers**: `__global__` (device callable from host), `__device__` (device-only), `__host__` (CPU-only)
- **Built-in variables**: `threadIdx`, `blockIdx`, `blockDim`, `gridDim`
- **Runtime API**: Memory allocation (`cudaMalloc`), transfer (`cudaMemcpy`), synchronization

### Memory Hierarchy
| Memory Type | Location | Latency | Scope |
|-------------|----------|---------|-------|
| Global Memory | Device DRAM | High (~400-800 cycles) | All threads |
| Shared Memory | On-chip | Low (~1-2 cycles) | Block |
| Registers | On-chip | Minimal | Thread |

### Host-Device Execution Flow
1. Allocate host and device memory
2. Transfer input data (Host → Device)
3. Launch kernel with configured grid/block dimensions
4. Transfer results (Device → Host)
5. Free all allocated memory

## Key Equations

**Global Thread Index (1D):**
```
global_id = blockIdx.x * blockDim.x + threadIdx.x
```

**Kernel Launch Configuration:**
```
total_threads = gridDim.x * blockDim.x
```

**Memory Transfer Time:**
```
t_transfer = t_setup + size / bandwidth
```

## Vector Addition Analysis

The vector addition kernel exemplifies data-parallelism:
- Each thread performs identical computation on different data elements
- No inter-thread communication required
- Memory access patterns are regular and coalescible
- Theoretical speedup approaches the number of available cores

## When to Use GPUs

**Suitable Workloads:**
- Data-parallel operations on large arrays
- Regular memory access patterns
- Compute-intensive kernels with minimal branching
- Operations repeated across many data elements

**Unsuitable Workloads:**
- Small dataset problems (transfer overhead dominates)
- Irregular memory access patterns
- Heavy branch divergence
- Sequential algorithms with dependencies

## Examination Preparation

Students should be able to:
1. Write and explain a basic CUDA kernel for vector operations
2. Calculate appropriate grid and block dimensions
3. Trace the host-device memory transfer sequence
4. Identify factors affecting GPU kernel performance
5. Determine when GPU acceleration provides benefit over CPU-only execution