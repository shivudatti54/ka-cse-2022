# Introduction to GPU Programming

## 1. What is GPU Programming?

GPU (Graphics Processing Unit) programming involves writing code that leverages the massively parallel architecture of GPUs to accelerate computational tasks beyond the capabilities of traditional CPUs. While CPUs are designed for sequential processing and complex control logic, GPUs are optimized for data-parallel computations—executing the same operation on multiple data elements simultaneously.

Originally designed for rendering graphics, GPUs evolved into General-Purpose GPUs (GPGPUs) when researchers realized their parallel architecture could accelerate scientific computations. This led to the development of programming frameworks like CUDA (Compute Unified Device Architecture) and OpenCL (Open Computing Language).

## 2. GPU Architecture vs CPU Architecture

### 2.1 Fundamental Differences

```
CPU Architecture (Few Complex Cores):
+-----------------------------------------+
| CPU Core 0 | CPU Core 1 | CPU Core 2 | ... |
| (Complex)  | (Complex)  | (Complex)  |     |
+-----------------------------------------+
|                  Cache                  |
+-----------------------------------------+
|              Control Logic              |
+-----------------------------------------+

GPU Architecture (Many Simple Cores):
+-------------------------------------------------+
| Streaming Multiprocessor 0 | Streaming Multiprocessor 1 |
+---------------------------+---------------------------+
| Core 0 | Core 1 | ... | Core N | Core 0 | Core 1 | ... |
| (Simple)| (Simple)|     |(Simple)| (Simple)| (Simple)|   |
+-------------------------------------------------+
|                 Shared Memory                   |
+-------------------------------------------------+
```

**Table: CPU vs GPU Architectural Comparison**

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Cores** | Few (2-64), complex | Many (1000s), simple |
| **Cache** | Large, hierarchical | Smaller, shared |
| **Thread Management** | Hardware + OS | Hardware managed |
| **Best For** | Sequential processing, complex logic | Data-parallel computations |
| **Latency Tolerance** | Low | High (throughput-oriented) |

### 2.2 Memory Hierarchy

GPU memory follows a hierarchical structure that programmers must understand for optimal performance:

```
+-----------------------+
|      Host (CPU)       |
|   Memory (DDR/RAM)    |
+-----------------------+
           ↑
       (PCIe Bus)
           ↓
+-----------------------+
|        Device         |
|      (GPU) Memory     |
+-----------------------+
| Global Memory (DRAM)  |
+-----------------------+
| Constant Memory       |
+-----------------------+
| Texture Memory        |
+-----------------------+
| Shared Memory (per SM)|
+-----------------------+
| Registers (per core)  |
+-----------------------+
```

## 3. Key Concepts in GPU Programming

### 3.1 Thread Hierarchy

GPU programming organizes computation using a hierarchical thread model:

- **Thread**: The smallest execution unit
- **Block**: A group of threads that can cooperate via shared memory
- **Grid**: A collection of blocks that execute the same kernel

```
Grid Structure:
+-------------------------------------------------+
|                   Grid                          |
+-------------------------------------------------+
| Block (0,0) | Block (0,1) | ... | Block (0,N-1) |
+-------------+-------------+-----+---------------+
| Block (1,0) | Block (1,1) | ... | Block (1,N-1) |
+-------------+-------------+-----+---------------+
|     ...     |     ...     | ... |     ...       |
+-------------+-------------+-----+---------------+
| Block (M-1,0)           ...     | Block (M-1,N-1)|
+-------------------------------------------------+

Inside Each Block:
+-------------------------------------------------+
|                 Thread Block                    |
+-------------------------------------------------+
| Thread (0,0) | Thread (0,1) | ... | Thread (0,K-1) |
+-------------+-------------+-----+---------------+
| Thread (1,0) | Thread (1,1) | ... | Thread (1,K-1) |
+-------------+-------------+-----+---------------+
|     ...     |     ...     | ... |     ...       |
+-------------+-------------+-----+---------------+
| Thread (J-1,0)          ...     | Thread (J-1,K-1)|
+-------------------------------------------------+
```

### 3.2 Kernel Execution

A kernel is a function that executes on the GPU. When launched, it creates a grid of threads:

```cpp
// CUDA example: Vector addition kernel
__global__ void vectorAdd(float* A, float* B, float* C, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        C[i] = A[i] + B[i];
    }
}

// Kernel launch configuration
int threadsPerBlock = 256;
int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;
vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, n);
```

## 4. GPU Programming Models

### 4.1 CUDA (Compute Unified Device Architecture)

