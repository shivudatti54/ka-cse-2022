# GPU Performance in Parallel Computing

=====================================

### Overview

GPU performance is driven by massive parallelism through the SIMT (Single Instruction, Multiple Thread) architecture with thousands of cores organized into Streaming Multiprocessors (SMs). Performance optimization centers on maximizing thread utilization, managing the memory hierarchy, and hiding latency through massive multithreading.

### Key Points

- **SIMT Architecture:** A single instruction is executed by multiple threads (32 threads = one warp in NVIDIA CUDA) simultaneously on different data.
- **Memory Hierarchy:** Global memory (large, high-latency DRAM), shared memory (small, fast on-chip per SM), registers (fastest, per thread).
- **Coalesced Memory Access:** Consecutive threads in a warp should access consecutive memory locations to maximize transfer efficiency.
- **Shared Memory Optimization:** Programmer-controlled scratchpad memory to reduce global memory accesses; key optimization technique.
- **Latency Hiding:** GPUs hide memory access latency by switching to other ready warps while some threads are stalled waiting for data.
- **Occupancy:** Ratio of active warps to maximum possible warps per SM. Higher occupancy enables better latency hiding. Limited by registers, shared memory, and block size.
- **Memory Bandwidth Bottleneck:** GPU performance is often constrained by memory bandwidth rather than computational power.

### Important Concepts

- Performance is maximized by launching thousands of threads to keep all cores busy and hide memory latency
- Matrix multiplication optimization: tiling with shared memory drastically reduces global memory accesses
- Non-coalesced global memory access dramatically reduces performance
- Occupancy is limited by: register usage per thread, shared memory usage per block, thread block size

### Notes

- For exams, explain how shared memory tiling optimizes matrix multiplication by reducing redundant global memory reads.
- Remember: GPU performance = parallel algorithm design + memory management; minimize data transfers, maximize computation.
- Be able to explain the relationship between occupancy, latency hiding, and GPU utilization.
