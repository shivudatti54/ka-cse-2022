# Heterogeneous Computing

=====================================

### Overview

Heterogeneous computing uses multiple processor types (CPUs and GPUs) with separate memory spaces to perform computation. The CUDA programming model is fundamentally heterogeneous: host code runs on the CPU, device code (kernels) runs on the GPU, and the programmer explicitly manages data movement between the two memory spaces via cudaMemcpy.

### Key Points

- **Host:** CPU and system memory (RAM); runs standard C/C++ code
- **Device:** GPU and device memory (DRAM); runs CUDA kernels compiled by nvcc
- **Execution Flow:** Initialize -> cudaMalloc -> cudaMemcpy (H2D) -> kernel launch -> cudaMemcpy (D2H) -> cudaFree
- **Pinned Memory:** Page-locked host memory allocated with `cudaMallocHost()`; enables higher transfer bandwidth and async transfers
- **Unified Memory:** Single address space via `cudaMallocManaged()`; automatic data migration between host and device
- **CUDA Streams:** Enable overlapping data transfer and computation for pipelined execution
- **PCIe Bottleneck:** PCIe bandwidth (16-64 GB/s) is much lower than GPU memory bandwidth (~2 TB/s)
- **NVLink:** High-bandwidth direct interconnect between GPUs (up to 900 GB/s bidirectional on H100)

### Important Concepts

- cudaMemcpy directions: cudaMemcpyHostToDevice, cudaMemcpyDeviceToHost, cudaMemcpyDeviceToDevice
- Asynchronous transfers with `cudaMemcpyAsync()` require pinned memory and CUDA streams
- Unified Memory simplifies code but may suffer from page fault overhead on first access
- `cudaMemPrefetchAsync()` and `cudaMemAdvise()` optimize Unified Memory performance

### Notes

- Minimize data transfers: keep data on GPU as long as possible across multiple kernel launches
- Use streams to overlap H2D transfer, kernel execution, and D2H transfer (pipelining)
- Pinned memory improves transfer bandwidth but reduces OS physical memory for paging
- The compute-to-transfer ratio determines whether GPU acceleration is worthwhile
