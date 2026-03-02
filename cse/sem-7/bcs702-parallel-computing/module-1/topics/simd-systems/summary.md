# SIMD Systems and Classifications

=====================================

### Overview

SIMD (Single Instruction, Multiple Data) is a parallel architecture where a single control unit broadcasts the same instruction to multiple processing elements (PEs), each applying it to their own local data in lockstep. SIMD is highly efficient for data-parallel tasks such as vector/matrix operations, image processing, and scientific simulations.

### Key Points

- **Lockstep Execution:** A central Control Processor fetches and decodes a single instruction, broadcast to all PEs executing simultaneously on different data.
- **Flynn's Taxonomy:** SISD (sequential), SIMD (data parallel), MISD (rare), MIMD (most flexible/common).
- **Processor Arrays (Classical SIMD):** Dedicated machines with thousands of simple PEs (e.g., ILLIAC IV with 64 PEs, CM-2 with 65,536 processors).
- **Packed SIMD (Modern CPUs):** Wide vector registers performing multiple operations per instruction (x86: MMX, SSE, AVX; ARM: NEON).
- **AVX Example:** A 256-bit register holds eight 32-bit floats; one ADD instruction performs eight additions in one clock cycle.
- **SIMT in GPUs:** GPU warps (32 threads in NVIDIA CUDA) execute the same instruction on different data in lockstep, embodying SIMD principles.
- **Conditional Execution Challenge:** if-else branches require predication (masking) where all PEs execute all paths, causing inefficiency.

### Important Concepts

- SIMD vs MIMD: SIMD has centralized synchronous control; MIMD has distributed asynchronous control
- SIMD advantages: high performance for data-parallel workloads, energy efficiency, hardware simplicity
- SIMD limitations: not suitable for irregular/task-parallel problems, conditional branching is inefficient, data alignment requirements
- GPU warps/wavefronts execute in SIMD fashion; GPUs use SIMT (Single Instruction, Multiple Threads) model

### Notes

- Be ready to define SIMD and contrast it with SISD and MIMD using a simple example like vector addition.
- Mention modern implementations: CPU vector extensions (AVX, NEON) and GPU warps/wavefronts for full marks.
- Draw a simple SIMD architecture diagram labeling Control Processor, PEs, and instruction/data flow.
