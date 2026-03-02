# CUDA Trapezoidal Rule I

=====================================

### Overview

The first CUDA implementation of the trapezoidal rule uses the simplest possible approach: each thread computes f(x_i) for one subinterval point and uses atomicAdd to accumulate its contribution into a single global result variable. The kernel handles boundary terms by applying half-weight to f(a) and f(b). This version is correct but suffers from severe performance limitations because atomicAdd serializes thousands of concurrent writes to the same memory location.

### Key Points

- **Formula:** Integral ~ h \* [f(a)/2 + f(a+h) + f(a+2h) + ... + f(b-h) + f(b)/2], where h = (b-a)/n
- **Thread Mapping:** Global index `my_i = blockIdx.x * blockDim.x + threadIdx.x` maps each thread to one point x_i = a + my_i \* h
- **Boundary Handling:** Threads with my_i == 0 or my_i == n multiply their f(x_i) value by 0.5
- **Accumulation:** All threads call `atomicAdd(result_p, my_f)` to add their contribution to a single global float
- **Host Workflow:** cudaMalloc, cudaMemset(0), kernel launch, cudaMemcpy(DeviceToHost), multiply by h
- **Single Block Version:** Uses `threadIdx.x` only; limited to n <= ~1024
- **Multi-Block Version:** Uses `blockIdx.x * blockDim.x + threadIdx.x`; supports arbitrary n

### Important Concepts

- atomicAdd performs a hardware-level read-modify-write that is thread-safe but serializes concurrent accesses
- The serialization bottleneck makes the accumulation phase O(n) instead of O(n/p), negating parallelism benefits
- Floating-point non-determinism arises because thread execution order varies between runs, and floating-point addition is not associative
- Guard condition `if (my_i <= n)` prevents extra threads from contributing invalid values
- The kernel computes the weighted sum only; multiplication by h happens on the host after copying the result back

### Notes

- This approach is analogous to using `#pragma omp critical` in OpenMP -- correct but slow
- The improved version (CUDA Trapezoidal Rule II) replaces atomicAdd with shared-memory parallel reduction
- cudaMemset to zero the result variable is essential; without it, accumulation starts from undefined memory
- Error is O(h^2) regardless of parallelization method; CUDA enables very large n for high accuracy
- For exams, be able to write both the kernel and the host code from scratch
