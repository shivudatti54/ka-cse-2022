# Multicore Processor And GPU

## Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

In the contemporary landscape of computing, the era of single-core processors reaching their frequency and power limits has given rise to two revolutionary architectural paradigms: **multicore processors** and **Graphics Processing Units (GPUs)**. These technologies form the backbone of modern computing systems, enabling unprecedented levels of performance, parallelism, and efficiency across diverse applications.

For students pursuing BSc (Hons) Computer Science at Delhi University under NEP 2024, understanding these architectures is not merely academic—it is essential for comprehending how contemporary software systems leverage hardware parallelism. From smartphone applications to supercomputers, from AI training to real-time graphics rendering, multicore processors and GPUs power the digital infrastructure of our world.

This study material aligns with the Delhi University syllabus for Computer System Architecture, covering the theoretical foundations, architectural details, programming models, and practical applications of these transformative technologies.

---

## 2. Multicore Processors

### 2.1 Fundamentals and Evolution

A **multicore processor** integrates multiple independent processing units (cores) onto a single integrated circuit (die). Each core functions as a complete CPU capable of executing instructions independently, yet they share certain resources like main memory and interconnect infrastructure.

The transition from single-core to multicore architectures was driven by:

- **Power Wall**: Increasing clock frequency led to exponential power consumption and heat generation
- **ILP (Instruction-Level Parallelism) Limits**: Diminishing returns from extracting more ILP from sequential code
- **Memory Wall**: Memory speed improvements lagged behind CPU speed improvements

**Key Terminology**:
- **Core**: An independent execution unit capable of fetching, decoding, and executing instructions
- **Socket**: A physical connector on the motherboard housing one processor package
- **Thread**: A unit of execution within a process; hardware threads represent physical execution contexts
- **Symmetric Multiprocessing (SMP)**: All cores share equal access to memory and I/O

### 2.2 Cache Coherence

In a multicore system, each core typically possesses its own private cache (L1, and often L2). This creates a fundamental challenge: **cache coherence**—ensuring that all cores observe a consistent view of memory.

**The Coherence Problem**: When Core A writes to a memory location that Core B has cached, Core B's cached copy becomes stale.

**MESI Protocol**: A widely used cache coherence protocol with four states:

| State | Meaning | Description |
|-------|---------|-------------|
| **M (Modified)** | Exclusive, Modified | Cache line is dirty; only this core has it |
| **E (Exclusive)** | Exclusive, Clean | Cache line is clean; only this core has it |
| **S (Shared)** | Shared | Multiple cores may have this line; all copies are identical |
| **I (Invalid)** | Invalid | Cache line is not present or is stale |

**Directory-Based Coherence**: For systems with many cores (more than can be efficiently handled with bus-based protocols), directory-based approaches maintain a directory entry for each memory block, tracking which caches have copies.

### 2.3 Memory Organization: NUMA

**Non-Uniform Memory Access (NUMA)** is a memory architecture common in enterprise multicore systems where memory access latency depends on the memory location relative to the processor.

```
                    [Core 0]   [Core 1]
                        |         |
                    Local Memory  Local Memory
                        \         /
                         \       /
                        Interconnect
                         /       \
                    [Core 2]   [Core 3]
                        |         |
                    Local Memory  Local Memory
```

**NUMA Characteristics**:
- **Local Memory**: Faster access for "home" core
- **Remote Memory**: Higher latency when accessing other processor's memory
- **NUMA Awareness**: Modern OS and applications can optimize memory placement

### 2.4 Thread Synchronization

With multiple threads executing concurrently, synchronization mechanisms become essential for maintaining correctness:

**Mutex (Mutual Exclusion Lock)**:
```c
#include <pthread.h>
pthread_mutex_t lock;

void* deposit(void* arg) {
    pthread_mutex_lock(&lock);
    // Critical section - modify shared balance
    balance += amount;
    pthread_mutex_unlock(&lock);
    return NULL;
}
```

