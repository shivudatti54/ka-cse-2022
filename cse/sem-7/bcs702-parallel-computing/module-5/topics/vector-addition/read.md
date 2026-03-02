# CUDA Vector Addition

## Introduction

Vector addition serves as the canonical introductory CUDA program, functioning as the "Hello World" of GPU computing. Given two input arrays `a` and `b` of length `n`, the objective is to compute a result array `c` where each element satisfies `c[i] = a[i] + b[i]`. Although the computational task is trivial, this program encapsulates the complete host-device programming paradigm that underlies all CUDA applications. The workflow encompasses: device memory allocation, host-to-device data transfer, kernel launch configuration, parallel kernel execution, and result retrieval back to the host memory space.

As articulated in Pacheco's _An Introduction to Parallel Programming_, vector addition provides an ideal vehicle for illustrating CUDA's fundamental programming structure without introducing the complexities inherent in reduction operations, shared memory utilization, or explicit synchronization mechanisms. Proficiency in this foundational pattern constitutes a prerequisite for all subsequent CUDA programming endeavors.

## The Host-Device Programming Model

CUDA adopts a heterogeneous computing model wherein the **host** (CPU) and the **device** (GPU) maintain separate physical memory spaces with distinct address domains. This architectural separation necessitates explicit memory management operations that would be unnecessary in homogeneous parallel computing environments. The host code orchestrates the entire computation through a well-defined sequence of operations:

1. **Memory Allocation**: Allocate buffers on both host (using malloc) and device (using cudaMalloc)
2. **Data Initialization**: Populate host arrays with input data
3. **Data Transfer**: Copy input arrays from host memory to device global memory
4. **Kernel Launch**: Configure and invoke the compute kernel with appropriate thread hierarchy
5. **Result Retrieval**: Copy the output array from device memory back to host memory
6. **Resource Cleanup**: Release all allocated device memory via cudaFree

The device kernel executes in parallel across thousands of lightweight threads, with each thread typically computing one element of the output array. This massive parallelism leverages the GPU's throughput-oriented architecture designed for data-parallel workloads.

```
Host (CPU)                           Device (GPU)
+------------------+               +------------------+
| float *h_a, *h_b |  cudaMemcpy   | float *d_a, *d_b |
| float *h_c       |  ==========>  | float *d_c       |
|                  |  H -> D       |                  |
| allocate arrays  |               | kernel executes  |
| initialize data  |  cudaMemcpy   | c[i] = a[i]+b[i] |
| launch kernel    |  <==========  |                  |
| read results     |  D -> H       |                  |
+------------------+               +------------------+
```

## Step 1: Device Memory Allocation with cudaMalloc

The GPU possesses dedicated global memory distinct from the host's system RAM. Consequently, developers must explicitly allocate storage for each array on the device prior to kernel execution. The `cudaMalloc` function parallels the semantics of standard C's `malloc`, though it performs allocation within device global memory.

### Function Signature

```c
cudaError_t cudaMalloc(void **devPtr, size_t size);
```

**Parameters:**

- `devPtr`: Pointer to the allocated device memory pointer (passed by reference)
- `size`: Number of bytes to allocate
- **Returns**: `cudaSuccess` on successful allocation; otherwise returns an error code

### Usage Pattern for Vector Addition

```c
float *d_a, *d_b, *d_c;
int n = 1000000;
size_t bytes = n * sizeof(float);

// Allocate device memory for three arrays
cudaMalloc((void **)&d_a, bytes);
cudaMalloc((void **)&d_b, bytes);
cudaMalloc((void **)&d_c, bytes);
```

Following these allocations, `d_a`, `d_b`, and `d_c` reference GPU memory buffers. Critically, host code cannot directly dereference these pointers—attempting to read from or write to these addresses from the CPU will result in undefined behavior. All device memory access must occur through explicit CUDA runtime functions.

## Step 2: Host-Device Data Transfer with cudaMemcpy

Given the separate memory spaces, data movement must be performed explicitly using the `cudaMemcpy` function, which handles copying between the distinct address domains.

### Function Signature

```c
cudaError_t cudaMemcpy(void *dst, const void *src, size_t count,
                       cudaMemcpyKind kind);
```

**Parameters:**

- `dst`: Destination buffer pointer
- `src`: Source buffer pointer
- `count`: Number of bytes to transfer
- `kind`: Direction of data movement

### Transfer Direction Enumeration

| Constant                   | Description                             |
| -------------------------- | --------------------------------------- |
| `cudaMemcpyHostToDevice`   | Transfer from host to device (upload)   |
| `cudaMemcpyDeviceToHost`   | Transfer from device to host (download) |
| `cudaMemcpyDeviceToDevice` | Transfer within device memory           |
| `cudaMemcpyHostToHost`     | Transfer within host memory             |

### Transferring Input Data to Device

```c
// Copy input arrays from host to device
cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
cudaMemcpy(d_b, h_b, bytes, cudaMemcpyHostToDevice);
```

### Retrieving Results to Host

```c
// Copy result array from device back to host
cudaMemcpy(h_c, d_c, bytes, cudaMemcpyDeviceToHost);
```

Note that `cudaMemcpy` operates **synchronously** by default—the calling thread blocks until the transfer completes. Asynchronous variants (`cudaMemcpyAsync`) exist for overlapping computation with data transfer using streams.

