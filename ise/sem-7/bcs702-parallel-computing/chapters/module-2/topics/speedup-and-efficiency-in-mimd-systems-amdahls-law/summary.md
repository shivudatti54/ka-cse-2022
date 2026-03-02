# **Speedup and Efficiency in MIMD Systems, Amdahl’s Law, Scalability in MIMD Systems, Taking Timings of MIMD Programs, GPU Performance**

### Definitions and Theorems

- **MIMD (Massively Parallel Machine/Distributed) system**: A type of parallel computing system that executes tasks in parallel by multiple processors or nodes, each of which can execute a different instruction.
- **Speedup**: The ratio of the time taken by a sequential program to the time taken by a parallel program.
- **Amdahl's Law**: A theoretical limit on the maximum speedup that can be achieved by a parallel program, which depends on the fraction of the program that cannot be parallelized.

### Key Points

**Speedup and Efficiency**

- Speedup = T_parallel / T_sequential
- Efficiency = Speedup / P (number of processors)
- Amdahl's Law: S = 1 / (1 - f \* (1 / P + T / P)), where f is the fraction of the program that cannot be parallelized

**Scalability in MIMD Systems**

- Scalability: The ability of a parallel system to scale up to a large number of processors.
- Karp's Law: The size of the input data grows with the number of processors, while the processing speed remains constant.

**Taking Timings of MIMD Programs**

- Timer functions: `clock()`, `gettimeofday()`, etc.
- Error margins: ± 1-5%

**GPU Performance**

- GPU (Graphics Processing Unit) is a specialized electronic circuit designed to quickly manipulate and alter memory to accelerate the creation of images in a frame buffer intended for output to a display device
- GPU parallelism: Thousands of processors working together to perform complex calculations.
