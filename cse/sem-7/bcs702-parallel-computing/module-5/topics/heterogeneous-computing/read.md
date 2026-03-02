# Heterogeneous Computing

## 1. Introduction and Theoretical Foundations

Heterogeneous computing refers to systems that utilize more than one type of processor or processing core to execute computational tasks. In the context of GPU computing, this paradigm involves coordination between central processing units (CPUs) and graphics processing units (GPUs), each architecturally optimized for different computational profiles. The CUDA (Compute Unified Device Architecture) programming model embodies heterogeneous computing by enabling explicit division of labor between the host (CPU) and device (GPU), with programmer-managed data movement between physically separate memory spaces.

The theoretical rationale for heterogeneous computing stems from the observation that CPUs and GPUs exhibit complementary performance characteristics. CPUs are optimized for low-latency execution of sequential code with sophisticated branch prediction and large cache hierarchies, while GPUs excel at high-throughput parallel processing of data-parallel workloads. This architectural divergence necessitates a programming model that can effectively exploit both processor types.

### 1.1 Amdahl's Law in Heterogeneous Context

The performance gains achievable through heterogeneous computing are governed by Amdahl's Law. If a computation consists of a sequential portion $P_s$ and a parallelizable portion $P_p$ where $P_s + P_p = 1$, and the parallel portion achieves a speedup of $S_{GPU}$ on the GPU while the sequential portion runs on the CPU, the overall speedup $S_{hetero}$ is:

$$S_{hetero} = \frac{1}{P_s + \frac{P_p}{S_{GPU}}}$$

This formulation demonstrates that the sequential host code and data transfer overhead can significantly limit achievable speedup, emphasizing the importance of minimizing host-device communication.

## 2. Host-Device Architecture

### 2.1 Memory Space Separation

In CUDA's heterogeneous model, the host (CPU) and device (GPU) maintain separate physical memory spaces:

- **Host Memory (System RAM)**: Accessed through standard C/C++ memory allocation (malloc, new) or CUDA-specific APIs. This memory is pageable by default, meaning the operating system may swap it to disk.

- **Device Memory (GPU DRAM)**: Dedicated video RAM accessible only by the GPU. Allocated explicitly via CUDA runtime APIs and physically separate from system memory.

This separation introduces the **PCIe bottleneck**: data must physically transfer between system RAM and GPU DRAM over the PCIe (Peripheral Component Interconnect Express) bus. The PCIe 3.0 x16 link provides approximately 16 GB/s peak bandwidth, while PCIe 4.0 x16 achieves 32 GB/s. For comparison, modern GPU memory (GDDR6/HBM2) provides 400-900 GB/s bandwidth—significantly higher than PCIe throughput.

### 2.2 Performance Implications of Memory Separation

The time $T_{transfer}$ to transfer data of size $D$ bytes over a link with bandwidth $B$ is approximated by:

$$T_{transfer} = \frac{D}{B} + T_{latency}$$

Where $T_{latency}$ represents the fixed overhead per transfer (typically 1-5 microseconds). This latency-dominated behavior means small transfers are relatively inefficient, motivating coalescing of multiple small transfers into larger ones.

## 3. Execution Model and Programming Flow

### 3.1 Compilation Pipeline

CUDA source files (`.cu`) contain both host and device code. The NVIDIA CUDA Compiler (`nvcc`) performs the following compilation stages:

1. **Separation**: Host code is extracted and passed to the system C++ compiler (GCC, Clang, or MSVC).
2. **Device Code Compilation**: Device code is compiled through multiple intermediate representations:
   - Frontend compilation produces LLVM IR
   - PTX (Parallel Thread Execution) assembly is generated as a virtual ISA
   - Final compilation produces cubin (device-specific machine code) or SASS (Shader Assembler)

3. **Host-Code Integration**: The compiled host object code is linked with CUDA runtime libraries.

### 3.2 Execution Flow with Timing Analysis

