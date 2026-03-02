# Multicore Processor and GPU

## Introduction

In modern computer architecture, **Multicore Processors** and **Graphics Processing Units (GPUs)** represent two pivotal approaches to enhancing computational performance through parallelism. As per the Delhi University BSc (Hons) Computer Science NEP 2024 syllabus, understanding these architectures is essential for comprehending contemporary computing paradigms.

## Multicore Processors

- **Definition**: A multicore processor integrates multiple independent processing units (cores) onto a single silicon chip
- **Types**:
  - **Homogeneous**: All cores have identical architecture (e.g., quad-core, octa-core)
  - **Heterogeneous**: Different core types for varying tasks (e.g., big.LITTLE architecture)
- **Key Concepts**:
  - **Symmetric Multiprocessing (SMP)**: All cores share common memory and I/O
  - **Cache Hierarchy**: L1, L2, and L3 caches for efficient data sharing between cores
  - **Inter-core Communication**: Through shared memory or dedicated interconnect buses
- **Advantages**:
  - Improved performance through parallel execution
  - Better power efficiency compared to increasing clock speed
  - Handles multiple tasks simultaneously (multitasking)

## Graphics Processing Unit (GPU)

- **Definition**: Specialized processor designed for rendering graphics and parallel computing
- **Architecture**:
  - **Streaming Multiprocessors (SMs)**: Contains hundreds of smaller cores
  - **Thousands of Threads**: Can execute massive parallel workloads
  - **SIMT (Single Instruction, Multiple Threads)**: Execution model
- **Key Features**:
  - High memory bandwidth
  - Massive parallelism (thousands of concurrent threads)
  - Optimized for throughput over latency

## CPU vs GPU Comparison

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Cores** | Few (2-16) powerful cores | Hundreds/Thousands of simple cores |
| **Latency** | Low latency focus | High throughput focus |
| **Task** | Sequential/General-purpose | Parallel/Specialized |
| **Control** | Complex control logic | Simple control, more ALU |

## Heterogeneous Computing

- **CPU-GPU Integration**: Modern systems combine both for optimal performance
- **CUDA/OpenCL**: Programming frameworks for GPU computing
- **Applications**: AI/ML, scientific simulations, video processing, gaming

## Conclusion

Multicore processors and GPUs represent the evolution from single-core to parallel computing architectures. While CPUs excel at sequential tasks with low latency, GPUs thrive on parallel workloads. Understanding their differences and integration is crucial for designing efficient modern computing solutions.

---
*For exam revision: Focus on definitions, key differences, advantages, and practical applications of both architectures.*