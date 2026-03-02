# CUDA Trapezoidal Rule I: The Basic atomicAdd Approach

## 1. Theoretical Foundation of the Trapezoidal Rule

The trapezoidal rule approximates the definite integral ∫ₐᵇ f(x)dx by partitioning the interval [a, b] into n equal subintervals of width h = (b-a)/n. The approximation is derived from summing the areas of trapezoids formed between successive function evaluations:

**Theorem (Trapezoidal Rule):** If f ∈ C²[a, b], then

∫ₐᵇ f(x)dx = (h/2)[f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)] - (b-a)h²/12 f''(ξ)

for some ξ ∈ (a, b). The error term O(h²) indicates the method is second-order accurate.

**Proof of Discrete Formulation:** Each subinterval [xᵢ, xᵢ₊₁] contributes area (h/2)[f(xᵢ) + f(xᵢ₊₁)]. Summing over all i from 0 to n-1:

∑\_{i=0}^{n-1} (h/2)[f(xᵢ) + f(xᵢ₊₁)] = (h/2)[f(x₀) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ₋₁) + f(xₙ)]

Each interior point xᵢ (1 ≤ i ≤ n-1) appears exactly twice, while endpoints appear once. ∎

## 2. Parallelization Analysis

### 2.1 Data Dependency Graph

**Definition:** A computation is _embarrassingly parallel_ if it consists of N independent tasks requiring no communication between them.

For the trapezoidal rule, the evaluation of f(xᵢ) for each i ∈ {0, 1, ..., n} is completely independent. The dependency graph is a set of n+1 isolated nodes with no edges—no task requires the output of any other.

**Theorem (Parallel Complexity):** The trapezoidal rule can be computed in O(1) parallel time using n+1 processors, assuming unlimited resources.

**Proof:** Each processor Pᵢ computes f(xᵢ) independently in constant time τ. The final sum requires one reduction operation across n+1 values, which takes O(log n) time using a parallel reduction tree. Thus T_par(n) = O(1) + O(log n) = O(log n). ∎

### 2.2 GPU Mapping Rationale

| Aspect              | Sequential CPU  | GPU Implementation      |
| ------------------- | --------------- | ----------------------- |
| Work per evaluation | O(1)            | O(1) per thread         |
| Total work          | O(n)            | O(n) with n threads     |
| Time complexity     | O(n)            | O(log n) with reduction |
| Memory access       | Sequential      | Coalesced global access |
| Bottleneck          | CPU computation | Memory atomicity        |

The embarrassingly parallel nature stems from the absence of loop-carried dependencies. Each thread computes f(xᵢ) without synchronization, making this an ideal CUDA kernel.

## 3. CUDA Implementation: atomicAdd Approach

### 3.1 Single-Block Kernel (n ≤ 1024)

```cuda
__device__ float f(float x) {
    // Example integrand: f(x) = x²
    // Replace with any function f(x) requiring integration
    return x * x;
}

__global__ void dev_trap_singleblock(float a, float b, int n, float h, float* result_p) {
    // Each thread computes one function evaluation f(xᵢ)
    int my_i = threadIdx.x;

    // Guard condition: prevent out-of-bounds access
    if (my_i <= n) {
        // Map thread index to x-coordinate
        float my_x = a + static_cast<float>(my_i) * h;

        // Evaluate the integrand
        float my_f = f(my_x);

        // Apply trapezoidal weights: endpoints get 0.5 weight
        if (my_i == 0 || my_i == n) {
            my_f *= 0.5f;
        }

        // Atomically accumulate to global result
        atomicAdd(result_p, my_f);
    }
}
```

**Kernel Analysis:**

- **Thread mapping:** One thread per evaluation point xᵢ
- **Boundary handling:** Threads 0 and n (corresponding to a and b) apply 0.5 factor
- **Synchronization:** `atomicAdd` ensures correct accumulation despite concurrent writes

### 3.2 Multi-Block Kernel (General n)

```cuda
__global__ void dev_trap_multiblock(float a, float b, int n, float h, float* result_p) {
    // Compute global thread index across all blocks
    int my_i = blockIdx.x * blockDim.x + threadIdx.x;

    // Boundary check: only valid indices participate
    if (my_i <= n) {
        float my_x = a + static_cast<float>(my_i) * h;
        float my_f = f(my_x);

        // Apply trapezoidal weighting for endpoints
        if (my_i == 0 || my_i == n) {
            my_f *= 0.5f;
        }

        // Accumulate contribution atomically
        atomicAdd(result_p, my_f);
    }
}
```

**Grid Configuration Calculation:**

```cuda
int threadsPerBlock = 256;
// Total points = n + 1; round up to cover all
int numBlocks = (n + 1 + threadsPerBlock - 1) / threadsPerBlock;
```

## 4. Complete Host Code

