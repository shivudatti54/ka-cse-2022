# Nvidia Compute Capabilities

## Introduction

Nvidia Compute Capabilities represent a versioning system that defines the feature set and hardware limits of GPU architectures supported by CUDA. Each compute capability version is denoted as "X.Y", where X represents the major version indicating the fundamental architecture generation (such as Volta, Ampere, or Hopper), and Y represents the minor version indicating incremental improvements within that generation. Understanding compute capabilities is essential for CUDA programmers because they determine which hardware features are available, what optimization strategies are applicable, and how to ensure code portability across different GPU generations.

The compute capability system enables developers to write code that can query GPU capabilities at runtime and adapt their algorithms accordingly. This abstraction layer allows CUDA programs to function correctly across diverse hardware while still leveraging advanced features when available. For instance, tensor cores introduced in Volta (compute capability 7.0) require specific capability detection to utilize them optimally, while maintaining backward compatibility with older GPUs that lack these units.

## Key Concepts

### Compute Capability Versioning System

The compute capability versioning follows a structured pattern where major versions correspond to distinct GPU architectures. The major version increases with significant architectural changes, while the minor version increments for minor enhancements within the same architectural family. This versioning directly maps to the hardware's instruction set architecture (ISA), memory hierarchy capabilities, and available execution units.

The CUDA toolkit provides compile-time flags to target specific compute capabilities. The `-arch` flag specifies the code generation architecture (the virtual architecture for PTX), while `-code` specifies the actual physical architecture to compile for. For example, `-arch=sm_80` compiles for Ampere architecture. It is important to note that PTX (Parallel Thread Execution) intermediate representation remains compatible across compute capabilities, allowing JIT compilation at runtime to newer architectures.

### Comprehensive Compute Capability to Architecture Table

| Compute Capability | Architecture | GPU Examples    | Key Features Introduced                                                 |
| ------------------ | ------------ | --------------- | ----------------------------------------------------------------------- |
| 5.0                | Maxwell      | GTX 900 series  | Unified memory, dynamic parallelism, atomic operations on global memory |
| 5.2                | Maxwell      | GTX 900 series  | Enhanced shared memory, foldable constants                              |
| 6.0                | Pascal       | GTX 1000 series | Unified memory improvements, Pascal arithmetic                          |
| 6.1                | Pascal       | GP100           | Enhanced double-precision performance, Cooperative Groups               |
| 7.0                | Volta        | V100            | Tensor Cores, Independent Thread Scheduling, FP64 improvements          |
| 7.5                | Turing       | RTX 2000 series | Ray tracing cores (RTX), INT8/INT4 tensor improvements                  |
| 8.0                | Ampere       | A100            | Third-generation Tensor Cores, async copy, sparse tensors               |
| 8.6                | Ampere       | RTX 3000 series | Enhanced RT cores, FP16 tensor acceleration                             |
| 8.9                | Ampere       | RTX 4000 series | Additional optimizations, wider memory bandwidth                        |
| 9.0                | Hopper       | H100            | FP8 support, Thread Block Clusters, Distributed Shared Memory           |

### Hardware Limits by Compute Capability

Different compute capabilities impose various hardware limitations that directly impact kernel design and occupancy calculations. The following summarizes critical limits:

**Thread Hierarchy Limits:**

- Maximum threads per block: 1024 (all capabilities 5.0+)
- Maximum threads per multiprocessor: 2048 (5.x), 1536 (6.x), 2048 (7.x-8.x), 2048 (9.x)
- Maximum blocks per multiprocessor: 32 (5.x), 32 (6.x), 16 (7.x), 32 (8.x), 32 (9.x)

**Warp and Register Limits:**

- Warp size: 32 threads (consistent across all capabilities)
- Maximum registers per thread: 255 (5.x-6.x), 255 (7.x-8.x), 255 (9.x)
- Maximum registers per multiprocessor: 65536 (5.x), 65536 (6.x), 65536 (7.x), 65536 (8.x), 65536 (9.x)

**Memory Limits:**