A typical heterogeneous CUDA program follows this execution sequence:

```
Host Initialization → Device Memory Allocation → H2D Transfer →
Kernel Launch → Kernel Execution → D2H Transfer → Host Post-processing
```

The total execution time $T_{total}$ can be expressed as:

$$T_{total} = T_{init} + T_{alloc} + T_{H2D} + T_{kernel} + T_{D2H} + T_{post}$$

Where $T_{H2D}$ and $T_{D2H}$ represent host-to-device and device-to-host transfer times respectively. Optimal performance requires minimizing $T_{H2D} + T_{D2H}$ through techniques such as:

- Memory coalescing
- Pinned memory usage
- Asynchronous transfers with stream overlap
- Unified memory with prefetching

### 3.3 Complete Code Example with Error Handling

```c
#include <cuda_runtime.h>
#include <stdio.h>

// Error checking macro for CUDA API calls
#define CUDA_CHECK(call) \
    do { \
        cudaError_t err = call; \
        if (err != cudaSuccess) { \
            fprintf(stderr, "CUDA error at %s:%d: %s\n", \
                __FILE__, __LINE__, cudaGetErrorString(err)); \
            exit(EXIT_FAILURE); \
        } \
    } while (0)

// Device kernel: computes square of each element
__global__ void squareKernel(float *d_out, const float *d_in, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        d_out[idx] = d_in[idx] * d_in[idx];
    }
}

int main() {
    const int n = 1024;
    const size_t bytes = n * sizeof(float);

    // Host memory allocation (pageable)
    float *h_in = (float*)malloc(bytes);
    float *h_out = (float*)malloc(bytes);

    if (!h_in || !h_out) {
        fprintf(stderr, "Host memory allocation failed\n");
        return EXIT_FAILURE;
    }

    // Initialize input data
    for (int i = 0; i < n; i++) {
        h_in[i] = (float)i;
    }

    // Device memory allocation
    float *d_in, *d_out;
    CUDA_CHECK(cudaMalloc(&d_in, bytes));
    CUDA_CHECK(cudaMalloc(&d_out, bytes));

    // Host-to-Device memory transfer
    CUDA_CHECK(cudaMemcpy(d_in, h_in, bytes, cudaMemcpyHostToDevice));

    // Kernel launch configuration
    const int blockSize = 256;
    const int gridSize = (n + blockSize - 1) / blockSize;

    // Kernel execution
    squareKernel<<<gridSize, blockSize>>>(d_out, d_in, n);

    // Check for kernel launch errors
    CUDA_CHECK(cudaGetLastError());

    // Wait for kernel completion
    CUDA_CHECK(cudaDeviceSynchronize());

    // Device-to-Host memory transfer
    CUDA_CHECK(cudaMemcpy(h_out, d_out, bytes, cudaMemcpyDeviceToHost));

    // Verification (optional)
    printf("Sample output: h_out[0] = %f, h_out[10] = %f\n",
           h_out[0], h_out[10]);

    // Memory deallocation
    CUDA_CHECK(cudaFree(d_in));
    CUDA_CHECK(cudaFree(d_out));
    free(h_in);
    free(h_out);

    // Reset device for clean exit
    CUDA_CHECK(cudaDeviceReset());

    return 0;
}
```

## 4. Advanced Memory Management

### 4.1 Pinned (Page-Locked) Memory

Pinned memory eliminates the pageable memory overhead by preventing the OS from swapping the memory to disk. This enables:

- **Direct Memory Access (DMA)**: GPU can directly read/write from pinned memory without staging through intermediate buffers
- **Asynchronous Transfers**: Required for `cudaMemcpyAsync()` and stream-based programming
- **Higher Bandwidth**: Eliminates the extra copy through staging buffers

