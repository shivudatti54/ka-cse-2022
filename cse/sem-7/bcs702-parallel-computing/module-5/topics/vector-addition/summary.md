# Vector Addition

=====================================

### Overview

CUDA vector addition is the classic introductory GPU program demonstrating the complete host-device workflow: allocate device memory, copy input data to the GPU, launch a kernel where each thread computes one element c[i] = a[i] + b[i], copy results back to the host, and free device memory. It illustrates cudaMalloc, cudaMemcpy, kernel launch syntax, thread indexing, and boundary checking.

### Key Points

- **cudaMalloc:** Allocates memory on the GPU device; signature: cudaMalloc((void \*\*)&ptr, size)
- **cudaMemcpy:** Transfers data between host and device; uses direction constants cudaMemcpyHostToDevice and cudaMemcpyDeviceToHost
- ****global**:** Function qualifier for kernels that execute on the device and are called from the host
- **Kernel Launch:** vecAdd<<<numBlocks, threadsPerBlock>>>(d_a, d_b, d_c, n)
- **Global Thread Index:** i = blockIdx.x \* blockDim.x + threadIdx.x gives each thread a unique element to process
- **Boundary Check:** if (i < n) prevents out-of-bounds access when total threads exceed array length
- **Ceiling Division:** numBlocks = (n + threadsPerBlock - 1) / threadsPerBlock ensures all elements are covered
- **cudaFree:** Releases device memory, analogous to free() on the host

### Important Concepts

- The host (CPU) and device (GPU) have separate memory spaces; data must be explicitly transferred
- Block size should be a multiple of 32 (warp size); 256 is a common default
- cudaGetLastError() checks for kernel launch errors; cudaDeviceSynchronize() catches execution errors
- Vector addition is memory bandwidth-bound: low arithmetic intensity (1 FLOP per 12 bytes of memory traffic)
- Consecutive threads accessing consecutive addresses produces coalesced memory access (optimal pattern)

### Notes

- The 8-step pattern (allocate, initialize, upload, launch, execute, download, verify, free) applies to virtually all CUDA programs
- CUDA source files use the .cu extension and are compiled with nvcc
- cudaMemcpy is synchronous by default; the host blocks until the transfer completes
- For small arrays, memory transfer overhead may exceed the parallel computation benefit