- Shared memory per block: 48KB (5.x), 64KB (6.x-7.x), 163KB (8.x), 228KB (9.x)
- Constant memory: 64KB (all capabilities)
- Maximum thread block size in shared memory: 48KB standard, up to 96KB with dynamic allocation on supported architectures

### Runtime Device Querying

CUDA provides the `cudaGetDeviceProperties` function to query compute capability and other device characteristics at runtime. This enables adaptive code that selects optimal algorithms based on available hardware features.

```cuda
#include <cuda_runtime.h>
#include <stdio.h>

int main() {
    int deviceCount;
    cudaGetDeviceCount(&deviceCount);

    for (int i = 0; i < deviceCount; i++) {
        cudaDeviceProp prop;
        cudaGetDeviceProperties(&prop, i);

        printf("Device %d: %s\n", i, prop.name);
        printf("  Compute Capability: %d.%d\n",
               prop.major, prop.minor);
        printf("  Total Global Memory: %.2f GB\n",
               prop.totalGlobalMem / (1024.0 * 1024.0 * 1024.0));
        printf("  Max Threads Per Block: %d\n",
               prop.maxThreadsPerBlock);
        printf("  Max Threads Per Multiprocessor: %d\n",
               prop.maxThreadsPerMultiProcessor);
        printf("  Number of Multiprocessors: %d\n",
               prop.multiProcessorCount);
        printf("  Shared Memory Per Block: %zu KB\n",
               prop.sharedMemPerBlock / 1024);
        printf("  Registers Per Block: %d\n",
               prop.regsPerBlock);
        printf("  Warp Size: %d\n", prop.warpSize);

        // Feature detection
        if (prop.major >= 7) {
            printf("  Supports Tensor Cores\n");
        }
        if (prop.major >= 8) {
            printf("  Supports Async Copy\n");
        }
        if (prop.major >= 9) {
            printf("  Supports FP8 and Thread Block Clusters\n");
        }
    }
    return 0;
}
```

### Architecture-Specific Programming Implications

**Volta (Compute Capability 7.0-7.5):** Introduced Tensor Cores that perform matrix multiply-accumulate operations on FP16/FP32 matrices, providing up to 12x throughput improvement over traditional CUDA cores for deep learning workloads. The Independent Thread Scheduling feature allows threads within a warp to synchronize and diverge more flexibly, enabling more sophisticated algorithms but requiring careful warp-level synchronization patterns.

**Turing (Compute Capability 7.5):** Added Ray Tracing (RT) cores for hardware-accelerated ray-triangle intersection and bounding volume hierarchy traversal. Extended INT8 and INT4 tensor operations for inference workloads. Memory bandwidth improvements enable better utilization of tensor cores.

**Ampere (Compute Capability 8.0-8.9):** Third-generation Tensor Cores support sparse matrices, providing 2x speedup for suitable workloads. The asynchronous copy feature allows data transfers directly from global memory to shared memory without going through registers. Multi-instance GPU (MIG) technology enables partitioning A100 into isolated GPU instances.

**Hopper (Compute Capability 9.0):** Introduced FP8 tensor core support with two formats (E4M3 and E5M2) for different precision requirements. Thread Block Clusters enable synchronization across multiple thread blocks within the same SM cluster. Distributed Shared Memory provides programmer-visible scratchpad for inter-thread-block communication. Transformer Engine dynamically switches between FP8 and higher precision based on layer requirements.

### Compile-Time Targeting and PTX Compatibility

CUDA compilation involves multiple stages: the frontend compiles CUDA C++ to PTX (virtual ISA), and the backend (ptxas) assembles PTX to cubin (machine code for specific architecture). The compilation model supports forward compatibility through PTX JIT compilation.

The compilation hierarchy follows:

- Virtual architecture (`-arch=compute_XY`): Defines the PTX version generated
- Physical architecture (`-code=sm_XY`): Defines the cubin generated
- Runtime JIT: Compiles PTX to cubin for architectures not explicitly specified

For maximum compatibility, compiling with `-arch=compute_80 -code=sm_80` produces code that only runs on Ampere. Compiling with `-arch=compute_80` alone produces PTX that JIT-compiles on first run for the actual device. Best practices suggest using the lowest compute capability that supports required features while including PTX for forward compatibility.

