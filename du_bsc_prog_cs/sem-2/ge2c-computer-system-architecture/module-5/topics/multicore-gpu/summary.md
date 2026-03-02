# Multicore and GPU Architecture - Summary

## Key Definitions and Concepts

- **Multicore Processor**: Single chip containing multiple independent CPU cores that share certain resources like cache and memory.
- **GPU (Graphics Processing Unit)**: Manycore processor designed for parallel processing of visual data, now generalized for parallel computing.
- **SIMT (Single Instruction, Multiple Threads)**: GPU execution model where threads execute the same instruction but on different data.
- **Streaming Multiprocessor (SM)**: GPU's fundamental compute unit containing multiple execution cores.
- **Warp**: Group of 32 threads that execute in lockstep on NVIDIA GPUs.
- **Heterogeneous Computing**: System combining different processor types (CPU + GPU) for optimal performance.

## Important Formulas and Theorems

- **Amdahl's Law**: Speedup = 1 / (S + (1-S)/N), where S = serial fraction, N = number of cores
- **Gustafson's Law**: Speedup = N + (1-N) × S (scales with problem size)
- **GPU Throughput**: Total work / time, optimized through massive thread parallelism

## Key Points

- Multicore CPUs (2-64 cores) optimize for low latency and complex control flow; GPUs (hundreds/thousands of cores) optimize for high throughput in data-parallel workloads.
- GPUs use SIMT execution where threads in a warp execute the same instruction simultaneously, diverging when needed.
- Memory hierarchy is critical: registers (fastest) → shared memory → caches → global memory (slowest).
- CPU-GPU communication involves data transfer over PCIe bus, creating overhead that must be amortized by compute-intensive kernels.
- Amdahl's Law shows serial portions limit maximum speedup; even with infinite cores, speedup is bounded by 1/serial_fraction.
- Modern applications use heterogeneous computing: CPU for control/logic, GPU for parallel kernels.
- Real-world GPU applications include deep learning training/inference, scientific simulation, cryptocurrency mining, video encoding.

## Common Mistakes to Avoid

1. **Ignoring memory transfer overhead**: Moving data between CPU and GPU memory takes significant time; small kernels may run slower on GPU.
2. **Using too few threads**: GPUs need thousands of threads to hide memory latency; underutilization wastes potential.
3. **Assuming more cores always means better performance**: Diminishing returns due to Amdahl's Law, increased power consumption, and programming complexity.
4. **Confusing warp and block sizes**: Warps (32 threads) are hardware execution units; blocks are software organization for shared memory and synchronization.

## Revision Tips

1. Practice numerical problems on Amdahl's Law - this is frequently tested in DU exams.
2. Draw and label the CPU vs GPU architecture diagrams to memorize components.
3. Remember the thread hierarchy: Grid → Block → Warp → Thread.
4. Review CUDA code examples to understand kernel execution patterns.
5. Know specific examples of where multicore (databases, OS) and GPU (ML, graphics) excel.