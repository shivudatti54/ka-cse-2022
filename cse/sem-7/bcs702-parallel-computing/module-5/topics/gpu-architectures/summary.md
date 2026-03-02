# GPU Architectures

=====================================

### Overview

NVIDIA GPUs are built around a hierarchical structure of Streaming Multiprocessors (SMs) containing CUDA cores, Tensor Cores, SFUs, and warp schedulers. The multi-level memory hierarchy spans from per-thread registers through shared memory and L1/L2 caches to off-chip global DRAM. Writing efficient CUDA code requires understanding these architectural details.

### Key Points

- **Streaming Multiprocessor (SM):** Fundamental compute unit containing CUDA cores, warp schedulers, shared memory
- **CUDA Cores:** Individual processing elements with INT ALU and FPU; count varies by architecture generation
- **Warp:** Group of 32 threads executing the same instruction (SIMT model)
- **Warp Divergence:** Threads in a warp taking different branches serialize execution, reducing performance
- **Tensor Cores:** Specialized for matrix multiply-accumulate operations (Volta and later)
- **Memory Hierarchy:** Registers > Shared Memory > L1 Cache > L2 Cache > Global Memory (DRAM) > Constant/Texture Memory
- **Memory Coalescing:** Consecutive threads accessing consecutive addresses combine into efficient single transactions
- **Occupancy:** Ratio of active warps to maximum supported warps on an SM

### Important Concepts

- Shared memory is per-block, on-chip (~48-164 KB); organized into 32 banks; bank conflicts cause serialization
- Global memory is off-chip with high bandwidth (~2 TB/s on A100) but high latency (~400-800 cycles)
- Constant memory (64 KB) is optimized for broadcast reads where all warp threads read the same address
- Use Structures of Arrays (SoA) instead of Arrays of Structures (AoS) for better coalescing

### Notes

- Higher occupancy helps hide memory latency but is not always the most important optimization
- Key architecture generations: Fermi, Kepler, Maxwell, Pascal, Volta, Turing, Ampere, Hopper, Blackwell
- Minimize warp divergence by ensuring threads within a warp follow the same control path
- Shared memory + \_\_syncthreads() enables fast inter-thread communication within a block
