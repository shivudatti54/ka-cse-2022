# NVIDIA Compute Capabilities

=====================================

### Overview

NVIDIA assigns a compute capability version (major.minor) to each GPU, specifying its hardware feature set, instruction support, and resource limits. The major number corresponds to the architecture generation while the minor number indicates incremental improvements. Compute capability is not a performance metric but determines which CUDA features are available.

### Key Points

- **Compute Capability:** Defines supported CUDA features, hardware limits, instruction set, and memory features
- **cudaGetDeviceProperties():** Runtime API to query GPU properties (SM count, max threads, memory, compute capability)
- **Key Architecture Generations:** Tesla (1.x), Fermi (2.x), Kepler (3.x), Maxwell (5.x), Pascal (6.x), Volta/Turing (7.x), Ampere (8.x), Hopper (9.0), Blackwell (10.x)
- **PTX:** Virtual instruction set for forward compatibility; JIT-compiled to SASS (native GPU machine code)
- **Compilation:** `-arch=sm_XY` targets specific capability; `-gencode` embeds multiple architectures in fat binaries
- ****CUDA_ARCH**:** Preprocessor macro for conditional compilation (e.g., 700 for CC 7.0)
- **Warp Size:** Always 32 across all compute capabilities
- **Max Threads per Block:** 1024 for CC 5.0 and above

### Important Concepts

- Key milestones: Dynamic Parallelism (CC 3.x), Tensor Cores (CC 7.0), RT Cores (CC 7.5), Async Copy (CC 8.0), Thread Block Clusters (CC 9.0)
- Hardware limits: max 1024 threads/block, 65536 registers/SM, 48-228 KB shared memory/SM
- Forward compatibility: embedding PTX code allows JIT compilation on future architectures
- Use `cudaFuncSetAttribute()` to request more shared memory on CC 7.0+

### Notes

- Higher compute capability does not automatically mean better performance -- it indicates newer features
- Always query device properties at runtime for portable code across different GPUs
- Use `-gencode` for multiple architectures to support a range of GPUs in a single binary
- Know the major architecture features: Tensor Cores (7.0), async copy (8.0), Transformer Engine (9.0)
