# GPU Programming

=====================================

### Overview

GPU programming leverages the massively parallel architecture of GPUs to accelerate data-parallel computational tasks. Originally designed for graphics, GPUs evolved into General-Purpose GPUs (GPGPUs) with programming frameworks like CUDA and OpenCL enabling scientific computing, machine learning, and simulation workloads.

### Key Points

- **CPU vs GPU:** CPUs have few complex cores optimized for sequential/control logic; GPUs have thousands of simple cores optimized for data-parallel throughput.
- **Thread Hierarchy:** Thread (smallest unit) -> Block (threads sharing shared memory) -> Grid (collection of blocks executing a kernel).
- **Kernel:** A function executing on the GPU; launched with configuration specifying grid and block dimensions (e.g., kernel<<<blocks, threads>>>).
- **CUDA Memory Types:** Global (large, high-latency), shared (fast, per-block), registers (fastest, per-thread), constant (read-only, cached), texture (specialized access patterns).
- **Memory Transfer:** Data must be explicitly copied between host (CPU) and device (GPU) using cudaMemcpy; this transfer can be a bottleneck.
- **CUDA Workflow:** Allocate host memory -> allocate device memory (cudaMalloc) -> copy to device -> launch kernel -> copy results back -> free memory.
- **Amdahl's Law for GPUs:** Speedup = 1 / [(1-P) + (P/N)]; data transfer phases add to the sequential component.
- **Strong vs Weak Scaling:** Strong scaling fixes problem size; weak scaling grows problem size with processors.

### Important Concepts

- Global thread index calculation: i = blockIdx.x \* blockDim.x + threadIdx.x
- Block size calculation: blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock
- OpenCL is a cross-platform alternative to CUDA for heterogeneous computing
- Optimization: coalesced memory access, effective shared memory use, maximizing arithmetic intensity, avoiding thread divergence

### Notes

- Know the GPU memory hierarchy and when to use each type (global vs shared vs registers vs constant).
- Practice calculating grid and block sizes for different problem dimensions.
- Remember that CPU-GPU data transfer is often the performance bottleneck; minimize transfers and keep data on the device.
