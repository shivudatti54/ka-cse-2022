# Learning Purpose: NVIDIA Compute Capabilities and Device Architectures

**1. Why this topic matters**
NVIDIA compute capability defines the feature set and hardware limits of a GPU, determining which CUDA features are available and how code should be compiled for optimal performance on specific hardware. As GPU architectures evolve rapidly across generations (Fermi, Kepler, Maxwell, Pascal, Volta, Turing, Ampere, Hopper), understanding compute capabilities ensures that CUDA programs are portable, correctly targeted, and take advantage of generation-specific optimizations.

**2. What you will learn**
You will learn what NVIDIA compute capability represents and how to query GPU features at runtime using cudaGetDeviceProperties(). You will understand the key features introduced in each major GPU architecture generation, the CUDA compilation pipeline (PTX, SASS, fat binaries), and how to use compiler flags (-arch, -gencode) to target specific architectures while maintaining forward compatibility.

**3. How it connects to other topics**
This topic applies the GPU architecture knowledge from earlier in this module to the practical concern of writing portable and optimized CUDA code. It connects to the threads/blocks/grids topic (hardware limits on block size, registers, shared memory per SM) and to the performance improvement topic that follows, where architecture-specific optimizations are applied.

**4. Real-world relevance**
Understanding compute capabilities is essential when developing CUDA applications that must run across different GPU models in data centers, cloud platforms, and workstations. It guides deployment decisions for AI inference servers, determines which GPU features can be leveraged for scientific codes, and ensures that software products work correctly across the diverse NVIDIA GPU ecosystem.