**Barriers**: Synchronize threads at a specific point, ensuring all reach before proceeding:
```c
pthread_barrier_t barrier;
pthread_barrier_wait(&barrier);  // All threads wait here
```

**Atomic Operations**: Lock-free operations for simple read-modify-write operations:
```c
#include <stdatomic.h>
atomic_fetch_add(&counter, 1);  // Thread-safe increment
```

---

## 3. GPU Architecture

### 3.1 GPU vs CPU: Architectural Differences

While CPUs are designed for **low-latency** execution of sequential tasks with sophisticated branch prediction and out-of-order execution, GPUs are optimized for **high-throughput** processing of many parallel operations.

| Feature | CPU | GPU |
|---------|-----|-----|
| **Focus** | Low latency, complex control flow | High throughput, massive parallelism |
| **Core Count** | 2-64 cores (modern) | Thousands of simple cores |
| **Cache** | Large, complex hierarchy | Smaller, more focused on throughput |
| **Control Logic** | Sophisticated branch prediction | SIMD/SIMT execution |
| **Thread Switching** | Fast hardware threads | Lightweight, warp-based |
| **Memory Bandwidth** | Moderate | Very High |

### 3.2 SIMT (Single Instruction, Multiple Threads)

**SIMT** is the execution model used by modern GPUs, extending SIMD concepts with thread-level parallelism:

- **Warps**: Groups of 32 threads that execute in lockstep
- **Divergence**: When threads within a warp take different paths, they execute both paths serially
- **Thread Hierarchy**: Thread → Warp → Block → Grid

```
Grid (entire kernel)
    └── Block 0 (can have multiple warps)
            ├── Warp 0 (32 threads) - executing same instruction
            ├── Warp 1 (32 threads)
            └── ...
    └── Block 1
            └── ...
```

### 3.3 GPU Memory Types

GPUs employ a complex memory hierarchy:

| Memory Type | Scope | Access | Latency |
|-------------|-------|--------|---------|
| **Registers** | Per-thread | R/W | ~1 cycle |
| **Shared Memory** | Per-block | R/W | ~1-2 cycles |
| **Local Memory** | Per-thread | R/W | ~400-600 cycles (off-chip) |
| **Global Memory** | All threads | R/W | ~400-600 cycles |
| **Constant Memory** | All threads | R | ~1-2 cycles (cached) |
| **Texture Memory** | All threads | R | Cached |

**Shared Memory**: A fast on-chip memory shared among threads within a block, critical for optimizing data reuse.

**Global Memory**: The main GPU memory; coalesced access patterns are essential for performance.

---

## 4. Heterogeneous Computing

### 4.1 Concept and Importance

**Heterogeneous computing** combines different processor types (CPU, GPU, FPGA, ASIC) to leverage each processor's strengths. The CPU handles control-intensive tasks, sequential logic, and system operations, while the GPU accelerates data-parallel computations.

### 4.2 CUDA Programming Model

**CUDA** (Compute Unified Device Architecture) is NVIDIA's parallel computing platform:

```cuda
// Kernel: executed by many threads in parallel
__global__ void vectorAdd(float* A, float* B, float* C, int n) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    if (tid < n) {
        C[tid] = A[tid] + B[tid];  // Each thread handles one element
    }
}

int main() {
    // Host code
    float *h_A, *h_B, *h_C;
    float *d_A, *d_B, *d_C;
    
    // Allocate device memory
    cudaMalloc(&d_A, size);
    cudaMalloc(&d_B, size);
    cudaMalloc(&d_C, size);
    
    // Copy data to device
    cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);
    
    // Launch kernel with 256 threads per block
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, n);
    
    // Copy result back to host
    cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
    
    cudaFree(d_A); cudaFree(d_B); cudaFree(d_C);
}
```

### 4.3 OpenCL Framework