```cuda
#include <stdio.h>
#include <cuda_runtime.h>

// Device function for integrand
__device__ float f_device(float x) {
    return x * x;  // Integrate x² from 0 to 1 = 1/3
}

__global__ void dev_trap_multiblock(float a, float b, int n, float h, float* result_p) {
    int my_i = blockIdx.x * blockDim.x + threadIdx.x;

    if (my_i <= n) {
        float my_x = a + static_cast<float>(my_i) * h;
        float my_f = f_device(my_x);

        if (my_i == 0 || my_i == n) {
            my_f *= 0.5f;
        }

        atomicAdd(result_p, my_f);
    }
}

int main() {
    // Integration parameters
    float a = 0.0f, b = 1.0f;
    int n = 1024 * 1024;  // 1,048,576 subintervals
    float h = (b - a) / n;

    // Device memory allocation
    float* d_result;
    cudaMalloc(&d_result, sizeof(float));
    cudaMemset(d_result, 0, sizeof(float));

    // Kernel launch configuration
    int threadsPerBlock = 256;
    int numBlocks = (n + 1 + threadsPerBlock - 1) / threadsPerBlock;

    // Execute kernel
    dev_trap_multiblock<<<numBlocks, threadsPerBlock>>>(a, b, n, h, d_result);

    // Copy result back to host
    float h_result;
    cudaMemcpy(&h_result, d_result, sizeof(float), cudaMemcpyDeviceToHost);

    // Final multiplication by step size
    float integral = h * h_result;

    printf("Numerical integral: %.15f\n", integral);
    printf("Exact integral:     %.15f\n", 1.0f/3.0f);
    printf("Absolute error:    %.15e\n", fabsf(integral - 1.0f/3.0f));

    // Cleanup
    cudaFree(d_result);
    return cudaDeviceSynchronize();
}
```

## 5. Performance Analysis

### 5.1 Atomic Operation Semantics

`atomicAdd(float* address, float value)` performs:

```
old = *address;
while (!CAS(address, old, old + value)) {
    old = *address;
}
```

The Compare-And-Swap (CAS) loop retry mechanism ensures correctness but introduces severe performance penalties.

### 5.2 Performance Modeling

**Theorem (Atomic Serialization):** When p threads concurrently execute atomicAdd to the same address, the time complexity of the accumulation phase is O(p) rather than O(1).

**Proof:** Each atomicAdd requires exclusive access to the memory location. The hardware implements this through sequentialization—only one thread can complete the read-modify-write cycle at a time. With p threads contending for a single location, the effective time scales linearly with p. ∎

### 5.3 Bottleneck Analysis

| Phase               | Ideal Parallel Time            | Actual with atomicAdd |
| ------------------- | ------------------------------ | --------------------- |
| Computation (f(xᵢ)) | O(1) per thread                | O(1) per thread       |
| Accumulation        | O(log n/p) with tree reduction | O(n) serial           |
| Total               | O(log n)                       | O(n)                  |

**Key Insight:** For large n, the accumulation phase dominates. With n = 10⁶ threads, approximately 10⁶ serialized atomic operations occur sequentially, negating parallelism benefits.

### 5.4 Memory Hierarchy Impact

Global memory atomicAdd operations incur:

- **L2 cache miss penalty:** ~400-800 cycles
- **L1 cache hit:** ~30-50 cycles (if lucky with contention)
- **DRAM access:** ~200-400 cycles

The atomicAdd to global memory traverses the entire memory hierarchy, introducing 100-1000× latency compared to shared memory operations.

### 5.5 When atomicAdd Approach Is Acceptable

This approach is suitable when:

1. **Small n:** n < 10⁴ reduces serialization impact
2. **Expensive f(x):** Compute time dominates accumulation time
3. **Prototyping:** Initial implementation before optimization
4. **Simplicity priority:** Educational code where readability matters more than performance

## 6. Correctness Verification

**Theorem (Numerical Correctness):** The CUDA kernel computes exactly the trapezoidal rule formula.

**Proof:** For each index i ∈ [0, n], thread i computes:

- xᵢ = a + i·h
- f(xᵢ) with weight wᵢ where w₀ = wₙ = 0.5 and wᵢ = 1 for 1 ≤ i ≤ n-1

The kernel sums S = Σᵢ wᵢ·f(xᵢ) using atomicAdd. Since addition is associative and commutative in floating-point arithmetic (ignoring rounding), the final value equals the mathematical sum. The host multiplies by h, yielding exactly the trapezoidal approximation. ∎

## 7. Compute Capability Considerations

Different GPU architectures handle atomic operations differently:

| Compute Capability | atomicAdd Support        | Performance |
| ------------------ | ------------------------ | ----------- |
| 1.x                | Limited (32-bit only)    | Slow        |
| 2.x-3.x            | Full 32-bit atomicAdd    | Moderate    |
| 5.x-8.x            | Full 32-bit, improved L2 | Better      |
| 9.x                | Enhanced atomics         | Best        |

For atomicAdd on global memory, newer architectures provide improved L2 caching and reduced latency.

## 8. Summary

The atomicAdd approach provides a conceptually straightforward CUDA implementation of the trapezoidal rule. While mathematically correct, it suffers from fundamental performance limitations due to serialization of atomic operations. This baseline implementation serves as a foundation for understanding optimization techniques—hierarchical shared memory reductions and warp-level primitives—which are explored in subsequent topics.