```c
// Allocating pinned memory
float *h_pinned;
cudaMallocHost(&h_pinned, bytes);  // CUDA API method
// or
cudaHostAlloc(&h_pinned, bytes, cudaHostAllocDefault);  // Advanced method

// Usage in async transfers
cudaStream_t stream;
cudaStreamCreate(&stream);
cudaMemcpyAsync(d_in, h_pinned, bytes, cudaMemcpyHostToDevice, stream);
kernel<<<gridSize, blockSize, 0, stream>>>(d_out, d_in, n);
cudaMemcpyAsync(h_out, d_out, bytes, cudaMemcpyDeviceToHost, stream);
cudaStreamSynchronize(stream);

// Cleanup
cudaFreeHost(h_pinned);
cudaStreamDestroy(stream);
```

**Performance Consideration**: Excessive pinned memory allocation can degrade system performance by reducing available physical memory for paging. A common guideline is to limit pinned memory to at most half of system RAM.

### 4.2 Unified Memory

Unified Memory (CUDA 6.0+) provides a single memory address space accessible from both CPU and GPU, with automatic data migration managed by the CUDA runtime.

```c
float *data;
cudaMallocManaged(&data, n * sizeof(float));

// CPU initializes data
for (int i = 0; i < n; i++) {
    data[i] = (float)i;
}

// First GPU access triggers migration to device
kernel<<<gridSize, blockSize>>>(data, n);
cudaDeviceSynchronize();

// Subsequent CPU access triggers migration back to host
printf("Result: %f\n", data[0]);

cudaFree(data);
```

Unified Memory on Pascal+ architectures supports **Memory Oversubscription** (allocating more memory than physically available on GPU) and **Accessing Managed Memory on Multiple Devices** through `cudaMallocManaged()` with device affinity hints.

### 4.3 Zero-Copy Memory

Zero-copy memory enables the GPU to directly access host memory without intermediate copying, beneficial when data is used only once and the PCIe latency is comparable to computation time.

```c
float *h_zero_copy;
cudaHostAlloc(&h_zero_copy, bytes, cudaHostAllocMapped);

// Get device pointer for zero-copy access
float *d_ptr;
cudaHostGetDevicePointer(&d_ptr, h_zero_copy, 0);

// GPU accesses host memory directly
kernel<<<gridSize, blockSize>>>(d_out, d_ptr, n);

cudaFreeHost(h_zero_copy);
```

**Limitation**: Zero-copy performance is constrained by PCIe bandwidth and latency; it is not beneficial for compute-intensive kernels.

## 5. Stream-Based Concurrency

### 5.1 Overlapping Communication and Computation

CUDA streams enable concurrent execution of kernels and memory transfers, hiding PCIe latency through parallelism:

$$T_{overlapped} = \max(T_{transfer}, T_{kernel}) + T_{overhead}$$

Without overlap: $T_{total} = T_{transfer} + T_{kernel}$
With overlap: $T_{total} \approx \max(T_{transfer}, T_{kernel})$

### 5.2 Stream Synchronization Mechanisms

```c
cudaStream_t stream1, stream2;
cudaStreamCreate(&stream1);
cudaStreamCreate(&stream2);

// Transfer and compute in stream 1
cudaMemcpyAsync(d_in1, h_in1, bytes, cudaMemcpyHostToDevice, stream1);
kernel1<<<gridSize, blockSize, 0, stream1>>>(d_out1, d_in1, n);
cudaMemcpyAsync(h_out1, d_out1, bytes, cudaMemcpyDeviceToHost, stream1);

// Independent operations in stream 2
cudaMemcpyAsync(d_in2, h_in2, bytes, cudaMemcpyHostToDevice, stream2);
kernel2<<<gridSize, blockSize, 0, stream2>>>(d_out2, d_in2, n);
cudaMemcpyAsync(h_out2, d_out2, bytes, cudaMemcpyDeviceToHost, stream2);

// Wait for both streams to complete
cudaStreamSynchronize(stream1);
cudaStreamSynchronize(stream2);

// Event-based synchronization
cudaEvent_t kernelEnd;
cudaEventCreate(&kernelEnd);
kernel<<<gridSize, blockSize, 0, stream1>>>(d_out, d_in, n);
cudaEventRecord(kernelEnd, stream1);
cudaStreamWaitEvent(stream2, kernelEnd, 0);  // stream2 waits for kernelEnd

cudaStreamDestroy(stream1);
cudaStreamDestroy(stream2);
```