**OpenCL** (Open Computing Language) provides a vendor-agnostic framework for heterogeneous computing:

```c
// OpenCL kernel for vector addition
__kernel void vector_add(__global const float* A,
                         __global const float* B,
                         __global float* C) {
    int gid = get_global_id(0);
    C[gid] = A[gid] + B[gid];
}
```

**OpenCL Advantages**:
- **Portability**: Works across different hardware vendors (NVIDIA, AMD, Intel)
- **Standardization**: Khronos Group maintained
- **Flexibility**: Supports CPUs, GPUs, FPGAs, and specialized accelerators

---

## 5. Practical Applications

### 5.1 Image Processing Application

**Example: Parallel Image Blur using CUDA**

```cuda
__global__ void blurKernel(unsigned char* input, 
                           unsigned char* output,
                           int width, int height) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;
    
    if (x > 0 && x < width - 1 && y > 0 && y < height - 1) {
        int sum = 0;
        // 3x3 kernel blur
        for (int dy = -1; dy <= 1; dy++) {
            for (int dx = -1; dx <= 1; dx++) {
                sum += input[(y + dy) * width + (x + dx)];
            }
        }
        output[y * width + x] = sum / 9;  // Average
    }
}
```

### 5.2 Matrix Multiplication with Shared Memory Optimization

```cuda
__global__ void matrixMulShared(float* A, float* B, float* C, 
                                int width) {
    __shared__ float sharedA[16][16];
    __shared__ float sharedB[16][16];
    
    int bx = blockIdx.x; int by = blockIdx.y;
    int tx = threadIdx.x; int ty = threadIdx.y;
    
    int row = by * 16 + ty;
    int col = bx * 16 + tx;
    
    float sum = 0;
    
    for (int m = 0; m < width / 16; m++) {
        // Load data into shared memory (coalesced)
        sharedA[ty][tx] = A[row * width + (m * 16 + tx)];
        sharedB[ty][tx] = B[(m * 16 + ty) * width + col];
        __syncthreads();
        
        // Compute partial result
        for (int k = 0; k < 16; k++) {
            sum += sharedA[ty][k] * sharedB[k][tx];
        }
        __syncthreads();
    }
    
    C[row * width + col] = sum;
}
```

### 5.3 Real-World Use Cases

1. **Scientific Computing**: Weather prediction, molecular dynamics, fluid dynamics simulations
2. **Deep Learning**: Training and inference for neural networks (TensorFlow, PyTorch)
3. **Computer Vision**: Object detection, image segmentation, real-time video processing
4. **Cryptocurrency Mining**: SHA-256 and Ethash algorithms
5. **Database Acceleration**: In-memory database operations, join processing

---

## 6. Key Takeaways

1. **Multicore Processors** represent the evolution from single-core designs, with multiple independent cores on a single chip enabling parallel execution of tasks.

2. **Cache Coherence** protocols (MESI, MOESI) ensure consistent memory views across cores with private caches—a fundamental challenge in shared-memory multiprocessing.

3. **NUMA** architectures recognize that memory access latency varies based on processor-memory distance, requiring NUMA-aware software design for optimal performance.

4. **GPU Architecture** differs fundamentally from CPUs—thousands of simple cores optimized for throughput rather than low-latency sequential execution.

5. **SIMT** execution model enables efficient parallel processing by grouping threads into warps that execute in lockstep.

6. **GPU Memory Hierarchy** offers various memory types with different characteristics; understanding and utilizing them correctly is crucial for performance.

7. **Heterogeneous Computing** combines CPUs and GPUs to leverage each processor type's strengths—CPU for control logic, GPU for data-parallel acceleration.

8. **CUDA** and **OpenCL** provide frameworks for programming GPUs; CUDA offers NVIDIA-specific optimizations while OpenCL provides vendor-agnostic portability.

9. **Thread Synchronization** mechanisms (mutexes, barriers, atomics) are essential for correct parallel program execution.

