# Learning Purpose: GPU Architectures

**1. Why this topic matters**
Understanding GPU architecture at the hardware level is essential for writing efficient CUDA programs because performance depends on how well the code maps to the underlying hardware. The structure of Streaming Multiprocessors (SMs), warp execution, and the multi-level memory hierarchy directly determines whether a GPU kernel achieves high throughput or wastes computational resources. Without this architectural knowledge, GPU programming becomes trial and error rather than informed engineering.

**2. What you will learn**
You will learn the internal architecture of NVIDIA GPUs, including Streaming Multiprocessors with their CUDA cores, warp schedulers, and special function units. You will understand the warp execution model and the performance impact of warp divergence, and study the GPU memory hierarchy (registers, shared memory, L1/L2 cache, global memory, constant memory, texture memory) including critical concepts like memory coalescing and occupancy.

**3. How it connects to other topics**
This topic builds on the GPU and GPGPU overview from the previous topic and provides the architectural foundation for understanding CUDA threads/blocks/grids, compute capabilities, and performance optimization in subsequent topics. It connects to the SIMD concepts from Module 1 (warp execution is a form of SIMT) and to the cache hierarchy concepts from Module 4.

**4. Real-world relevance**
GPU architecture knowledge is essential for CUDA developers optimizing deep learning frameworks (TensorFlow, PyTorch), building high-performance scientific simulation codes, developing real-time graphics engines, and creating GPU-accelerated data processing pipelines. Understanding architecture enables developers to achieve 10x or greater performance improvements through informed optimization choices.
