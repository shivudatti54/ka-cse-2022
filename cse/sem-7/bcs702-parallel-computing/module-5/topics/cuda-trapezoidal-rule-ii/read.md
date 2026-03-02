# CUDA Trapezoidal Rule: Shared Memory Reduction Implementation

## 1. Introduction

The trapezoidal rule constitutes a foundational numerical integration technique that approximates definite integrals by partitioning the integration domain into discrete subintervals and approximating the area under the curve through trapezoidal geometries. When implemented using NVIDIA's Compute Unified Device Architecture (CUDA), this algorithm exemplifies an embarrassingly parallel computation where thousands of concurrent threads can independently evaluate the integrand at distinct spatial coordinates, thereby achieving substantial acceleration relative to sequential CPU implementations.

This document presents a comprehensive examination of the CUDA implementation employing shared memory reduction, analyzing both the theoretical foundations and practical considerations for optimal GPU utilization.

## 2. Mathematical Foundation

### 2.1 Trapezoidal Rule Formulation

Given a continuous function f(x) defined on the closed interval [a, b], the definite integral I = ∫[a,b] f(x) dx is approximated by dividing the interval into n equal subintervals of width h = (b - a)/n. The trapezoidal approximation takes the form:

$$I_n = \frac{h}{2} \left[ f(x_0) + 2\sum_{i=1}^{n-1} f(x_i) + f(x_n) \right]$$

where x_i = a + ih for i = 0, 1, 2, ..., n.

### 2.2 Error Analysis and Convergence

**Theorem (Trapezoidal Rule Error Bound)**: If f''(x) is continuous on [a, b], then the error E_T in the trapezoidal approximation satisfies:

$$|E_T| = \left| \int_a^b f(x)dx - I_n \right| \leq \frac{(b-a)^3}{12n^2} \max_{x \in [a,b]} |f''(x)|$$

**Proof**: Consider the error on a single subinterval [x_i, x_{i+1}] of width h. Define g(x) as the linear interpolation of f(x) at the endpoints:

$$g(x) = f(x_i) + \frac{f(x_{i+1}) - f(x_i)}{h}(x - x_i)$$

Using Taylor's theorem with remainder about x_i + h/2:

$$f(x) = f\left(x_i + \frac{h}{2}\right) + f'\left(x_i + \frac{h}{2}\right)\left(x - x_i - \frac{h}{2}\right) + \frac{f''(\xi)}{2}\left(x - x_i - \frac{h}{2}\right)^2$$

Integrating and simplifying, the error on each subinterval is:

$$E_i = \int_{x_i}^{x_{i+1}} [f(x) - g(x)]dx = -\frac{h^3}{12}f''(\xi_i)$$

Summing over all n subintervals:

$$E_T = \sum_{i=0}^{n-1} E_i = -\frac{h^3}{12}\sum_{i=0}^{n-1} f''(\xi_i)$$

By the intermediate value property and continuity of f'':

$$|E_T| \leq \frac{n h^3}{12} \max_{x \in [a,b]} |f''(x)| = \frac{(b-a)^3}{12n^2} \max_{x \in [a,b]} |f''(x)| \blacksquare$$

This error bound demonstrates second-order convergence: halving the step size h reduces the error by a factor of four, making the trapezoidal rule particularly efficient for smooth integrands.

## 3. Parallelization Strategy on GPU Architecture

### 3.1 Why GPUs Excel at Trapezoidal Integration

The trapezoidal rule possesses characteristics that align optimally with GPU parallel execution models:

1. **Instruction-Level Independence**: Each function evaluation f(x_i) depends solely on its corresponding x_i coordinate, requiring no inter-thread communication during the evaluation phase.

2. **Scalability to Massive Thread Counts**: Contemporary GPUs support concurrent execution of millions of threads. For numerical integration, employing n = 10^6 to 10^8 subintervals directly maps to equivalent thread counts.

3. **Uniform Computational Workload**: All threads execute identical instruction sequences, ensuring optimal SIMD (Single Instruction Multiple Data) utilization and eliminating divergent execution paths.

4. **Minimal Data Transfer**: The algorithm produces a single scalar result, minimizing PCIe bandwidth constraints between device and host memory.