10. **Performance Optimization** in parallel systems requires careful consideration of memory access patterns, thread divergence, and load balancing.

---

## 7. Assessment Material

### 7.1 Multiple Choice Questions (MCQs)

**Question 1:** In the MESI cache coherence protocol, what does the 'M' state represent?
- a) Modified
- b) Main
- c) Memory
- d) Multicore

**Question 2:** What is a warp in GPU terminology?
- a) A single thread executing independently
- b) A group of 32 threads executing in lockstep
- c) A cache line
- d) A memory transaction

**Question 3:** Which memory type in GPUs has the lowest latency?
- a) Global Memory
- b) Shared Memory
- c) Local Memory
- d) Constant Memory

**Question 4:** In CUDA, what does the `__global__` qualifier indicate?
- a) Function executes only on CPU
- b) Function executes only on GPU
- c) Function is a device kernel callable from host
- d) Function is a memory allocation

**Question 5:** What is the primary advantage of NUMA architecture?
- a) Simpler programming model
- b) Uniform memory access latency
- c) Scalability for many-core systems
- d) Reduced cache coherence complexity

**Question 6:** Which OpenCL component manages execution of kernels on devices?
- a) Kernel
- b) Program
- c) Command Queue
- d) Context

**Question 7:** What is thread divergence in GPU execution?
- a) Threads executing different instructions
- b) Threads taking different code paths within a warp
- c) Threads terminating early
- d) Threads accessing different memory locations

**Question 8:** What is the purpose of shared memory in GPUs?
- a) Permanent storage for all data
- b) Fast on-chip memory for thread communication
- c) Read-only cache
- d) Virtual memory management

### 7.2 Flashcards

| Term | Definition |
|------|------------|
| **Multicore Processor** | A processor with multiple independent cores on a single integrated circuit |
| **Cache Coherence** | Property ensuring multiple caches show the same value for the same memory location |
| **MESI Protocol** | Cache coherence protocol with Modified, Exclusive, Shared, and Invalid states |
| **NUMA** | Non-Uniform Memory Access—memory architecture where access time depends on memory location |
| **SIMT** | Single Instruction, Multiple Threads—GPU execution model where threads execute in groups (warps) |
| **Warp** | A group of 32 threads that execute the same instruction in lockstep on a GPU |
| **CUDA** | NVIDIA's parallel computing platform and API for GPU programming |
| **OpenCL** | Open standard for heterogeneous computing across CPUs, GPUs, and accelerators |
| **Shared Memory** | Fast on-chip GPU memory shared among threads within a block |
| **Thread Block** | A group of threads that can cooperate via shared memory and synchronization |
| **Grid** | Collection of thread blocks that execute the same kernel |
| **Global Memory** | GPU memory accessible by all threads with high capacity but high latency |

### 7.3 Short Answer Questions

1. Explain the difference between symmetric multiprocessing (SMP) and NUMA architectures.
2. Describe the MESI protocol states and transitions.
3. Why is thread divergence a performance concern in GPU programming?
4. Compare CUDA and OpenCL in terms of portability and performance.
5. Explain the concept of coalesced memory access in GPUs and its importance.
6. How does heterogeneous computing combine CPU and GPU strengths?
7. Discuss the memory hierarchy in GPUs and their access latencies.
8. What are the advantages of using shared memory in GPU kernels?

### 7.4 Answers to MCQs

1. (a) Modified
2. (b) A group of 32 threads executing in lockstep
3. (b) Shared Memory
4. (c) Function is a device kernel callable from host
5. (c) Scalability for many-core systems
6. (c) Command Queue
7. (b) Threads taking different code paths within a warp
8. (b) Fast on-chip memory for thread communication

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. For further reading, refer to "Computer Architecture: A Quantitative Approach" by Hennessy and Patterson, and NVIDIA's CUDA Programming Guide.*