CUDA is NVIDIA's parallel computing platform and programming model. It provides:
- C/C++ extensions for GPU programming
- Comprehensive development tools
- Extensive libraries for various domains

**CUDA Memory Types:**
- Global memory: Large, high-latency (all threads)
- Shared memory: Fast, on-chip (per block)
- Registers: Fastest (per thread)
- Constant memory: Read-only, cached
- Texture memory: Specialized for certain access patterns

### 4.2 OpenCL (Open Computing Language)

OpenCL is an open standard for cross-platform parallel programming across CPUs, GPUs, and other processors. It offers:
- Vendor-neutral approach
- Support for heterogeneous systems
- Broader hardware support

## 5. Performance Considerations

### 5.1 Amdahl's Law

Amdahl's Law predicts the maximum speedup achievable when parallelizing a program:

```
Speedup = 1 / [(1 - P) + (P / N)]
```

Where:
- P = Proportion of program that can be parallelized
- N = Number of processors

**Example:** If 90% of a program can be parallelized (P=0.9) and we have 10 processors (N=10):
```
Speedup = 1 / [(1 - 0.9) + (0.9 / 10)] = 1 / [0.1 + 0.09] = 1 / 0.19 ≈ 5.26x
```

### 5.2 Scalability

Scalability measures how well a parallel system can handle increasing workloads:

- **Strong Scaling**: Fixed problem size, increasing processors
- **Weak Scaling**: Problem size increases with processors

### 5.3 Optimization Techniques

**Memory Optimization:**
- Coalesced memory access patterns
- Effective use of shared memory
- Minimizing global memory accesses

**Computation Optimization:**
- Maximizing arithmetic intensity
- Avoiding thread divergence
- Proper block and grid sizing

## 6. Hybrid Systems

Modern computing often uses hybrid CPU-GPU systems:

```
Hybrid System Architecture:
+-------------------------------------+
|               Host CPU              |
| +---------------------------------+ |
| |          Multi-core CPU         | |
| |    (Control and serial tasks)    | |
| +---------------------------------+ |
|                PCIe Bus              |
+-------------------------------------+
|               Device GPU             |
| +---------------------------------+ |
| |     Many-core GPU               | |
| |    (Data-parallel computation)   | |
| +---------------------------------+ |
+-------------------------------------+
```

## 7. Practical Example: Vector Addition

Let's examine a complete CUDA vector addition example:

```cpp
#include <stdio.h>
#include <cuda_runtime.h>

// Kernel function
__global__ void vectorAdd(const float *A, const float *B, float *C, int numElements) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < numElements) {
        C[i] = A[i] + B[i];
    }
}

int main() {
    // Initialize host arrays
    int numElements = 50000;
    size_t size = numElements * sizeof(float);
    float *h_A = (float *)malloc(size);
    float *h_B = (float *)malloc(size);
    float *h_C = (float *)malloc(size);
    
    // Initialize input vectors
    for (int i = 0; i < numElements; ++i) {
        h_A[i] = rand() / (float)RAND_MAX;
        h_B[i] = rand() / (float)RAND_MAX;
    }
    
    // Allocate device memory
    float *d_A, *d_B, *d_C;
    cudaMalloc((void **)&d_A, size);
    cudaMalloc((void **)&d_B, size);
    cudaMalloc((void **)&d_C, size);
    
    // Copy data to device
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
    
    // Launch kernel
    int threadsPerBlock = 256;
    int blocksPerGrid = (numElements + threadsPerBlock - 1) / threadsPerBlock;
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, numElements);
    
    // Copy result back to host
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
    
    // Verify result
    for (int i = 0; i < numElements; ++i) {
        if (fabs(h_A[i] + h_B[i] - h_C[i]) > 1e-5) {
            fprintf(stderr, "Result verification failed at element %d!\n", i);
            exit(EXIT_FAILURE);
        }
    }
    
    printf("Test PASSED\n");
    
    // Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    free(h_A);
    free(h_B);
    free(h_C);
    
    return 0;
}
```

## 8. Exam Tips

1. **Understand the memory hierarchy**: Be able to explain the different memory types in GPUs and when to use each.
2. **Know thread organization**: Understand how threads, blocks, and grids relate to each other.
3. **Calculate grid and block sizes**: Practice determining optimal configurations for different problem sizes.
4. **Apply Amdahl's Law**: Be prepared to calculate theoretical speedup given parallel and serial portions.
5. **Identify appropriate applications**: Recognize which types of problems benefit from GPU acceleration.
6. **Compare CPU and GPU architectures**: Understand the fundamental differences and when to use each.
7. **Memory transfer considerations**: Remember that data transfer between CPU and GPU can be a bottleneck.