### 3.2 Thread Hierarchy Mapping

CUDA organizes threads into a two-level hierarchy: grids containing blocks, each block comprising multiple threads. For the trapezoidal kernel:

- **Grid Dimension**: ⌈(n+1)/threadsPerBlock⌉ blocks
- **Block Dimension**: threadsPerBlock threads (typically 256 or 512)
- **Global Thread Index**: i = threadIdx.x + blockIdx.x × blockDim.x

The index i directly corresponds to the subinterval position x_i = a + ih, enabling straightforward parallelization.

## 4. CUDA Kernel Implementation with Shared Memory Reduction

### 4.1 Kernel Design Rationale

The implementation employs a two-phase reduction strategy:

**Phase 1 (Device)**: Each block independently reduces its assigned partial sums using shared memory, producing one partial sum per block.

**Phase 2 (Host)**: The host aggregates block-level partial sums to compute the final integral.

This hierarchical approach balances computation intensity with memory bandwidth efficiency.

### 4.2 Complete Kernel Implementation

```cuda
__device__ double f(double x) {
    return x * x;  // Example: f(x) = x²
}

__global__ void trapezoidalKernel(double a, double h, int n, double* partialSums) {
    // Shared memory for intra-block reduction
    extern __shared__ double sdata[];

    int tid = threadIdx.x;
    int i = threadIdx.x + blockIdx.x * blockDim.x;

    // Phase 1: Compute individual thread contributions
    double mySum = 0.0;
    if (i <= n) {
        double x_i = a + i * h;
        mySum = f(x_i);

        // Apply half-weight to boundary points (i=0 and i=n)
        if (i == 0 || i == n) {
            mySum *= 0.5;
        }
    }

    // Store result in shared memory
    sdata[tid] = mySum;
    __syncthreads();

    // Phase 2: Parallel reduction within block
    // Tree-based reduction: stride halves each iteration
    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] += sdata[tid + s];
        }
        __syncthreads();
    }

    // Thread 0 writes block result to global memory
    if (tid == 0) {
        partialSums[blockIdx.x] = sdata[0];
    }
}
```

### 4.3 Parallel Reduction Algorithm Analysis

The reduction algorithm employs a tree-based summation strategy requiring ⌈log₂(blockDim.x)⌉ iterations. For blockDim.x = 256:

| Iteration | Active Threads | Stride | Operation                                             |
| --------- | -------------- | ------ | ----------------------------------------------------- |
| 1         | 128            | 128    | sdata[0] += sdata[128], ..., sdata[127] += sdata[255] |
| 2         | 64             | 64     | sdata[0] += sdata[64], ...                            |
| 3         | 32             | 32     | sdata[0] += sdata[32], ...                            |
| 4         | 16             | 16     | sdata[0] += sdata[16], ...                            |
| 5         | 8              | 8      | sdata[0] += sdata[8], ...                             |
| 6         | 4              | 4      | sdata[0] += sdata[4], ...                             |
| 7         | 2              | 2      | sdata[0] += sdata[2], ...                             |
| 8         | 1              | 1      | sdata[0] += sdata[1]                                  |

**Correctness Proof**: By induction on the iteration number, after k iterations, sdata[0] contains the sum of all elements whose original indices differ by at most blockDim.x/2^k. After ⌈log₂(blockDim.x)⌉ iterations, all elements are aggregated in sdata[0].

### 4.4 Host Code and Memory Management