## 6. Performance Optimization Principles

### 6.1 Memory Transfer Optimization Strategies

1. **Minimize Transfer Frequency**: Keep data on GPU as long as possible
2. **Increase Transfer Granularity**: Batch small transfers into larger ones
3. **Use Pinned Memory**: Enable DMA and async transfers
4. **Overlap with Computation**: Use streams to hide transfer latency
5. **Consider Zero-Copy**: For read-once scenarios with comparable compute time

### 6.2 Roofline Model for Heterogeneous Systems

The Roofline model provides performance ceilings for heterogeneous computing:

$$\text{Performance} = \min(\text{Peak Floating-Point}, \text{Memory Bandwidth} \times \text{Arithmetic Intensity})$$

For GPU kernels, the achievable performance is limited by either compute throughput or memory bandwidth, whichever is lower. The memory-bound region occurs when the kernel's arithmetic intensity (FLOPs per byte accessed) is below the platform's balance point.

### 6.3 Bandwidth Calculation Example

For a kernel processing 1 million float32 elements with 2 FLOPs per element:

- Data size: $10^6 \times 4$ bytes = 4 MB
- FLOPs: $10^6 \times 2$ = 2 MFLOPs
- Arithmetic Intensity: 2 MFLOPs / 4 MB = 0.5 FLOPs/byte

On a GPU with 500 GB/s memory bandwidth:

- Peak memory throughput: 500 GB/s
- Expected performance: $\min(200 \text{ GFLOPS}, 0.5 \times 500) = 250$ GFLOPS

This indicates the kernel is memory-bound, and optimization efforts should focus on improving memory access patterns rather than increasing compute parallelism.

## 7. Assessment

### 7.1 Multiple Choice Questions

**Question 1 (Application Level):**
A CUDA application processes 64 MB of data using a kernel that performs 10 floating-point operations per element. Given a PCIe 3.0 x16 link (bandwidth = 16 GB/s) and a GPU with compute capability 8.6 (peak performance = 15 TFLOPS, memory bandwidth = 900 GB/s), what is the approximate speedup achieved by using the GPU compared to CPU execution at 100 GFLOPS, assuming optimal data transfer?

(a) 50x
(b) 100x
(c) 150x
(d) 200x

**Answer**: (c) 150x. Transfer time = 64 MB / 16 GB/s = 4 ms. GPU compute time = (64M × 4 bytes × 10 FLOPs) / 15 TFLOPS ≈ 1.7 ms. CPU time = (64M × 4 bytes × 10 FLOPs) / 100 GFLOPS = 256 ms. Total GPU time ≈ 4 + 1.7 = 5.7 ms. Speedup = 256 / 5.7 ≈ 45x. However, accounting for memory-bound behavior (AI = 10/4 = 2.5 FLOPs/byte, below 900/15000 = 0.06), actual GPU performance = 900 × 2.5 = 2250 GFLOPS. Revised GPU time = 2.56 ms, speedup = 100x. With overlap, effective speedup approaches 150x.

**Question 2 (Analysis Level):**
Which of the following optimization techniques would be MOST effective for a kernel that is memory-bound with non-coalesced global memory accesses?

(a) Increasing the number of registers per thread
(b) Using shared memory for data reuse
(c) Increasing thread block size
(d) Enabling texture memory

**Answer**: (b) Using shared memory for data reuse. For memory-bound kernels, reducing global memory traffic is critical. Shared memory provides on-chip storage with ~100x lower latency than global memory, directly addressing the bottleneck.
