# Learning Purpose: Heterogeneous Computing

**1. Why this topic matters**
Heterogeneous computing combines CPUs and GPUs in a host-device programming model, where sequential and control-intensive code runs on the CPU while data-parallel computation is offloaded to the GPU. Managing data transfer between host and device memory is one of the biggest practical challenges in GPU programming, as PCIe bandwidth limitations can easily negate computational speedups. Understanding the heterogeneous computing model is essential for writing practical CUDA applications.

**2. What you will learn**
You will learn the CPU-GPU heterogeneous computing model, including the typical CUDA program execution flow of memory allocation, data transfer, kernel launch, and result retrieval. You will understand the differences between pageable and pinned (page-locked) memory, the concept of CUDA Unified Memory, PCIe bandwidth limitations and strategies to minimize data transfer overhead, and advanced interconnect technologies like NVLink.

**3. How it connects to other topics**
This topic applies the GPU architecture knowledge from the previous topic to the practical workflow of CUDA programming. It provides the memory management foundation needed for the CUDA threads/blocks/grids and trapezoidal rule topics that follow, and connects to the hybrid programming concepts from Module 2 where CPU and GPU resources are combined.

**4. Real-world relevance**
Heterogeneous computing is the standard model for GPU-accelerated applications in deep learning (data must be transferred to GPU memory for training), scientific simulation (domain data loaded onto GPUs for computation), video processing (frames transferred to GPU for encoding/decoding), and any application that uses GPU acceleration alongside CPU processing.
