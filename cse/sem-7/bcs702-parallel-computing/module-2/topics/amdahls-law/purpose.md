# Learning Purpose: Amdahl's Law

**1. Why this topic matters**
Amdahl's Law is one of the most important theoretical results in parallel computing, providing an upper bound on the speedup achievable by parallelizing a program. It reveals that the sequential fraction of a program fundamentally limits how much faster it can run, no matter how many processors are added. Understanding this law is critical for setting realistic expectations and guiding optimization efforts in parallel program development.

**2. What you will learn**
You will learn to state and apply Amdahl's Law to calculate theoretical speedup given the parallel fraction and processor count. You will understand the concept of diminishing returns when adding processors, learn to identify sequential bottlenecks that limit speedup, and compare Amdahl's Law with Gustafson's Law, which offers a more optimistic perspective by scaling problem size with processor count.

**3. How it connects to other topics**
Amdahl's Law connects directly to performance evaluation and timing of MIMD programs in this module, providing the theoretical framework for interpreting measured speedup and efficiency. It applies to all programming models in this course, including MPI (Module 3), OpenMP (Module 4), and CUDA (Module 5), where data transfer overhead introduces additional sequential components.

**4. Real-world relevance**
Amdahl's Law guides hardware purchasing decisions, algorithm design choices, and optimization priorities in HPC centers and software companies. It explains why simply adding more GPUs or cluster nodes does not always yield proportional speedup, and it helps engineers focus their optimization efforts on the sequential portions of code that matter most.