## Examples

### Example 1: Feature-Adaptive Kernel Launch

This example demonstrates how to adapt kernel launch parameters based on compute capability:

```cuda
__global__ void adaptiveKernel(float* data, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        // Kernel computation
        data[idx] = data[idx] * 2.0f + 1.0f;
    }
}

void launchAdaptiveKernel(float* d_data, int n) {
    cudaDeviceProp prop;
    cudaGetDeviceProperties(&prop, 0);

    int blockSize;
    int minGridSize;

    // Calculate optimal block size based on compute capability
    // Higher capabilities can support more registers per thread
    if (prop.major >= 8) {
        // Ampere and newer: utilize more resources
        blockSize = 256;
    } else if (prop.major >= 7) {
        // Volta/Turing
        blockSize = 256;
    } else {
        // Older architectures
        blockSize = 128;
    }

    cudaOccupancyMaxPotentialBlockSize(&minGridSize, &blockSize,
                                        adaptiveKernel,
                                        0, 0);

    int gridSize = (n + blockSize - 1) / blockSize;
    adaptiveKernel<<<gridSize, blockSize>>>(d_data, n);
}
```

### Example 2: Tensor Core Detection and Usage

```cuda
// Check tensor core availability at runtime
bool checkTensorCoreSupport() {
    cudaDeviceProp prop;
    cudaGetDeviceProperties(&prop, 0);

    // Tensor cores available from CC 7.0+
    // But specific matrix dimensions vary by generation
    if (prop.major == 7 && prop.minor == 0) {
        // Volta: m=16, n=16, k=16 (FP16)
        return true;
    } else if (prop.major == 8) {
        // Ampere: supports more data types and sparse matrices
        return true;
    } else if (prop.major >= 9) {
        // Hopper: FP8 support
        return true;
    }
    return false;
}
```

### Example 3: Compute Capability-Based Occupancy Calculation

Given a GPU with compute capability 8.0 (Ampere) and the following specifications:

- Max threads per block: 1024
- Max threads per SM: 2048
- Max registers per SM: 65536
- Max shared memory per SM: 164KB
- Warp size: 32

Calculate the maximum theoretical occupancy for a kernel using 256 threads per block with 32 registers per thread and 8KB shared memory:

**Solution:**

- Threads per SM available: 2048
- Threads per block: 256
- Blocks per SM = min(2048/256, 32) = min(8, 32) = 8
- Registers per block: 256 × 32 = 8192
- Blocks that fit in register limit: 65536/8192 = 8
- Shared memory blocks per SM: 164KB/8KB = 20

Limiting factor: min(8 blocks, 20 blocks, 32) = 8 blocks
Active warps per SM: 8 × 256/32 = 8 × 8 = 64 warps
Maximum warps per SM: 2048/32 = 64
Occupancy: 64/64 × 100% = 100%

## Exam Tips

1. **Understand the version numbering:** Remember that the major version indicates the architecture generation (e.g., 7 = Volta, 8 = Ampere, 9 = Hopper) while the minor version indicates incremental updates within that generation.

2. **Know the feature timeline:** Associate key features with their introduction: Tensor Cores (7.0), Ray Tracing cores (7.5), Async copy (8.0), FP8 support (9.0).

3. **Remember hardware limits:** Maximum threads per block (1024) and warp size (32) are constant across all compute capabilities, while registers and shared memory limits vary.

4. **Compile flags matter:** The `-arch` flag controls PTX generation (virtual architecture), while `-code` controls cubin generation (physical architecture).

5. **Runtime vs compile-time decisions:** Use `cudaGetDeviceProperties` for runtime feature detection; use compile-time conditionals (`#if __CUDA_ARCH__ >= 700`) for architecture-specific code paths.

6. **Occupancy calculations:** Be able to calculate occupancy given hardware limits and kernel resource usage (registers, shared memory, threads per block).

7. **Backward compatibility:** PTX code generated for a lower compute capability can run on higher capability hardware through JIT compilation, but not vice versa.
