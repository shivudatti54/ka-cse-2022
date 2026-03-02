# Returning Results from CUDA Kernels

=====================================

### Overview

CUDA kernels are declared `__global__ void` and cannot return values directly. Instead, results must be written to device memory by kernel threads and then explicitly transferred back to the host using `cudaMemcpy` with the `cudaMemcpyDeviceToHost` direction flag. For scalar results computed by many threads, techniques such as atomicAdd, parallel reduction in shared memory, and unified memory provide different trade-offs between simplicity and performance.

### Key Points

- **Void Kernels:** CUDA kernels must have `void` return type because thousands of threads execute simultaneously with no single caller to receive a return value
- **Device Memory + cudaMemcpy:** The standard pattern is cudaMalloc on device, kernel writes results, then cudaMemcpy DeviceToHost copies results to host
- **atomicAdd:** Provides thread-safe accumulation to a single variable but serializes concurrent writes, causing severe performance degradation with many threads
- **Parallel Reduction:** Tree-based reduction in shared memory combines values in log2(blockDim) steps; thread 0 writes block sum to global memory; host sums block results
- **Unified Memory:** `cudaMallocManaged` creates a single pointer accessible from both CPU and GPU; no explicit cudaMemcpy needed but requires `cudaDeviceSynchronize()` before host access
- **Pinned Memory:** `cudaHostAlloc` allocates page-locked host memory enabling direct DMA transfers, faster than pageable memory; freed with `cudaFreeHost()`
- **Error Handling:** Use `cudaGetLastError()` immediately after kernel launch for configuration errors and `cudaDeviceSynchronize()` to catch execution errors

### Important Concepts

- Reduction takes log2(blockDim.x) steps with stride halving; each step requires `__syncthreads()`
- For array results, each thread writes to its own index -- no contention
- For scalar results, naive concurrent writes cause race conditions requiring atomic operations or reduction
- Unified memory uses page-fault-based migration, adding overhead for large sequential transfers

### Notes

- Always initialize device result variables (e.g., set to 0) before launching accumulation kernels
- Pinned memory locks physical RAM -- do not over-allocate or system performance degrades
- The CUDA_CHECK macro pattern wraps error checking for cleaner production code
- Reduction + host summation is the standard approach used in the CUDA trapezoidal rule implementation