```cuda
#include <stdio.h>
#include <cuda_runtime.h>

#define CUDA_CHECK(call) \
    do { \
        cudaError_t err = call; \
        if (err != cudaSuccess) { \
            fprintf(stderr, "CUDA error at %s:%d: %s\n", \
                __FILE__, __LINE__, cudaGetErrorString(err)); \
            exit(EXIT_FAILURE); \
        } \
    } while(0)

int main() {
    // Integration parameters
    double a = 0.0, b = 1.0;
    int n = 1000000;  // Number of subintervals
    double h = (b - a) / n;

    // Thread configuration
    int threadsPerBlock = 256;
    int numBlocks = (n + 1 + threadsPerBlock - 1) / threadsPerBlock;

    // Device memory allocation for block partial sums
    double* d_partialSums;
    CUDA_CHECK(cudaMalloc(&d_partialSums, numBlocks * sizeof(double)));

    // Shared memory size: one double per thread
    int sharedMemSize = threadsPerBlock * sizeof(double);

    // Kernel launch
    trapezoidalKernel<<<numBlocks, threadsPerBlock, sharedMemSize>>>(
        a, h, n, d_partialSums);

    // Copy results back to host
    double* h_partialSums = (double*)malloc(numBlocks * sizeof(double));
    CUDA_CHECK(cudaMemcpy(h_partialSums, d_partialSums,
                numBlocks * sizeof(double), cudaMemcpyDeviceToHost));

    // Final aggregation on host
    double integral = 0.0;
    for (int i = 0; i < numBlocks; i++) {
        integral += h_partialSums[i];
    }
    integral *= h;  // Multiply by step size

    printf("Integral approximation: %.15f\n", integral);
    printf("Exact value (∫₀¹ x² dx): %.15f\n", 1.0/3.0);
    printf("Absolute error: %.15e\n", fabs(integral - 1.0/3.0));

    // Memory cleanup
    CUDA_CHECK(cudaFree(d_partialSums));
    free(h_partialSums);

    return 0;
}
```

## 5. Performance Analysis

### 5.1 Occupancy Calculations

Occupancy, defined as the ratio of active warps to maximum warps per streaming multiprocessor (SM), critically impacts kernel performance. For our configuration:

- **Registers per thread**: ~10 (mySum, x_i, tid, i)
- **Shared memory per block**: 256 × 8 bytes = 2 KB
- **Maximum blocks per SM**: Limited by shared memory (48 KB / 2 KB = 24) and registers

For an NVIDIA Ampere GPU with 16384 registers/SM and 48 KB shared memory/SM:

$$\text{Block occupancy} = \min\left(\frac{16384}{10 \times 256}, \frac{48000}{2048}, \text{maxBlocks}\right) = \min(6.4, 23, 16) = 6$$

$$\text{Warp occupancy} = \frac{6 \times 32}{64} = 50\%$$

### 5.2 Memory Access Optimization

The implementation achieves efficient memory utilization through:

1. **Coalesced Global Memory Access**: Threads within a warp access consecutive global memory addresses (partialSums[blockIdx.x]), enabling memory coalescing.

2. **Shared Memory Bandwidth**: Shared memory provides ~10× higher bandwidth than global memory, reducing memory latency during reduction.

3. **Register Utilization**: Frequently accessed variables (tid, i, mySum) reside in registers, avoiding shared memory thrashing.

### 5.3 Theoretical Speedup Estimation

For a CPU implementation with sequential reduction:

$$T_{CPU} = O(n) \text{ operations}$$

For the CUDA implementation:

$$T_{GPU} = O\left(\frac{n}{\text{threads}}\right) + O(\text{blocks} \times \log(\text{threads}))$$

With n = 10^6, threads = 256, and assuming 1000× bandwidth advantage:

$$\text{Speedup} \approx \frac{10^6}{3907} \times 1000 \approx 256\times$$

Actual speedups typically range from 50× to 500× depending on GPU architecture and integration function complexity.

## 6. Alternative Implementation: Atomic Operations

For comparison, a simpler atomic-based kernel:

```cuda
__global__ void trapezoidalAtomic(double a, double h, int n, double* result) {
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    if (i <= n) {
        double x_i = a + i * h;
        double val = f(x_i);
        if (i == 0 || i == n) val *= 0.5;
        atomicAdd(result, val);
    }
}
```

**Performance Trade-off**: While conceptually simpler, atomicAdd introduces serialization as threads contend for write access to result. This reduces effective parallelism, typically yielding 2-5× slower performance than shared memory reduction for large n.

## 7. Summary

This implementation demonstrates fundamental GPU computing principles:

- Thread-to-data mapping via global indices
- Shared memory reduction for intra-block aggregation
- Hierarchical parallelism (thread → block → grid)
- Performance optimization through occupancy and memory access analysis

The shared memory reduction approach achieves near-optimal GPU utilization for the trapezoidal rule, providing substantial acceleration over CPU-based sequential integration.
