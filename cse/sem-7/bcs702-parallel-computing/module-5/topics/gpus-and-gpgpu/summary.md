# GPUs and GPGPU

=====================================

### Overview

GPUs evolved from fixed-function graphics accelerators into massively parallel, general-purpose processors. GPGPU (General-Purpose computing on GPUs) harnesses this parallelism for non-graphics workloads using platforms like CUDA and OpenCL. GPUs trade single-thread latency for aggregate throughput by running thousands of threads simultaneously.

### Key Points

- **GPU Design Philosophy:** Optimized for throughput; thousands of simple cores, high memory bandwidth, hardware thread management
- **CPU Design Philosophy:** Optimized for latency; large caches, branch prediction, few powerful cores
- **SIMT Model:** Single Instruction, Multiple Threads; warps of 32 threads execute in lockstep
- **CUDA (2006):** NVIDIA's platform providing C-language extensions, direct memory access, shared memory, and thread hierarchy
- **OpenCL (2008):** Open standard for heterogeneous parallel programming across multiple vendor GPUs
- **CUDA Workflow:** cudaMalloc -> cudaMemcpy (H2D) -> kernel launch -> cudaMemcpy (D2H) -> cudaFree
- **Kernel:** Function prefixed with `__global__` that runs on the GPU; executed by many threads in parallel
- **Global Thread Index:** `i = blockIdx.x * blockDim.x + threadIdx.x`

### Important Concepts

- GPUs excel at data-parallel, compute-intensive, regular memory access workloads
- CPUs are better for complex branching, low parallelism, irregular memory access, and small datasets
- Host = CPU + system memory; Device = GPU + device memory
- Key terms: Warp (32 threads), SM (Streaming Multiprocessor), Kernel, Host, Device

### Notes

- CUDA provides better performance and tooling on NVIDIA hardware; OpenCL offers vendor portability
- GPUs revolutionized deep learning: frameworks like TensorFlow and PyTorch are built on CUDA
- Evolution: Fixed-function pipeline -> Programmable shaders (2001) -> CUDA (2006) -> Modern GPGPU
- Be able to explain CPU vs GPU architectural differences and when each is appropriate