## Step 3: Kernel Definition and Execution

A CUDA **kernel** constitutes a function that executes on the GPU, with one thread instance launched per specified array element. Kernels are decorated with the `__global__` qualifier to indicate device execution with host invocation capability.

### Kernel Implementation for Vector Addition

```c
__global__ void vecAdd(float *a, float *b, float *c, int n) {
    // Compute global thread index
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    // Boundary check: ensure thread processes valid array element
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}
```

### CUDA Function Qualifiers

| Qualifier    | Execution Location | Invocation Location                       |
| ------------ | ------------------ | ----------------------------------------- |
| `__global__` | Device             | Host (or device with dynamic parallelism) |
| `__device__` | Device             | Device only                               |
| `__host__`   | Host               | Host only                                 |

The kernel must return `void` and cannot be called like standard C functions—it requires launch configuration via the `<<<gridSize, blockSize>>>` syntax.

## Step 4: Thread Hierarchy and Index Computation

Each thread must uniquely identify which array element it processes. The global thread index in a 1D grid configuration derives from block and thread identifiers:

```c
int i = blockIdx.x * blockDim.x + threadIdx.x;
```

### Index Calculation Derivation

Given a launch configuration of 3 blocks with 4 threads per block:

- **Block 0**: threadIdx.x ∈ {0,1,2,3} → global indices = 0, 1, 2, 3
- **Block 1**: threadIdx.x ∈ {0,1,2,3} → global indices = 4, 5, 6, 7
- **Block 2**: threadIdx.x ∈ {0,1,2,3} → global indices = 8, 9, 10, 11

### Built-in Variables

- `threadIdx.x`: Index of thread within its block (0 to blockDim.x - 1)
- `blockIdx.x`: Index of block within the grid (0 to gridDim.x - 1)
- `blockDim.x`: Number of threads per block (compile-time constant)
- `gridDim.x`: Number of blocks in the grid

## Step 5: Kernel Launch Configuration

The kernel launch syntax specifies the thread hierarchy using angle brackets:

```c
// Define launch parameters
int blockSize = 256;
int gridSize = (n + blockSize - 1) / blockSize;  // Ceiling division

// Launch kernel with gridSize blocks and blockSize threads per block
vecAdd<<<gridSize, blockSize>>>(d_a, d_b, d_c, n);
```

The grid size calculation ensures sufficient threads to cover all array elements through ceiling division.

## Step 6: Memory Deallocation

Device memory must be explicitly released when no longer needed:

```c
cudaFree(d_a);
cudaFree(d_b);
cudaFree(d_c);
```

## Complete Vector Addition Program

```c
#include <stdio.h>
#include <cuda.h>

__global__ void vecAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 1000000;
    size_t bytes = n * sizeof(float);

    // Host memory allocation and initialization
    float *h_a = (float*)malloc(bytes);
    float *h_b = (float*)malloc(bytes);
    float *h_c = (float*)malloc(bytes);

    for (int i = 0; i < n; i++) {
        h_a[i] = 1.0f;
        h_b[i] = 2.0f;
    }

    // Device memory allocation
    float *d_a, *d_b, *d_c;
    cudaMalloc((void**)&d_a, bytes);
    cudaMalloc((void**)&d_b, bytes);
    cudaMalloc((void**)&d_c, bytes);

    // Data transfer: Host to Device
    cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, bytes, cudaMemcpyHostToDevice);

    // Kernel launch
    int blockSize = 256;
    int gridSize = (n + blockSize - 1) / blockSize;
    vecAdd<<<gridSize, blockSize>>>(d_a, d_b, d_c, n);

    // Data transfer: Device to Host
    cudaMemcpy(h_c, d_c, bytes, cudaMemcpyDeviceToHost);

    // Verify result (first element should be 3.0)
    printf("c[0] = %f\n", h_c[0]);

    // Cleanup
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    free(h_a);
    free(h_b);
    free(h_c);

    return 0;
}
```

## Performance Considerations

### Memory Coalescing

For optimal memory bandwidth, consecutive threads should access consecutive memory addresses. The vector addition kernel naturally achieves coalesced accesses since thread `i` reads `a[i]` and `b[i]`—adjacent threads access adjacent memory locations.

### Occupancy and Block Size

The choice of `blockSize` affects GPU occupancy (ratio of active warps to maximum warps). Common block sizes include 128, 256, and 512 threads, with 256 representing a good default for compute capability 2.0 and above. Warp size is 32 threads, so block sizes should be multiples of 32 for optimal efficiency.

### Throughput Estimation

For vector addition on a GPU with memory bandwidth `B` GB/s, the theoretical maximum throughput equals `B / (3 × sizeof(float))` elements per second, since each output element requires reading two inputs and writing one output (3 × 4 = 12 bytes per element).

## Error Handling

All CUDA API functions return a `cudaError_t` status that should be checked:

```c
cudaError_t err = cudaMalloc((void**)&d_a, bytes);
if (err != cudaSuccess) {
    fprintf(stderr, "cudaMalloc failed: %s\n", cudaGetErrorString(err));
    exit(EXIT_FAILURE);
}
```

Kernel launch errors are captured via `cudaGetLastError()` immediately after the kernel invocation.
